"""Blank/Legend Plate quest receipts, item upgrade and old Bag compatibility."""
from pathlib import Path
import tempfile,struct,json,hashlib,zlib
R=Path.cwd()
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'docs/features/legend-plate';D.mkdir(parents=True,exist_ok=True)
plates=['FLAME','SPLASH','ZAP','MEADOW','ICICLE','FIST','TOXIC','EARTH','SKY','MIND','INSECT','STONE','SPOOKY','DRACO','DREAD','IRON','PIXIE']
names=['ITEM_BLANK_PLATE','ITEM_LEGEND_PLATE','ITEM_RIFT_TRACKER','ITEM_OUTFIT_BOX','ITEM_BOTTLE_CAP','ITEMS_COUNT','VAR_LA_RIFT_TRACKER','LA_QUEST_PLATES','LA_QUEST_PLATE_FIRST','FLAG_LA_BLANK_PLATE_RECEIVED','FLAG_LA_LEGEND_PLATE_AWAKENED','FLAG_BADGE01_GET','FLAG_BADGE02_GET','B_OUTCOME_WON','B_OUTCOME_LOST','B_OUTCOME_RAN','B_OUTCOME_CAUGHT','POCKET_ITEMS','sizeof(struct BagPocket)','SECTOR_ID_PKMN_STORAGE_END','BAG_EQUIPMENT']+['ITEM_'+x+'_PLATE' for x in plates]
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "item.h"\n#include "bag_categories.h"\n#include "battle.h"\n#include "save.h"\n#include "legends_quests.h"\n#include "constants/flags.h"\n#include "constants/vars.h"\nconst unsigned v[]={'+','.join(names)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 c=dict(zip(names,struct.unpack('<'+str(len(names))+'I',(td/'c.bin').read_bytes())))
checks=[]
def check(n,v):checks.append(dict(test=n,passed=bool(v)));assert v,n
def qty(item):return invoke('CountTotalItemQuantityInBag',c[item])
def plate_call(name,index):
 wr(symbols['gSpecialVar_0x8004'],index,2);invoke(name);return rd(symbols['gSpecialVar_Result'],2)
def qstate(i):return invoke('LegendsQuest_State',c['LA_QUEST_PLATE_FIRST']+i)
def show_relic(item,label):
 invoke('GoToBagMenu',0,c['BAG_EQUIPMENT'],symbols['CB2_ReturnToField']|1)
 wr(symbols['gMain']+4,symbols['CB2_Bag']|1);frames(180);wait('Task_BagMenu_HandleInput')
 index=next(i for i in range(invoke('BagCategory_Count',c['BAG_EQUIPMENT'])) if invoke('BagCategory_GetItem',c['BAG_EQUIPMENT'],i)==c[item])
 for i in range(index):tap(128)
 frames(20);shutil.copy2(shot(label+'_icon'),D/(label+'_icon.png'))
 tap(1);frames(20);tap(1);frames(400);shutil.copy2(shot(label+'_progress'),D/(label+'_progress.png'))
 for i in range(4):tap(2);frames(60)
 check(label+'_Bag_returns_cleanly',rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1)

mg=json.loads((R/'data/maps/map_groups.json').read_text())
for group,gname in enumerate(mg['group_order']):
 if 'LittlerootTown_ProfessorBirchsLab' in mg[gname]:mid=mg[gname].index('LittlerootTown_ProfessorBirchsLab');break
