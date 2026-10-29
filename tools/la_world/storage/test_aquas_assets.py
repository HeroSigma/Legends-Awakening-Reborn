"""Native visual and behavior checks for credited imported UI/world art."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
import tempfile,struct
D=R/'docs/art/aquas_assets';D.mkdir(exist_ok=True)
ids=['GOLD_BALL','MEGA_STONE','TYRANTRUM_EXHIBIT']+['APRICORN_'+n for n in ['RED','BLUE','YELLOW','GREEN','PINK','WHITE','BLACK']]
names=['OBJ_EVENT_GFX_LA_'+n for n in ids]+['MAP_GROUP(MAP_RUSTBORO_CITY_DEVON_CORP_1F)','MAP_NUM(MAP_RUSTBORO_CITY_DEVON_CORP_1F)','MOVEMENT_TYPE_FACE_DOWN','OBJECT_EVENTS_COUNT','ITEM_POTION','ITEM_POKE_BALL','FLAG_BADGE01_GET','FLAG_BADGE08_GET','sizeof(struct ObjectEvent)','offsetof(struct ObjectEvent,spriteId)','offsetof(struct Sprite,oam)','sizeof(struct Sprite)','offsetof(struct ObjectEvent,trainerRange_berryTreeId)','BAG_MEDICINE','offsetof(struct SaveBlock1,money)','OBJ_EVENT_GFX_BERRY_TREE_EARLY_STAGES','BERRY_STAGE_BERRIES','BERRY_ID_CHERI','BERRY_ID_CHESTO','BERRY_ID_PECHA','BERRY_ID_RAWST','BERRY_ID_ASPEAR','BERRY_ID_LEPPA','BERRY_ID_ORAN','BERRY_ID_PERSIM','BERRY_ID_LUM','BERRY_ID_SITRUS']
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "sprite.h"\n#include "berry.h"\n#include "bag_categories.h"\n#include "constants/event_objects.h"\n#include "constants/event_object_movement.h"\n#include <stddef.h>\nconst unsigned v[]={'+','.join(names)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 c=dict(zip(names,struct.unpack('<'+str(len(names))+'I',(td/'c.bin').read_bytes())))
start(0)
# Register and render each new sprite on a disposable map; no user map/save is changed.
for i,n in enumerate(ids):
 obj=invoke('SpawnSpecialObjectEventParameterized',c['OBJ_EVENT_GFX_LA_'+n],c['MOVEMENT_TYPE_FACE_DOWN'],200,10,10,3)
 check('spawn_'+n,obj<c['OBJECT_EVENTS_COUNT'])
 frames(30)
 if n in ['GOLD_BALL','MEGA_STONE','TYRANTRUM_EXHIBIT','APRICORN_RED']:shutil.copy2(shot(n.lower()),D/(n.lower()+'.png'))
 invoke('RemoveObjectEvent',symbols['gObjectEvents']+obj*c['sizeof(struct ObjectEvent)'])
# Every improved berry has its own correctly loaded palette at the ripe stage.
for n in ['CHERI','CHESTO','PECHA','RAWST','ASPEAR','LEPPA','ORAN','PERSIM','LUM','SITRUS']:
 obj=invoke('SpawnSpecialObjectEventParameterized',c['OBJ_EVENT_GFX_BERRY_TREE_EARLY_STAGES'],c['MOVEMENT_TYPE_FACE_DOWN'],200,10,10,3)
 address=symbols['gObjectEvents']+obj*c['sizeof(struct ObjectEvent)']
 wr(address+c['offsetof(struct ObjectEvent,trainerRange_berryTreeId)'],0,1)
 invoke('PlantBerryTree',0,c['BERRY_ID_'+n],c['BERRY_STAGE_BERRIES'],0)
 sprite_id=rd(address+c['offsetof(struct ObjectEvent,spriteId)'],1)
 invoke('SetBerryTreeGraphics',address,symbols['gSprites']+sprite_id*c['sizeof(struct Sprite)'])
 frames(20)
 check('berry_palette_'+n,invoke('IndexOfSpritePaletteTag',0xDCC0+['CHERI','CHESTO','PECHA','RAWST','ASPEAR','LEPPA','ORAN','PERSIM','LUM','SITRUS'].index(n))!=255)
 if n in ['CHERI','ORAN']:shutil.copy2(shot('berry_'+n),D/('berry-'+n.lower()+'.png'))
 invoke('RemoveObjectEvent',address)
warp(c['MAP_GROUP(MAP_RUSTBORO_CITY_DEVON_CORP_1F)'],c['MAP_NUM(MAP_RUSTBORO_CITY_DEVON_CORP_1F)'],10,5)
frames(60);shutil.copy2(shot('devon_exhibit'),D/'devon-exhibit.png')
check('devon_map_running',rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1)
lib.shutdown()
start(0)
for f in range(c['FLAG_BADGE01_GET'],c['FLAG_BADGE08_GET']+1):invoke('FlagSet',f)
invoke('ShowPlayerTrainerCard',symbols['CB2_ReturnToField']|1)
# Invoker restores callbacks; honor the actual trainer-card initializer.
wr(symbols['gMain']+4,symbols['CB2_InitTrainerCard']|1);frames(240)
shutil.copy2(shot('badges'),D/'badges.png')
for _ in range(12):tap(2);frames(20)
lib.shutdown()
start(0)
scratch=0x0203fc00
for i,item in enumerate([c['ITEM_POTION'],c['ITEM_POKE_BALL'],0]):wr(scratch+i*2,item,2)
invoke('CreatePokemartMenu',scratch);frames(30)
check('shop_prompt',active('Task_ShopMenu') is not None)
tap(1);frames(240)
check('shop_buy_list',active('Task_BuyMenu') is not None)
shutil.copy2(shot('new_mart'),D/'mart.png')
tap(1);frames(60)
shutil.copy2(shot('mart_quantity'),D/'mart-quantity.png')
money_ptr=rd(symbols['gSaveBlock1Ptr'])+c['offsetof(struct SaveBlock1,money)'];before=invoke('GetMoney',money_ptr)
for attempt in range(40):
 if invoke('CountTotalItemQuantityInBag',c['ITEM_POTION'])==1:break
 tap(1);frames(30)
shutil.copy2(shot('mart_purchase'),D/'mart-purchase.png')
check('mart_purchase_item',invoke('CountTotalItemQuantityInBag',c['ITEM_POTION'])==1)
for attempt in range(40):
 if invoke('GetMoney',money_ptr)!=before:break
 tap(1);frames(30)
check('mart_purchase_cost',invoke('GetMoney',money_ptr)==before-invoke('GetItemPrice',c['ITEM_POTION']))
for _ in range(16):tap(2);frames(20)
check('shop_no_reset',rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1)
lib.shutdown()
for gender in [0,1]:
 start(gender);invoke('AddBagItem',c['ITEM_POTION'],5)
 invoke('GoToBagMenu',0,c['BAG_MEDICINE'],symbols['CB2_ReturnToField']|1)
 wr(symbols['gMain']+4,symbols['CB2_Bag']|1);frames(180)
 check('bag_opens_'+str(gender),active('Task_BagMenu_HandleInput') is not None)
 shutil.copy2(shot('bag_'+str(gender)),D/('bag-'+str(gender)+'.png'))
 tap(2);frames(180)
 check('bag_returns_'+str(gender),rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1)
 lib.shutdown()
(D/'validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'imported art checks')
