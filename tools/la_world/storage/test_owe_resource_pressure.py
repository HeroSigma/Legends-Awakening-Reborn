"""Route 104 resource exhaustion is a deferred spawn, never a fatal assert."""
from pathlib import Path
R=Path.cwd()
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
import struct,tempfile,json,hashlib
start(0);invoke('ScriptGiveMon',1,10,0)
warp(0,19,26,55);invoke('ScriptContext_Init');invoke('UnlockPlayerFieldControls')
# Ensure all field-message gates are clear and the production timer can run.
frames(120)
bitmap=symbols['sSpriteTileAllocBitmap'];pal=symbols['sSpritePaletteTags']
tiles=bytes(rd(bitmap+i,1) for i in range(128));pals=bytes(rd(pal+i,1) for i in range(32))
for pressure in ['tiles','palettes','both']:
 for i in range(128):wr(bitmap+i,255 if pressure in ['tiles','both'] else tiles[i],1)
 for i in range(16):wr(pal+i*2,100+i if pressure in ['palettes','both'] else int.from_bytes(pals[i*2:i*2+2],'little'),2)
 for i in range(100):
  wr(symbols['sOWESpawnCountdown'],0,2)
  invoke('UpdateOverworldWildEncounter')
 check('resource_pressure_returns_'+pressure,rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1)
 for i,b in enumerate(tiles):wr(bitmap+i,b,1)
 for i,b in enumerate(pals):wr(pal+i,b,1)
# A real 64x64 regional sprite can still load when there is room.
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "constants/event_object_movement.h"\n#include <stddef.h>\nconst struct ObjectEventTemplate o={.localId=247,.x=26,.y=54,.elevation=3,.movementType=MOVEMENT_TYPE_FACE_DOWN};\nconst unsigned v[]={sizeof(struct ObjectEventTemplate),offsetof(struct ObjectEventTemplate,graphicsId)};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 raw=(td/'c.bin').read_bytes();size,off=struct.unpack('<II',raw[-8:])
 for i,b in enumerate(raw[:size]):wr(0x03007400+i,b,1)
 graphics=invoke('GetGraphicsIdForMon',972,0,1)
 for i in range(2):wr(0x03007400+off+i,(graphics>>(8*i))&255,1)
 invoke('DespawnAllOverworldWildEncounters',1,0);frames(60)
 obj=invoke('SpawnSpecialObjectEvent',0x03007400)
 check('alolan_exeggutor_sprite_available',obj<16)
 frames(3)
 print(shot('route104_alolan_exeggutor'),flush=True)
# Return to normal field execution after resource restoration.
for _ in range(100):frames(10)
check('route104_keeps_running',rd(symbols['gMain']+4) in [symbols['CB2_Overworld']|1,symbols['BattleMainCB2']|1])
report=dict(passed=True,checks=checks,user_save_loaded=False,rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest())
(R/'docs/features/owe-resource-validation.json').write_text(json.dumps(report,indent=2)+'\n')
print('PASS',len(checks),'resource pressure checks',flush=True)
