"""Native follower selection, party UI and save compatibility in both PC modes."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
import tempfile,struct
D=R/'docs/features/preferred-follower';D.mkdir(exist_ok=True)
names=['MON_DATA_HP','MON_DATA_IS_EGG','MON_DATA_SANITY_IS_BAD_EGG','FLAG_SYS_POKEMON_GET','VAR_LA_FOLLOWER_MODE','MON_DATA_SPECIES']
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'a.c').write_text('#include "global.h"\n#include "pokemon.h"\n#include "constants/flags.h"\nconst unsigned v[]={'+','.join(names)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'a.c'),'-o',str(td/'a.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'a.o'),str(td/'a.bin')],check=True)
 c=dict(zip(names,struct.unpack('<6I',(td/'a.bin').read_bytes())))
for mode in [0,1]:
 start(0);invoke('StorageChangeMode',mode,1)
 invoke('ScriptGiveMon',4,10,0);invoke('ScriptGiveMon',25,10,0)
 p=symbols['gParties'];a=0x0203fc00
 def setfield(mon,field,value):
  wr(a,value);invoke('SetMonData',mon,c[field],a)
 def selected(label,expected):check(str(mode)+'_'+label,invoke('GetFirstLiveMon')==expected)
 selected('default_lead',p)
 check('choose_second_'+str(mode),invoke('PreferredFollower_Set',1)==1)
 selected('chosen_second',p+100)
 check('lead_unchanged_'+str(mode),invoke('GetMonData3',p,c['MON_DATA_SPECIES'],0)==4)
 # Reorder the party without changing Pokémon identities.
 old=[bytes(rd(p+i*100+j,1) for j in range(100)) for i in range(2)]
 for i,mon in enumerate(reversed(old)):
  for j,value in enumerate(mon):wr(p+i*100+j,value,1)
 selected('selection_survives_swap',p)
 setfield(p,'MON_DATA_HP',0);selected('fainted_fallback',p+100)
 setfield(p,'MON_DATA_HP',20);selected('healed_preference',p)
 setfield(p,'MON_DATA_IS_EGG',1);selected('egg_fallback',p+100)
 check('egg_cannot_select_'+str(mode),invoke('PreferredFollower_Set',0)==0)
 setfield(p,'MON_DATA_IS_EGG',0)
 check('invalid_slot_'+str(mode),invoke('PreferredFollower_Set',6)==0)
 invoke('PreferredFollower_Recall');selected('recalled',0)
 invoke('PreferredFollower_Automatic');selected('automatic',p)
 invoke('PreferredFollower_Set',1);selected('before_save',p+100)
 check('save_'+str(mode),invoke('TrySavingData',0)==1)
 invoke('PreferredFollower_Automatic')
 check('reload_'+str(mode),invoke('LoadGameSave',0)==1)
 selected('preference_reloaded',p+100)
 invoke('StorageWriteMon',59 if mode else 13,29,p+100)
 invoke('ZeroMonData',p+100);wr(symbols['gPartiesCount'],1,1)
 selected('stored_fallback',p)
 # Use the actual party menu, not just the selection helpers.
 invoke('FlagSet',c['FLAG_SYS_POKEMON_GET'])
 wr(symbols['sStartMenuPage'],0,1);wr(symbols['sStartMenuCursorPos'],0,1)
 tap(8);frames(45);tap(1);frames(150);tap(1);frames(30)
 # One-mon menu: Summary, Field Skills, Item, Follower, Cancel.
 for i in range(3):tap(128)
 tap(1);frames(30)
 check('follower_submenu_'+str(mode),active('Task_HandleSelectionMenuInput') is not None)
 shutil.copy2(shot('follower_menu_'+str(mode)),D/('menu-'+str(mode)+'.png'))
 tap(1);frames(45);tap(1);frames(45)
 check('ui_sets_preference_'+str(mode),invoke('PreferredFollower_Get')==p)
 tap(2);frames(180);tap(2);frames(60)
 check('menu_returns_'+str(mode),rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1)
 lib.shutdown()
(D/'validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'follower checks')
