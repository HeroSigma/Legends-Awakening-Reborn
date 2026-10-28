"""Legends Store economy and real menu transactions in isolated native mGBA."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'.la_work/legends-store';D.mkdir(exist_ok=True)
import tempfile,struct
names=['ITEMS_COUNT','ITEM_NONE','ITEM_POTION','ITEM_POKE_BALL','ITEM_MASTER_BALL','ITEM_ABILITY_PATCH','ITEM_ABILITY_CAPSULE','ITEM_CHARIZARDITE_X','ITEM_NORMALIUM_Z','ITEM_FIRE_TERA_SHARD','ITEM_MACH_BIKE','ITEM_TM_FOCUS_PUNCH','BAG_TRAINING','BAG_MEDICINE','BAG_KEYS','BAG_TERA_SHARDS','BAG_CATEGORIES_COUNT','offsetof(struct SaveBlock1,money)','sizeof(struct ItemInfo)','offsetof(struct ItemInfo,price)','FLAG_SYS_POKEDEX_GET','FLAG_SYS_POKEMON_GET','FLAG_SYS_POKENAV_GET','DN_FLAG_DEXNAV_GET']
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "item.h"\n#include "bag_categories.h"\n#include "dexnav.h"\n#include <stddef.h>\nconst unsigned v[]={'+','.join(names)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 c=dict(zip(names,struct.unpack('<'+str(len(names))+'I',(td/'c.bin').read_bytes())))
def wallet():return rd(symbols['gSaveBlock1Ptr'])+c['offsetof(struct SaveBlock1,money)']
def money():return invoke('GetMoney',wallet())
def quantity(item):return invoke('CountTotalItemQuantityInBag',item)
prices=[]
for mode in [0,1]:
 start(0);invoke('StorageChangeMode',mode,1);invoke('ClearBag')
 for name in ['ITEM_NONE','ITEM_FIRE_TERA_SHARD','ITEM_MACH_BIKE']:
  check('excluded_'+str((mode,name)),invoke('LegendsStore_ItemAllowed',c[name])==0)
  check('excluded_purchase_'+str((mode,name)),invoke('LegendsStore_Buy',c[name],1,99)==1)
 for name in ['ITEM_POTION','ITEM_MASTER_BALL','ITEM_ABILITY_PATCH','ITEM_ABILITY_CAPSULE','ITEM_CHARIZARDITE_X','ITEM_NORMALIUM_Z']:
  item=c[name];cat=invoke('GetItemBagCategory',item)
  regular=invoke('LegendsStore_Price',item,99);sale=invoke('LegendsStore_Price',item,cat)
  check('positive_discount_'+str((mode,name)),0<sale<regular)
  invoke('SetMoney',wallet(),999999)
  check('buy_'+str((mode,name)),invoke('LegendsStore_Buy',item,1,99)==0)
  check('delivered_'+str((mode,name)),quantity(item)==1)
  check('charged_'+str((mode,name)),money()==999999-regular)
  if mode==0:prices.append(dict(item=name,price=regular,sale=sale))
 item=c['ITEM_POTION'];before=quantity(item)
 invoke('SetMoney',wallet(),0)
 check('insufficient_'+str(mode),invoke('LegendsStore_Buy',item,1,99)==2)
 check('insufficient_no_item_'+str(mode),quantity(item)==before and money()==0)
 invoke('SetMoney',wallet(),999999)
 for q in [0,100,0xffffffff]:
  check('invalid_quantity_'+str((mode,q)),invoke('LegendsStore_Buy',item,q,99)==1)
 check('invalid_no_charge_'+str(mode),money()==999999)
 invoke('AddBagItem',item,999-before)
 check('full_'+str(mode),invoke('LegendsStore_Buy',item,1,99)==3)
 check('full_no_charge_'+str(mode),money()==999999 and quantity(item)==999)
 item=c['ITEM_TM_FOCUS_PUNCH']
 check('tm_single_'+str(mode),invoke('LegendsStore_Buy',item,1,99)==0)
 before=money()
 check('tm_duplicate_'+str(mode),invoke('LegendsStore_Buy',item,1,99)==1)
 check('tm_no_charge_'+str(mode),money()==before and quantity(item)==1)
 check('save_'+str(mode),invoke('TrySavingData',0)==1)
 invoke('ClearBag');check('reload_'+str(mode),invoke('LoadGameSave',0)==1)
 check('purchases_persist_'+str(mode),quantity(c['ITEM_POTION'])==999 and quantity(item)==1 and money()==before)
 # All story unlocks: the new tenth Start row must be reachable without overflow.
 for n in ['FLAG_SYS_POKEDEX_GET','FLAG_SYS_POKEMON_GET','FLAG_SYS_POKENAV_GET','DN_FLAG_DEXNAV_GET']:invoke('FlagSet',c[n])
 wr(symbols['sStartMenuCursorPos'],0,1);tap(8);frames(60)
 check('ten_rows_'+str(mode),rd(symbols['sNumStartMenuActions'],1)==10)
 if mode==0:shutil.copy2(shot('start'),R/'docs/features/legends-store-start.png')
 for _ in range(9):tap(128)
 tap(1);frames(40)
 check('store_open_'+str(mode),active('Task_LegendsStore') is not None)
 if mode==0:shutil.copy2(shot('browse'),R/'docs/features/legends-store.png')
 # Change pocket, choose and adjust quantity, cancel confirmation, then exit.
 tap(16);frames(20);tap(1);frames(20)
 if mode==0:shutil.copy2(shot('confirm'),R/'docs/features/legends-store-confirm.png')
 tap(16);frames(20);tap(2);frames(20)
 check('cancel_keeps_store_'+str(mode),active('Task_LegendsStore') is not None)
 # Complete a real purchase and verify quantity/cost match the confirmation.
 item=c['ITEM_POKE_BALL'];owned=quantity(item);funds=money()
 t=active('Task_LegendsStore');sale=rd(symbols['gTasks']+t*40+8+4*2,2)
 tap(1);frames(20);tap(16);frames(20);tap(1);frames(20)
 check('ui_purchase_quantity_'+str(mode),quantity(item)==owned+2)
 check('ui_purchase_charge_'+str(mode),money()==funds-2*invoke('LegendsStore_Price',item,sale))
 # Every category is reachable; excluded pockets are never displayed.
 visited=set()
 for _ in range(11):
  t=active('Task_LegendsStore');cat=rd(symbols['gTasks']+t*40+8+2,2);visited.add(cat)
  check('ui_allowed_pocket_'+str((mode,cat)),cat not in [c['BAG_KEYS'],c['BAG_TERA_SHARDS']])
  tap(16);frames(20)
 check('all_store_pockets_'+str(mode),len(visited)==11)
 tap(2);frames(20)
 check('store_closed_'+str(mode),active('Task_LegendsStore') is None and rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1)
 check('controls_released_'+str(mode),invoke('ArePlayerFieldControlsLocked')==0)
 if mode==0:
  for item in range(1,c['ITEMS_COUNT']):
   if not invoke('LegendsStore_ItemAllowed',item):continue
   cat=invoke('GetItemBagCategory',item)
   regular=invoke('LegendsStore_Price',item,99);sale=invoke('LegendsStore_Price',item,cat)
   native=rd(symbols['gItemsInfo']+item*c['sizeof(struct ItemInfo)']+c['offsetof(struct ItemInfo,price)'])
   check('catalog_price_'+str(item),0<sale<=regular<=999999 and sale>=invoke('GetItemSellPrice',item))
 lib.shutdown()
result=dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),examples=prices,checks=checks)
(R/'docs/features/legends-store-validation.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS',len(checks),'Legends Store checks')
