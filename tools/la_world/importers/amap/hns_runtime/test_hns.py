from probe import *
M=json.loads((R/'docs/la_world/hns_canary/manifest.json').read_text());groups=json.loads((R/'data/maps/map_groups.json').read_text());group=groups['group_order'].index('gMapGroup_HnS_Canary');rows=[]
def loc():
 p=rd(symbols['gSaveBlock1Ptr']);return rd(p+4,1),rd(p+5,1)
def target(name):return group,groups['gMapGroup_HnS_Canary'].index(name)
def visit(name,x,y):warp(*target(name),x,y)
def snap(name):shot('hns_'+name)
def check(name,ok,details):
 rows.append(dict(test=name,passed=bool(ok),details=details));print(name,ok,details)
assert lib.boot(str(R/'pokeemerald.gba').encode());frames(600);wr(symbols['gMain']+4,symbols['CB2_NewGame']|1);frames(300);check('new_game',loc()==target('HnSTest_NewBarkTown'),dict(map=loc(),pos=pos()));snap('newbark');state('hns_newbark')
visit('HnSTest_CherrygroveCity',41,8);snap('mart_exterior');frames(24,64);frames(180);check('mart_entry',loc()==target('HnSTest_CherrygroveCity_Mart'),dict(map=loc(),pos=pos()));snap('mart_inside');state('hns_mart_inside');frames(40,128);frames(180);check('mart_exit',loc()==target('HnSTest_CherrygroveCity'),dict(map=loc(),pos=pos()))
visit('HnSTest_VioletCity',23,37);snap('gym_exterior');frames(24,64);frames(180);check('gym_entry',loc()==target('HnSTest_VioletCity_Gym'),dict(map=loc(),pos=pos()));snap('gym_inside');frames(40,128);frames(180);check('gym_exit',loc()==target('HnSTest_VioletCity'),dict(map=loc(),pos=pos()))
visit('HnSTest_Route31',24,13);snap('stairs_before');before=pos();trail=[]
for i in range(4):frames(16,16);trail.append(pos())
frames(20);snap('stairs_high');check('stairs_up',pos()!=before and pos()[0]>26,dict(before=before,after=pos(),trail=trail));high=pos();trail=[]
for i in range(4):frames(16,32);trail.append(pos())
frames(20);snap('stairs_low');check('stairs_down',pos()!=high and pos()[0]<25,dict(before=high,after=pos(),trail=trail))
# Native counter: stand east of clerk-facing counter and interact west.
visit('HnSTest_CherrygroveCity_Mart',4,3);frames(1,32);frames(15);frames(1,1);frames(60);frames(1,1);frames(60);snap('shop_menu');state('hns_shop_menu')
(HERE/'hns_runtime_results.json').write_text(json.dumps(rows,indent=2)+'\n')
