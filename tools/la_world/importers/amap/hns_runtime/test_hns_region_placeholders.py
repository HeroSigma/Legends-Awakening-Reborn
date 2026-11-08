"""Runtime checks for dormant variants, placeholder interactions, stairs and animations."""
from probe import *
D=R/'docs/la_world/hns_regions';mf=json.loads((D/'manifest.json').read_text());rows=mf['maps'];byname={r['name']:r for r in rows};results=[]
assert lib.boot(str(R/'pokeemerald.gba').encode());frames(600);wr(symbols['gMain']+4,symbols['CB2_NewGame']|1);frames(300);state('regions_placeholders_base')
def check(name,passed,**details):
 results.append(dict(test=name,passed=bool(passed),**details))
 if not passed:print('FAIL',results[-1],flush=True)
def visit(row,x,y):warp(row['group'],row['map'],x,y)
def objects():
 result=[]
 for i in range(16):
  a=symbols['gObjectEvents']+i*0x24
  if rd(a,1)&1:result.append(dict(local_id=rd(a+8,1),map=rd(a+9,1),group=rd(a+10,1),graphics=rd(a+4,2),trainer=rd(a+7,1)))
 return result
def money():
 p=rd(symbols['gSaveBlock1Ptr']);s=rd(symbols['gSaveBlock2Ptr']);return rd(p+0x490)^rd(s+0xac)
# Walk source stairs with the two native player graphics paths.
row=byname['HnSTest_Route31']
for gender in [0,1]:
 state('regions_placeholders_base',True);wr(rd(symbols['gSaveBlock2Ptr'])+8,gender,1);visit(row,24,13);before=pos()
 for i in range(4):frames(16,16)
 frames(20);high=pos();check('route31_stairs_up',high[0]>26,gender=gender,before=before,after=high)
 for i in range(4):frames(16,32)
 frames(20);check('route31_stairs_down',pos()[0]<25,gender=gender,after=list(pos()))
# Every hidden actor remains absent when that actor's own cell is brought on-screen.
for row in rows:
 mp=json.loads((R/'data/maps'/row['name']/'map.json').read_text())
 hidden=[(i,e) for i,e in enumerate(mp['object_events']) if e['flag']=='FLAG_HIDE_HNS_PLACEHOLDER_VARIANTS' and 0<=e['x']<row['width'] and 0<=e['y']<row['height']]
 if not hidden:continue
 state('regions_placeholders_base',True)
 for i,e in hidden:
  visit(row,e['x'],min(e['y']+1,row['height']-1));active=objects()
  present=any(o['local_id']==i+1 and o['map']==row['map'] and o['group']==row['group'] for o in active)
  check('hidden_actor_absent',not present,map=row['name'],local_id=i+1)
# Sample trainer/leader and shopkeeper art: interaction stays in overworld, takes no money.
samples=['HnSTest_CherrygroveCity_Mart','HnSTest_VioletCity_Gym','HnS_GoldenrodCity_Gym','HnS_PewterCity_Gym','HnS_CeruleanCity_Gym','HnS_CeladonCity_Mart']
for name in samples:
 if name not in byname:continue
 row=byname[name];mp=json.loads((R/'data/maps'/name/'map.json').read_text())
 actor=next((e for e in mp['object_events'] if e['script']=='HnsRegion_Placeholder' and e['flag']=='0' and e['y']+1<row['height']),None)
 if not actor:continue
 for gender in [0,1]:
  state('regions_placeholders_base',True);wr(rd(symbols['gSaveBlock2Ptr'])+8,gender,1);visit(row,actor['x'],actor['y']+1);frames(1,64);frames(15);before=money()
  frames(1,1);frames(100)
  shot('placeholder_'+name+'_'+str(gender))
  for i in range(8):frames(1,1);frames(30)
  check('placeholder_no_battle_or_charge',rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1 and money()==before,map=name,gender=gender,money_before=before,money_after=money())
# New bank callbacks actually change tile VRAM; all map callbacks were also exercised in the load sweep.
for name in ['HnSTest_NewBarkTown','HnS_GoldenrodCity','HnS_NationalPark_Normal']:
 if name not in byname:continue
 row=byname[name];state('regions_placeholders_base',True);visit(row,*row['arrival'])
 before=bytes(rd(0x6000000+i,1) for i in range(0x8000));frames(37);after=bytes(rd(0x6000000+i,1) for i in range(0x8000))
 check('animation_vram_changes',before!=after,map=name)
(D/'runtime_placeholders.json').write_text(json.dumps(dict(checks=results,passed=sum(x['passed'] for x in results),total=len(results)),indent=2)+'\n')
print('PASS',sum(x['passed'] for x in results),'/',len(results),flush=True)
lib.shutdown()
