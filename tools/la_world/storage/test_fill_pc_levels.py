"""Both Fill PC variants create exact level-five records in both storage modes."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'.la_work/fill-pc-levels';D.mkdir(exist_ok=True)
def level(box,slot):return invoke('GetLevelFromBoxMonExp',invoke('GetBoxedMonPtr',box,slot))
for mode in [0,1]:
 for random_ivs in [0,1]:
  start(0);invoke('StorageChangeMode',mode,1);invoke('ScriptGiveMon',25,20,0)
  invoke('StorageWriteMon',0,0,symbols['gParties'])
  added=invoke('Debug_FillPCBoxes',random_ivs)
  check('added_'+str((mode,random_ivs)),added>0)
  check('existing_level_preserved_'+str((mode,random_ivs)),level(0,0)==20)
  for index in range(1,added+1):
   check('level_five_'+str((mode,random_ivs,index)),level(index//30,index%30)==5)
  check('stops_'+str((mode,random_ivs)),invoke('Debug_FillPCBoxes',random_ivs)==0)
  check('save_'+str((mode,random_ivs)),invoke('TrySavingData',0)==1)
  check('reload_'+str((mode,random_ivs)),invoke('LoadGameSave',0)==1)
  for index in [1,added//2,added]:check('saved_level_five_'+str((mode,random_ivs,index)),level(index//30,index%30)==5)
  check('saved_existing_untouched_'+str((mode,random_ivs)),level(0,0)==20)
  lib.shutdown()
(R/'docs/features/fill-pc-levels-validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'Fill PC level checks')
