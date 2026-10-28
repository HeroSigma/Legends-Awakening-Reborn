"""One-cast auto-fishing on isolated emulator flash; never a user battery."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0], 'pc_helpers', 'exec'))
D=R/'.la_work/qol_features/fishing-test';D.mkdir(parents=True,exist_ok=True)
start(0);invoke('ScriptGiveMon',265,10,0)
groups=json.loads((R/'data/maps/map_groups.json').read_text())
def visit(name):
 group=next(i for i,g in enumerate(groups['group_order']) if name in groups[g]);num=groups[groups['group_order'][group]].index(name)
 warp(group,num,12,12)
def fishing():return active('Task_Fishing')
state('automatic_fishing_baseline')
for mode in [0,1]:
 for rod in [0,1,2]:
  state('automatic_fishing_baseline',True);invoke('StorageChangeMode',mode,1);visit('Route102')
  check('fishing_table_'+str((mode,rod)),invoke('DoesCurrentMapHaveFishingMons')==1)
  before=invoke('GetGameStat',12);invoke('StartFishing',rod)
  for _ in range(1500):
   frames(1)
   if fishing() is None:break
  check('automatic_battle_'+str((mode,rod)),rd(symbols['gIsFishingEncounter'],1)==1 and fishing() is None)
  check('fishing_counter_'+str((mode,rod)),invoke('GetGameStat',12)==before+1)
# Failure/cancel uses normal dismissal; never starts an encounter.
for cancel in [False,True]:
 state('automatic_fishing_baseline',True);visit('Route102' if cancel else 'LittlerootTown');wr(symbols['gIsFishingEncounter'],0,1)
 if not cancel:check('no_fish_table',invoke('DoesCurrentMapHaveFishingMons')==0)
 invoke('StartFishing',0);frames(20)
 if cancel:tap(2)
 for i in range(1500):
  frames(1,1 if i%30==0 else 0)
  if fishing() is None:break
 check('clean_exit_'+str(cancel),fishing() is None and rd(symbols['gIsFishingEncounter'],1)==0)
 check('overworld_restored_'+str(cancel),rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1)
lib.shutdown()
(R/'docs/features/automatic-fishing-validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'automatic-fishing checks')
