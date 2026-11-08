"""Native summary -> stat editor -> summary and compact storage validation."""
from pathlib import Path
import tempfile,struct,json,hashlib
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'docs/features/summary-stat-editor';D.mkdir(parents=True,exist_ok=True)
checks=[]
def check(n,v):
 checks.append(dict(test=n,passed=bool(v)));assert v,n
names=['SUMMARY_MODE_NORMAL','PC_MON_CHOSEN','MON_DATA_HP','MON_DATA_MAX_HP','MON_DATA_PERSONALITY','MON_DATA_TERA_TYPE','MON_DATA_HIDDEN_NATURE','MON_DATA_ABILITY_NUM','MON_DATA_IS_EGG','MON_DATA_SANITY_IS_BAD_EGG','MON_DATA_SPECIES','MON_DATA_LEVEL']+[f'MON_DATA_{s}_{t}' for t in ['IV','EV'] for s in ['HP','ATK','DEF','SPATK','SPDEF','SPEED']]
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'a.c').write_text('#include "global.h"\n#include "pokemon.h"\n#include "pokemon_summary_screen.h"\n#include "pokemon_storage_system.h"\n#include "constants/party_menu.h"\nconst unsigned values[]={'+','.join(names)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'a.c'),'-o',str(td/'a.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'a.o'),str(td/'a.bin')],check=True)
 c=dict(zip(names,struct.unpack('<'+str(len(names))+'I',(td/'a.bin').read_bytes())))
def field(mon,n):return invoke('GetMonData3',mon,c['MON_DATA_'+n],0)
def put(mon,n,value):wr(0x03007400,value);invoke('SetMonData',mon,c['MON_DATA_'+n],0x03007400)
def capture(n):shutil.copy2(shot('stat_'+n),D/(n+'.png'))
def skills(index=0):
 invoke('ShowPokemonSummaryScreen_SwSh',0,symbols['gParties'],index,1,symbols['CB2_ReturnToField']|1)
 wr(symbols['gMain']+4,symbols['CB2_InitSummaryScreen']|1);wait('Task_HandleInput',1800);frames(40);tap(16);frames(60)
def editor():
 tap(8);wait('Task_StatEditorMain',1800);frames(25)
for mode in [0,1]:
 print('CASE',mode,flush=True)
 start(mode);invoke('StorageChangeMode',mode,1);invoke('ScriptGiveMon',4,16,0);invoke('ScriptGiveMon',7,16,0)
 m=symbols['gParties'];m2=m+100
 put(m,'HP',1);put(m2,'HP',0);put(m,'HIDDEN_NATURE',0);put(m,'ABILITY_NUM',0)
 oldhp=field(m,'MAX_HP')-1;pid=field(m,'PERSONALITY');tera=field(m,'TERA_TYPE')
 skills();capture(f'{mode}_skills_entry');editor();capture(f'{mode}_editor')
 tap(8);frames(30)
 check(f'{mode}_31_all',all(field(m,s+'_IV')==31 for s in ['HP','ATK','DEF','SPATK','SPDEF','SPEED']))
 check(f'{mode}_damage_preserved',field(m,'MAX_HP')-field(m,'HP')==oldhp)
 tap(16)
 for i in range(3):
  tap(1);tap(256);tap(2)
  if i<2:tap(128)
 check(f'{mode}_ev_budget',tuple(field(m,s+'_EV') for s in ['HP','ATK','DEF','SPATK','SPDEF','SPEED'])==(252,252,6,0,0,0))
 tap(32);tap(128);tap(1);tap(16);tap(2)
 check(f'{mode}_legal_ability',field(m,'ABILITY_NUM')==2)
 tap(128);tap(1);tap(16);tap(2)
 check(f'{mode}_nature_effects',field(m,'HIDDEN_NATURE')==1)
 check(f'{mode}_identity_and_tera_preserved',field(m,'PERSONALITY')==pid and field(m,'TERA_TYPE')==tera)
 tap(256);wait('Task_StatEditorMain',500);tap(8)
 check(f'{mode}_cycles_to_second_mon',field(m2,'HP_IV')==31)
 check(f'{mode}_fainted_stays_fainted',field(m2,'HP')==0)
 tap(2);wait('Task_HandleInput',1800);frames(30);capture(f'{mode}_back_to_summary')
 check(f'{mode}_return_index',rd(symbols['gLastViewedMonIndex'],1)==1)
 tap(2);frames(150)
 # Edit the final slot of the final box, then save/reload using native storage.
 box=59 if mode else 13;slot=29
 put(m,'HP_IV',0);invoke('StorageWriteMon',box,slot,m)
 wr(rd(symbols['gPokemonStoragePtr']),box,1)
 wr(symbols['gSpecialVar_MonBoxId'],box,2);wr(symbols['gSpecialVar_MonBoxPos'],slot,2)
 invoke('ShowPokemonSummaryScreen_SwSh',0,0,c['PC_MON_CHOSEN'],29,symbols['CB2_ReturnToField']|1)
 wr(symbols['gMain']+4,symbols['CB2_InitSummaryScreen']|1);wait('Task_HandleInput',1800);frames(40);tap(16);frames(60);editor()
 tap(8);frames(25)
 check(f'{mode}_last_box_edited',invoke('GetBoxMonDataAt',box,slot,c['MON_DATA_HP_IV'])==31)
 tap(2);wait('Task_HandleInput',1800);tap(2);frames(160)
 check(f'{mode}_save',invoke('TrySavingData',0)==1)
 check(f'{mode}_reload',invoke('LoadGameSave',0)==1)
 check(f'{mode}_box_edit_persisted',invoke('GetBoxMonDataAt',box,slot,c['MON_DATA_HP_IV'])==31)
 check(f'{mode}_party_edits_persisted',field(m,'HIDDEN_NATURE')==1 and field(m,'ATK_EV')==252)
 lib.shutdown()
def confirm_scientist():
 for i in range(1800):
  if active('Task_HandleYesNoInput') is not None:break
  frames(1,1 if i%20==0 else 0)
 else:raise AssertionError('scientist confirmation did not open')
 frames(15);tap(1);frames(45)
# Exercise the remaining scientist services through their real field menus.
start(0);invoke('ScriptGiveMon',4,5,0);m=symbols['gParties']
wr(symbols['gSpecialVar_0x8009'],0,2)
invoke('ScriptContext_SetupScript',symbols['LegendsTraining_Main'])
wait('Task_HandleScrollingMultichoiceInput',600);frames(15);capture('scientist_services')
tap(128);tap(1);wait('Task_HandleScrollingMultichoiceInput',600);frames(20);tap(1)
confirm_scientist()
check('scientist_presets_retained',tuple(field(m,x+'_EV') for x in ['HP','ATK','DEF','SPATK','SPDEF','SPEED'])==(6,252,0,0,0,252))
for i in range(400):
 if active('Task_HandleScrollingMultichoiceInput') is not None:break
 frames(1,1 if i%20==0 else 0)
wait('Task_HandleScrollingMultichoiceInput',600);tap(2);frames(40)
wait('Task_HandleScrollingMultichoiceInput',600);tap(1);frames(40)
wait('Task_HandleScrollingMultichoiceInput',600);tap(128);tap(1)
confirm_scientist()
check('scientist_level_retained',field(m,'LEVEL')==6)
lib.shutdown()
(D/'validation.json').write_text(json.dumps(dict(rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks,user_save_loaded=False),indent=2)+'\n')
print('PASS',len(checks),'summary stat editor checks',flush=True)
