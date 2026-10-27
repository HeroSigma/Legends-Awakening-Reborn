"""Synthetic save tests. Never opens any player's .sav file."""
from pathlib import Path
import json, random
from collection_format import *
from audit_layout import audit, R, D
schema=audit();rng=random.Random(0x60b0);checks=0

def check(v,msg):
    global checks
    checks+=1
    assert v,msg

def invalid(action):
    try:action()
    except InvalidSave:return True
    return False
blocks={name:rng.randbytes(schema['sizes'][name]) for name in ['SaveBlock1','SaveBlock2']}
records=(R/'.la_work/compact_pc/1800_records.bin').read_bytes()
check(len(records)==55800,'1800 specimens')
pc=b'\x00'*4+records+rng.randbytes(schema['pc_bytes']-55804)
extra=rng.randbytes(schema['sizes']['SaveBlock3'])
a=encode_slot(schema,blocks,pc,extra,1,3)
b=encode_slot(schema,blocks,pc,extra,2,11)
c=encode_slot(schema,blocks,pc,extra,3,5)
result=decode_slot(schema,b)
check(result['pc']==pc,'all PC records and metadata')
check(result['extra']==extra,'SaveBlock3')
for name in blocks:
    for start,end in keep_ranges(schema,name):check(result['blocks'][name][start:end]==blocks[name][start:end],('retained story range',name,start,end))
    for span in schema['expanded_omissions']:
        if span['block']==name:check(result['blocks'][name][span['offset']:span['offset']+span['size']]==bytes(span['size']),('cleared retired record',span['field']))
check(newest(schema,a+b)[1]['counter']==2,'latest bank')
# Interrupted writes to the older bank must leave the completed bank usable.
for completed in range(17):
    partial=c[:completed*4096]+a[completed*4096:]
    check(newest(schema,partial+b)[1]['counter']==(3 if completed==16 else 2),('power cut',completed))
for sector in range(16):
    for offset in [0,7,8,12,2048,4083,4084,4086,4088,4092,4095]:
        bad=bytearray(b);bad[sector*4096+offset]^=1
        check(newest(schema,a+bad)[1]['counter']==1,('corruption fallback',sector,offset))
        check(invalid(lambda:decode_slot(schema,bad)),('corrupt reject',sector,offset))
check(invalid(lambda:newest(schema,bytes(131072))),'empty banks rejected')
check(invalid(lambda:decode_slot(schema,b[:-1])),'truncated reject')
other=dict(schema);other['abi_sha256']='00'*32
check(invalid(lambda:decode_slot(other,b)),'ABI mismatch rejected')
wrapa=encode_slot(schema,blocks,pc,extra,0xffffffff)
wrapb=encode_slot(schema,blocks,pc,extra,0)
check(newest(schema,wrapa+wrapb)[1]['counter']==0,'counter wrap')
for rotation in range(16):check(decode_slot(schema,encode_slot(schema,blocks,pc,extra,42,rotation))['pc']==pc,('rotation',rotation))
result=dict(passed=True,assertions=checks,stored_slots=1800,record_bytes=31,image_bytes=131072,slot_capacity=schema['slot_capacity'],slot_used=schema['slot_used'],slot_spare=schema['slot_spare'],scope='Synthetic host-side format; production save integration is tested separately')
(D/'save_format_validation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
