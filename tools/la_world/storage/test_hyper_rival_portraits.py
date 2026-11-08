"""Native speaker portraits, ownership and cleanup; disposable saves only."""
from pathlib import Path
import tempfile, struct
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'docs/art/hyper-rival-portraits/runtime';D.mkdir(parents=True,exist_ok=True)
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
import hashlib,json,re
from PIL import Image
names=['VAR_LA_PLAYER_OUTFIT', 'FLAG_LA_RED_DEX_GIFTS', 'TRAINER_PIC_HYPER_RIVAL_BRENDAN', 'TRAINER_PIC_HYPER_RIVAL_MAY', 'TRAINER_PIC_BRENDAN', 'TRAINER_PIC_MAY', 'TRAINER_PIC_RS_BRENDAN', 'TRAINER_PIC_RS_MAY', 'sizeof(struct Trainer)', 'offsetof(struct Trainer,trainerPic)', 'sizeof(((struct Trainer*)0)->trainerPic)', 'TRAINERS_COUNT', 'DIFFICULTY_NORMAL', 'TRAINER_BRENDAN_ROUTE_103_MUDKIP', 'TRAINER_BRENDAN_ROUTE_110_MUDKIP', 'TRAINER_BRENDAN_ROUTE_119_MUDKIP', 'TRAINER_BRENDAN_ROUTE_103_TREECKO', 'TRAINER_BRENDAN_ROUTE_110_TREECKO', 'TRAINER_BRENDAN_ROUTE_119_TREECKO', 'TRAINER_BRENDAN_ROUTE_103_TORCHIC', 'TRAINER_BRENDAN_ROUTE_110_TORCHIC', 'TRAINER_BRENDAN_ROUTE_119_TORCHIC', 'TRAINER_MAY_ROUTE_103_MUDKIP', 'TRAINER_MAY_ROUTE_110_MUDKIP', 'TRAINER_MAY_ROUTE_119_MUDKIP', 'TRAINER_MAY_ROUTE_103_TREECKO', 'TRAINER_MAY_ROUTE_110_TREECKO', 'TRAINER_MAY_ROUTE_119_TREECKO', 'TRAINER_MAY_ROUTE_103_TORCHIC', 'TRAINER_MAY_ROUTE_110_TORCHIC', 'TRAINER_MAY_ROUTE_119_TORCHIC', 'TRAINER_BRENDAN_RUSTBORO_TREECKO', 'TRAINER_BRENDAN_RUSTBORO_MUDKIP', 'TRAINER_BRENDAN_RUSTBORO_TORCHIC', 'TRAINER_MAY_RUSTBORO_MUDKIP', 'TRAINER_BRENDAN_LILYCOVE_MUDKIP', 'TRAINER_BRENDAN_LILYCOVE_TREECKO', 'TRAINER_BRENDAN_LILYCOVE_TORCHIC', 'TRAINER_MAY_LILYCOVE_MUDKIP', 'TRAINER_MAY_LILYCOVE_TREECKO', 'TRAINER_MAY_LILYCOVE_TORCHIC', 'TRAINER_MAY_RUSTBORO_TREECKO', 'TRAINER_MAY_RUSTBORO_TORCHIC', 'TRAINER_LA_BRENDAN_ROUTE103_0', 'TRAINER_LA_BRENDAN_ROUTE103_1', 'TRAINER_LA_BRENDAN_ROUTE103_2', 'TRAINER_LA_MAY_ROUTE103_0', 'TRAINER_LA_MAY_ROUTE103_1', 'TRAINER_LA_MAY_ROUTE103_2']
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'a.c').write_text('#include "global.h"\n#include "pokemon.h"\n#include "data.h"\n#include <stddef.h>\nconst unsigned values[]={'+','.join(names)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'a.c'),'-o',str(td/'a.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'a.o'),str(td/'a.bin')],check=True)
 c=dict(zip(names,struct.unpack('<'+str(len(names))+'I',(td/'a.bin').read_bytes())))
def raw(name):
 im=Image.open(R/f'graphics/trainers/front_pics/hyper_rival_{name.lower()}.png');out=[]
 for ty in range(8):
  for tx in range(8):
   for y in range(8):
    for x in range(0,8,2):out.append(im.getpixel((tx*8+x,ty*8+y))|(im.getpixel((tx*8+x+1,ty*8+y))<<4))
 return bytes(out)
for gender in [0,1]:
 start(gender);invoke('StorageChangeMode',gender,1);invoke('FlagSet',c['FLAG_LA_RED_DEX_GIFTS'])
 for outfit in [0,1]:
  invoke('VarSet',c['VAR_LA_PLAYER_OUTFIT'],0xC101 if outfit else 0)
  for choice in [0,0x123]:
   invoke('DynamicPal_SetSelection',choice)
   for name in ['BRENDAN','MAY']:
    show(name);frames(30)
    tile=invoke('GetSpriteTileStartByTag',0xb75a);got=bytes(rd(0x06010000+tile*32+i,1) for i in range(2048))
    check(f'hyper_pixels_{gender}_{outfit}_{choice}_{name}',got==raw(name))
    slot=invoke('IndexOfSpritePaletteTag',0xb75a);pal=symbols['gTrainerPalette_HyperRival'+name.title()]
    check(f'hyper_palette_{gender}_{outfit}_{choice}_{name}',all(rd(symbols['gPlttBufferUnfaded']+(256+16*slot+i)*2,2)==rd(pal+i*2,2) for i in range(16)))
    if choice:capture(f'{gender}_{outfit}_{name}')
    clean(name)
   show('PLAYER');slot=invoke('IndexOfSpritePaletteTag',0xb75a)
   pic=c['TRAINER_PIC_'+('RS_' if outfit else '')+('MAY' if gender else 'BRENDAN')]
   pal=invoke('DynamicPal_TrainerPalette',pic,1)
   check(f'player_palette_separate_{gender}_{outfit}_{choice}',all(rd(symbols['gPlttBufferUnfaded']+(256+16*slot+i)*2,2)==rd(pal+i*2,2) for i in range(16)))
   clean('PLAYER')
 for key in names[13:]:
  addr=symbols['gTrainers']+(c['DIFFICULTY_NORMAL']*c['TRAINERS_COUNT']+c[key])*c['sizeof(struct Trainer)']
  info=invoke('LegendsTrainer_Get',c[key],addr)
  pic=rd(info+c['offsetof(struct Trainer,trainerPic)'],c['sizeof(((struct Trainer*)0)->trainerPic)'])
  expected=c['TRAINER_PIC_HYPER_RIVAL_MAY' if 'MAY' in key else 'TRAINER_PIC_HYPER_RIVAL_BRENDAN']
  check('battle_portrait_'+str(gender)+'_'+key,pic==expected)
 lib.shutdown()
(D/'validation.json').write_text(json.dumps(dict(rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks,user_save_loaded=False),indent=2)+'\n')
print('PASS',len(checks),'Hyper rival portrait checks',flush=True)
