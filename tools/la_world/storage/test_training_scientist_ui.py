"""In-game scientist menus, cancellation, free edits and normal evolution flow."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_training_scientist.py').read_text().split('for mode in [0,1]:')[0],'training_helpers','exec'))
# Hold inputs across multiple hardware frames to avoid sampling a one-frame tap.
def tap(key):
 frames(2);frames(3,key);frames(12)
mg=json.loads((R/'data/maps/map_groups.json').read_text());name='OldaleTown_PokemonCenter_2F'
for group,gname in enumerate(mg['group_order']):
 if name in mg[gname]:mapnum=mg[gname].index(name);break
row=next(x for x in json.loads((R/'docs/features/training-scientist-locations.json').read_text()) if x['map']==name)
def menu(kind):
 if kind==0:
  waitfor(lambda:task('Task_HandleScrollingMultichoiceInput') is not None)
  frames(20)
  actual=rd(symbols['gSpecialVar_0x8005'],2)
  if actual!=0:
   assert actual in [1,3,4,8],('unexpected return menu',actual)
   tap(2)
 waitfor(lambda:rd(symbols['gSpecialVar_0x8005'],2)==kind and task('Task_HandleScrollingMultichoiceInput') is not None)
 frames(15)
def selected_row():
 t=task('Task_HandleScrollingMultichoiceInput')
 list_id=rd(symbols['gTasks']+t*40+8,2)
 invoke('ListMenuGetCurrentItemArrayId',list_id,0x0203fc00)
 return rd(0x0203fc00,2)
def text_bytes(pointer):
 out=[]
 for i in range(600):
  value=rd(pointer+i,1)
  if value==255:return bytes(out)
  out.append(value)
 raise AssertionError('unterminated text')
def stat_label(index):return text_bytes(rd(rd(symbols['gMultiuseListMenuTemplate'])+index*8))
def budget_numbers():
 import re
 return [int(''.join(str(x-0xa1) for x in group)) for group in re.findall(b'[\xa1-\xaa]+',text_bytes(symbols['gStringVar4']))]
def choose(index):
 current=selected_row()
 for _ in range(abs(index-current)):tap(128 if index>current else 64)
 tap(1);frames(15)
def confirm(yes=True):
 waitfor(lambda:task('Task_HandleYesNoInput') is not None);frames(10);tap(1 if yes else 2)
def begin():
 warp(group,mapnum,4,4)
 # Interact through the actual counter, rather than invoking the script directly.
 frames(12,64);frames(8);tap(1)
 waitfor(lambda:task('Task_HandleChooseMonInput') is not None)
 tap(1);menu(0)
for mode in [0,1]:
 start(0);invoke('StorageChangeMode',mode,1);invoke('ScriptGiveMon',4,5,0)
 # Ensure edits differ from the generated Pokemon's randomized initial values.
 setdata('MON_DATA_HIDDEN_NATURE',0);setdata('MON_DATA_ATK_IV',31)
 invoke('FlagSet',c['FLAG_LA_RED_DEX_GIFTS'])
 if mode:
  for i in range(8):invoke('FlagSet',c['FLAG_BADGE01_GET']+i)
 money=invoke('GetMoney',rd(symbols['gSaveBlock1Ptr'])+c['offsetof(struct SaveBlock1,money)'])
 begin();shutil.copy2(shot('training_menu'),R/'docs/features/training-scientist-menu.png')
 choose(0);menu(0);check('inspection_returns_'+str(mode),True)
 # Cancelling confirmation must not edit an EV.
 before=get('MON_DATA_HP_EV');choose(1);menu(1)
 check('ev_label_current_'+str(mode),stat_label(0).endswith(bytes([0xa1,0,0xbf,0xd0])))
 check('ev_budget_initial_'+str(mode),budget_numbers()==[0,510,510])
 shutil.copy2(shot('ev_stats'),R/'docs/features/training-scientist-ev-menu.png')
 choose(0);menu(2);choose(0)
 confirm(False);menu(1);check('cancel_returns_to_ev_stats_'+str(mode),selected_row()==0);menu(0);check('cancel_no_edit_'+str(mode),get('MON_DATA_HP_EV')==before)
 choose(1);menu(1)
 check('ev_label_after_cancel_'+str(mode),stat_label(0).endswith(bytes([0xa1,0,0xbf,0xd0])))
 choose(0);menu(2);choose(0)
 waitfor(lambda:task('Task_HandleYesNoInput') is not None);frames(10)
 shutil.copy2(shot('training_confirm'),R/'docs/features/training-scientist-confirm.png')
 tap(1);menu(1);check('ev_returns_to_stat_'+str(mode),selected_row()==0);menu(0);check('ui_ev252_'+str(mode),get('MON_DATA_HP_EV')==252)
 # Set Attack IV to zero through the numeric list, then confirm.
 choose(3);menu(1)
 check('iv_label_current_'+str(mode),stat_label(1).endswith(bytes([0xa4,0xa2,0,0xc3,0xd0])))
 shutil.copy2(shot('iv_stats'),R/'docs/features/training-scientist-iv-menu.png')
 choose(1);menu(6)
 old=get('MON_DATA_ATK_IV')
 for _ in range(old):tap(64)
 tap(1);confirm();menu(1);check('iv_returns_to_attack_'+str(mode),selected_row()==1);menu(0);check('ui_iv0_'+str(mode),get('MON_DATA_ATK_IV')==0)
 # 31 All uses the existing confirmation, supports cancellation, and preserves EVs.
 fields=['MON_DATA_HP_IV','MON_DATA_ATK_IV','MON_DATA_DEF_IV','MON_DATA_SPATK_IV','MON_DATA_SPDEF_IV','MON_DATA_SPEED_IV']
 before=[get(f) for f in fields]
 choose(3);menu(1);choose(6);confirm(False);menu(0)
 check('all_ivs_cancel_'+str(mode),[get(f) for f in fields]==before)
 choose(3);menu(1);choose(6);confirm();menu(1);check('all_iv_returns_to_31_all_'+str(mode),selected_row()==6);menu(0)
 check('all_ivs_31_'+str(mode),all(get(f)==31 for f in fields))
 check('all_ivs_keep_evs_'+str(mode),get('MON_DATA_HP_EV')==252)
 choose(3);menu(1);choose(6);menu(0)
 check('all_ivs_already_max_'+str(mode),all(get(f)==31 for f in fields))
 choose(4);menu(3);choose(3);confirm();menu(3);check('nature_return_selection_'+str(mode),selected_row()==3);menu(0)
 check('ui_nature_adamant_'+str(mode),get('MON_DATA_HIDDEN_NATURE')==3)
 choose(5);menu(4);choose(1);confirm();menu(4);check('ability_return_selection_'+str(mode),selected_row()==1);menu(0)
 check('ui_hidden_ability_'+str(mode),get('MON_DATA_ABILITY_NUM')==2)
 # A real exact-value EV choice at 127 must not be mistaken for B/cancel.
 choose(1);menu(1)
 check('ev_budget_updated_'+str(mode),budget_numbers()==[252,510,258])
 check('ev_label_updated_'+str(mode),stat_label(0).endswith(bytes([0xa3,0xa6,0xa3,0,0xbf,0xd0])))
 choose(2);menu(2);choose(3);menu(5)
 for _ in range(127):tap(128)
 check('numeric_ev_cursor_'+str(mode),selected_row()==127)
 tap(1);confirm();menu(0);check('ui_exact_ev127_'+str(mode),get('MON_DATA_DEF_EV')==127)
 # Presets replace the whole EV spread, with cancellable preview.
 evfields=['MON_DATA_HP_EV','MON_DATA_ATK_EV','MON_DATA_DEF_EV','MON_DATA_SPATK_EV','MON_DATA_SPDEF_EV','MON_DATA_SPEED_EV']
 presets=[[6,252,0,0,0,252],[6,0,0,252,0,252],[252,0,252,0,6,0],[252,0,6,0,252,0]]
 before=[get(f) for f in evfields]
 choose(7);menu(8);choose(0);confirm(False);menu(0)
 check('preset_cancel_'+str(mode),[get(f) for f in evfields]==before)
 for index,spread in enumerate(presets):
  choose(7);menu(8)
  if index==0:shutil.copy2(shot('ev_presets'),R/'docs/features/training-scientist-presets.png')
  choose(index);confirm();menu(8);check('preset_return_selection_'+str((mode,index)),selected_row()==index);menu(0)
  check('preset_spread_'+str((mode,index)),[get(f) for f in evfields]==spread)
  check('preset_legal_total_'+str((mode,index)),sum(get(f) for f in evfields)==510)
  check('preset_keeps_ivs_'+str((mode,index)),all(get(f)==31 for f in fields))
 choose(7);menu(8);choose(3);menu(0)
 check('preset_unchanged_'+str(mode),[get(f) for f in evfields]==presets[3])
 choose(6);menu(7)
 level=36 if mode else 16
 choose(level-5);confirm()
 if mode:
  waitfor(lambda:task('Task_EvolutionScene') is not None)
  for i in range(12000):
   if rd(symbols['gSpecialVar_0x8005'],2)==0 and task('Task_HandleScrollingMultichoiceInput') is not None:break
   frames(1,2 if i%20<5 else 0)
  else:raise AssertionError('cancelled evolution did not return')
  check('cancel_evolution_keeps_species',get('MON_DATA_SPECIES')==4 and get('MON_DATA_LEVEL')==36)
  menu(0);choose(6);menu(7);choose(0);confirm()
 menu(0)
 check('ui_level_'+str(mode),get('MON_DATA_LEVEL')==level)
 check('ui_evolution_'+str(mode),get('MON_DATA_SPECIES')==(6 if mode else 5))
 check('ui_money_preserved_'+str(mode),invoke('GetMoney',rd(symbols['gSaveBlock1Ptr'])+c['offsetof(struct SaveBlock1,money)'])==money)
 tap(2);waitfor(lambda:rd(symbols['sGlobalScriptContextStatus'],1)==2)
 check('ui_clean_exit_'+str(mode),task('Task_HandleScrollingMultichoiceInput') is None)
 lib.shutdown()
(R/'docs/features/training-scientist-ui-validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),checks=checks,rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest()),indent=2)+'\n')
print('PASS',len(checks),'training UI/evolution checks')