for mode in [0,1]:
 print('PLATES',mode,flush=True);start(0);invoke('StorageChangeMode',mode,1)
 check(f'{mode}_no_research_before_tracker',invoke('LegendsPlates_StartResearch')==0)
 check(f'{mode}_no_guardian_before_research',plate_call('LegendsPlates_ActivateQuest',0)==0)
 invoke('VarSet',c['VAR_LA_RIFT_TRACKER'],2)
 check(f'{mode}_research_grants_blank',invoke('LegendsPlates_StartResearch')==1 and qty('ITEM_BLANK_PLATE')==1)
 check(f'{mode}_no_duplicate_blank',invoke('LegendsPlates_StartResearch')==0 and qty('ITEM_BLANK_PLATE')==1)
 if mode==0:show_relic('ITEM_BLANK_PLATE','blank')
 category=invoke('GetItemBagCategory',c['ITEM_FLAME_PLATE'])
 check(f'{mode}_same_category_as_Plates',invoke('GetItemBagCategory',c['ITEM_BLANK_PLATE'])==category and invoke('GetItemBagCategory',c['ITEM_LEGEND_PLATE'])==category)
 check(f'{mode}_relics_protected',invoke('GetItemImportance',c['ITEM_BLANK_PLATE'])==1 and invoke('GetItemImportance',c['ITEM_LEGEND_PLATE'])==1)
 check(f'{mode}_not_in_store',invoke('LegendsStore_ItemAllowed',c['ITEM_BLANK_PLATE'])==0 and invoke('LegendsStore_ItemAllowed',c['ITEM_LEGEND_PLATE'])==0)
 for x in plates:invoke('AddBagItem',c['ITEM_'+x+'_PLATE'],1)
 check(f'{mode}_ownership_never_bypasses_guardians',invoke('LegendsPlates_CountCompleted')==0 and all(qstate(i)==0 for i in range(17)) and invoke('LegendsPlates_TryAwaken')==0)
 check(f'{mode}_invalid_guardian_rejected',plate_call('LegendsPlates_ActivateQuest',17)==0 and plate_call('LegendsPlates_RecordGuardianResult',65535)==0 and plate_call('LegendsPlates_CollectResonance',17)==0)
 for i in range(17):
  check(f'{mode}_{i}_activate',plate_call('LegendsPlates_ActivateQuest',i)==1 and qstate(i)==1)
  for outcome in ['LOST','RAN','CAUGHT']:
   wr(symbols['gBattleOutcome'],c['B_OUTCOME_'+outcome],1)
   check(f'{mode}_{i}_{outcome}_not_completed',plate_call('LegendsPlates_RecordGuardianResult',i)==0 and qstate(i)==1)
  wr(symbols['gBattleOutcome'],c['B_OUTCOME_WON'],1)
  check(f'{mode}_{i}_victory_ready',plate_call('LegendsPlates_RecordGuardianResult',i)==1 and qstate(i)==2 and invoke('LegendsPlates_CountCompleted')==i)
  if i==0:
   wr(symbols['gSpecialVar_0x8004'],c['LA_QUEST_PLATE_FIRST'],2);invoke('LegendsQuest_Claim')
   check(f'{mode}_guardian_menu_cannot_alias_Gym_flags',rd(symbols['gSpecialVar_Result'],2)==4 and invoke('FlagGet',c['FLAG_BADGE02_GET'])==0)
   cap=symbols['gBagPockets']+c['POCKET_ITEMS']*c['sizeof(struct BagPocket)']+4;old=rd(cap,2);wr(cap,old&~1023,2)
   check(f'{mode}_full_Bag_keeps_victory_pending',plate_call('LegendsPlates_CollectResonance',i)==2 and qstate(i)==2)
   wr(cap,old,2)
  if i==16:check(f'{mode}_uncollected_last_reward_not_complete',invoke('LegendsPlates_TryAwaken')==0)
  check(f'{mode}_{i}_claim',plate_call('LegendsPlates_CollectResonance',i)==1 and qstate(i)==3 and invoke('LegendsPlates_CountCompleted')==i+1)
  check(f'{mode}_{i}_no_duplicate',plate_call('LegendsPlates_CollectResonance',i)==0 and plate_call('LegendsPlates_ActivateQuest',i)==0 and qty('ITEM_'+plates[i]+'_PLATE')==1)
 check(f'{mode}_not_awakened_outside_lab',invoke('LegendsPlates_TryAwaken')==0)
 check(f'{mode}_ready_quest',invoke('LegendsQuest_State',c['LA_QUEST_PLATES'])==2)
 # New quest IDs must never alias the old ledger's Gym flags.
 check(f'{mode}_gym_flags_untouched',invoke('FlagGet',c['FLAG_BADGE01_GET'])==0 and invoke('FlagGet',c['FLAG_BADGE02_GET'])==0)
 warp(group,mid,6,5)
 wr(symbols['gSpecialVar_0x8004'],c['LA_QUEST_PLATES'],2);invoke('LegendsQuest_Claim')
 check(f'{mode}_menu_directs_to_scene',rd(symbols['gSpecialVar_Result'],2)==4 and qty('ITEM_BLANK_PLATE')==1)
 check(f'{mode}_awaken',invoke('LegendsPlates_TryAwaken')==1 and qty('ITEM_BLANK_PLATE')==0 and qty('ITEM_LEGEND_PLATE')==1)
 check(f'{mode}_normal_Plates_retained',all(qty('ITEM_'+x+'_PLATE')==1 for x in plates))
 check(f'{mode}_awakening_idempotent',invoke('LegendsPlates_TryAwaken')==0 and qty('ITEM_LEGEND_PLATE')==1)
 if mode==0:show_relic('ITEM_LEGEND_PLATE','legend')
 check(f'{mode}_save',invoke('TrySavingData',0)==1)
 check(f'{mode}_reload',invoke('LoadGameSave',0)==1)
 check(f'{mode}_persistent_research',invoke('LegendsPlates_CountCompleted')==17 and qty('ITEM_LEGEND_PLATE')==1 and qty('ITEM_BLANK_PLATE')==0 and invoke('LegendsQuest_State',c['LA_QUEST_PLATES'])==3)
 invoke('LegendsQuests_Open');tid=wait('Task_Quests');frames(20)
 for i in range(64):
  if rd(symbols['gTasks']+tid*40+8+2,2)==c['LA_QUEST_PLATES']:break
  tap(128)
 tap(1);frames(20);shutil.copy2(shot('Plate_quest_'+str(mode)),D/('quest_'+str(mode)+'.png'));tap(2);tap(2);frames(60)
 lib.shutdown()
# Load a packed Bag from the previous 877-item schema into this expanded build.
start(0);legacy_count=c['ITEM_BLANK_PLATE'];raw=bytearray(((legacy_count-1)*10+7)//8)
for item,n in [(c['ITEM_OUTFIT_BOX'],1),(c['ITEM_BOTTLE_CAP'],7)]:
 bit=(item-1)*10
 for j in range(10):
  if n>>j&1:raw[(bit+j)//8]|=1<<((bit+j)%8)
sector=bytearray(32)+struct.pack('<IIII',0x33474142,legacy_count,len(raw),zlib.crc32(raw))+raw
A=0x03007400
for i,v in enumerate(sector):wr(A+i,v,1)
invoke('ExpandedBag_BeginLoad');invoke('ExpandedBag_ReadSector',c['SECTOR_ID_PKMN_STORAGE_END'],A,32)
check('legacy_Bag_items_retained',qty('ITEM_OUTFIT_BOX')==1 and qty('ITEM_BOTTLE_CAP')==7)
check('legacy_Bag_new_slots_empty',qty('ITEM_BLANK_PLATE')==0 and qty('ITEM_LEGEND_PLATE')==0)
lib.shutdown()
(D/'validation.json').write_text(json.dumps(dict(checks=checks,user_save_loaded=False,rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest()),indent=2)+'\n')
print('PASS',len(checks),'Plate foundation checks',flush=True)
