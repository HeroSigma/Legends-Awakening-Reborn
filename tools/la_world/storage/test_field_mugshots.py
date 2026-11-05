"""Native speaker portraits, ownership and cleanup; disposable saves only."""
from pathlib import Path
import tempfile, struct
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'docs/features/field-mugshots';D.mkdir(parents=True,exist_ok=True)
checks=[]
def check(n,v):
 checks.append(dict(test=n,passed=bool(v)));assert v,n
speakers=['PLAYER','BIRCH','RED','BRENDAN','MAY','WALLY','NORMAN','GIOVANNI','OAK','BLUE','GREEN','SHADOW_TRIAD','AQUA_GRUNT','CYRUS','NONE','DEVON_RESEARCHER']
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "constants/speaker_names.h"\nconst unsigned v[]={'+','.join('SP_NAME_'+n for n in speakers)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 ids=dict(zip(speakers,struct.unpack('<'+str(len(speakers))+'I',(td/'c.bin').read_bytes())))
def speaker(n):wr(symbols['gSpeakerName'],rd(symbols['gSpeakerNamesTable']+ids[n]*4))
def show(n):
 speaker(n);check('show_'+n,invoke('ShowFieldMessage',symbols['LegendsVoice_WoodsQuestion'])==1);frames(180)
def capture(n):shutil.copy2(shot('portrait_'+n),D/(n+'.png'))
def clean(n):
 invoke('HideFieldMessageBox');frames(3)
 check('hidden_'+n,not invoke('IsFieldMugshotActive'))
 check('palette_freed_'+n,invoke('IndexOfSpritePaletteTag',0xb75a)==255)
 check('tiles_freed_'+n,invoke('GetSpriteTileStartByTag',0xb75a)==65535)
for mode in [0,1]:
 start(mode);invoke('StorageChangeMode',mode,1)
 for n in speakers:
  show(n)
  check(f'portrait_{mode}_{n}',bool(invoke('IsFieldMugshotActive'))==(n not in ['CYRUS','NONE','DEVON_RESEARCHER']))
  if n in ['PLAYER','RED','BIRCH','GIOVANNI','WALLY','CYRUS']:capture(f'mode{mode}_{n}')
  clean(n)
 # Switching speakers while the previous textbox is still drawn.
 for n in ['RED','BIRCH','PLAYER','NONE','MAY','DEVON_RESEARCHER']:
  show(n);frames(180,1)
  for i in range(600):
   if invoke('IsFieldMessageBoxHidden'):break
   frames(1,1 if i%15==0 else 0)
  check('switch_active_'+n,bool(invoke('IsFieldMugshotActive'))==(n not in ['NONE','DEVON_RESEARCHER']))
 clean('switch_end')
 # Dark-cave visibility uses a matching OBJ-window mask, restored on close.
 invoke('SetFlashLevel',1)
 before=rd(0x04000000,2);out=rd(0x0400004a,2)
 show('RED');check('flash_mask_'+str(mode),rd(symbols['sMask'],1)<64);capture(f'mode{mode}_flash')
 clean('flash');check('flash_window_restore_'+str(mode),rd(0x04000000,2)==before and rd(0x0400004a,2)==out)
 invoke('SetFlashLevel',0)
 # The player uses custom colors; same-gender rivals retain their original art.
 invoke('DynamicPal_SetSelection',0x123)
 show('PLAYER')
 slot=invoke('IndexOfSpritePaletteTag',0xb75a)
 ptr=invoke('DynamicPal_TrainerPalette',mode+1,1)
 check('custom_player_palette_'+str(mode),all(rd(symbols['gPlttBufferUnfaded']+(256+16*slot+i)*2,2)==rd(ptr+i*2,2) for i in range(16)))
 capture(f'mode{mode}_custom_PLAYER');clean('custom_player')
 rival='MAY' if mode else 'BRENDAN'
 show(rival);slot=invoke('IndexOfSpritePaletteTag',0xb75a);ptr=symbols['gTrainerPalette_HyperRivalMay' if mode else 'gTrainerPalette_HyperRivalBrendan']
 check('rival_palette_unchanged_'+str(mode),all(rd(symbols['gPlttBufferUnfaded']+(256+16*slot+i)*2,2)==rd(ptr+i*2,2) for i in range(16)))
 clean('custom_rival');invoke('DynamicPal_SetSelection',0)
 # Palette exhaustion must not reclaim an encounter palette.
 for tag in range(0x7100,0x7110):invoke('AllocSpritePalette',tag)
 show('RED');check('palette_exhaustion_safe_'+str(mode),not invoke('IsFieldMugshotActive'));clean('palette_exhausted')
 for tag in range(0x7100,0x7110):invoke('FreeSpritePaletteByTag',tag)
 # Resource exhaustion must leave readable dialogue without touching field sprites.
 for j in range(24):wr(0x03007400+j,rd(symbols['sFieldPortraitTemplate']+j,1),1)
 wr(0x03007400,0,2);wr(0x03007402,65535,2)
 for i in range(64):invoke('CreateSpriteUnchecked',0x03007400,1000,1000,0)
 show('RED');check('sprite_exhaustion_safe_'+str(mode),not invoke('IsFieldMugshotActive'));clean('exhausted')
 lib.shutdown()
(D/'validation.json').write_text(json.dumps(dict(rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks,user_save_loaded=False),indent=2)+'\n')
print('PASS',len(checks),'field mugshot checks',flush=True)
