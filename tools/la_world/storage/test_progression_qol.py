"""Native progression gates and real wild-battle Strange Ball dispatch."""
from pathlib import Path
import tempfile,subprocess,struct,json,hashlib,shutil
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'docs/features/progression-qol';D.mkdir(parents=True,exist_ok=True)
checks=[]
def check(n,v):
 checks.append(dict(test=n,passed=bool(v)));assert v,n
species=['POOCHYENA','DITTO','MEWTWO','MEW','ARTICUNO','NIHILEGO','IRON_VALIANT','MIRAIDON']
names=['ITEM_STRANGE_BALL','ITEM_MASTER_BALL','ITEM_EXP_SHARE','I_EXP_SHARE_FLAG','FLAG_RECEIVED_EXP_SHARE','FLAG_BADGE01_GET','FLAG_BADGE02_GET','FLAG_SYS_GAME_CLEAR','FLAG_LA_MIRAIDON_BATTLE','FLAG_LA_BIRCH_RESCUE_BATTLE','BATTLE_TYPE_FIRST_BATTLE','BATTLE_TYPE_TRAINER','BATTLE_TYPE_RAID','sizeof(struct BattlePokemon)','offsetof(struct BattlePokemon,species)','offsetof(struct SaveBlock1,money)','SUMMARY_MODE_NORMAL']+['SPECIES_'+x for x in species]
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "pokemon.h"\n#include "battle.h"\n#include "item.h"\n#include "constants/flags.h"\n#include "pokemon_summary_screen.h"\n#include "pokemon_storage_system.h"\n#include <stddef.h>\nconst unsigned v[]={'+','.join(names)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 c=dict(zip(names,struct.unpack('<'+str(len(names))+'I',(td/'c.bin').read_bytes())))
def snap(n):shutil.copy2(shot('progression_'+n),D/(n+'.png'))
start(0)
check('start_has_ExpShare',invoke('CheckBagHasItem',c['ITEM_EXP_SHARE'],1)==1)
check('start_ExpShare_ON',invoke('FlagGet',c['I_EXP_SHARE_FLAG'])==1)
invoke('FlagClear',c['I_EXP_SHARE_FLAG']);invoke('ProgressionQol_EnsureExpShare')
check('existing_OFF_preserved',invoke('FlagGet',c['I_EXP_SHARE_FLAG'])==0)
check('no_duplicate_ExpShare',invoke('CountTotalItemQuantityInBag',c['ITEM_EXP_SHARE'])==1)
invoke('RemoveBagItem',c['ITEM_EXP_SHARE'],1);invoke('ProgressionQol_EnsureExpShare')
check('older_save_gets_ExpShare',invoke('CheckBagHasItem',c['ITEM_EXP_SHARE'],1)==1 and invoke('FlagGet',c['I_EXP_SHARE_FLAG'])==1)
check('StrangeBall_not_sold',invoke('LegendsStore_ItemAllowed',c['ITEM_STRANGE_BALL'])==0)
check('Master_before_League',invoke('LegendsStore_ItemAllowed',c['ITEM_MASTER_BALL'])==0)
invoke('SetMoney',rd(symbols['gSaveBlock1Ptr'])+c['offsetof(struct SaveBlock1,money)'],999999)
check('Master_purchase_blocked',invoke('LegendsStore_Buy',c['ITEM_MASTER_BALL'],1,99)==1)
invoke('FlagSet',c['FLAG_SYS_GAME_CLEAR'])
check('Master_after_League',invoke('LegendsStore_ItemAllowed',c['ITEM_MASTER_BALL'])==1)
check('Master_purchase_unlocked',invoke('LegendsStore_Buy',c['ITEM_MASTER_BALL'],1,99)==0)
invoke('FlagClear',c['FLAG_SYS_GAME_CLEAR'])
check('summary_locked_no_badges',invoke('StatEditor_IsUnlocked')==0)
invoke('FlagSet',c['FLAG_BADGE01_GET']);check('summary_locked_after_Roxanne',invoke('StatEditor_IsUnlocked')==0)
invoke('FlagSet',c['FLAG_BADGE02_GET']);check('summary_unlocked_after_Brawly',invoke('StatEditor_IsUnlocked')==1)
for flag in ['FLAG_BADGE01_GET','FLAG_BADGE02_GET']:invoke('FlagClear',c[flag])
invoke('ScriptGiveMon',c['SPECIES_MEWTWO'],70,0)
invoke('ScriptContext_SetupScript',symbols['LegendsTraining_Scientist']);frames(60);snap('scientist_locked')
expected=bytes(rd(symbols['LegendsTraining_Text_Locked']+i,1) for i in range(12))
check('scientist_locked_script',bytes(rd(symbols['gStringVar4']+i,1) for i in range(12))==expected)
for i in range(8):tap(1);frames(20)
check('scientist_did_not_open_party',invoke('ArePlayerFieldControlsLocked')==0)
# Verify the actual summary shortcut is blocked, not only the unlock predicate.
invoke('ShowPokemonSummaryScreen_SwSh',c['SUMMARY_MODE_NORMAL'],symbols['gParties'],0,0,symbols['CB2_ReturnToField']|1)
wr(symbols['gMain']+4,symbols['CB2_InitSummaryScreen']|1);wait('Task_HandleInput',1800);frames(40);tap(16);frames(60)
tap(8);frames(80);check('summary_actual_no_badge_block',active('Task_StatEditorMain') is None)
invoke('FlagSet',c['FLAG_BADGE01_GET']);tap(8);frames(80);check('summary_actual_one_badge_block',active('Task_StatEditorMain') is None)
invoke('FlagSet',c['FLAG_BADGE02_GET']);tap(8);wait('Task_StatEditorMain',1800);frames(30)
check('summary_actual_two_badge_open',active('Task_StatEditorMain') is not None);snap('summary_editor_unlocked')
tap(2);wait('Task_HandleInput',1800);tap(2);frames(180)
lib.shutdown()
start(0);invoke('FlagSet',c['FLAG_BADGE01_GET']);invoke('ScriptGiveMon',c['SPECIES_MEWTWO'],16,0)
invoke('ScriptContext_SetupScript',symbols['LegendsTraining_Scientist'])
for i in range(2400):
 if active('Task_HandleChooseMonInput') is not None:break
 frames(1,1 if i%20==0 else 0)
