"""First visits, retry choices and battle/reward parity in disposable saves."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_woods_triad_story.py').read_text().split('for gender,mode,x in ')[0],'woods_helpers','exec'))
D=R/'docs/features/repeat-scenes';D.mkdir(parents=True,exist_ok=True)
checks=[]
def check(n,v):
 checks.append(dict(test=n,passed=bool(v)));assert v,n
names=['FLAG_LA_SEEN_ROUTE103_INTRO','FLAG_LA_SEEN_WOODS_TRIAD_INTRO','FLAG_LA_SEEN_RUSTURF_GRUNT_INTRO','MAP_GROUP(MAP_RUSTURF_TUNNEL)','MAP_NUM(MAP_RUSTURF_TUNNEL)','VAR_RUSTURF_TUNNEL_STATE','LOCALID_RUSTURF_TUNNEL_GRUNT','VAR_LAST_TALKED','FLAG_HIDE_RUSTURF_TUNNEL_AQUA_GRUNT','ITEM_DEVON_PARTS','FLAG_RECOVERED_DEVON_GOODS','FLAG_LA_RED_ROUTE103_COMPLETE','FLAG_LA_WOODS_TRIAD_COMPLETE','FLAG_LA_RED_LAB_COMPLETE','VAR_LA_LITTLEROOT_ARC','VAR_BIRCH_LAB_STATE']
# Optional story milestones are read directly from the project's current constants.
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "constants/maps.h"\n#include "constants/map_event_ids.h"\nconst unsigned v[]={'+','.join(names)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 c.update(zip(names,struct.unpack('<'+str(len(names))+'I',(td/'c.bin').read_bytes())))
intro={'route':'LegendsArc_Text_BrendanRecognizes','woods':'LegendsWoods_Text_Scope','rusturf':'RusturfTunnel_Text_GruntIntro'}
seenflags={'route':c[names[0]],'woods':c[names[1]],'rusturf':c[names[2]]}
def matches(label):
 return any(all(rd(symbols['gStringVar4']+o+j,1)==rd(symbols[label]+j,1) for j in range(10)) for o in [0,3])
def progress_to_battle(scene,seen,skip):
 prompted=False;heard=False
 for i in range(18000):
  heard |= matches(intro[scene])
  if active('Task_HandleYesNoInput') is not None:
   check('correct_prompt_'+scene,matches('LegendsScene_Text_SkipConversation'))
   check('never_prompt_first_'+scene,seen)
   if not prompted:
    frames(20);shutil.copy2(shot('skip_'+scene),D/(scene+'_prompt.png'))
    if not skip:tap(128)
    tap(1);prompted=True
  if rd(symbols['gMain']+4)==symbols['BattleMainCB2']|1:
   frames(240);break
  frames(1,1 if i%31<4 else 0)
 else:raise AssertionError('battle timeout '+scene)
 check('prompt_matches_seen_'+scene,prompted==seen)
 check('intro_matches_choice_'+scene,heard==(not seen or not skip))
 check('seen_recorded_'+scene,invoke('FlagGet',seenflags[scene])==1)
 return heard
for mode in [0,1]:
 for scene in ['route','woods','rusturf']:
  for seen,skip in [(False,False),(True,False),(True,True)]:
   print("CASE",mode,scene,seen,skip,flush=True)
   setup(mode,mode,False)
   invoke('FlagClear',seenflags[scene])
   if seen:invoke('FlagSet',seenflags[scene])
   if scene=='woods':enter(35)
   elif scene=='route':
    invoke('FlagSet',c['FLAG_LA_RED_LAB_COMPLETE']);invoke('VarSet',c['VAR_LA_LITTLEROOT_ARC'],2);invoke('VarSet',c['VAR_BIRCH_LAB_STATE'],3)
    invoke('RecordStarterChoice',3);warp(0,18,6,6);move(64,1)
   else:
    invoke('FlagClear',c['FLAG_HIDE_RUSTURF_TUNNEL_AQUA_GRUNT']);invoke('VarSet',c['VAR_RUSTURF_TUNNEL_STATE'],2)
    warp(c['MAP_GROUP(MAP_RUSTURF_TUNNEL)'],c['MAP_NUM(MAP_RUSTURF_TUNNEL)'],12,5);frames(60)
    invoke('VarSet',c['VAR_LAST_TALKED'],c['LOCALID_RUSTURF_TUNNEL_GRUNT']);invoke('ScriptContext_SetupScript',symbols['RusturfTunnel_EventScript_Grunt'])
   progress_to_battle(scene,seen,skip)
   check('battle_format_'+scene,bool(rd(symbols['gBattleTypeFlags'])&1)==(scene=='route'))
   check('no_early_parts_'+scene,invoke('CheckBagHasItem',c['ITEM_DEVON_PARTS'],1)==0)
   if scene=='woods':
    check('woods_staging_'+str((mode,seen,skip)),actor_position('LOCALID_PETALBURG_WOODS_DEVON_EMPLOYEE')==(36,20) and actor_position('LOCALID_WOODS_SILPH')==(36,18) and actor_position('LOCALID_PETALBURG_WOODS_GRUNT')==(35,19))
   finish(1)
   for i in range(18000):
    if rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1 and rd(symbols['sGlobalScriptContextStatus'],1)==2:break
    frames(1,1 if i%31<4 else 0)
   else:raise AssertionError('completion timeout '+scene)
   check('controls_restored_'+scene,invoke('ArePlayerFieldControlsLocked')==0)
   if scene=='route':check('route_completed',invoke('FlagGet',c['FLAG_LA_RED_ROUTE103_COMPLETE'])==1)
   elif scene=='woods':check('woods_reward',invoke('FlagGet',c['FLAG_LA_WOODS_TRIAD_COMPLETE'])==1 and invoke('CheckBagHasItem',c['ITEM_POKEVIAL'],1)==1 and invoke('CountTotalItemQuantityInBag',c['ITEM_GREAT_BALL'])==1)
   else:check('parts_received',invoke('CountTotalItemQuantityInBag',c['ITEM_DEVON_PARTS'])==1)
   check('save',invoke('TrySavingData',0)==1)
   invoke('FlagClear',seenflags[scene]);check('load',invoke('LoadGameSave',0)==1)
   check('seen_persists',invoke('FlagGet',seenflags[scene])==1)
   lib.shutdown()
(D/'validation.json').write_text(json.dumps(dict(rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks,user_save_loaded=False,battle_outcomes='Injected using native end handlers; this suite tests scene and reward state, not difficulty.'),indent=2)+'\n')
print('PASS',len(checks),'repeat-scene checks',flush=True)
