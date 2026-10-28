"""Exercise actual Gym format prompt, battle setup and badge continuation."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_competitive_trainers.py').read_text().split('\nstart(0)')[0],'competitive_helpers','exec'))
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'abi.c').write_text('#include "global.h"\n#include "pokemon.h"\nconst unsigned v=sizeof(struct BattlePokemon);')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'abi.c'),'-o',str(td/'abi.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'abi.o'),str(td/'abi.bin')],check=True)
 battle_mon_size=struct.unpack('<I',(td/'abi.bin').read_bytes())[0]
D=R/'.la_work/competitive-formats';D.mkdir(exist_ok=True)
mapgroups=json.loads((R/'data/maps/map_groups.json').read_text())
def mapid(name):
 for group,groupname in enumerate(mapgroups['group_order']):
  if name in mapgroups[groupname]:return group,mapgroups[groupname].index(name)
 raise KeyError(name)
def wait_for(predicate,limit=5000,press=True):
 for i in range(limit):
  if predicate():return
  frames(1,1 if press and i%20==0 else 0)
 raise AssertionError(('timeout',hex(rd(symbols['gMain']+4))))
def active_task(name):
 return any(rd(symbols['gTasks']+j*40+4,1) and rd(symbols['gTasks']+j*40)==symbols[name]|1 for j in range(16))
for title,double,moncount in [('singles',False,6),('doubles',True,6),('fallback',True,1),('tate_singles',False,6)]:
 start(0)
 # Exercise each supported gimmick in actual battle state, on separate new saves.
 for seed in range(100):
  for j in range(4):wr(rd(symbols['gSaveBlock2Ptr'])+0x0a+j,(seed>>(8*j))&255,1)
  if invoke('LegendsTrainer_Gimmick',c['TRAINER_ROXANNE_1'])==(2 if double else 1):break
 invoke('FlagSet',c['FLAG_LA_RED_DEX_GIFTS'])
 for species in [1,4,7,25,133,155][:moncount]:invoke('ScriptGiveMon',species,16,0)
 name='MossdeepCity_Gym' if title=='tate_singles' else 'RustboroCity_Gym'
 if title=='tate_singles':
  for j in range(6):invoke('FlagSet',c['FLAG_BADGE01_GET']+j)
 group,mid=mapid(name);warp(group,mid,5,3)
 actor=1
 wr(symbols['gSpecialVar_LastTalked'],actor,2)
 wr(symbols['gSelectedObjectEvent'],invoke('GetObjectEventIdByLocalIdAndMap',actor,mid,group),1)
 script='MossdeepCity_Gym_EventScript_TateAndLiza' if title=='tate_singles' else 'RustboroCity_Gym_EventScript_Roxanne'
 invoke('ScriptContext_SetupScript',symbols[script])
 wait_for(lambda:active_task('Task_HandleYesNoInput'))
 frames(15)
 shutil.copy2(shot('format_prompt_'+title),R/'docs/features'/('competitive-format-'+title+'.png'))
 if not double:tap(128)
 tap(1)
 wait_for(lambda:rd(symbols['gBattlersCount'],1) in [2,4],8000)
 wait_for(lambda:rd(symbols['gBattleMainFunc'])==symbols['HandleTurnActionSelectionState']|1,12000)
 frames(30)
 expected=4 if double and moncount>=2 else 2
 check(title+'_battlers',rd(symbols['gBattlersCount'],1)==expected)
 check(title+'_battle_flag',bool(rd(symbols['gBattleTypeFlags'])&1)==(expected==4))
 # Opponent party follows the player party in gParties.
 opponent=symbols['gParties']+600
 check(title+'_six_opponents',all(rd(opponent+j*100+c['offsetof(struct Pokemon,level)'],1)>0 for j in range(6)))
 shutil.copy2(shot('battle_'+title),R/'docs/features'/('competitive-battle-'+title+'.png'))
 if title in ['singles','doubles']:
  bm=symbols['gBattleMons']+battle_mon_size
  saved=bytes(rd(bm+j,1) for j in range(battle_mon_size))
  oldindex=rd(symbols['gBattlerPartyIndexes']+2,2)
  wr(symbols['gBattlerPartyIndexes']+2,5,2)
  invoke('PokemonToBattleMon',opponent+500,bm)
  expected_gimmick=invoke('LegendsTrainer_Gimmick',c['TRAINER_ROXANNE_1'])
  print('GIMMICK',title,expected_gimmick,'tera',invoke('GetBoxMonData3',opponent+500,c['MON_DATA_TERA_TYPE'],0),'zitem',invoke('GetBoxMonData3',opponent+500,c['MON_DATA_HELD_ITEM'],0),'pos',rd(symbols['gBattlerPositions']+1,1),'active',invoke('GetActiveGimmick',1),'teraEligible',invoke('CanTerastallize',1),'zEligible',invoke('CanUseZMove',1),flush=True)
  check(title+'_native_tera_eligibility',invoke('CanTerastallize',1)==int(expected_gimmick==1))
  check(title+'_native_z_eligibility',invoke('CanUseZMove',1)==int(expected_gimmick==2))
  if expected_gimmick==2:
   t=invoke('LegendsTrainer_Get',c['TRAINER_ROXANNE_1'],symbols['gTrainers']+c['TRAINER_ROXANNE_1']*c['sizeof(struct Trainer)'])
   ace=rd(t+c['offsetof(struct Trainer,party)'])+5*c['sizeof(struct TrainerMon)']
   check('native_usable_z_attack',any(invoke('GetUsableZMove',1,rd(ace+c['offsetof(struct TrainerMon,moves)']+j*2,2)) for j in range(4)))
  wr(symbols['gBattlerPartyIndexes']+2,oldindex,2)
  for j,value in enumerate(saved):wr(bm+j,value,1)
 if title=='singles':
  # Supply a won result through the real end callback, then run the original
  # postbattle script. This tests award/continuation, not combat AI performance.
  wr(symbols['gBattleOutcome'],1,1)
  wr(symbols['gBattleMainFunc'],symbols['HandleEndTurn_BattleWon']|1)
  wait_for(lambda: (rd(rd(symbols['gSaveBlock1Ptr'])+0x1270+c['FLAG_BADGE01_GET']//8,1)>>(c['FLAG_BADGE01_GET']%8))&1,16000)
  check('badge_awarded_by_original_script',invoke('GetCurrentLevelCap')==20)
 lib.shutdown()
(R/'docs/features/competitive-formats-validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),checks=checks,rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest()),indent=2)+'\n')
print('PASS',len(checks),'format/battle checks')
