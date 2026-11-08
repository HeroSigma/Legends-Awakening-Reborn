"""Native SwSh storage transfer and summary checks in both storage profiles."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'docs/features/swsh-storage';D.mkdir(parents=True,exist_ok=True)
import tempfile,struct
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include \"global.h\"\n#include \"pokemon.h\"\nconst unsigned v[]={ITEM_LEFTOVERS,MON_DATA_HELD_ITEM};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 item,held=struct.unpack('<2I',(td/'c.bin').read_bytes())
for mode in [0,1]:
 start(0);invoke('StorageChangeMode',mode,1)
 invoke('ScriptGiveMon',4,10,0);invoke('ScriptGiveMon',25,10,0)
 p=symbols['gParties'];last=invoke('GetStorageBoxCount')-1
 invoke('StorageWriteMon',last,29,p+100);invoke('StorageFlush')
 wr(rd(symbols['gPokemonStoragePtr']),last,1)
 invoke('ShowPokemonStorageSystemPC');frames(90);tap(1)
 wait('Task_PokeStorageMain',900);frames(120)
 check('last_box_'+str(mode),invoke('StorageGetCurrentBox')==last)
 
 for key in [128]*4+[16]*5:tap(key);frames(20)
 shutil.copy2(shot('storage-last-'+str(mode)),D/('last-box-'+str(mode)+'.png'))
 tap(8);frames(40);shutil.copy2(shot('storage-info-'+str(mode)),D/('info-'+str(mode)+'.png'));tap(8);frames(30)
 tap(1);frames(30);tap(1);frames(100)
 check('picked_up_'+str(mode),invoke('GetBoxMonDataAt',last,29,18)==0)
 # Move across the last-to-first boundary while holding the Pokemon.
 
 for _ in range(5):tap(64);frames(20)
 tap(16);frames(160)
 check('holding_wrap_'+str(mode),invoke('StorageGetCurrentBox')==0)
 
 tap(128);frames(30)
 for _ in range(rd(symbols['sCursorPosition'],1)%6):tap(32);frames(20)
 tap(1);frames(30);tap(1);frames(120)
 check('placed_first_box_'+str(mode),invoke('GetBoxMonDataAt',0,0,18)==25)
 check('source_stays_empty_'+str(mode),invoke('GetBoxMonDataAt',last,29,18)==0)
 tap(1);frames(30);tap(128);tap(1);frames(240)
 shutil.copy2(shot('storage-summary-'+str(mode)),D/('summary-'+str(mode)+'.png'))
 check('summary_open_'+str(mode),rd(symbols['gMain']+4)!=symbols['CB2_PokeStorageSystem']|1 if 'CB2_PokeStorageSystem' in symbols else active('Task_PokeStorageMain') is None)
 tap(2);frames(240);wait('Task_PokeStorageMain',900)
 check('summary_return_'+str(mode),invoke('GetBoxMonDataAt',0,0,18)==25)
 shutil.copy2(shot('storage-return-'+str(mode)),D/('return-'+str(mode)+'.png'))
 # Withdraw through the actual menu (Move, Summary, Withdraw).
 tap(1);frames(30);tap(128);tap(128);tap(1);frames(240)
 check('withdraw_clears_box_'+str(mode),invoke('GetBoxMonDataAt',0,0,18)==0)
 check('withdraw_grows_party_'+str(mode),invoke('CountPartyMons')==3)
 # Flush and save with the decoded box cache alive, then reload.
 tap(2);frames(30);tap(128);tap(1);frames(240);tap(2);frames(60)
 check('save_'+str(mode),invoke('TrySavingData',0)==1)
 check('reload_'+str(mode),invoke('LoadGameSave',0)==1)
 check('profile_preserved_'+str(mode),invoke('GetStorageBoxCount')==last+1)
 check('party_preserved_'+str(mode),invoke('CountPartyMons')==3)
 check('no_duplicate_'+str(mode),invoke('CountStorageNonEggMons')==0)
 # PC Move Items sends a boxed held item to the correct Bag pocket once.
 wr(0x03007400,item);invoke('SetMonData',p+100,held,0x03007400)
 invoke('StorageWriteMon',0,0,p+100);invoke('StorageFlush')
 before=invoke('CountTotalItemQuantityInBag',item)
 invoke('ShowPokemonStorageSystemPC');frames(90)
 for _ in range(3):tap(128)
 tap(1);wait('Task_PokeStorageMain',900);frames(120)
 tap(1);frames(30);tap(128);tap(1);frames(240)
 check('pc_item_cleared_'+str(mode),invoke('GetBoxMonDataAt',0,0,held)==0)
 check('pc_item_to_bag_'+str(mode),invoke('CountTotalItemQuantityInBag',item)==before+1)
 shutil.copy2(shot('storage-items-'+str(mode)),D/('items-'+str(mode)+'.png'))
 tap(2);frames(30);tap(128);tap(1);frames(240);tap(2);frames(60)
 lib.shutdown()
(D/'validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'SwSh storage checks')
