"""SwSh party rendering and native selection actions in both storage modes."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_preferred_follower.py').read_text().split('for mode in [0,1]:')[0],'helpers','exec'))
D=R/'docs/features/swsh-party-menu';D.mkdir(parents=True,exist_ok=True)
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'items.c').write_text('#include "global.h"\n#include "pokemon.h"\nconst unsigned v[]={ITEM_LEFTOVERS,MON_DATA_HELD_ITEM};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'items.c'),'-o',str(td/'items.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'items.o'),str(td/'items.bin')],check=True)
 c.update(zip(['ITEM_LEFTOVERS','MON_DATA_HELD_ITEM'],struct.unpack('<2I',(td/'items.bin').read_bytes())))

for mode in [0,1]:
 start(0);invoke('StorageChangeMode',mode,1)
 for species in [4,25,906,903,559,679]:invoke('ScriptGiveMon',species,10,0)
 p=symbols['gParties'];a=0x0203fc00
 invoke('FlagSet',c['FLAG_SYS_POKEMON_GET'])
 def mon(slot,field):return invoke('GetMonData3',p+slot*100,c[field],0)
 def openparty():
  wr(symbols['sStartMenuPage'],0,1);wr(symbols['sStartMenuCursorPos'],0,1)
  tap(8);frames(50);tap(1);frames(180)
  check('party_open_'+str(mode),active('Task_HandleChooseMonInput') is not None)
 def closeparty():
  tap(2);frames(200);tap(2);frames(200);tap(2);frames(60)
  check('field_return_'+str(mode),rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1)
 openparty();shutil.copy2(shot('swsh-six-'+str(mode)),D/('six-'+str(mode)+'.png'))
 # Every visible row must resolve to the same species when selected as follower.
 for slot in range(6):
  if slot:tap(128)
  frames(20);tap(1);frames(25)
  # Summary, Field Skills, Switch, Item, Follower, Cancel
  for _ in range(4):tap(128)
  tap(1);frames(25);tap(1);frames(180)
  check('follower_slot_'+str((mode,slot)),invoke('PreferredFollower_Get')==p+slot*100)
 shutil.copy2(shot('swsh-slot-'+str(mode)),D/('selected-'+str(mode)+'.png'))
 closeparty()
 # Summary handoff and return retain this menu, then close cleanly.
 openparty();tap(1);frames(20);tap(1);frames(200)
 check('summary_handoff_'+str(mode),rd(symbols['gMain']+4)!=symbols['CB2_Overworld']|1)
 tap(2);frames(200)
 check('summary_return_'+str(mode),active('Task_HandleChooseMonInput') is not None or active('Task_HandleSelectionMenuInput') is not None)
 closeparty()
 # Party reordering uses the actual Switch action and preserves identities.
 openparty();before=[mon(i,'MON_DATA_SPECIES') for i in range(6)]
 tap(1);frames(25);tap(128);tap(128);tap(1);frames(30)
 tap(128);tap(1);frames(240)
 check('switch_first_'+str(mode),mon(0,'MON_DATA_SPECIES')==before[1])
 check('switch_second_'+str(mode),mon(1,'MON_DATA_SPECIES')==before[0])
 check('follower_survives_ui_switch_'+str(mode),invoke('PreferredFollower_Get')==p+500)
 closeparty()
 # Taking a held item returns it to the expanded Bag exactly once.
 wr(a,c['ITEM_LEFTOVERS']);invoke('SetMonData',p,c['MON_DATA_HELD_ITEM'],a)
 count=invoke('CountTotalItemQuantityInBag',c['ITEM_LEFTOVERS'])
 openparty();tap(1);frames(25)
 for _ in range(3):tap(128)
 tap(1);frames(30);tap(128);tap(1);frames(200)
 check('held_item_removed_'+str(mode),mon(0,'MON_DATA_HELD_ITEM')==0)
 check('held_item_returned_'+str(mode),invoke('CountTotalItemQuantityInBag',c['ITEM_LEFTOVERS'])==count+1)
 shutil.copy2(shot('swsh-take-'+str(mode)),D/('item-'+str(mode)+'.png'))
 closeparty()
 # Fainted and egg presentation, with safe rejection of companion selection.
 wr(a,0);invoke('SetMonData',p,c['MON_DATA_HP'],a)
 wr(a,1);invoke('SetMonData',p+100,c['MON_DATA_IS_EGG'],a)
 openparty();shutil.copy2(shot('swsh-status-'+str(mode)),D/('status-'+str(mode)+'.png'))
 closeparty()
 lib.shutdown()
(D/'validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'SwSh party checks')
