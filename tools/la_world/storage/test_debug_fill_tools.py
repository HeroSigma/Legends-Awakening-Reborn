"""Full bag capacity, versioned migration, and terminating PC fills. Isolated flash only."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'.la_work/debug-fill-tests';D.mkdir(exist_ok=True)
import tempfile,struct
names=['ITEM_TM51','ITEM_TM100','ITEMS_COUNT','NUM_SPECIES','MON_DATA_SPECIES','MON_DATA_SANITY_HAS_SPECIES','ITEM_POTION','ITEM_STELLAR_TERA_SHARD','ITEM_CHARIZARDITE_X','ITEM_MACH_BIKE','BAG_CATEGORIES_COUNT','BAG_EQUIPMENT','offsetof(struct SaveBlock1,bag)','sizeof(struct Bag)','offsetof(struct BagPosition,pocket)','offsetof(struct BagMenu,numItemStacks)']
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "pokemon.h"\n#include "item_menu.h"\n#include <stddef.h>\nconst unsigned v[]={'+','.join(names)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 c=dict(zip(names,struct.unpack('<'+str(len(names))+'I',(td/'c.bin').read_bytes())))
def qty(item):return invoke('CountTotalItemQuantityInBag',item)
def mon(box,slot):return invoke('GetBoxMonDataAt',box,slot,c['MON_DATA_SPECIES'])
def flash():
 image=bytearray()
 for sector in range(32):
  invoke('ReadFlash',sector,0,symbols['gSaveDataBuffer'],4096)
  image.extend(rd(symbols['gSaveDataBuffer']+i,1) for i in range(4096))
 return bytes(image)
invalid=set(range(c['ITEM_TM51'],c['ITEM_TM100']+1))
for mode in [0,1]:
 start(0);invoke('StorageChangeMode',mode,1)
 # Manufacture an old-format bag and save with the retained legacy writer.
 invoke('ExpandedBag_Suspend')
 bag=rd(symbols['gSaveBlock1Ptr'])+c['offsetof(struct SaveBlock1,bag)']
 for i in range(c['sizeof(struct Bag)']):wr(bag+i,0,1)
 invoke('AddBagItem',c['ITEM_POTION'],12);invoke('AddBagItem',c['ITEM_CHARIZARDITE_X'],3)
 check('legacy_save_'+str(mode),invoke('TrySavingData',0)==1)
 check('legacy_reload_'+str(mode),invoke('LoadGameSave',0)==1)
 check('legacy_migrated_'+str(mode),invoke('ExpandedBag_Active')==1)
 check('legacy_quantities_'+str(mode),qty(c['ITEM_POTION'])==12 and qty(c['ITEM_CHARIZARDITE_X'])==3)
 check('fill_all_'+str(mode),invoke('Debug_FillBagCategory',c['BAG_CATEGORIES_COUNT'])==c['ITEMS_COUNT']-1-len(invalid))
 counts={i:invoke('BagCategory_Count',i) for i in range(c['BAG_CATEGORIES_COUNT'])}
 check('all_items_have_home_'+str(mode),sum(counts.values())==c['ITEMS_COUNT']-1-len(invalid))
 expected={}
 for item in range(1,c['ITEMS_COUNT']):
  target=1 if invoke('GetItemImportance',item) or invoke('GetItemPocket',item)==2 else 999
  # Existing quantities of an important item are never reduced.
  target=max(target,3 if item==c['ITEM_CHARIZARDITE_X'] else 0)
  if item in invalid:target=0
  expected[item]=target
  check('full_quantity_'+str((mode,item)),qty(item)==target)
 check('repeat_fill_no_duplicates_'+str(mode),invoke('Debug_FillBagCategory',c['BAG_CATEGORIES_COUNT'])==0)
 invoke('BagCategory_Sort',c['BAG_EQUIPMENT'],0)
 invoke('MoveSaveBlocks_ResetHeap')
 check('relocation_keeps_last_item_'+str(mode),qty(c['ITEMS_COUNT']-1)==expected[c['ITEMS_COUNT']-1])
 check('expanded_save_'+str(mode),invoke('TrySavingData',0)==1)
 if mode==0:
  # The normal-format bag extension participates in the sector checksum.
  invoke('RemoveBagItem',c['ITEM_POTION'],1)
  check('normal_second_bag_save',invoke('TrySavingData',0)==1)
  counter=rd(symbols['gSaveCounter']);sector=None
  for candidate in range(28):
   invoke('ReadFlash',candidate,0,symbols['gSaveDataBuffer'],4096)
   if rd(symbols['gSaveDataBuffer']+4084,2)==13 and rd(symbols['gSaveDataBuffer']+4092)==counter:
    sector=candidate;break
  check('normal_bag_sector_found',sector is not None)
  original=bytes(rd(symbols['gSaveDataBuffer']+i,1) for i in range(4096))
  wr(symbols['gSaveDataBuffer']+2440,original[2440]^1,1)
  invoke('ProgramFlashSectorAndVerify',sector,symbols['gSaveDataBuffer'])
  check('normal_bag_recovery_load',invoke('LoadGameSave',0) in [1,255])
  check('normal_bag_recovery_previous_generation',qty(c['ITEM_POTION'])==999)
  for i,v in enumerate(original):wr(symbols['gSaveDataBuffer']+i,v,1)
  invoke('ProgramFlashSectorAndVerify',sector,symbols['gSaveDataBuffer'])
  check('normal_restored_latest_load',invoke('LoadGameSave',0)==1)
  check('normal_restored_latest_quantity',qty(c['ITEM_POTION'])==998)
  invoke('AddBagItem',c['ITEM_POTION'],1)
  check('normal_restored_inventory_save',invoke('TrySavingData',0)==1)
 if mode:
  from collection_format import newest
  schema=json.loads((R/'docs/la_world/compact_pc/layout_audit.json').read_text())
  bank,decoded=newest(schema,flash())
  check('host_v3_decoder',decoded['version']==3 and decoded['bag_quantities']==expected)
 invoke('ClearBag');check('expanded_reload_'+str(mode),invoke('LoadGameSave',0)==1)
 for item in range(1,c['ITEMS_COUNT']):check('loaded_quantity_'+str((mode,item)),qty(item)==expected[item])
 check('profile_unchanged_'+str(mode),invoke('GetStorageBoxCount')==(60 if mode else 14))
 # All 198 equipment entries, including the end of the list, must be usable.
 invoke('GoToBagMenu',0,c['BAG_EQUIPMENT'],symbols['CB2_ReturnToField']|1)
 wr(symbols['gMain']+4,symbols['CB2_Bag']|1);frames(150)
 check('full_bag_ui_'+str(mode),active('Task_BagMenu_HandleInput') is not None)
 for _ in range(counts[c['BAG_EQUIPMENT']]-1):tap(128)
 tap(1);frames(20)
 selected=rd(symbols['gSpecialVar_ItemId'],2)
 check('last_equipment_selects_'+str(mode),invoke('GetItemBagCategory',selected)==c['BAG_EQUIPMENT'])
 if mode==0:shutil.copy2(shot('expanded_equipment'),R/'docs/features/expanded-bag-full-equipment.png')
 tap(2);frames(20);tap(2);frames(150)
 lib.shutdown()
# Exercise the real debug menu bindings, not only the underlying fill helpers.
start(0);invoke('StorageChangeMode',1,1);invoke('ClearBag')
invoke('Debug_ShowMainMenu');frames(30)
tap(128);tap(1);frames(20);tap(128);tap(1);frames(20);tap(1);frames(180)
check('debug_menu_fill_bag',sum(invoke('BagCategory_Count',i) for i in range(c['BAG_CATEGORIES_COUNT']))==c['ITEMS_COUNT']-1-len(invalid))
for _ in range(9):tap(128)
tap(1);frames(240)
check('debug_menu_fill_pc',invoke('CountStorageNonEggMons')>1000)
check('debug_menu_pc_stops',invoke('Debug_FillPCBoxes',0)==0)
lib.shutdown()
# Both fill paths preserve existing records, skip owned species and stop at the final one.
for mode,random_ivs in [(0,0),(1,0),(1,1)]:
 start(0);invoke('StorageChangeMode',mode,1);invoke('ScriptGiveMon',25,20,0)
 invoke('StorageWriteMon',0,0,symbols['gParties'])
 expected=[i for i in range(1,c['NUM_SPECIES']) if invoke('IsSpeciesEnabled',i) and i!=25]
 capacity=(60 if mode else 14)*30
 added=invoke('Debug_FillPCBoxes',random_ivs)
 check('pc_added_'+str((mode,random_ivs)),added==min(len(expected),capacity-1))
 check('existing_mon_preserved_'+str((mode,random_ivs)),mon(0,0)==25)
 for n,species in enumerate(expected[:added],1):check('pc_sequence_'+str((mode,random_ivs,n)),mon(n//30,n%30)==species)
 if added<capacity-1:check('no_wrap_after_last_'+str((mode,random_ivs)),mon((added+1)//30,(added+1)%30)==0)
 check('pc_repeat_stops_'+str((mode,random_ivs)),invoke('Debug_FillPCBoxes',random_ivs)==0)
 check('pc_save_'+str((mode,random_ivs)),invoke('TrySavingData',0)==1)
 check('pc_reload_'+str((mode,random_ivs)),invoke('LoadGameSave',0)==1)
 check('pc_last_survives_'+str((mode,random_ivs)),mon(added//30,added%30)==expected[added-1])
 lib.shutdown()
(R/'docs/features/debug-fill-tools-validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'debug fill, full bag and migration checks')
