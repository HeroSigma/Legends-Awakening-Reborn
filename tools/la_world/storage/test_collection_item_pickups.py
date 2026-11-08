"""Actual field item pickups must finish and close their header in both PC modes."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
import tempfile,struct
names=['MAP_GROUP(MAP_PETALBURG_WOODS)','MAP_NUM(MAP_PETALBURG_WOODS)','FLAG_LA_INTRO_ACTIVE','VAR_LITTLEROOT_INTRO_STATE','FLAG_ITEM_PETALBURG_WOODS_ETHER','ITEM_ETHER','WINDOW_TILE_DATA','BATTLE_PYRAMID_FUNC_CURRENT_LOCATION','BATTLE_PYRAMID_FUNC_INIT','FLAG_GET_ITEM_OBTAINED']
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "window.h"\n#include "overworld.h"\n#include "constants/maps.h"\n#include "constants/items.h"\n#include "constants/battle_pyramid.h"\nconst unsigned v[]={'+','.join(names)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 c=dict(zip(names,struct.unpack('<'+str(len(names))+'I',(td/'c.bin').read_bytes())))
def windows():return sum(bool(invoke('GetWindowAttribute',i,c['WINDOW_TILE_DATA'])) for i in range(32))
proof=R/'docs/la_world/compact_pc/item_pickups';proof.mkdir(parents=True,exist_ok=True)
for mode in [0,1]:
 start(0);invoke('FlagClear',c['FLAG_LA_INTRO_ACTIVE']);invoke('VarSet',c['VAR_LITTLEROOT_INTRO_STATE'],7)
 invoke('StorageChangeMode',mode,1)
 for operation in ['first','repeat','full']:
  invoke('FlagClear',c['FLAG_ITEM_PETALBURG_WOODS_ETHER'])
  if operation=='full':invoke('AddBagItem',c['ITEM_ETHER'],999-invoke('CountTotalItemQuantityInBag',c['ITEM_ETHER']))
  warp(c[names[0]],c[names[1]],15,20);frames(60)
  baseline=windows();before=invoke('CountTotalItemQuantityInBag',c['ITEM_ETHER'])
  wr(symbols['gSpecialVar_LastTalked'],7,2)
  wr(symbols['gSelectedObjectEvent'],invoke('GetObjectEventIdByLocalIdAndMap',7,c[names[0]],c[names[1]]),1)
  invoke('ScriptContext_SetupScript',symbols['Common_EventScript_FindItem'])
  blocked=False;seen=True;header_seen=False
  for frame in range(3000):
   if frame%30==0:header_seen |= windows()>baseline
   ptr=rd(symbols['sGlobalScriptContext']+8)
   if symbols['LaCollection_Blocked']<=ptr<symbols['LaCollection_Blocked']+20:blocked=True
   if rd(symbols['sGlobalScriptContextStatus'],1)!=2:seen=True
   if seen and frame>90 and rd(symbols['sGlobalScriptContextStatus'],1)==2:break
   frames(1,1 if frame%31<4 else 0)
  else:
   shutil.copy2(shot('pickup_timeout'),proof/'timeout.png')
   raise AssertionError(('pickup timeout',mode,operation,pos(),rd(symbols['sGlobalScriptContextStatus'],1),hex(rd(symbols['sGlobalScriptContext']+8))))
  frames(30)
  check('no_warning_'+str((mode,operation)),not blocked)
  check('header_removed_'+str((mode,operation)),windows()==baseline)
  check('controls_restored_'+str((mode,operation)),invoke('ArePlayerFieldControlsLocked')==0)
  check('quantity_'+str((mode,operation)),invoke('CountTotalItemQuantityInBag',c['ITEM_ETHER'])==before+(operation!='full'))
  if operation=='first':check('description_shown_'+str(mode),header_seen)
  if operation=='first':shutil.copy2(shot('ether_pickup_'+str(mode)),proof/('completed_'+str(mode)+'.png'))
 wr(symbols['gSpecialVar_0x8004'],c['BATTLE_PYRAMID_FUNC_CURRENT_LOCATION'],2)
 check('location_query_allowed_'+str(mode),invoke('LaPcBlockedSpecial',symbols['SPECIAL_CallBattlePyramidFunction'])==0)
 wr(symbols['gSpecialVar_0x8004'],c['BATTLE_PYRAMID_FUNC_INIT'],2)
 check('pyramid_gameplay_still_blocked_'+str(mode),invoke('LaPcBlockedSpecial',symbols['SPECIAL_CallBattlePyramidFunction'])==mode)
lib.shutdown()
(proof/'validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'item pickup checks')
