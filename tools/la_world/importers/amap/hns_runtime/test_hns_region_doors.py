"""Test actual movement through every outdoor Mart/Gym entrance."""
from probe import *
import time
D=R/'docs/la_world/hns_regions';mf=json.loads((D/'manifest.json').read_text());rows=mf['maps'];byid={r['id']:r for r in rows}
assert lib.boot(str(R/'pokeemerald.gba').encode());frames(600);wr(symbols['gMain']+4,symbols['CB2_NewGame']|1);frames(300);state('regions_doors_base')
results=[];start=time.time()
for row in rows:
 mp=json.loads((R/'data/maps'/row['name']/'map.json').read_text())
 if mp['map_type'] not in ['MAP_TYPE_TOWN','MAP_TYPE_CITY','MAP_TYPE_ROUTE']:continue
 for i,e in enumerate(mp['warp_events']):
  dest=byid[e['dest_map']]
  if not any(x in dest['source'].lower() for x in ['_mart','_gym']):continue
  for gender in [0,1]:
   state('regions_doors_base',True);wr(rd(symbols['gSaveBlock2Ptr'])+8,gender,1)
   warp(row['group'],row['map'],e['x'],e['y']+1)
   frames(100,64);frames(180)
   p=rd(symbols['gSaveBlock1Ptr']);actual=[rd(p+4,1),rd(p+5,1)];expected=[dest['group'],dest['map']]
   result=dict(source=row['name'],source_warp=i,destination=dest['name'],gender=gender,actual=actual,expected=expected,position=list(pos()),passed=actual==expected)
   results.append(result)
   if not result['passed']:print('FAIL',result,flush=True)
(D/'runtime_doors.json').write_text(json.dumps(dict(checks=results,passed=sum(x['passed'] for x in results),total=len(results),seconds=round(time.time()-start,1)),indent=2)+'\n')
print('PASS',sum(x['passed'] for x in results),'/',len(results),flush=True)
lib.shutdown()