else:raise AssertionError('Unlocked scientist did not open party')
check('scientist_actual_after_Roxanne',active('Task_HandleChooseMonInput') is not None)
tap(2);frames(180)
lib.shutdown()
# Each capture test uses a genuine initialized wild battle. Stop at the native
# dispatch result so no user battery or scripted turn sequence is involved.
for name,expected in [('POOCHYENA',False),('DITTO',False),('MEWTWO',True),('MEW',True),('ARTICUNO',True),('NIHILEGO',False),('IRON_VALIANT',False),('MIRAIDON',True)]:
 start(0);invoke('ScriptGiveMon',c['SPECIES_MEWTWO'],70,0)
 check(name+'_classification',bool(invoke('StrangeBall_CanCatch',c['SPECIES_'+name]))==expected)
 invoke('CreateScriptedWildMon',c['SPECIES_'+name],5,0);invoke('BattleSetup_StartWildBattle');frames(600)
 if name=='MEWTWO':
  check('Master_ball_use_locked',invoke('CannotUseItemsInBattle',c['ITEM_MASTER_BALL'],symbols['gParties'])==1)
  invoke('FlagSet',c['FLAG_SYS_GAME_CLEAR'])
  check('Master_ball_use_unlocked',invoke('CannotUseItemsInBattle',c['ITEM_MASTER_BALL'],symbols['gParties'])==0)
  invoke('FlagClear',c['FLAG_SYS_GAME_CLEAR'])
 if name=='DITTO':
  wr(symbols['gBattleMons']+c['sizeof(struct BattlePokemon)']+c['offsetof(struct BattlePokemon,species)'],c['SPECIES_MEWTWO'],2)
 # Victory-catch raid overrides must not make an ordinary species catchable.
 if name=='POOCHYENA':wr(symbols['gBattleTypeFlags'],rd(symbols['gBattleTypeFlags'])|c['BATTLE_TYPE_RAID'])
 wr(symbols['gBattlerAttacker'],0,1);wr(symbols['gBattlerTarget'],1,1)
 wr(symbols['gLastUsedItem'],c['ITEM_STRANGE_BALL'],2);wr(symbols['gBattleControllerExecFlags'],0)
 invoke('Cmd_handleballthrow')
 check(name+'_throw_result',rd(symbols['gBattlescriptCurrInstr'])==symbols['BattleScript_SuccessBallThrow' if expected else 'BattleScript_ShakeBallThrow'])
 lib.shutdown()
for name,flag in [('MIRAIDON','FLAG_LA_MIRAIDON_BATTLE'),('IRON_VALIANT','FLAG_LA_BIRCH_RESCUE_BATTLE')]:
 start(0);invoke('ScriptGiveMon',c['SPECIES_MEWTWO'],70,0)
 invoke('CreateScriptedWildMon',c['SPECIES_'+name],70,0);invoke('BattleSetup_StartWildBattle');frames(600)
 invoke('FlagSet',c[flag]);wr(symbols['gBattleTypeFlags'],rd(symbols['gBattleTypeFlags'])|c['BATTLE_TYPE_FIRST_BATTLE'])
 check(name+'_story_lock',invoke('IsStoryBattleCaptureBlocked')==1)
 wr(symbols['gBattlerAttacker'],0,1);wr(symbols['gBattlerTarget'],1,1);wr(symbols['gLastUsedItem'],c['ITEM_STRANGE_BALL'],2);wr(symbols['gBattleControllerExecFlags'],0)
 invoke('Cmd_handleballthrow')
 check(name+'_StrangeBall_blocked',rd(symbols['gBattlescriptCurrInstr'])==symbols['BattleScript_GhostBallDodge'])
 lib.shutdown()
(D/'validation.json').write_text(json.dumps(dict(checks=checks,user_save_loaded=False,rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest()),indent=2)+'\n')
print('PASS',len(checks),'progression/capture checks',flush=True)
