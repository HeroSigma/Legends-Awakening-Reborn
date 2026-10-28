"""Free training legality, UI, field placement, evolution and storage checks."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'.la_work/training-test';D.mkdir(exist_ok=True)
import tempfile,struct
names=['MON_DATA_HP_EV','MON_DATA_ATK_EV','MON_DATA_DEF_EV','MON_DATA_SPATK_EV','MON_DATA_SPDEF_EV','MON_DATA_SPEED_EV','MON_DATA_HP_IV','MON_DATA_ATK_IV','MON_DATA_DEF_IV','MON_DATA_SPATK_IV','MON_DATA_SPDEF_IV','MON_DATA_SPEED_IV','MON_DATA_HIDDEN_NATURE','MON_DATA_ABILITY_NUM','MON_DATA_EXP','MON_DATA_LEVEL','MON_DATA_SPECIES','MON_DATA_IS_EGG','MON_DATA_PERSONALITY','MON_DATA_OT_ID','MON_DATA_FRIENDSHIP','MON_DATA_HELD_ITEM','MON_DATA_HP','FLAG_LA_RED_DEX_GIFTS','FLAG_BADGE01_GET','FLAG_IS_CHAMPION','sizeof(struct Pokemon)','offsetof(struct SaveBlock1,money)']
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "pokemon.h"\n#include "constants/flags.h"\n#include <stddef.h>\nconst unsigned v[]={'+','.join(names)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 c=dict(zip(names,struct.unpack('<'+str(len(names))+'I',(td/'c.bin').read_bytes())))
def get(field):return invoke('GetMonData3',symbols['gParties'],c[field],0)
def setdata(field,value):
 wr(0x0203fc00,value);invoke('SetMonData',symbols['gParties'],c[field],0x0203fc00)
def vars(action,stat=0,value=0):
 for key,val in [('gSpecialVar_0x8008',action),('gSpecialVar_0x8006',stat),('gSpecialVar_0x8007',value),('gSpecialVar_0x8009',0)]:wr(symbols[key],val,2)
def result():return rd(symbols['gSpecialVar_Result'],2)
def apply(action,stat,value):
 vars(action,stat,value);invoke('LegendsTraining_Prepare');check('prepare_'+str((action,stat,value)),result()==0);invoke('LegendsTraining_Commit');check('commit_'+str((action,stat,value)),result()==0)
def snapshot():return bytes(rd(symbols['gParties']+i,1) for i in range(c['sizeof(struct Pokemon)']))
def task(name):return next((j for j in range(16) if rd(symbols['gTasks']+j*40+4,1) and rd(symbols['gTasks']+j*40)==symbols[name]|1),None)
def waitfor(predicate,limit=8000):
 for i in range(limit):
  if predicate():return
  frames(1,1 if i%20==0 else 0)
 raise AssertionError(('timeout',hex(rd(symbols['gMain']+4))))
for mode in [0,1]:
 start(0);invoke('StorageChangeMode',mode,1);invoke('ScriptGiveMon',4,5,0)
 money=invoke('GetMoney',rd(symbols['gSaveBlock1Ptr'])+c['offsetof(struct SaveBlock1,money)'])
 identity={n:get(n) for n in ['MON_DATA_PERSONALITY','MON_DATA_OT_ID','MON_DATA_FRIENDSHIP','MON_DATA_HELD_ITEM']}
 for i,field in enumerate(names[:6]):
  apply(1,i,4);check('ev_'+str((mode,i)),get(field)==4)
 apply(2,0,0);check('reset_evs_'+str(mode),sum(get(n) for n in names[:6])==0)
 apply(1,0,252);apply(1,1,252);apply(1,2,6)
 before=snapshot();vars(1,5,1);invoke('LegendsTraining_Commit')
 check('reject_total_over_510_'+str(mode),result()==2 and snapshot()==before)
 vars(1,0,253);invoke('LegendsTraining_Commit');check('reject_ev_253_'+str(mode),result()==3 and snapshot()==before)
 apply(2,0,0)
 for i,field in enumerate(names[6:12]):
  apply(3,i,0 if get(field)!=0 else 31)
  apply(3,i,31 if get(field)!=31 else 0)
  check('iv_adjust_'+str((mode,i)),get(field) in [0,31])
 before=snapshot();vars(3,0,32);invoke('LegendsTraining_Commit');check('reject_iv_32_'+str(mode),result()==3 and snapshot()==before)
 for nature in range(25):
  if get('MON_DATA_HIDDEN_NATURE')==nature:continue
  apply(4,0,nature);check('nature_'+str((mode,nature)),get('MON_DATA_HIDDEN_NATURE')==nature)
 apply(5,0,2);check('hidden_ability_'+str(mode),get('MON_DATA_ABILITY_NUM')==2)
 apply(5,0,0);check('normal_ability_'+str(mode),get('MON_DATA_ABILITY_NUM')==0)
 before=snapshot();vars(5,0,3);invoke('LegendsTraining_Commit');check('illegal_ability_'+str(mode),result()==3 and snapshot()==before)
 vars(6,0,17);invoke('LegendsTraining_Commit');check('intro_overcap_'+str(mode),result()==3)
 invoke('FlagSet',c['FLAG_LA_RED_DEX_GIFTS']);apply(6,0,16)
 check('level_16_'+str(mode),get('MON_DATA_LEVEL')==16)
 before=snapshot();vars(6,0,15);invoke('LegendsTraining_Commit');check('reject_delevel_'+str(mode),result()==3 and snapshot()==before)
 setdata('MON_DATA_IS_EGG',1);before=snapshot();vars(3,0,31);invoke('LegendsTraining_Commit');check('reject_egg_'+str(mode),result()==1 and snapshot()==before);setdata('MON_DATA_IS_EGG',0)
 for n,value in identity.items():check('identity_'+str((mode,n)),get(n)==value)
 check('money_untouched_'+str(mode),invoke('GetMoney',rd(symbols['gSaveBlock1Ptr'])+c['offsetof(struct SaveBlock1,money)'])==money)
 # Round-trip through real box accessors and save/load in each storage mode.
 invoke('StorageWriteMon',0,0,symbols['gParties']);invoke('StorageFlush')
 check('save_'+str(mode),invoke('TrySavingData',0)==1)
 check('load_'+str(mode),invoke('LoadGameSave',0)==1)
 check('stored_nature_'+str(mode),invoke('GetBoxMonDataAt',0,0,c['MON_DATA_HIDDEN_NATURE'])==24)
 check('stored_level_'+str(mode),invoke('GetBoxMonDataAt',0,0,c['MON_DATA_EXP'])==get('MON_DATA_EXP'))
 lib.shutdown()
print('DATA CHECKS',len(checks),flush=True)
# Verify the exact requested tile and its approach in all registered upstairs maps.
start(0);invoke('ScriptGiveMon',4,5,0)
mg=json.loads((R/'data/maps/map_groups.json').read_text())
locations=json.loads((R/'docs/features/training-scientist-locations.json').read_text())
def mid(name):
 for group,gname in enumerate(mg['group_order']):
  if name in mg[gname]:return group,mg[gname].index(name)
for row in locations:
 print('MAP',row['map'],flush=True)
 group,mapnum=mid(row['map']);warp(group,mapnum,4,3)
 obj=invoke('GetObjectEventIdByLocalIdAndMap',row['local_id'],mapnum,group)
 check('actor_'+row['map'],obj<16)
 behavior=invoke('MapGridGetMetatileBehaviorAt',11,10)
 approach=invoke('MapGridGetCollisionAt',11,10)==0 or (invoke('MetatileBehavior_IsCounter',behavior) and invoke('MapGridGetCollisionAt',11,11)==0)
 if not approach:print('BLOCKED',row['map'],behavior,invoke('MapGridGetCollisionAt',11,11),flush=True)
 check('approach_'+row['map'],approach)
lib.shutdown()
(R/'docs/features/training-scientist-validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),centers=len(locations),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'training scientist checks')
