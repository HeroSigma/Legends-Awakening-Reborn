"""Route baselines rise with badges and never follow the player's party level."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_competitive_trainers.py').read_text().split('\nstart(0)')[0],'helpers','exec'))
start(0);invoke('FlagSet',c['FLAG_LA_RED_DEX_GIFTS']);invoke('ScriptGiveMon',4,5,0)
p=symbols['gParties'];base=symbols['gTrainers'];size=c['sizeof(struct Trainer)'];ms=c['sizeof(struct TrainerMon)'];po=c['offsetof(struct Trainer,party)'];lo=c['offsetof(struct TrainerMon,lvl)']
def ace(tid):
 t=invoke('LegendsTrainer_Get',tid,base+tid*size)
 return rd(rd(t+po)+5*ms+lo,1)
calvin=c['TRAINER_CALVIN_1'];roxanne=c['TRAINER_ROXANNE_1']
initial=ace(calvin)
check('early_route_below_gym',initial<16)
for level in [1,5,16,100]:
 wr(p+c['offsetof(struct Pokemon,level)'],level,1)
 check('party_does_not_raise_route_'+str(level),ace(calvin)==initial)
check('gym_keeps_level',ace(roxanne)==16)
for stage,cap in enumerate([16,20,26,32,37,43,49,56,65]):
 check('route_badge_progression_'+str(stage),ace(calvin)==min(cap-2,initial+stage*2))
 check('general_baseline_'+str(stage),invoke('LegendsTrainer_ScaledLevel',8)==min(cap-2,8+stage*2))
 if stage<8:invoke('FlagSet',c['FLAG_BADGE01_GET']+stage)
lib.shutdown()
(R/'docs/features/reborn-upgrades/scaling-validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'route scaling checks')
