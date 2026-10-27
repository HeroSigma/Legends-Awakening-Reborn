"""Executable specification for the proposed collection save format.
Host-side prototype only. No flash driver or game-save writes are connected.
"""
import struct, zlib
SECTOR=4096
CHUNK=4072
SLOT_SECTORS=16
SIGNATURE=0x3243504C
VERSION=2

class InvalidSave(ValueError):pass

def keep_ranges(schema,block):
    end=0
    for span in sorted((v for v in schema['expanded_omissions'] if v['block']==block),key=lambda v:v['offset']):
        start=span['offset']
        if start<end or start+span['size']>schema['sizes'][block]:raise InvalidSave('overlapping/out-of-range omission')
        if start>end:yield end,start
        end=start+span['size']
    if end<schema['sizes'][block]:yield end,schema['sizes'][block]

def pack_story(schema,blocks):
    out=bytearray()
    for name in ['SaveBlock1','SaveBlock2']:
        if len(blocks[name])!=schema['sizes'][name]:raise InvalidSave('wrong block size')
        for a,b in keep_ranges(schema,name):out.extend(blocks[name][a:b])
    if len(out)!=schema['story_bytes']:raise InvalidSave('story size')
    return bytes(out)

def unpack_story(schema,packed):
    if len(packed)!=schema['story_bytes']:raise InvalidSave('story size')
    out={};pos=0
    for name in ['SaveBlock1','SaveBlock2']:
        data=bytearray(schema['sizes'][name])
        for a,b in keep_ranges(schema,name):data[a:b]=packed[pos:pos+b-a];pos+=b-a
        out[name]=bytes(data)
    return out

def payload(schema,blocks,pc,extra):
    if len(pc)!=schema['pc_bytes'] or len(extra)!=schema['sizes']['SaveBlock3']:raise InvalidSave('PC/extra size')
    body=pack_story(schema,blocks)+pc+extra
    head=bytearray(64)
    struct.pack_into('<8sIIII',head,0,b'LACOLL2\0',VERSION,len(body),len(pc),zlib.crc32(body))
    head[24:56]=bytes.fromhex(schema['abi_sha256'])
    struct.pack_into('<I',head,56,zlib.crc32(head[:56]))
    out=bytes(head)+body
    if len(out)>CHUNK*SLOT_SECTORS:raise InvalidSave('capacity exceeded')
    return out.ljust(CHUNK*SLOT_SECTORS,b'\0')

def checksum(data):
    n=sum(struct.unpack('<'+'I'*(len(data)//4),data))&0xffffffff
    return ((n>>16)+n)&0xffff

def encode_slot(schema,blocks,pc,extra,counter,rotation=0):
    content=payload(schema,blocks,pc,extra);out=bytearray(SECTOR*SLOT_SECTORS)
    counter&=0xffffffff
    for logical in range(SLOT_SECTORS):
        sector=bytearray(SECTOR)
        chunk=content[logical*CHUNK:(logical+1)*CHUNK]
        sector[:8]=struct.pack('<4sHH',b'LACS',VERSION,CHUNK)
        sector[12:4084]=chunk
        crc=zlib.crc32(struct.pack('<HI',logical,counter)+sector[:8]+chunk)
        struct.pack_into('<I',sector,8,crc)
        struct.pack_into('<HHII',sector,4084,logical,checksum(sector[:4084]),SIGNATURE,counter)
        physical=(logical+rotation)%SLOT_SECTORS
        out[physical*SECTOR:(physical+1)*SECTOR]=sector
    return bytes(out)

def decode_slot(schema,slot):
    if len(slot)!=SECTOR*SLOT_SECTORS:raise InvalidSave('slot size')
    chunks={};counters=set()
    for i in range(SLOT_SECTORS):
        s=slot[i*SECTOR:(i+1)*SECTOR]
        logical,check,sig,counter=struct.unpack_from('<HHII',s,4084)
        if logical>=SLOT_SECTORS or logical in chunks or sig!=SIGNATURE:raise InvalidSave('sector identity')
        if s[:8]!=struct.pack('<4sHH',b'LACS',VERSION,CHUNK):raise InvalidSave('sector version')
        if check!=checksum(s[:4084]):raise InvalidSave('sector checksum')
        if struct.unpack_from('<I',s,8)[0]!=zlib.crc32(struct.pack('<HI',logical,counter)+s[:8]+s[12:4084]):raise InvalidSave('sector CRC')
        chunks[logical]=s[12:4084];counters.add(counter)
    if len(counters)!=1:raise InvalidSave('mixed generations')
    data=b''.join(chunks[i] for i in range(SLOT_SECTORS))
    magic,version,size,pc_size,crc=struct.unpack_from('<8sIIII',data)
    expected=schema['story_bytes']+schema['pc_bytes']+schema['sizes']['SaveBlock3']
    if magic!=b'LACOLL2\0' or version!=VERSION or size!=expected or pc_size!=schema['pc_bytes']:raise InvalidSave('payload header')
    if data[24:56]!=bytes.fromhex(schema['abi_sha256']):raise InvalidSave('incompatible ABI')
    if struct.unpack_from('<I',data,56)[0]!=zlib.crc32(data[:56]):raise InvalidSave('header CRC')
    body=data[64:64+size]
    if zlib.crc32(body)!=crc:raise InvalidSave('payload CRC')
    story_end=schema['story_bytes'];pc_end=story_end+pc_size
    return dict(counter=counters.pop(),blocks=unpack_story(schema,body[:story_end]),pc=body[story_end:pc_end],extra=body[pc_end:])

def newest(schema,image):
    if len(image)!=2*SECTOR*SLOT_SECTORS:raise InvalidSave('image size')
    valid=[]
    for bank in range(2):
        try:valid.append((bank,decode_slot(schema,image[bank*65536:(bank+1)*65536])))
        except InvalidSave:pass
    if not valid:raise InvalidSave('no complete valid bank')
    if len(valid)==1:return valid[0]
    a,b=valid
    delta=(b[1]['counter']-a[1]['counter'])&0xffffffff
    if delta==0x80000000:raise InvalidSave('ambiguous save generation')
    return b if 0<delta<0x80000000 else a
