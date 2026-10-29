"""Native party-relative scaling boundaries, cache refresh and protected gym levels."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_competitive_trainers.py').read_text().split('\nstart(0)')[0],'competitive_helpers','exec'))
start(0)
invoke('FlagSet',c['FLAG_LA_RED_DEX_GIFTS'])
invoke('ScriptGiveMon',4,5,0)
party=symbols['gParties']; leveloff=c['offsetof(struct Pokemon,level)']
for level,expected in [(1,1),(15,15),(16,16),(100,16)]:
 wr(party+leveloff,level,1)
 check('party_level_'+str(level),invoke('LegendsTrainer_PlayerLevel')==expected)
 check('authored_floor_'+str(level),invoke('LegendsTrainer_ScaledLevel',10)==max(10,expected))
 check('authored_ceiling_'+str(level),invoke('LegendsTrainer_ScaledLevel',100)==16)
# The cache must respond immediately to a changed party level.
import re
ids={name:int(value) for name,value in re.findall(r'#define (TRAINER_\w+)\s+(\d+)',(R/'include/constants/opponents.h').read_text())}
manifest=json.loads((R/'docs/features/competitive-trainer-profiles.json').read_text())
# Choose an ordinary profile with a baseline below the first badge cap.
for badge in range(3):invoke('FlagSet',c['FLAG_BADGE01_GET']+badge)
key='TRAINER_SAWYER_1'
tid=ids[key];base=symbols['gTrainers']+tid*c['sizeof(struct Trainer)']
for level in [5,32,5]:
 wr(party+leveloff,level,1)
 trainer=invoke('LegendsTrainer_Get',tid,base)
 team=rd(trainer+c['offsetof(struct Trainer,party)'])
 ace=rd(team+5*c['sizeof(struct TrainerMon)']+c['offsetof(struct TrainerMon,lvl)'],1)
 check('cache_refresh_'+str((level,len(checks))),ace==min(32,max(level,manifest['profiles'][key]['level'])))
lib.shutdown()
(R/'docs/features/reborn-upgrades/scaling-validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'scaling boundary checks')
