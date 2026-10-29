"""Verify generated Gym student typing at each Gym's progression cap."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_competitive_trainers.py').read_text().split('\nstart(0)')[0],'helpers','exec'))
manifest=json.loads((R/'docs/features/competitive-trainer-profiles.json').read_text())['profiles']
ids={name:int(value) for name,value in re.findall(r'#define (TRAINER_\w+)\s+(\d+)',(R/'include/constants/opponents.h').read_text())}
types=['ROCK','FIGHTING','ELECTRIC','FIRE','NORMAL','FLYING','PSYCHIC','WATER']
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\nconst unsigned v[]={'+','.join('TYPE_'+t for t in types)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 type_ids=struct.unpack('<8I',(td/'c.bin').read_bytes())
start(0);invoke('FlagSet',c['FLAG_LA_RED_DEX_GIFTS'])
for stage,(theme,target) in enumerate(zip(types,type_ids)):
 if stage:invoke('FlagSet',c['FLAG_BADGE01_GET']+stage-1)
 members={k:v for k,v in manifest.items() if v.get('location_theme')=='gym:'+theme.lower()}
 check('gym_has_students_'+theme,len(members)>0)
 for key,profile in members.items():
  tid=ids[key];t=invoke('LegendsTrainer_Get',tid,symbols['gTrainers']+tid*c['sizeof(struct Trainer)'])
  party=rd(t+c['offsetof(struct Trainer,party)'])
  for slot in range(6):
   m=party+slot*c['sizeof(struct TrainerMon)'];sp=rd(m+c['offsetof(struct TrainerMon,species)'],2)
   check('gym_type_'+str((key,slot)),target in [invoke('GetSpeciesType',sp,i) for i in [0,1]])
   check('legal_gym_member_'+str((key,slot)),invoke('LegendsTrainer_MemberLegal',m)==1)
  check('student_no_format_choice_'+key,not profile['format_choice'])
  check('student_no_shiny_ace_'+key,not profile['shiny_ace'])
# All eight Lavaridge student scripts use a special macro with a local ID before trainer ID.
for key in ['TRAINER_COLE','TRAINER_AXLE','TRAINER_KEEGAN','TRAINER_DANIELLE','TRAINER_GERALD','TRAINER_JACE','TRAINER_JEFF','TRAINER_ELI']:
 check('buried_fire_trainer_'+key,manifest[key].get('location_theme')=='gym:fire')
lib.shutdown()
(R/'docs/features/trainer-locations-validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'location-theme checks')
