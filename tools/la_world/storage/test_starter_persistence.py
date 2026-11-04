"""Starter identity compatibility in disposable native saves."""
from pathlib import Path
import json, hashlib
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'docs/features/nine-starters'
checks=[]
def check(n,v):
 checks.append(dict(test=n,passed=bool(v)));assert v,n
for mode in [0,1]:
 start(0);invoke('StorageChangeMode',mode,1)
 for legacy in range(3):
  invoke('VarSet',0x409d,0);invoke('VarSet',0x4023,legacy)
  check(f'legacy_{mode}_{legacy}',invoke('GetChosenStarterChoice')==legacy)
 for bad in [0xffff,0x5309,0x1207]:
  invoke('VarSet',0x409d,bad)
  check(f'invalid_falls_back_{mode}_{bad}',invoke('GetChosenStarterChoice')==2)
 for choice in range(9):
  invoke('RecordStarterChoice',choice)
  check(f'record_{mode}_{choice}',invoke('GetChosenStarterChoice')==choice)
  check(f'save_{mode}_{choice}',invoke('TrySavingData',0)==1)
  invoke('RecordStarterChoice',(choice+1)%9)
  check(f'load_{mode}_{choice}',invoke('LoadGameSave',0)==1)
  check(f'persist_{mode}_{choice}',invoke('GetChosenStarterChoice')==choice)
  check(f'species_{mode}_{choice}',invoke('GetChosenStarterPokemon')==invoke('GetStarterPokemon',choice))
 lib.shutdown()
(D/'persistence-validation.json').write_text(json.dumps(dict(rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks,user_save_loaded=False),indent=2)+'\n')
print('PASS',len(checks),'persistence checks',flush=True)
