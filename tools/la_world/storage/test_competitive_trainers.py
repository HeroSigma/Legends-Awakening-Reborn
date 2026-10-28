"""Native curated trainer, legality, cap and gimmick integration checks."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'.la_work/competitive-trainers-test';D.mkdir(parents=True,exist_ok=True)
import tempfile,struct
names=['TRAINER_CALVIN_1','TRAINER_RICK','TRAINER_TIANA','TRAINER_ALLEN','TRAINER_ROXANNE_1','TRAINER_RED','FLAG_LA_RED_DEX_GIFTS','FLAG_BADGE01_GET','FLAG_IS_CHAMPION','sizeof(struct Trainer)','sizeof(struct TrainerMon)','offsetof(struct Trainer,party)','offsetof(struct Trainer,items)','offsetof(struct TrainerMon,lvl)','offsetof(struct TrainerMon,species)','offsetof(struct TrainerMon,moves)','offsetof(struct TrainerMon,ability)','offsetof(struct TrainerMon,iv)','MON_DATA_SPECIES','MON_DATA_LEVEL','MON_DATA_HP_IV','MON_DATA_ATK_IV','MON_DATA_DEF_IV','MON_DATA_SPEED_IV','MON_DATA_SPATK_IV','MON_DATA_SPDEF_IV','MON_DATA_HELD_ITEM','MON_DATA_TERA_TYPE','ITEM_SUPER_POTION','TYPE_MYSTERY','(u32)AI_FLAG_SMART_TRAINER','(u32)(AI_FLAG_SMART_TRAINER>>32)','MOVE_TACKLE','MON_DATA_HP_EV','MON_DATA_ATK_EV','MON_DATA_DEF_EV','MON_DATA_SPEED_EV','MON_DATA_SPATK_EV','MON_DATA_SPDEF_EV','MON_DATA_IS_SHINY','offsetof(struct Pokemon,level)']
# TRAINER_RED is donor-specific; ordinary untouched trainer ID 1 suffices as exclusion.
names[5]='TRAINER_NONE'
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "data.h"\n#include "constants/opponents.h"\n#include "constants/flags.h"\n#include "constants/battle_ai.h"\n#include "constants/items.h"\n#include <stddef.h>\nconst unsigned v[]={'+','.join(names)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 c=dict(zip(names,struct.unpack('<'+str(len(names))+'I',(td/'c.bin').read_bytes())))
start(0)
flag=c['FLAG_LA_RED_DEX_GIFTS'];base=symbols['gTrainers'];ts=c['sizeof(struct Trainer)'];ms=c['sizeof(struct TrainerMon)'];partyoff=c['offsetof(struct Trainer,party)'];leveloff=c['offsetof(struct TrainerMon,lvl)'];spoff=c['offsetof(struct TrainerMon,species)'];moveoff=c['offsetof(struct TrainerMon,moves)']
ids=[c[n] for n in names[:4]]
# Diagnose every authored move using linked native learnsets before enabling teams.
issues=[]
for label in ['CALVIN_1','RICK','TIANA','ALLEN']:
 for slot in range(6):
  m=symbols['sTeam_'+label]+slot*ms;sp=rd(m+spoff,2);level=rd(m+leveloff,1)
  for j in range(4):
   mv=rd(m+moveoff+j*2,2)
   if not invoke('LegendsTrainer_MoveLegal',sp,level,mv):issues.append((label,slot,sp,level,j,mv))
print('MOVE ISSUES',issues,flush=True)
assert not issues,issues
# Before Dex milestone, preserve all original roster pointers and no player cap.
check('pre_dex_uncapped',invoke('GetCurrentLevelCap')==100)
for id in ids:check('pre_dex_native_'+str(id),invoke('LegendsTrainer_Get',id,base+id*ts)==base+id*ts)
invoke('FlagSet',flag)
check('roxanne_cap_16',invoke('GetCurrentLevelCap')==16)
check('exp_stops_at_cap',invoke('GetSoftLevelCapExpValue',16,100)==0)
check('exp_below_cap',invoke('GetSoftLevelCapExpValue',15,100)==100)
for mode in [0,1]:
 invoke('StorageChangeMode',mode,1)
 for label,id in zip(['CALVIN_1','RICK','TIANA','ALLEN'],ids):
  t=invoke('LegendsTrainer_Get',id,base+id*ts)
  check('override_'+str((mode,id)),t!=base+id*ts)
  smart=c['(u32)AI_FLAG_SMART_TRAINER']|(c['(u32)(AI_FLAG_SMART_TRAINER>>32)']<<32)
  check('smart_ai_'+str((mode,id)),rd(t)|(rd(t+4)<<32)==smart)
  itemoff=t+c['offsetof(struct Trainer,items)']
  check('two_heals_'+str((mode,id)),rd(itemoff,2)==rd(itemoff+2,2)==c['ITEM_SUPER_POTION'])
  team=rd(t+partyoff)
  for slot in range(6):check('legal_member_'+str((mode,id,slot)),invoke('LegendsTrainer_MemberLegal',team+slot*ms)==1)
  g=invoke('LegendsTrainer_Gimmick',id)
  check('stable_gimmick_'+str((mode,id)),g in [1,2] and all(invoke('LegendsTrainer_Gimmick',id)==g for _ in range(8)))
  A=0x0203f000
  invoke('CreateNPCTrainerPartyFromTrainer',A,t)
  for slot in range(6):
   mon=A+slot*100
   check('created_member_'+str((mode,id,slot)),invoke('GetBoxMonData3',mon,c['MON_DATA_SPECIES'],0)!=0)
   check('level_cap_'+str((mode,id,slot)),1<=rd(mon+c['offsetof(struct Pokemon,level)'],1)<=16)
   ivfields=['MON_DATA_HP_IV','MON_DATA_ATK_IV','MON_DATA_DEF_IV','MON_DATA_SPEED_IV','MON_DATA_SPATK_IV','MON_DATA_SPDEF_IV']
   check('perfect_ivs_'+str((mode,id,slot)),all(invoke('GetBoxMonData3',mon,c[f],0)==31 for f in ivfields))
   evfields=['MON_DATA_HP_EV','MON_DATA_ATK_EV','MON_DATA_DEF_EV','MON_DATA_SPEED_EV','MON_DATA_SPATK_EV','MON_DATA_SPDEF_EV']
   ev=[invoke('GetBoxMonData3',mon,c[f],0) for f in evfields]
   check('legal_evs_'+str((mode,id,slot)),sum(ev)==508 and max(ev)<=252)
   tera=invoke('GetBoxMonData3',mon,c['MON_DATA_TERA_TYPE'],0)
   check('exclusive_tera_'+str((mode,id,slot)),(tera!=c['TYPE_MYSTERY'])==(g==1 and slot==5))
   check('ordinary_not_shiny_'+str((mode,id,slot)),invoke('GetBoxMonData3',mon,c['MON_DATA_IS_SHINY'],0)==0)
  # Subsequent trainer lookups cannot overwrite this trainer's party view.
  before=bytes(rd(team+i,1) for i in range(ms*6))
  other=ids[(ids.index(id)+1)%4];invoke('LegendsTrainer_Get',other,base+other*ts)
  check('independent_views_'+str((mode,id)),before==bytes(rd(team+i,1) for i in range(ms*6)))
# Mutated scratch copies must reject early evolution, over-cap levels and illegal moves.
source=symbols['sTeam_RICK'];scratch=0x0203f000
for i in range(ms):wr(scratch+i,rd(source+i,1),1)
wr(scratch+leveloff,9,1)
check('reject_early_butterfree',invoke('LegendsTrainer_MemberLegal',scratch)==0)
wr(scratch+leveloff,17,1)
check('reject_over_cap',invoke('LegendsTrainer_MemberLegal',scratch)==0)
wr(scratch+leveloff,15,1);wr(scratch+moveoff,0,2)
check('reject_missing_move',invoke('LegendsTrainer_MemberLegal',scratch)==0)
# No gym/story/partner conversion is included in this first batch.
id=c['TRAINER_ROXANNE_1'];check('gym_untouched',invoke('LegendsTrainer_Get',id,base+id*ts)==base+id*ts)
for badge_stage,expected_cap in enumerate([16,20,26,32,37,43,49,56,65]):
 check('badge_cap_'+str(badge_stage),invoke('GetCurrentLevelCap')==expected_cap)
 if badge_stage<8:invoke('FlagSet',c['FLAG_BADGE01_GET']+badge_stage)
invoke('FlagSet',c['FLAG_IS_CHAMPION']);check('post_league_caps_deferred',invoke('GetCurrentLevelCap')==100)
# A fresh emulator verifies the actual trainerbattle command and battle initialization.
lib.shutdown();start(0);invoke('FlagSet',flag)
for species in [1,4,7,25,133,155]:invoke('ScriptGiveMon',species,16,0)
warp(0,17,37,16)
wr(symbols['gSpecialVar_LastTalked'],2,2)
obj=invoke('GetObjectEventIdByLocalIdAndMap',2,17,0);wr(symbols['gSelectedObjectEvent'],obj,1)
invoke('ScriptContext_SetupScript',symbols['Route102_EventScript_Calvin'])
for i in range(4000):
 frames(1,1 if i%20==0 else 0)
 if i>400 and any(rd(symbols['gParties']+600+j*100+c['offsetof(struct Pokemon,level)'],1) for j in range(6)):
  break
frames(240)
# All six opponents must be built by the production battle setup, not just the helper.
opponent=symbols['gParties']+600
check('real_battle_six_opponents',all(rd(opponent+j*100+c['offsetof(struct Pokemon,level)'],1)>0 for j in range(6)))
check('real_battle_cap',all(rd(opponent+j*100+c['offsetof(struct Pokemon,level)'],1)<=16 for j in range(6)))
shutil.copy2(shot('competitive_calvin_battle'),R/'docs/features/competitive-calvin-battle.png')
lib.shutdown()
(R/'docs/features/competitive-trainers-validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'competitive trainer checks')
