"""Exhaustive native legality and capped party generation for the registered roster.
Uses isolated mGBA memory/battery only; never opens the player's save.
"""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_competitive_trainers.py').read_text().split('\nstart(0)')[0],'competitive_helpers','exec'))
manifest=json.loads((R/'docs/features/competitive-trainer-profiles.json').read_text())
text=(R/'include/constants/opponents.h').read_text()
trainer_ids={name:int(value) for name,value in re.findall(r'#define (TRAINER_\w+)\s+(\d+)',text)}
start(0)
dexflag=c['FLAG_LA_RED_DEX_GIFTS'];base=symbols['gTrainers'];ts=c['sizeof(struct Trainer)'];ms=c['sizeof(struct TrainerMon)'];partyoff=c['offsetof(struct Trainer,party)']
for key in manifest['profiles']:
 tid=trainer_ids[key]
 check('pre_dex_'+key,invoke('LegendsTrainer_Get',tid,base+tid*ts)==base+tid*ts)
invoke('FlagSet',dexflag)
issues=[]
for badge_stage,expected_cap in enumerate([16,20,26,32,37,43,49,56,65,100]):
 if badge_stage==9:invoke('FlagSet',c['FLAG_IS_CHAMPION'])
 check('cap_'+str(expected_cap),invoke('GetCurrentLevelCap')==expected_cap)
 if badge_stage<9:check('wild_next_leader_floor_'+str(expected_cap),invoke('GetWildProgressionCap')==expected_cap-2)
 for key in manifest['profiles']:
  tid=trainer_ids[key];t=invoke('LegendsTrainer_Get',tid,base+tid*ts)
  if t==base+tid*ts:issues.append((key,expected_cap,'native fallback'));continue
  team=rd(t+partyoff)
  itemoff=t+c['offsetof(struct Trainer,items)']
  check('two_heals_'+str(expected_cap)+'_'+key,rd(itemoff,2)!=0 and rd(itemoff+2,2)!=0)
  for slot in range(6):
   if invoke('LegendsTrainer_MemberLegal',team+slot*ms)!=1:
    m=team+slot*ms
    issues.append((key,expected_cap,slot,rd(m+c['offsetof(struct TrainerMon,species)'],2),rd(m+c['offsetof(struct TrainerMon,lvl)'],1),[rd(m+c['offsetof(struct TrainerMon,moves)']+j*2,2) for j in range(4)]))
  checks.append(dict(test='six_legal_'+str(expected_cap)+'_'+key,passed=not issues))
 if issues:
  print('ISSUES',issues[:60],flush=True);break
 print('VALIDATED CAP',expected_cap,len(manifest['profiles']),'teams',flush=True)
 if badge_stage<8:invoke('FlagSet',c['FLAG_BADGE01_GET']+badge_stage)
assert not issues,issues[:60]
for key in manifest['excluded']:
 tid=trainer_ids[key];check('protected_'+key,invoke('LegendsTrainer_Get',tid,base+tid*ts)==base+tid*ts)
# Verify generated shiny data rather than just the trainer definition bitfield.
for mode in [0,1]:
 invoke('StorageChangeMode',mode,1)
 for key in ['TRAINER_ROXANNE_1','TRAINER_SIDNEY','TRAINER_WALLACE','TRAINER_BRENDAN_ROUTE_110_TREECKO','TRAINER_GRUNT_AQUA_HIDEOUT_1']:
  tid=trainer_ids[key];t=invoke('LegendsTrainer_Get',tid,base+tid*ts);A=0x0203f000
  invoke('CreateNPCTrainerPartyFromTrainer',A,t)
  for slot in range(6):
   mon=A+slot*100
   check('generated_'+str((mode,key,slot)),invoke('GetBoxMonData3',mon,c['MON_DATA_SPECIES'],0)>0)
   shiny=invoke('GetBoxMonData3',mon,c['MON_DATA_IS_SHINY'],0)
   check('one_shiny_ace_'+str((mode,key,slot)),shiny==int(manifest['profiles'][key]['shiny_ace'] and slot==5))
   check('ivs_'+str((mode,key,slot)),all(invoke('GetBoxMonData3',mon,c[f],0)==31 for f in ['MON_DATA_HP_IV','MON_DATA_ATK_IV','MON_DATA_DEF_IV','MON_DATA_SPEED_IV','MON_DATA_SPATK_IV','MON_DATA_SPDEF_IV']))
lib.shutdown()
(R/'docs/features/competitive-full-validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),profiles=len(manifest['profiles']),caps=[16,20,26,32,37,43,49,56,65,100],rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest()),indent=2)+'\n')
print('PASS',len(checks),'full-roster checks')
