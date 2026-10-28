"""Real DexNav search approach/contact tests; no player battery save."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'.la_work/qol_features/free-approach-test';D.mkdir(parents=True,exist_ok=True)
start(0);invoke('ScriptGiveMon',1,10,0)
import tempfile,struct
source=(R/'src/dexnav.c').read_text();decl=source[source.index('struct DexNavSearch\n'):source.index('struct DexNavGUI\n')]
fields=['tileX','tileY','startingTime','movementCount','species']
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "dexnav.h"\n#include "field_player_avatar.h"\n#include <stddef.h>\n'+decl+'\nconst unsigned v[]={'+','.join('offsetof(struct DexNavSearch,'+f+')' for f in fields)+',DN_VAR_SPECIES,DN_FLAG_SEARCHING,PLAYER_AVATAR_FLAG_DASH,PLAYER_AVATAR_FLAG_MACH_BIKE,PLAYER_AVATAR_FLAG_ON_FOOT,offsetof(struct SaveBlock3,dexNavChain)};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 xoff,yoff,timeoff,movementoff,speciesoff,var,searching,dash,bike,foot,chainoff=struct.unpack('<11I',(td/'c.bin').read_bytes())
warp(0,17,10,12);frames(60)
header=invoke('GetCurrentMapWildMonHeaderId');check('route_encounters',header!=65535)
tod=invoke('GetTimeOfDayForEncounters',header,0)
types=invoke('GetEffectiveWildEncounterTypes',header,tod)
info=rd(types);table=rd(info+4);target=rd(table+2,2)
invoke('VarSet',var,target)
for attempt in range(40):
 invoke('TryStartDexNavSearch')
 if invoke('FlagGet',searching):break
 # Ignore only the retry message from unsuccessful random tile placement.
 invoke('ScriptContext_Init');invoke('UnlockPlayerFieldControls')
else:raise AssertionError('could not place DexNav target')
pointer=rd(symbols['sDexNavSearchDataPtr']);check('real_search_started',pointer!=0 and invoke('FlagGet',searching)==1)
save=rd(symbols['gSaveBlock1Ptr']);x=rd(save,2)+7;y=rd(save+2,2)+7
originalflags=rd(symbols['gPlayerAvatar'],1)
for label,flags in [('walk',foot),('sprint',foot|dash),('bike',bike)]:
 wr(pointer+xoff,x+1,2);wr(pointer+yoff,y,2)
 wr(pointer+timeoff,(rd(symbols['gMain']+0x24)-120)&0xffffffff)
 wr(pointer+movementoff,2,1)
 wr(symbols['gPlayerAvatar'],flags,1)
 chain=rd(symbols['gSaveBlock3Ptr'])+chainoff;wr(chain,77,2)
 check(label+'_no_A_required',invoke('OnStep_DexNavSearch')==0)
 check(label+'_target_stays',rd(symbols['sDexNavSearchDataPtr'])==pointer and invoke('FlagGet',searching)==1)
 check(label+'_chain_preserved',rd(chain,2)==77)
wr(symbols['gPlayerAvatar'],originalflags,1)
# No A press: entering the target's tile follows the native DexNav battle path.
wr(pointer+xoff,x,2);wr(pointer+yoff,y,2)
check('contact_starts_battle',invoke('OnStep_DexNavSearch')==1)
check('search_consumed_once',invoke('FlagGet',searching)==0 and rd(symbols['sDexNavSearchDataPtr'])==0)
check('correct_target_species',rd(symbols['gDexNavSpecies'],2)==target)
check('no_active_search_safe',invoke('OnStep_DexNavSearch')==0)
lib.shutdown()
(R/'docs/features/dexnav-free-approach-validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'DexNav approach/contact checks')
