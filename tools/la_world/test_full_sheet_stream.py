#!/usr/bin/env python3
"""Exercise the actual C cache through every map camera position and evictions."""
import ctypes as C,struct,subprocess,tempfile,json
from pathlib import Path
from collections import Counter
root=Path(__file__).resolve().parents[2]
with tempfile.TemporaryDirectory() as tmp:
 libpath=Path(tmp)/'cache.so'
 subprocess.run(['gcc','-shared','-fPIC','-fsanitize=undefined','-O2','-I'+str(root/'include'),str(root/'src/full_sheet_tile_cache.c'),'-o',str(libpath)],check=True)
 lib=C.CDLL(str(libpath))
 class Cache(C.Structure):
  _fields_=[('ids',C.c_uint16*1024),('refs',C.c_uint16*1024),('dirty',C.c_uint32*32),('mapping',C.POINTER(C.c_uint16)),('count',C.c_uint16),('cursor',C.c_uint16)]
 lib.FullSheetCacheInit.argtypes=[C.POINTER(Cache),C.POINTER(C.c_uint16),C.c_uint16]
 lib.FullSheetCacheAcquire.argtypes=[C.POINTER(Cache),C.c_uint16];lib.FullSheetCacheAcquire.restype=C.c_uint16
 lib.FullSheetCacheRelease.argtypes=[C.POINTER(Cache),C.c_uint16]
 raw=(root/'data/full_sheet/accumula_test/tiles.4bpp').read_bytes();count=len(raw)//32
 meta=(root/'data/tilesets/primary/accumula_fullsheet_test/metatiles.extended.bin').read_bytes()+(root/'data/tilesets/secondary/accumula_fullsheet_test/metatiles.extended.bin').read_bytes()
 records=list(struct.iter_unpack('<12I',meta));cells=struct.unpack('<1258H',(root/'data/layouts/Accumula_FullSheetTest_Layout/map.bin').read_bytes())
 mapping=(C.c_uint16*count)();cache=Cache();lib.FullSheetCacheInit(C.byref(cache),mapping,count)
 ring={};peak=0;maxuploads=0;steps=0
 def place(x,y):
  key=(x%16,y%16)
  for slot,ref in ring.get(key,[]):lib.FullSheetCacheRelease(C.byref(cache),slot)
  rec=records[cells[y*37+x]&1023] if 0<=x<37 and 0<=y<34 else records[0]
  new=[]
  for ref in rec:
   slot=lib.FullSheetCacheAcquire(C.byref(cache),ref&65535)
   assert slot!=65535,(x,y,ref,'cache overflow')
   new.append((slot,ref))
  ring[key]=new
 def verify():
  global peak,maxuploads,steps
  counts=Counter()
  for pairs in ring.values():
   for slot,ref in pairs:
    assert cache.ids[slot]==(ref&65535),'visible tile evicted'
    assert mapping[ref&65535]==slot
    if slot:counts[slot]+=1
  assert all(cache.refs[i]==counts[i] for i in range(1,1024)), 'reference leak'
  peak=max(peak,len(counts)+1)
  uploads=sum(int(d).bit_count() for d in cache.dirty)
  if steps:maxuploads=max(maxuploads,uploads)
  for i in range(32):cache.dirty[i]=0
  steps+=1
 old=None
 # Every origin with border on all four sides; alternate sweep direction.
 for y in range(-15,34):
  for x in (range(-15,37) if (y+15)%2==0 else range(36,-16,-1)):
   if old is None:
    for yy in range(y,y+16):
     for xx in range(x,x+16):place(xx,yy)
   elif old[0]!=x:
    xx=x+15 if x>old[0] else x
    for yy in range(y,y+16):place(xx,yy)
   else:
    for xx in range(x,x+16):place(xx,y+15)
   verify();old=(x,y)
 # Exhaustion must not overwrite referenced tiles, and freed slots are reusable.
 m=(C.c_uint16*2050)();c=Cache();lib.FullSheetCacheInit(C.byref(c),m,2050)
 for v in range(1,1024):assert lib.FullSheetCacheAcquire(C.byref(c),v)==v
 assert lib.FullSheetCacheAcquire(C.byref(c),1024)==65535
 lib.FullSheetCacheRelease(C.byref(c),500)
 assert lib.FullSheetCacheAcquire(C.byref(c),1024)==500
 assert m[500]==65535 and c.ids[500]==1024
 assert lib.FullSheetCacheAcquire(C.byref(c),2050)==65535
 print(json.dumps({'camera_positions_verified':steps,'maximum_resident_tiles':peak,'maximum_incremental_uploads':maxuploads,'all_visible_references_correct':True,'exhaustion_and_eviction_checked':True}))
