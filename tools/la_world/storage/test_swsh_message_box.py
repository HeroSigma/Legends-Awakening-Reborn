"""SwSh message/name frame bounds, cleanup and repeated opening in native mGBA."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
import tempfile,struct
names=['SP_NAME_PLAYER','SP_NAME_WALLY','SP_NAME_BIRCH','SP_NAME_NONE','WINDOW_WIDTH','WINDOW_HEIGHT','WINDOW_TILEMAP_LEFT','WINDOW_TILEMAP_TOP','WINDOW_NONE']
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "window.h"\n#include "constants/speaker_names.h"\nconst unsigned v[]={'+','.join(names)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 c=dict(zip(names,struct.unpack('<'+str(len(names))+'I',(td/'c.bin').read_bytes())))
D=R/'docs/features/swsh-message-box';D.mkdir(parents=True,exist_ok=True)
for mode in [0,1]:
 start(0);invoke('StorageChangeMode',mode,1)
 for i,speaker in enumerate(['BIRCH','WALLY','PLAYER','NONE']*3):
  wr(symbols['gSpeakerName'],rd(symbols['gSpeakerNamesTable']+c['SP_NAME_'+speaker]*4))
  check('opens_'+str((mode,i)),invoke('ShowFieldMessage',symbols['LegendsVoice_WoodsQuestion'])==1)
  frames(180)
  check('dialog_width_'+str((mode,i)),invoke('GetWindowAttribute',0,c['WINDOW_WIDTH'])==26)
  win=invoke('GetNameboxWindowId')
  if speaker!='NONE':
   check('name_height_'+str((mode,i)),invoke('GetWindowAttribute',win,c['WINDOW_HEIGHT'])==3)
   check('name_above_frame_'+str((mode,i)),invoke('GetWindowAttribute',win,c['WINDOW_TILEMAP_TOP'])==12)
  if i<4:shutil.copy2(shot('message-'+str((mode,i))),D/(speaker.lower()+'-'+str(mode)+'.png'))
  invoke('HideFieldMessageBox');frames(10)
  check('name_removed_'+str((mode,i)),invoke('GetNameboxWindowId')==c['WINDOW_NONE'])
  tilemap=invoke('GetBgTilemapBuffer',0)
  check('field_frame_cleared_'+str((mode,i)),all((rd(tilemap+(y*32+x)*2,2)&0x3ff)==0 for y in range(12,20) for x in range(30)))
 lib.shutdown()
(D/'validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'message frame checks')
