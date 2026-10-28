"""Save-compatible bag category routing and real bag UI in isolated native mGBA."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0], 'helpers', 'exec'))
D=R/'.la_work/bag-categories';D.mkdir(exist_ok=True)
import tempfile,struct
names=['BAG_CATEGORIES_COUNT','ITEMS_COUNT','offsetof(struct BagPosition,pocket)','offsetof(struct BagMenu,numItemStacks)','sizeof(struct Bag)','offsetof(struct SaveBlock1,bag)','MON_DATA_HP','MON_DATA_HELD_ITEM']
samples=[('ITEM_REPEL','BAG_REGULAR'),('ITEM_POKE_BALL','BAG_BALLS'),('ITEM_TM_FOCUS_PUNCH','BAG_MACHINES'),('ITEM_ORAN_BERRY','BAG_BERRIES'),('ITEM_MACH_BIKE','BAG_KEYS'),('ITEM_POTION','BAG_MEDICINE'),('ITEM_SUPER_POTION','BAG_MEDICINE'),('ITEM_CHOICE_SCARF','BAG_EQUIPMENT'),('ITEM_X_ATTACK','BAG_EQUIPMENT'),('ITEM_TIMID_MINT','BAG_TRAINING'),('ITEM_RARE_CANDY','BAG_TRAINING'),('ITEM_FIRE_STONE','BAG_EVOLUTION'),('ITEM_DRAGON_SCALE','BAG_EVOLUTION'),('ITEM_CHARIZARDITE_X','BAG_MEGA_STONES'),('ITEM_CHARIZARDITE_Y','BAG_MEGA_STONES'),('ITEM_NORMALIUM_Z','BAG_Z_CRYSTALS'),('ITEM_STELLAR_TERA_SHARD','BAG_TERA_SHARDS'),('ITEM_FIRE_TERA_SHARD','BAG_TERA_SHARDS'),('ITEM_NUGGET','BAG_TREASURES')]
names+=list(dict.fromkeys(n for pair in samples for n in pair))
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "pokemon.h"\n#include "item_menu.h"\n#include <stddef.h>\nconst unsigned v[]={'+','.join(names)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 c=dict(zip(names,struct.unpack('<'+str(len(names))+'I',(td/'c.bin').read_bytes())))
def category():return rd(symbols['gBagPosition']+c['offsetof(struct BagPosition,pocket)'],1)
def inventory():return {n:invoke('CountTotalItemQuantityInBag',c[n]) for n,_ in samples}
def openbag(cat=0,location=0):
 invoke('GoToBagMenu',location,cat,symbols['CB2_ReturnToField']|1)
 wr(symbols['gMain']+4,symbols['CB2_Bag']|1);frames(180)
 check('bag_open_'+str((cat,location)),active('Task_BagMenu_HandleInput') is not None)
def closebag():
 tap(2);frames(180)
 check('bag_closed',rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1)
for mode in [0,1]:
 start(0);invoke('StorageChangeMode',mode,1);invoke('ClearBag');invoke('ScriptGiveMon',4,16,0)
 for name,cat in samples:
  check('classification_'+str((mode,name)),invoke('GetItemBagCategory',c[name])==c[cat])
  check('add_'+str((mode,name)),invoke('AddBagItem',c[name],3)==1)
 before=inventory()
 counts={i:invoke('BagCategory_Count',i) for i in range(c['BAG_CATEGORIES_COUNT'])}
 check('all_items_once_'+str(mode),sum(counts.values())==len(samples))
 for i in range(c['BAG_CATEGORIES_COUNT']):
  expected={c[n] for n,cat in samples if c[cat]==i}
  got={invoke('BagCategory_GetItem',i,j) for j in range(counts[i])}
  check('category_contents_'+str((mode,i)),got==expected)
  check('cancel_slot_empty_'+str((mode,i)),invoke('BagCategory_GetItem',i,counts[i])==0)
  invoke('BagCategory_Sort',i,0)
  if counts[i]>1:invoke('BagCategory_Move',i,0,counts[i])
 check('sort_move_preserves_quantities_'+str(mode),inventory()==before)
 invoke('MoveSaveBlocks_ResetHeap')
 check('aslr_preserves_inventory_'+str(mode),inventory()==before)
 check('save_'+str(mode),invoke('TrySavingData',0)==1)
 invoke('ClearBag');check('reload_'+str(mode),invoke('LoadGameSave',0)==1)
 check('save_inventory_preserved_'+str(mode),inventory()==before)
 check('storage_mode_preserved_'+str(mode),invoke('GetStorageBoxCount')==(60 if mode else 14))
 openbag()
 for i in range(c['BAG_CATEGORIES_COUNT']):
  check('ui_category_'+str((mode,i)),category()==i)
  stacks=rd(rd(symbols['gBagMenu'])+c['offsetof(struct BagMenu,numItemStacks)']+i,1)
  check('ui_filtered_count_'+str((mode,i)),stacks==counts[i]+1)
  if mode==0 and i in [c['BAG_MEDICINE'],c['BAG_MEGA_STONES'],c['BAG_TERA_SHARDS']]:
   shutil.copy2(shot('category_'+str(i)),R/'docs/features'/('bag-category-'+str(i)+'.png'))
  tap(1);frames(20)
  check('ui_select_correct_item_'+str((mode,i)),invoke('GetItemBagCategory',rd(symbols['gSpecialVar_ItemId'],2))==i)
  tap(2);frames(20)
  tap(16);frames(40)
 check('wrap_forward_'+str(mode),category()==0)
 tap(32);frames(40);check('wrap_backward_'+str(mode),category()==c['BAG_CATEGORIES_COUNT']-1)
 closebag()
 check('browsing_keeps_inventory_'+str(mode),inventory()==before)
 # Toss one item via the real category context menu; neighboring categories survive.
 openbag(c['BAG_TRAINING'])
 tap(1);frames(20);selected=rd(symbols['gSpecialVar_ItemId'],2)
 tap(128);tap(1);frames(25);tap(1);frames(25);tap(1);frames(25);tap(1);frames(40)
 after=inventory()
 check('toss_only_selected_'+str(mode),all(after[n]==q-(1 if c[n]==selected else 0) for n,q in before.items()))
 closebag()
 # Give a Mega Stone from its category through the normal party selector.
 openbag(c['BAG_MEGA_STONES'])
 tap(1);frames(20);selected=rd(symbols['gSpecialVar_ItemId'],2)
 tap(16);tap(1);frames(180);tap(1);frames(180)
 check('give_mega_stone_'+str(mode),invoke('GetMonData3',symbols['gParties'],c['MON_DATA_HELD_ITEM'],0)==selected)
 for _ in range(3):tap(1);frames(30)
 tap(2);frames(180)
 # Healing from Medicine must consume the selected medicine, not an underlying slot.
 wr(0x0203fc00,1);invoke('SetMonData',symbols['gParties'],c['MON_DATA_HP'],0x0203fc00)
 openbag(c['BAG_MEDICINE'])
 tap(1);frames(20);selected=rd(symbols['gSpecialVar_ItemId'],2)
 quantity=invoke('CountTotalItemQuantityInBag',selected)
 tap(1);frames(180);tap(1);frames(180)
 check('medicine_heals_'+str(mode),invoke('GetMonData3',symbols['gParties'],c['MON_DATA_HP'],0)>1)
 check('medicine_consumes_correct_'+str(mode),invoke('CountTotalItemQuantityInBag',selected)==quantity-1)
 for _ in range(3):tap(2);frames(90)
 lib.shutdown()
# Full item-table audit: every valid ID has exactly one category.
start(0)
audit=[]
for item in range(1,c['ITEMS_COUNT']):
 cat=invoke('GetItemBagCategory',item)
 check('valid_category_'+str(item),cat<c['BAG_CATEGORIES_COUNT'])
 audit.append(dict(item=item,category=cat))
lib.shutdown()
(R/'docs/features/bag-category-audit.json').write_text(json.dumps(dict(categories=13,items=audit),indent=2)+'\n')
(R/'docs/features/bag-categories-validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'bag category checks')
