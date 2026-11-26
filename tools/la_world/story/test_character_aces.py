"""Native legal, capped and shiny signature partners for existing battle profiles."""
from pathlib import Path
R=Path.cwd()
h=(R/'tools/la_world/storage/test_competitive_trainers.py').read_text().split('\nstart(0)')[0]
h=h.replace("names=[", "names=['TRAINERS_COUNT','DIFFICULTY_NORMAL','FLAG_SYS_GAME_CLEAR','SPECIES_GALLADE','SPECIES_FLYGON',",1)
exec(compile(h,'ace_helpers','exec'))
import json,re
manifest=json.loads((R/'docs/features/competitive-trainer-profiles.json').read_text())['profiles']
ids={n:int(v) for n,v in re.findall(r'#define (TRAINER_\w+)\s+(\d+)',(R/'include/constants/opponents.h').read_text())}
import sys
sys.path.insert(0,str(R/'tools/la_world'))
from character_aces import align_ace
keys=[k for k,v in manifest.items() if k.startswith(('TRAINER_BRENDAN_ROUTE_','TRAINER_MAY_ROUTE_','TRAINER_WALLY_')) or k in ['TRAINER_RED','TRAINER_LEAF','TRAINER_SILVER_RUSTBORO','TRAINER_BARRY_ROUTE_110','TRAINER_MAXIE_1','TRAINER_ARCHIE','TRAINER_STEVEN','TRAINER_WALLACE']]
start(0);invoke('FlagSet',c['FLAG_LA_RED_DEX_GIFTS'])
ts=c['sizeof(struct Trainer)'];base=symbols['gTrainers']+c['DIFFICULTY_NORMAL']*c['TRAINERS_COUNT']*ts;ms=c['sizeof(struct TrainerMon)'];po=c['offsetof(struct Trainer,party)'];so=c['offsetof(struct TrainerMon,species)']
for badges in range(9):
 for key in keys:
  tid=ids[key];t=invoke('LegendsTrainer_Get',tid,base+tid*ts)
  check('expanded_'+str((badges,key)),t!=base+tid*ts)
  team=rd(t+po)
  for j in range(6):check('legal_'+str((badges,key,j)),invoke('LegendsTrainer_MemberLegal',team+j*ms)==1)
  check('authored_ace_'+key,manifest[key]['species']==align_ace(key,manifest[key]['species']))
 if badges<8:invoke('FlagSet',c['FLAG_BADGE01_GET']+badges)
# Same cached trainer, same cap: changing League state must still switch Wally's ace.
key='TRAINER_WALLY_VR_1';tid=ids[key]
t=invoke('LegendsTrainer_Get',tid,base+tid*ts);check('wally_pre_league',rd(rd(t+po)+5*ms+so,2)==c['SPECIES_GALLADE'])
invoke('FlagSet',c['FLAG_SYS_GAME_CLEAR'])
t=invoke('LegendsTrainer_Get',tid,base+tid*ts);check('wally_post_league',rd(rd(t+po)+5*ms+so,2)==c['SPECIES_FLYGON'])
for key in ['TRAINER_RED','TRAINER_BARRY_ROUTE_110','TRAINER_SILVER_RUSTBORO','TRAINER_WALLY_VR_1']:
 tid=ids[key];t=invoke('LegendsTrainer_Get',tid,base+tid*ts)
 # Use an isolated scratch party buffer, never the user battery.
 scratch=0x03007400
 invoke('CreateNPCTrainerPartyFromTrainer',scratch,t)
 for j in range(6):check('one_shiny_'+str((key,j)),invoke('GetBoxMonData3',scratch+j*100,c['MON_DATA_IS_SHINY'],0)==int(j==5))
p=R/'docs/story/chimney-alliance/ace-validation.json';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(dict(passed=True,checks=len(checks),profiles=len(keys),user_save_loaded=False),indent=2)+'\n')
print('PASS',len(checks),'ace checks across',len(keys),'profiles',flush=True)
