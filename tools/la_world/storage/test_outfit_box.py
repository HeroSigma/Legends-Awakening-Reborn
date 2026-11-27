"""Native item/menu/Mom gift coverage, using isolated batteries only."""
from pathlib import Path
import tempfile,subprocess,struct,json,hashlib,shutil,zlib
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'docs/features/player-outfits/outfit-box';D.mkdir(parents=True,exist_ok=True)
checks=[]
def check(n,v):
 checks.append(dict(test=n,passed=bool(v)));assert v,n
names=['ITEM_OUTFIT_BOX','ITEM_POTION','SECTOR_ID_PKMN_STORAGE_END','FLAG_RECEIVED_RUNNING_SHOES','POCKET_KEY_ITEMS','ITEMMENULOCATION_FIELD','BAG_KEYS','PLAYER_AVATAR_FLAG_SURFING','PLAYER_AVATAR_FLAG_MACH_BIKE','PLAYER_AVATAR_FLAG_UNDERWATER','FLAG_LA_RED_DEX_GIFTS','offsetof(struct SaveBlock1,registeredItem)','offsetof(struct PlayerAvatar,flags)']
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'a.c').write_text('#include "global.h"\n#include "constants/items.h"\n#include "constants/flags.h"\n#include "item_menu.h"\n#include "field_player_avatar.h"\n#include "bag_categories.h"\n#include "save.h"\n#include <stddef.h>\nconst unsigned values[]={'+','.join(names)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'a.c'),'-o',str(td/'a.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'a.o'),str(td/'a.bin')],check=True)
 c=dict(zip(names,struct.unpack('<'+str(len(names))+'I',(td/'a.bin').read_bytes())))
item=c['ITEM_OUTFIT_BOX']
def snap(n):shutil.copy2(shot('outfit_box_'+n),D/(n+'.png'))
def waitfield():
 for i in range(1200):
  frames(1)
  if rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1 and active('Task_OutfitBox') is None:
   frames(120);return
 raise AssertionError('return to field timed out')
def registered():
 wr(rd(symbols['gSaveBlock1Ptr'])+c['offsetof(struct SaveBlock1,registeredItem)'],item,2)
 check('registered_item_opens',invoke('UseRegisteredKeyItemOnField')==1)
 wait('Task_OutfitBox',900);frames(45)
for gender in [0,1]:
 start(gender)
 check(f'g{gender}_not_before_shoes',invoke('CheckBagHasItem',item,1)==0)
 invoke('OutfitBox_EnsureOwned')
 check(f'g{gender}_migration_gated',invoke('CheckBagHasItem',item,1)==0)
 # Exercise both the legacy and current story versions of Mom's gift.
 if gender:invoke('FlagSet',c['FLAG_LA_RED_DEX_GIFTS'])
 invoke('ScriptContext_SetupScript',symbols['LittlerootTown_EventScript_GiveRunningShoes'])
 advance(limit=12000)
 check(f'g{gender}_mom_gives_shoes',invoke('FlagGet',c['FLAG_RECEIVED_RUNNING_SHOES'])==1)
 check(f'g{gender}_mom_gives_box',invoke('CheckBagHasItem',item,1)==1)
 check(f'g{gender}_key_pocket',invoke('GetItemPocket',item)==c['POCKET_KEY_ITEMS'])
 invoke('OutfitBox_EnsureOwned');invoke('OutfitBox_EnsureOwned')
 check(f'g{gender}_no_duplicate',invoke('CheckBagHasItem',item,2)==0)
 # Old saves missing the new item recover it after receiving the shoes.
 invoke('RemoveBagItem',item,1);invoke('OutfitBox_EnsureOwned')
 check(f'g{gender}_legacy_recovery',invoke('CheckBagHasItem',item,1)==1)
 invoke('PlayerOutfit_Set',0);invoke('DynamicPal_SetSelection',0)
 registered();snap(f'g{gender}_emerald')
 for style in range(1,5):
  tap(128);snap(f'g{gender}_style{style}')
  check(f'g{gender}_browse{style}_uncommitted',invoke('PlayerOutfit_Get')==0)
 tap(256);snap(f'g{gender}_colors') # R
 tap(16);tap(128);tap(16);tap(128);tap(32)
 check(f'g{gender}_colors_uncommitted',invoke('DynamicPal_GetSelection')==0)
 tap(2);tap(2);waitfield()
 check(f'g{gender}_cancel_style',invoke('PlayerOutfit_Get')==0)
 check(f'g{gender}_cancel_colors',invoke('DynamicPal_GetSelection')==0)
 registered();tap(128);tap(128);tap(256);tap(16);tap(128);tap(16);tap(128);tap(16);snap(f'g{gender}_custom')
 tap(1);waitfield();snap(f'g{gender}_equipped')
 check(f'g{gender}_apply_style',invoke('PlayerOutfit_Get')==2)
 check(f'g{gender}_apply_colors',invoke('DynamicPal_GetSelection')==0x111)
 # Use the actual Bag item context menu, not just registered-item access.
 invoke('GoToBagMenu',c['ITEMMENULOCATION_FIELD'],c['BAG_KEYS'],symbols['CB2_ReturnToField'])
 wr(symbols['gMain']+0x438,0,1);wr(symbols['gMain']+4,symbols['CB2_Bag']|1)
 wait('Task_BagMenu_HandleInput',900);frames(60)
 snap(f'g{gender}_bag_box');tap(1);frames(25);tap(1)
 wait('Task_OutfitBox',900);frames(45);snap(f'g{gender}_from_bag')
 tap(2);waitfield()
 check(f'g{gender}_bag_exit_style',invoke('PlayerOutfit_Get')==2)
 check(f'g{gender}_field_unlocked',invoke('ArePlayerFieldControlsLocked')==0)
 tap(8);wait('StartMenuTask');frames(60);snap(f'g{gender}_start_after_box')
 tap(2);frames(120)
 check(f'g{gender}_start_no_restart',rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1)
 check(f'g{gender}_start_exit_unlocked',invoke('ArePlayerFieldControlsLocked')==0)
 # Riding states must keep the wardrobe closed and return field controls.
 for mode in ['PLAYER_AVATAR_FLAG_MACH_BIKE','PLAYER_AVATAR_FLAG_SURFING','PLAYER_AVATAR_FLAG_UNDERWATER']:
  ptr=symbols['gPlayerAvatar']+c['offsetof(struct PlayerAvatar,flags)'];previous=rd(ptr,1)
  wr(ptr,c[mode],1)
  invoke('UseRegisteredKeyItemOnField');frames(90)
  check(f'g{gender}_blocked_{mode}',active('Task_OutfitBox') is None)
  tap(1);tap(2);frames(90);wr(ptr,previous,1)
 # Repeated menu entry/exit must release trainer pictures, windows and field locks.
 for repeat in range(4):
  registered();tap(2);waitfield()
  check(f'g{gender}_reopen{repeat}',invoke('PlayerOutfit_Get')==2)
 check(f'g{gender}_save',invoke('TrySavingData',0)==1)
 invoke('PlayerOutfit_Set',0);invoke('DynamicPal_SetSelection',0)
 check(f'g{gender}_load',invoke('LoadGameSave',0)==1)
 check(f'g{gender}_saved_style',invoke('PlayerOutfit_Get')==2)
 check(f'g{gender}_saved_colors',invoke('DynamicPal_GetSelection')==0x111)
 # Import an actual previous-item-count packed bag header and CRC. Old item
 # quantities survive the appended item, and only the new field is zero-filled.
 count=item;packed=bytearray(((count-1)*10+7)//8)
 bit=(c['ITEM_POTION']-1)*10
 value=int.from_bytes(packed,'little') | (37<<bit)
 packed[:]=value.to_bytes(len(packed),'little')
 raw=struct.pack('<4I',0x33474142,count,len(packed),zlib.crc32(packed))+packed
 buf=invoke('AllocZeroed_',4096,0)
 for i,v in enumerate(raw):wr(buf+i,v,1)
 invoke('ExpandedBag_ReadSector',c['SECTOR_ID_PKMN_STORAGE_END'],buf,0)
 check(f'g{gender}_legacy_inventory',invoke('CheckBagHasItem',c['ITEM_POTION'],37)==1)
 check(f'g{gender}_legacy_new_item_zero',invoke('CheckBagHasItem',item,1)==0)
 invoke('OutfitBox_EnsureOwned')
 check(f'g{gender}_legacy_box_granted',invoke('CheckBagHasItem',item,1)==1)
 invoke('Free',buf)
 lib.shutdown()
(D/'validation.json').write_text(json.dumps(dict(rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks,user_save_loaded=False),indent=2)+'\n')
print('PASS',len(checks),'portable wardrobe checks',flush=True)
