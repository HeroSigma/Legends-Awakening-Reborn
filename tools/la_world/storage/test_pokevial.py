"""Pokévial charge, healing, field-use, reward and persistence tests in isolated saves."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_training_scientist.py').read_text().split('for mode in [0,1]:')[0],'helpers','exec'))
names2=['ITEM_POKEVIAL','VAR_LA_POKEVIAL_CHARGES','FLAG_LA_POKEVIAL_RECEIVED','FLAG_LA_INTRO_ACTIVE','VAR_LITTLEROOT_INTRO_STATE','VAR_PETALBURG_WOODS_STATE','MON_DATA_MAX_HP','MON_DATA_STATUS','MON_DATA_PP1','MON_DATA_MOVE1','MON_DATA_PP_BONUSES','offsetof(struct SaveBlock1,registeredItem)','MAP_GROUP(MAP_RUSTBORO_CITY_DEVON_CORP_1F)','MAP_NUM(MAP_RUSTBORO_CITY_DEVON_CORP_1F)','POCKET_KEY_ITEMS']
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "constants/items.h"\n#include "constants/item.h"\n#include "constants/maps.h"\n#include <stddef.h>\nconst unsigned v[]={'+','.join(names2)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 c.update(zip(names2,struct.unpack('<'+str(len(names2))+'I',(td/'c.bin').read_bytes())))
proof=R/'docs/features/pokevial';proof.mkdir(parents=True,exist_ok=True)
def quiet(limit=12000):
 for i in range(limit):
  if i>60 and rd(symbols['sGlobalScriptContextStatus'],1)==2 and not invoke('ArePlayerFieldControlsLocked'):return
  frames(1,1 if i%31<4 else 0)
 raise AssertionError(('script timeout',pos()))
def prepare():invoke('LegendsPokevialPrepare');return result()
def doses():return invoke('VarGet',c['VAR_LA_POKEVIAL_CHARGES'])
for mode in [0,1]:
 start(0);invoke('FlagClear',c['FLAG_LA_INTRO_ACTIVE']);invoke('VarSet',c['VAR_LITTLEROOT_INTRO_STATE'],7)
 invoke('StorageChangeMode',mode,1);invoke('ScriptGiveMon',4,16,0)
 check('not_owned_'+str(mode),prepare()==3)
 invoke('AddBagItem',c['ITEM_POKEVIAL'],1);invoke('LegendsPokevialGrant')
 check('key_pocket_'+str(mode),invoke('GetItemPocket',c['ITEM_POKEVIAL'])==c['POCKET_KEY_ITEMS'])
 check('starts_full_'+str(mode),doses()==3)
 check('healthy_rejected_'+str(mode),prepare()==2)
 invoke('LegendsPokevialHeal');check('healthy_no_charge_'+str(mode),doses()==3)
 invoke('StorageWriteMon',59 if mode else 13,29,symbols['gParties'])
 invoke('ScriptGiveEgg',7)
 egg=bytes(rd(symbols['gParties']+100+i,1) for i in range(100))
 for remaining in [2,1,0]:
  setdata('MON_DATA_HP',0);setdata('MON_DATA_STATUS',8);setdata('MON_DATA_PP1',0)
  check('ready_'+str((mode,remaining)),prepare()==0)
  invoke('LegendsPokevialHeal')
  check('charge_consumed_'+str((mode,remaining)),doses()==remaining)
  check('revives_'+str((mode,remaining)),get('MON_DATA_HP')==get('MON_DATA_MAX_HP'))
  check('status_cured_'+str((mode,remaining)),get('MON_DATA_STATUS')==0)
  check('pp_restored_'+str((mode,remaining)),get('MON_DATA_PP1')>0)
  check('icon_'+str((mode,remaining)),invoke('GetItemIconPic',c['ITEM_POKEVIAL'])==symbols['gItemIcon_Pokevial'+str(remaining*3)])
 check('egg_untouched_'+str(mode),egg==bytes(rd(symbols['gParties']+100+i,1) for i in range(100)))
 setdata('MON_DATA_HP',1);invoke('LegendsPokevialHeal')
 check('empty_no_heal_'+str(mode),result()==1 and get('MON_DATA_HP')==1 and doses()==0)
 invoke('HealPlayerParty');check('center_refills_'+str(mode),doses()==3)
 # A PP-only deficit should also be sufficient to spend one dose.
 setdata('MON_DATA_PP1',0);invoke('LegendsPokevialHeal');check('pp_only_'+str(mode),doses()==2 and get('MON_DATA_PP1')>0)
 invoke('TrySavingData',0);invoke('VarSet',c['VAR_LA_POKEVIAL_CHARGES'],0)
 check('reload_'+str(mode),invoke('LoadGameSave',0)==1)
 check('charges_persist_'+str(mode),doses()==2)
 check('item_persists_'+str(mode),invoke('CheckBagHasItem',c['ITEM_POKEVIAL'],1)==1)
 check('last_box_preserved_'+str(mode),invoke('GetBoxMonDataAt',59 if mode else 13,29,c['MON_DATA_SPECIES'])==4)
 # Real registered item entry point, followed by cancel and confirmed use.
 warp(c['MAP_GROUP(MAP_RUSTBORO_CITY_DEVON_CORP_1F)'],c['MAP_NUM(MAP_RUSTBORO_CITY_DEVON_CORP_1F)'],5,5)
 wr(rd(symbols['gSaveBlock1Ptr'])+c['offsetof(struct SaveBlock1,registeredItem)'],c['ITEM_POKEVIAL'],2)
 setdata('MON_DATA_HP',1)
 check('registered_starts_'+str(mode),invoke('UseRegisteredKeyItemOnField')==1)
 for i in range(600):
  if task('Task_HandleYesNoInput') is not None:break
  frames(1,1 if i%31<4 else 0)
 else:raise AssertionError('no confirmation')
 frames(30);shutil.copy2(shot('pokevial_confirm_'+str(mode)),proof/('confirm_'+str(mode)+'.png'))
 frames(4,2);frames(60)
 check('cancel_keeps_charge_'+str(mode),doses()==2 and get('MON_DATA_HP')==1)
 invoke('UseRegisteredKeyItemOnField')
 for i in range(600):
  if task('Task_HandleYesNoInput') is not None:break
  frames(1,1 if i%31<4 else 0)
 frames(30);frames(4,1);quiet()
 check('registered_heals_'+str(mode),doses()==1 and get('MON_DATA_HP')==get('MON_DATA_MAX_HP'))
 check('controls_restored_'+str(mode),invoke('ArePlayerFieldControlsLocked')==0)
 # Use through the actual Key Items bag action, then decline the charge.
 setdata('MON_DATA_HP',1)
 invoke('GoToBagMenu',0,c['POCKET_KEY_ITEMS'],symbols['CB2_ReturnToField']|1)
 wr(symbols['gMain']+4,symbols['CB2_Bag']|1);frames(100)
 shutil.copy2(shot('pokevial_bag_'+str(mode)),proof/('bag_'+str(mode)+'.png'))
 frames(4,1);frames(30);frames(4,1)
 for i in range(900):
  if task('Task_HandleYesNoInput') is not None:break
  frames(1,1 if i%31<4 else 0)
 else:raise AssertionError('no bag confirmation')
 frames(30);frames(4,2);quiet()
 check('bag_use_cancel_'+str(mode),doses()==1 and get('MON_DATA_HP')==1)
 # Existing-save reward path, once only; replay must not refill or duplicate.
 invoke('RemoveBagItem',c['ITEM_POKEVIAL'],1);invoke('FlagClear',c['FLAG_LA_POKEVIAL_RECEIVED'])
 invoke('VarSet',c['VAR_PETALBURG_WOODS_STATE'],1)
 invoke('ScriptContext_SetupScript',symbols['RustboroCity_DevonCorp_1F_EventScript_Greeter']);quiet()
 check('catchup_reward_'+str(mode),invoke('CheckBagHasItem',c['ITEM_POKEVIAL'],1)==1 and doses()==3)
 setdata('MON_DATA_HP',1);invoke('LegendsPokevialHeal')
 invoke('ScriptContext_SetupScript',symbols['RustboroCity_DevonCorp_1F_EventScript_Greeter']);quiet()
 check('reward_once_'+str(mode),invoke('CountTotalItemQuantityInBag',c['ITEM_POKEVIAL'])==1 and doses()==2)
for name in sorted(n for n in symbols if n.startswith('LegendsPokevial_Text_')):
 invoke('StringExpandPlaceholders',symbols['gStringVar4'],symbols[name]);lines=[[]]
 for i in range(1200):
  value=rd(symbols['gStringVar4']+i,1)
  if value==255:break
  if value in (250,251,254):lines.append([])
  else:lines[-1].append(value)
 for line_id,line in enumerate(lines):
  for i,value in enumerate(line+[255]):wr(0x0203fc00+i,value,1)
  check('text_fits_'+name+'_'+str(line_id),invoke('GetStringWidth',1,0x0203fc00,0)<=208)
lib.shutdown()
(proof/'validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'Pokevial checks')
