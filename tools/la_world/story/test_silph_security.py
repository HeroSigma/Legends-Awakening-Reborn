"""Native security doors, elevator Card Key and one-time Silph rewards."""
from pathlib import Path
R=Path.cwd()
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
import tempfile,struct,re,json,hashlib
names=['ITEM_CARD_KEY','ITEM_ALAKAZITE','ITEM_MANECTITE','ITEM_SCIZORITE','ITEM_NORMALIUM_Z','ITEM_ELECTRIUM_Z','ITEM_PSYCHIUM_Z','FLAG_LA_SILPH_CARD_KEY','FLAG_LA_SILPH_PORYGON','FLAG_LA_SILPH_DOOR_BASE','FLAG_LA_SILPH_WALLY_FOUND','FLAG_LA_SILPH_PETREL_DEFEATED','FLAG_LA_SILPH_ARIANA_DEFEATED','FLAG_LA_RED_DEX_GIFTS','FLAG_BADGE01_GET','VAR_LA_ASHES_STATE','SPECIES_PORYGON','MON_DATA_SPECIES','FLAG_HIDE_LITTLEROOT_TOWN_BIRCHS_LAB_BIRCH','FLAG_HIDE_ROUTE_103_RIVAL']
for floor in range(1,12):names.append('MAP_KANTOAR_1_'+str(46+floor)+'_SILPHCO_'+str(floor)+'F')
names.append('MAP_KANTOAR_1_58_SILPHCO_ELEVATOR')
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "constants/flags.h"\n#include "constants/vars.h"\n#include "constants/maps.h"\n#include "constants/items.h"\nconst unsigned v[]={'+','.join(names)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 c=dict(zip(names,struct.unpack('<'+str(len(names))+'I',(td/'c.bin').read_bytes())))
def flag(n):return invoke('FlagGet',c[n])
def at(f,x=1,y=4):
 m=c['MAP_KANTOAR_1_'+str(46+f)+'_SILPHCO_'+str(f)+'F'];warp(m>>8,m&255,x,y);frames(60)
def ended():return rd(symbols['sGlobalScriptContextStatus'],1)==2 and not rd(symbols['sLockFieldControls'],1) and rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1
def finish(label,limit=16000):
 for i in range(limit):
  if ended():frames(20);return
  frames(1,1 if i%24<3 else 0)
 print(shot('security_timeout_'+label),flush=True);raise AssertionError(label)
def run(label):invoke('ScriptContext_SetupScript',symbols[label]);frames(2)
start(0);invoke('FlagSet',c['FLAG_LA_RED_DEX_GIFTS']);invoke('VarSet',c['VAR_LA_ASHES_STATE'],4)
for i in range(3):invoke('FlagSet',c['FLAG_BADGE01_GET']+i)
for sp in [1,4,7,25,133,155]:invoke('ScriptGiveMon',sp,26,0)
preserved_flags={n:invoke('FlagGet',c[n]) for n in ['FLAG_HIDE_LITTLEROOT_TOWN_BIRCHS_LAB_BIRCH','FLAG_HIDE_ROUTE_103_RIVAL']}
# Native font widths for security, reward and Flannery text.
for name in sorted(symbols):
 if not(name.startswith('SilphSecurity_Text_') or name.startswith('Ashes_Text_Flannery')):continue
 data=bytearray()
 for j in range(2000):
  b=rd(symbols[name]+j,1)
  if b==255:break
  data.append(b)
 for i,line in enumerate(re.split(b'[\xfe\xfb\xfa]',bytes(data))):
  for j,b in enumerate(line+b'\xff'):wr(0x03007500+j,b,1)
  check('fit_'+name+'_'+str(i),invoke('GetStringWidth',1,0x03007500,0)<=208)
# Every native card door has an independent project flag; the bed routes stay open.
source=(R/'data/scripts/silphco_doors.inc').read_text()
doors=[]
for i,m in enumerate(re.finditer(r'EventScript_Close(\d+)FDoor(\d*)::',source)):
 floor=int(m[1]);suffix=m[2];key=f'{floor}FDoor{suffix}'
 close=source.split('EventScript_Close'+key+'::',1)[1].split('return',1)[0]
 opened=source.split('EventScript_Open'+key+'::',1)[1].split('return',1)[0]
 closed={(int(x),int(y)) for x,y,coll in re.findall(r'setmetatile (\d+), (\d+), \w+, ([01])',close) if coll=='1'}
 passage=next((int(x),int(y)) for x,y,coll in re.findall(r'setmetatile (\d+), (\d+), \w+, ([01])',opened) if coll=='0' and (int(x),int(y)) in closed)
 at(floor)
 check('door_initial_'+str(i),(invoke('MapGridGetCollisionAt',passage[0]+7,passage[1]+7)==0)==(floor==9 and suffix in ['1','2']))
 doors.append((floor,suffix,key,i,passage))
