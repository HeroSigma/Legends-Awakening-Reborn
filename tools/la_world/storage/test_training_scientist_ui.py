"""In-game scientist menus, cancellation, free edits and normal evolution flow."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_training_scientist.py').read_text().split('for mode in [0,1]:')[0],'training_helpers','exec'))
mg=json.loads((R/'data/maps/map_groups.json').read_text());name='OldaleTown_PokemonCenter_2F'
for group,gname in enumerate(mg['group_order']):
 if name in mg[gname]:mapnum=mg[gname].index(name);break
row=next(x for x in json.loads((R/'docs/features/training-scientist-locations.json').read_text()) if x['map']==name)
def menu(kind):
 waitfor(lambda:rd(symbols['gSpecialVar_0x8005'],2)==kind and task('Task_HandleScrollingMultichoiceInput') is not None)
 frames(15)
def choose(index):
 for _ in range(index):tap(128)
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
 invoke('FlagSet',c['FLAG_LA_RED_DEX_GIFTS'])
 if mode:
  for i in range(8):invoke('FlagSet',c['FLAG_BADGE01_GET']+i)
 money=invoke('GetMoney',rd(symbols['gSaveBlock1Ptr'])+c['offsetof(struct SaveBlock1,money)'])
 begin();shutil.copy2(shot('training_menu'),R/'docs/features/training-scientist-menu.png')
 choose(0);menu(0);check('inspection_returns_'+str(mode),True)
 # Cancelling confirmation must not edit an EV.
 before=get('MON_DATA_HP_EV');choose(1);menu(1);choose(0);menu(2);choose(0)
 confirm(False);menu(0);check('cancel_no_edit_'+str(mode),get('MON_DATA_HP_EV')==before)
 choose(1);menu(1);choose(0);menu(2);choose(0)
 waitfor(lambda:task('Task_HandleYesNoInput') is not None);frames(10)
 shutil.copy2(shot('training_confirm'),R/'docs/features/training-scientist-confirm.png')
 tap(1);menu(0);check('ui_ev252_'+str(mode),get('MON_DATA_HP_EV')==252)
 # Set Attack IV to zero through the numeric list, then confirm.
 choose(3);menu(1);choose(1);menu(6)
 old=get('MON_DATA_ATK_IV')
 for _ in range(old):tap(64)
 tap(1);confirm();menu(0);check('ui_iv0_'+str(mode),get('MON_DATA_ATK_IV')==0)
 choose(4);menu(3);choose(3);confirm();menu(0)
 check('ui_nature_adamant_'+str(mode),get('MON_DATA_HIDDEN_NATURE')==3)
 choose(5);menu(4);choose(1);confirm();menu(0)
 check('ui_hidden_ability_'+str(mode),get('MON_DATA_ABILITY_NUM')==2)
 # A real exact-value EV choice at 127 must not be mistaken for B/cancel.
 choose(1);menu(1);choose(2);menu(2);choose(3);menu(5)
 for _ in range(127):tap(128)
 tap(1);confirm();menu(0);check('ui_exact_ev127_'+str(mode),get('MON_DATA_DEF_EV')==127)
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
