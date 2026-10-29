"""Native regression for the regular Emerald protagonists and existing SwSh summary."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
import tempfile,struct
D=R/'docs/features/regular-protagonists';D.mkdir(exist_ok=True)
source=(R/'src/swsh_summary_screen.c').read_text();prefix=source[source.index('#if SWSH_SUMMARY_SCREEN == TRUE'):source.index('} *sMonSummaryScreen = NULL;')+len('} *sMonSummaryScreen = NULL;')].replace('static EWRAM_DATA struct','struct').replace('} *sMonSummaryScreen = NULL;','};')+'\n#endif\n'
names=['offsetof(struct PokemonSummaryScreenData,summary.teraType)','offsetof(struct PokemonSummaryScreenData,summary.mintNature)','offsetof(struct PokemonSummaryScreenData,currPageIndex)','MON_DATA_HIDDEN_NATURE','MON_DATA_TERA_TYPE','TYPE_WATER','TRAINER_PIC_BRENDAN','TRAINER_PIC_MAY','VERSION_EMERALD','OBJ_EVENT_GFX_BRENDAN_NORMAL','OBJ_EVENT_GFX_MAY_NORMAL','offsetof(struct ObjectEventGraphicsInfo,images)','offsetof(struct ObjectEventGraphicsInfo,paletteTag)','SUMMARY_MODE_BOX','OBJ_EVENT_PAL_TAG_AREN','OBJ_EVENT_PAL_TAG_ARIA']
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "pokemon.h"\n#include "main.h"\n#include "pokemon_summary_screen.h"\n#include "swsh_summary_screen.h"\n#include "sprite.h"\n#include "constants/trainers.h"\n#include "constants/event_objects.h"\n#include <stddef.h>\n'+prefix+'const unsigned v[]={'+','.join(names)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 c=dict(zip(names,struct.unpack('<'+str(len(names))+'I',(td/'c.bin').read_bytes())))
for mode in [0,1]:
 start(mode);invoke('StorageChangeMode',mode,1);invoke('ScriptGiveMon',4,16,0)
 check('restored_battle_sprite_'+str(mode),invoke('GetPlayerTrainerPic',mode,c['VERSION_EMERALD'])==c['TRAINER_PIC_MAY' if mode else 'TRAINER_PIC_BRENDAN'])
 info=invoke('GetObjectEventGraphicsInfo',c['OBJ_EVENT_GFX_MAY_NORMAL' if mode else 'OBJ_EVENT_GFX_BRENDAN_NORMAL'])
 check('regular_player_sheet_'+str(mode),rd(info+c['offsetof(struct ObjectEventGraphicsInfo,images)'])==symbols['sPicTable_MayNormal' if mode else 'sPicTable_BrendanNormal'])
 check('regular_player_palette_'+str(mode),rd(info+c['offsetof(struct ObjectEventGraphicsInfo,paletteTag)'],2)==c['OBJ_EVENT_PAL_TAG_ARIA' if mode else 'OBJ_EVENT_PAL_TAG_AREN'])
 shutil.copy2(shot('restored_player_'+str(mode)),D/('player-'+str(mode)+'.png'))
 scratch=0x0203fc00;wr(scratch,10);invoke('SetMonData',symbols['gParties'],c['MON_DATA_HIDDEN_NATURE'],scratch)
 wr(scratch,c['TYPE_WATER']);invoke('SetMonData',symbols['gParties'],c['MON_DATA_TERA_TYPE'],scratch)
 invoke('ShowPokemonSummaryScreen',0,symbols['gParties'],0,0,symbols['CB2_ReturnToField']|1)
 wr(symbols['gMain']+4,symbols['CB2_InitSummaryScreen']|1);frames(240)
 ptr=rd(symbols['sMonSummaryScreen'])
 check('swsh_tera_'+str(mode),rd(ptr+c['offsetof(struct PokemonSummaryScreenData,summary.teraType)'],1)==c['TYPE_WATER'])
 check('swsh_mint_'+str(mode),rd(ptr+c['offsetof(struct PokemonSummaryScreenData,summary.mintNature)'],1)==10)
 shutil.copy2(shot('swsh_info_'+str(mode)),D/('summary-info-'+str(mode)+'.png'))
 for i in range(5):tap(16);frames(120)
 check('summary_stays_open_'+str(mode),rd(symbols['sMonSummaryScreen'])==ptr)
 tap(2);frames(240)
 check('summary_returns_'+str(mode),rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1)
 check('tera_unchanged_'+str(mode),invoke('GetMonData3',symbols['gParties'],c['MON_DATA_TERA_TYPE'],0)==c['TYPE_WATER'])
 # Exercise the final box in each storage mode through the summary's box adapter.
 box=59 if mode else 13
 invoke('StorageWriteMon',box,29,symbols['gParties'])
 boxed=invoke('GetBoxedMonPtr',box,29)
 invoke('ShowPokemonSummaryScreen',c['SUMMARY_MODE_BOX'],boxed,0,0,symbols['CB2_ReturnToField']|1)
 wr(symbols['gMain']+4,symbols['CB2_InitSummaryScreen']|1);frames(240)
 ptr=rd(symbols['sMonSummaryScreen'])
 check('boxed_summary_tera_'+str(mode),rd(ptr+c['offsetof(struct PokemonSummaryScreenData,summary.teraType)'],1)==c['TYPE_WATER'])
 check('boxed_summary_mint_'+str(mode),rd(ptr+c['offsetof(struct PokemonSummaryScreenData,summary.mintNature)'],1)==10)
 tap(2);frames(240)
 check('boxed_summary_returns_'+str(mode),rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1)
 check('boxed_mon_preserved_'+str(mode),invoke('GetBoxMonDataAt',box,29,c['MON_DATA_TERA_TYPE'])==c['TYPE_WATER'])
 lib.shutdown()
(D/'validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'upgrade checks')
