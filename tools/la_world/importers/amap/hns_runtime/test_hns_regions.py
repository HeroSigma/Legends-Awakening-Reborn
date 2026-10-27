"""Headless native-ROM map load sweep. Does not touch user battery saves."""
from probe import *
import time,hashlib
D=R/'docs/la_world/hns_regions';manifest=json.loads((D/'manifest.json').read_text());rows=manifest['maps']
assert lib.boot(str(R/'pokeemerald.gba').encode())
frames(600);wr(symbols['gMain']+4,symbols['CB2_NewGame']|1);frames(300);state('regions_baseline')
out=[];start=time.time()
shots=D/'screenshots';shots.mkdir(exist_ok=True)
for i,row in enumerate(rows):
 state('regions_baseline',True)
 warp(row['group'],row['map'],*row['arrival'])
 p=rd(symbols['gSaveBlock1Ptr']);actual=[rd(p+4,1),rd(p+5,1)]
 callback=rd(symbols['gMain']+4);frames(30)
 result=dict(name=row['name'],expected=[row['group'],row['map']],actual=actual,callback=hex(callback),position=list(pos()),passed=actual==[row['group'],row['map']] and callback==symbols['CB2_Overworld']|1)
 # Capture every map as a useful rendering review set.
 path=shots/(row['name']+'.ppm');lib.shot(str(path).encode());im=Image.open(path);im.save(path.with_suffix('.png'));path.unlink()
 result['colors']=len(im.getcolors(38400) or [])
 result['passed'] &= result['colors']>5
 out.append(result)
 (D/'runtime_load_sweep.json').write_text(json.dumps(dict(rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),maps=out,elapsed_seconds=round(time.time()-start,1)),indent=2)+'\n')
 if i%25==0 or not result['passed']:print(i,row['name'],result['passed'],result['actual'],result['callback'],flush=True)
print('PASS',sum(x['passed'] for x in out),'/',len(out),'seconds',round(time.time()-start,1),flush=True)
lib.shutdown()
