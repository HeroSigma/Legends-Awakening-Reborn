"""Outdoor battle palette blending and indoor/UI/sprite isolation."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
import tempfile,struct
D=R/'docs/features/battle-dns';D.mkdir(exist_ok=True)
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "battle_environment.h"\n#include "constants/map_types.h"\n#include <stddef.h>\nconst unsigned v[]={sizeof(struct BattleEnvironment),offsetof(struct BattleEnvironment,palette),offsetof(struct MapHeader,mapType),MAP_TYPE_ROUTE,MAP_TYPE_INDOOR,MAP_TYPE_UNDERGROUND};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 size,off,mapoff,route,indoor,cave=struct.unpack('<6I',(td/'c.bin').read_bytes())
start(0)
wr(0x03007300,0x4770,2);wr(symbols['gMain']+4,0x03007301)
pal=rd(symbols['gBattleEnvironmentInfo']+off)
def readpal(base):return [rd(base+i*2,2) for i in range(512)]
raw=[rd(pal+i*2,2) for i in range(48)]
for hour in [12,6,20,23]:
 wr(symbols['sHoursOverride'],hour,1);invoke('UpdateTimeOfDay',1)
 for kind in [route,indoor,cave]:
  wr(symbols['gMapHeader']+mapoff,kind,1)
  before=readpal(symbols['gPlttBufferUnfaded'])
  invoke('LoadBattleTimePalette',pal)
  after=readpal(symbols['gPlttBufferUnfaded'])
  check('ui_sprites_untouched_'+str((hour,kind)),before[:32]+before[80:]==after[:32]+after[80:])
  if kind!=route or hour==12:check('normal_colors_'+str((hour,kind)),after[32:80]==raw)
  else:check('outdoor_tinted_'+str(hour),after[32:80]!=raw)
  invoke('LoadBattleTimePalette',pal)
  check('no_compounding_'+str((hour,kind)),readpal(symbols['gPlttBufferUnfaded'])[32:80]==after[32:80])
lib.shutdown()
battle_colors=[]
for hour in [12,23]:
 start(0);wr(symbols['sHoursOverride'],hour,1)
 invoke('SetWarpDestination',0,17,255,5,12);invoke('WarpIntoMap')
 wr(symbols['gMain']+4,symbols['CB2_LoadMap']|1);frames(240)
 wr(symbols['sHoursOverride'],hour,1)
 invoke('UpdateTimeOfDay',1)
 check('outdoor_map_'+str(hour),rd(symbols['gMapHeader']+mapoff,1)==route)
 invoke('ScriptGiveMon',25,10,0);invoke('CreateScriptedWildMon',261,3,0)
 invoke('BattleSetup_StartWildBattle')
 for i in range(1200):
  frames(1,1 if i%30==0 else 0)
  if rd(symbols['gBattleMainFunc'])==symbols['HandleTurnActionSelectionState']|1:
   frames(40);break
 battle_colors.append(readpal(symbols['gPlttBufferUnfaded'])[32:80])
 check('battle_running_'+str(hour),rd(symbols['gMain']+4)!=symbols['CB2_Overworld']|1)
 shutil.copy2(shot('battle_dns_'+str(hour)),D/('battle-'+str(hour)+'.png'))
 lib.shutdown()
check('real_night_background_differs',battle_colors[0]!=battle_colors[1])
(D/'validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'battle lighting checks')
