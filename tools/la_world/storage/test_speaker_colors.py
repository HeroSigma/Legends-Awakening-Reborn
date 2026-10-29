"""Character color defaults, explicit overrides and neutral messages in a native field window."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
import tempfile,struct
factions={'GIOVANNI':(22,3,6),'TEAM_ROCKET':(22,3,6),'AQUA_GRUNT':(3,8,23),'TEAM_AQUA':(3,8,23),'TEAM_MAGMA':(23,8,2),'CYRUS':(15,5,23),'TEAM_GALACTIC':(15,5,23),'SHADOW_TRIAD':(6,12,17),'TEAM_PLASMA':(6,12,17),'TEAM_FLARE':(26,5,2),'TEAM_SKULL':(5,5,7),'TEAM_YELL':(23,3,14),'TEAM_STAR':(17,10,2),'AETHER_FOUNDATION':(2,15,13)}
names=['SP_NAME_PLAYER','SP_NAME_WALLY','SP_NAME_BRENDAN','SP_NAME_MAY','SP_NAME_RED','SP_NAME_BRINEY','SP_NAME_AQUA_GRUNT','SP_NAME_BIRCH','SP_NAME_NONE','TEXT_COLOR_LIGHT_BLUE','TEXT_COLOR_LIGHT_GREEN','TEXT_COLOR_GREEN','TEXT_COLOR_RED','TEXT_COLOR_BLUE','EXT_CTRL_CODE_BEGIN','EXT_CTRL_CODE_COLOR']
names += ['SP_NAME_'+s for s in factions] + ['TEXT_DYNAMIC_COLOR_1','WINDOW_PALETTE_NUM']
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "constants/speaker_names.h"\n#include "constants/characters.h"\n#include "window.h"\nconst unsigned v[]={'+','.join(names)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 c=dict(zip(names,struct.unpack('<'+str(len(names))+'I',(td/'c.bin').read_bytes())))
start(0)
proof=R/'docs/story/spoken_protagonist'
for speaker,color in [('PLAYER','LIGHT_BLUE'),('WALLY','LIGHT_GREEN'),('BRENDAN','GREEN'),('MAY','RED'),('RED','RED'),('BRINEY','BLUE')]:
 pointer=rd(symbols['gSpeakerNamesTable']+c['SP_NAME_'+speaker]*4)
 wr(symbols['gSpeakerName'],pointer)
 label='LegendsPetalburg_Text_Reassure' if speaker=='WALLY' else 'LegendsVoice_WoodsQuestion'
 check('opens_'+speaker,invoke('ShowFieldMessage',symbols[label])==1)
 expected=[c['EXT_CTRL_CODE_BEGIN'],c['EXT_CTRL_CODE_COLOR'],c['TEXT_COLOR_'+color]]
 check('color_'+speaker,[rd(symbols['gStringVar4']+i,1) for i in range(3)]==expected)
 frames(600)
 if speaker=='WALLY':shutil.copy2(shot('wally_light_green'),proof/'wally_light_green.png')
 invoke('HideFieldMessageBox');frames(5)
# Exercise the live palette after frame initialization, including back-to-back factions.
for speaker,rgb in factions.items():
 wr(symbols['gSpeakerName'],rd(symbols['gSpeakerNamesTable']+c['SP_NAME_'+speaker]*4))
 check('opens_'+speaker,invoke('ShowFieldMessage',symbols['LegendsVoice_WoodsQuestion'])==1)
 check('faction_index_'+speaker,rd(symbols['gStringVar4']+2,1)==c['TEXT_DYNAMIC_COLOR_1'])
 frames(120)
 palette=invoke('GetWindowAttribute',0,c['WINDOW_PALETTE_NUM'])
 expected=rgb[0]|rgb[1]<<5|rgb[2]<<10
 check('faction_palette_'+speaker,rd(symbols['gPlttBufferUnfaded']+(palette*16+c['TEXT_DYNAMIC_COLOR_1'])*2,2)==expected)
 if speaker in ['GIOVANNI','CYRUS','SHADOW_TRIAD','AQUA_GRUNT']:
  shutil.copy2(shot('faction_'+speaker.lower()),proof/('faction_'+speaker.lower()+'.png'))
 invoke('HideFieldMessageBox');frames(5)
# An already authored color control must not be duplicated or replaced.
wr(symbols['gSpeakerName'],rd(symbols['gSpeakerNamesTable']+c['SP_NAME_WALLY']*4))
raw=bytes([c['EXT_CTRL_CODE_BEGIN'],c['EXT_CTRL_CODE_COLOR'],c['TEXT_COLOR_RED'],0xbb,255])
for i,v in enumerate(raw):wr(0x0203fc00+i,v,1)
invoke('ShowFieldMessage',0x0203fc00)
check('explicit_color_preserved',bytes(rd(symbols['gStringVar4']+i,1) for i in range(len(raw)))==raw)
frames(30);invoke('HideFieldMessageBox')
for speaker in ['NONE','BIRCH']:
 wr(symbols['gSpeakerName'],rd(symbols['gSpeakerNamesTable']+c['SP_NAME_'+speaker]*4))
 label=symbols['LegendsVoice_WoodsQuestion'];invoke('ShowFieldMessage',label)
 check('neutral_'+speaker,bytes(rd(symbols['gStringVar4']+i,1) for i in range(12))==bytes(rd(label+i,1) for i in range(12)))
 frames(30);invoke('HideFieldMessageBox')
lib.shutdown()
(proof/'colors-validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'speaker color checks')
