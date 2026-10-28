"""Native nursery, portable daycare, follower and replant checks; isolated save."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'.la_work/qol_features/remaining-test';D.mkdir(parents=True,exist_ok=True)
start(0)
import tempfile,struct
with tempfile.TemporaryDirectory() as td:
 td=Path(td)
 (td/'c.c').write_text('#include "global.h"\n#include "constants/flags.h"\n#include "constants/layouts.h"\n#include "constants/items.h"\n#include "constants/berry.h"\n#include <stddef.h>\nconst unsigned values[]={FLAG_RETURNED_DEVON_GOODS,FLAG_RECEIVED_POKENAV,FLAG_LANDMARK_POKEMON_DAYCARE,FLAG_LA_TIMELESS_WOODS_CONSPIRACY_SEEN,MON_DATA_FRIENDSHIP,MON_DATA_IS_EGG,MON_DATA_SANITY_IS_BAD_EGG,MON_DATA_SPECIES,LAYOUT_HYPERHOENN_34_67_TIMELESS_WOODS,LAYOUT_HYPERHOENN_34_10_BASEMENT,ITEM_ORAN_BERRY,BERRY_ID_ORAN,BERRY_STAGE_BERRIES,BERRY_STAGE_PLANTED,offsetof(struct SaveBlock1,daycare),offsetof(struct DayCare,stepCounter),MON_DATA_PERSONALITY,MON_DATA_MOVE1,MON_DATA_IVS,FLAG_SYS_POKEMON_GET,offsetof(struct SaveBlock1,berryTrees),sizeof(struct BerryTree)};\n')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 c=struct.unpack('<22I',(td/'c.bin').read_bytes())
goods,nav,registered,seen,friend,egg,bad,species,woods,basement,oran,berry,ripe,planted,dayoff,stepoff,pid,move,ivs,partyflag,treeoff,treesize=c
A=0x0203f000;V=A+0x300
invoke('ScriptGiveMon',1,10,0)
party=symbols['gParties']
def setdata(field,value):
 wr(V,value);invoke('SetMonData',A,field,V)
def flags(g,n):
 invoke('FlagSet' if g else 'FlagClear',goods);invoke('FlagSet' if n else 'FlagClear',nav)
for mode in [0,1]:
 invoke('StorageChangeMode',mode,1)
 invoke('CreateEgg',A,133,0);setdata(friend,3)
 invoke('SetBoxMonAt',0,29,A);invoke('SetBoxMonAt',1,0,A)
 before=[invoke('GetBoxMonDataAt',0,29,f) for f in [pid,move,ivs]]
 for g,n in [(0,0),(1,0),(0,1)]:
  flags(g,n);invoke('LegendsNursery_AdvanceCycle',1)
  check('nursery_locked_'+str((mode,g,n)),invoke('GetBoxMonDataAt',0,29,friend)==3)
 flags(1,1)
 invoke('LegendsNursery_AdvanceCycle',2)
 check('nursery_progress_'+str(mode),invoke('GetBoxMonDataAt',0,29,friend)==1)
 check('other_boxes_paused_'+str(mode),invoke('GetBoxMonDataAt',1,0,friend)==3)
 invoke('LegendsNursery_AdvanceCycle',2);invoke('LegendsNursery_AdvanceCycle',2)
 check('nursery_zero_floor_'+str(mode),invoke('GetBoxMonDataAt',0,29,friend)==0)
 check('still_egg_'+str(mode),invoke('GetBoxMonDataAt',0,29,egg)==1)
 check('inheritance_unchanged_'+str(mode),before==[invoke('GetBoxMonDataAt',0,29,f) for f in [pid,move,ivs]])
 # Normal Pokemon must not lose friendship in nursery.
 invoke('SetBoxMonAt',0,0,party)
 beforefriend=invoke('GetBoxMonDataAt',0,0,friend)
 invoke('LegendsNursery_AdvanceCycle',2)
 check('non_egg_friendship_'+str(mode),invoke('GetBoxMonDataAt',0,0,friend)==beforefriend)
 # The actual walking-cycle hatch checker advances nursery eggs.
 invoke('SetBoxMonAt',0,28,A)
 save1=rd(symbols['gSaveBlock1Ptr']);wr(save1+dayoff+stepoff,127,1)
 invoke('ShouldEggHatch')
 check('native_step_hook_'+str(mode),invoke('GetBoxMonDataAt',0,28,friend)<3)
 invoke('StorageFlush');check('nursery_save_'+str(mode),invoke('TrySavingData',0)==1)
 invoke('StorageInitialize');check('nursery_load_'+str(mode),invoke('LoadGameSave',0)==1)
 check('saved_ready_egg_'+str(mode),invoke('GetBoxMonDataAt',0,29,friend)==0 and invoke('GetBoxMonDataAt',0,29,egg)==1)
 # Replant spends exactly one berry and resets to the normal growing stage.
 invoke('PlantBerryTree',0,berry,ripe,1);invoke('AddBagItem',oran,3)
 check('replant_'+str(mode),invoke('LegendsBerry_Replant',0)==1)
 check('planted_'+str(mode),invoke('GetStageByBerryTreeId',0)==planted)
 check('cannot_double_replant_'+str(mode),invoke('LegendsBerry_Replant',0)==0)
 check('one_seed_spent_'+str(mode),invoke('CheckBagHasItem',oran,3)==0 and invoke('CheckBagHasItem',oran,2)==1)
 invoke('RemoveBagItem',oran,2)
 invoke('PlantBerryTree',0,berry,ripe,1)
 check('no_seed_no_replant_'+str(mode),invoke('LegendsBerry_Replant',0)==0 and invoke('GetStageByBerryTreeId',0)==ripe)
 check('invalid_tree_'+str(mode),invoke('LegendsBerry_Replant',255)==0)
 check('berries_save_'+str(mode),invoke('TrySavingData',0)==1)
 invoke('RemoveBerryTree',0);invoke('LoadGameSave',0)
 check('tree_persists_'+str(mode),invoke('GetStageByBerryTreeId',0)==ripe)
 # Native RTC growth progresses the replanted plot; no real-time polling loop.
 invoke('AddBagItem',oran,1);invoke('LegendsBerry_Replant',0)
 invoke('BerryTreeTimeUpdate',180)
 check('rtc_regrowth_'+str(mode),invoke('GetStageByBerryTreeId',0)>planted)
# Contextual text changes only after the actual conspiracy flag.
invoke('FlagClear',seen)
base=invoke('LegendsFollower_EnvironmentalText',woods)
check('woods_hint_exists',base!=0)
invoke('FlagSet',seen)
check('woods_hint_changes',invoke('LegendsFollower_EnvironmentalText',woods)!=base)
check('devon_hint_exists',invoke('LegendsFollower_EnvironmentalText',basement)!=0)
check('ordinary_map_native_reactions',invoke('LegendsFollower_EnvironmentalText',0)==0)
check('follower_no_flag_writes',invoke('FlagGet',seen)==1)
# Real journal SELECT handoff; script dialogues auto-advance only within test.
invoke('FlagSet',partyflag)
def remote_open():
 invoke('AdventureJournal_Open');frames(20);tap(4);frames(20)
 check('journal_handoff_'+str(len(checks)),active('Task_AdventureJournal') is None)
def drain(n=500):
 for i in range(n):frames(1,1 if i%24<2 else 0)
flags(0,0);remote_open();drain()
check('locked_remote_returns',rd(symbols['sGlobalScriptContextStatus'],1)==2)
flags(1,1);invoke('FlagClear',registered);remote_open();drain()
check('unregistered_remote_returns',rd(symbols['sGlobalScriptContextStatus'],1)==2)
# Exercise parent menu cancellation from a real remote call (no map actor).
invoke('FlagSet',registered);invoke('ScriptGiveMon',4,10,0);invoke('ScriptGiveMon',7,10,0)
remote_open();drain(350)
# Cancel any outstanding party/PC chooser and the native followup dialogue.
for i in range(20):tap(2);frames(15)
drain(250)
check('remote_cancel_returns',rd(symbols['sGlobalScriptContextStatus'],1)==2)
# A real remote retrieval must avoid moving the current map's NPCs.
wr(symbols['gSpecialVar_0x8004'],1,2);invoke('StoreSelectedPokemonInDaycare')
check('one_parent_deposited',invoke('GetDaycareState')==2)
invoke('AddMoney',10000)
remote_open();drain(1000)
# With one parent the native dialogue first offers the second slot; cancel it,
# then approve retrieval and its fee.
for i in range(25):tap(2);frames(10)
drain(100)
# Invoke the production remote retrieval branch with the native fee prepared.
wr(symbols['gSpecialVar_0x8004'],0,2);invoke('GetDaycareCostAndPrepareString')
invoke('ScriptContext_SetupScript',symbols['LegendsDaycare_RetrieveRemote']);drain(1000)
for i in range(12):tap(2);frames(10)
check('remote_retrieval_complete',invoke('GetDaycareState')==0)
check('retrieval_script_finished',rd(symbols['sGlobalScriptContextStatus'],1)==2)
# Compatible parents and the native pending-egg path are shared locally/remotely.
invoke('ScriptGiveMon',132,10,0)
count=invoke('CalculatePlayerPartyCount')
wr(symbols['gSpecialVar_0x8004'],count-1,2);invoke('StoreSelectedPokemonInDaycare')
parent_species=invoke('GetBoxMonData3',party+100,species,0)
wr(symbols['gSpecialVar_0x8004'],1,2);invoke('StoreSelectedPokemonInDaycare')
check('two_parents_shared',invoke('GetDaycareState')==3)
# Fill party and prove remote collection leaves a pending egg untouched.
while invoke('CalculatePlayerPartyCount')<6:invoke('ScriptGiveMon',25,5,0)
invoke('TriggerPendingDaycareEgg')
invoke('ScriptContext_SetupScript',symbols['LegendsDaycare_AskEgg']);drain(1000)
check('remote_full_party_keeps_egg',invoke('GetDaycareState')==1)
invoke('ZeroMonData',party+500);invoke('CalculatePlayerPartyCount')
invoke('ScriptContext_SetupScript',symbols['LegendsDaycare_AskEgg']);drain(1200)
check('remote_egg_delivered',invoke('CalculatePlayerPartyCount')==6 and invoke('GetDaycareState')==3)
check('remote_egg_is_egg',invoke('GetBoxMonData3',party+500,egg,0)==1)
check('remote_egg_species_inherits',invoke('GetBoxMonData3',party+500,species,0)==parent_species)
check('egg_script_finished',rd(symbols['sGlobalScriptContextStatus'],1)==2)
shutil.copy2(shot('remote_daycare_return'),D/'remote_return.png')
lib.shutdown()
(R/'docs/features/remaining-qol-validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'remaining QoL checks')