at(3,8,12);run('LegendsSilph_Door_2');finish('locked')
check('no_key_keeps_door_locked',not invoke('FlagGet',c['FLAG_LA_SILPH_DOOR_BASE']+2))
# Ninth-floor beds remain accessible; Wally supplies the key hint and heals.
at(9,5,16);tap(32);tap(1);frames(20);finish('wally_hint')
check('wally_hint_saved',flag('FLAG_LA_SILPH_WALLY_FOUND'))
# Interact with the actual ninth-floor elevator entrance.
at(9,24,4);tap(64);tap(1);frames(30)
elevator=c['MAP_KANTOAR_1_58_SILPHCO_ELEVATOR']
for i in range(8000):
 if location()==(elevator>>8,elevator&255):break
 frames(1,1 if i%24<3 else 0)
else:raise AssertionError('Ninth-floor elevator did not open')
finish('elevator_arrival')
tap(32);frames(16,32);frames(10);tap(64);tap(1);frames(30);finish('card_key')
check('card_key_in_bag',invoke('CheckBagHasItem',c['ITEM_CARD_KEY'],1)==1)
check('key_pickup_persistent',flag('FLAG_LA_SILPH_CARD_KEY'))
print(shot('silph_ninth_elevator_key'),flush=True)
# Explicit exit warp must return to the same ninth floor.
tap(16);frames(16,16);frames(10);frames(40,128);frames(150)
check('elevator_returns_to_ninth',location()==(97,16))
for floor,suffix,key,i,passage in doors:
 if floor==9 and suffix in ['1','2']:continue
 if floor==11:
  invoke('FlagSet',c['FLAG_LA_SILPH_PETREL_DEFEATED']);invoke('FlagSet',c['FLAG_LA_SILPH_ARIANA_DEFEATED'])
 at(floor);run('LegendsSilph_Door_'+str(i));finish('open_'+str(i))
 check('key_unlocks_door_'+str(i),invoke('FlagGet',c['FLAG_LA_SILPH_DOOR_BASE']+i)==1 and invoke('MapGridGetCollisionAt',passage[0]+7,passage[1]+7)==0)
 at(floor)
 check('door_stays_open_'+str(i),invoke('MapGridGetCollisionAt',passage[0]+7,passage[1]+7)==0)
# Each reward goes to the bag, and its world object is consumed only on success.
for i,(floor,item) in enumerate([(3,'ITEM_ALAKAZITE'),(4,'ITEM_MANECTITE'),(6,'ITEM_SCIZORITE'),(5,'ITEM_NORMALIUM_Z'),(7,'ITEM_ELECTRIUM_Z'),(10,'ITEM_PSYCHIUM_Z')]):
 at(floor);run('LegendsSilph_Loot_'+str(i));finish('loot_'+str(i))
 check('reward_in_bag_'+item,invoke('CheckBagHasItem',c[item],1)==1)
at(5);run('LegendsSilph_Porygon');finish('porygon')
check('porygon_reward_saved',flag('FLAG_LA_SILPH_PORYGON'))
check('full_party_porygon_sent_to_storage',invoke('GetBoxMonDataAt',0,0,c['MON_DATA_SPECIES'])==c['SPECIES_PORYGON'])
run('LegendsSilph_Porygon');finish('porygon_repeat')
check('porygon_cannot_duplicate',invoke('GetBoxMonDataAt',0,1,c['MON_DATA_SPECIES'])==0)
check('saving_security_state',invoke('TrySavingData',0)==1)
check('security_save_reloads',invoke('LoadGameSave',0)==1)
check('card_and_porygon_flags_survive',flag('FLAG_LA_SILPH_CARD_KEY') and flag('FLAG_LA_SILPH_PORYGON'))
check('Hoenn_story_flags_unchanged',all(invoke('FlagGet',c[n])==v for n,v in preserved_flags.items()))
report=dict(passed=True,checks=checks,user_save_loaded=False,rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest())
p=R/'docs/story/silph-security/validation.json';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(report,indent=2)+'\n')
print('PASS',len(checks),'security and reward checks',flush=True)
