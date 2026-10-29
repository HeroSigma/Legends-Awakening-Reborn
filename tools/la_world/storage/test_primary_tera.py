"""Primary defaults, debug PC species reuse, scientist overrides and native summary badges."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
import tempfile,struct
source=(R/'src/pokemon_summary_screen.c').read_text()
enums=source[source.index('enum\n{\n    SPRITE_ARR_ID_MON'):source.index('static EWRAM_DATA struct PokemonSummaryScreenData')]
decl=source[source.index('static EWRAM_DATA struct PokemonSummaryScreenData'):source.index('EWRAM_DATA u8 gLastViewedMonIndex')].replace('static EWRAM_DATA struct','struct').replace('} *sMonSummaryScreen = NULL;','};')
names=['sizeof(struct SpeciesInfo)','offsetof(struct SpeciesInfo,forceTeraType)','MON_DATA_TERA_TYPE','MON_DATA_SPECIES','MON_DATA_IS_EGG','SPECIES_CHARMANDER','SPECIES_WOOPER','SPECIES_MAGNEMITE','TYPE_FIRE','TYPE_WATER','TYPE_ELECTRIC','TYPE_GRASS','TYPE_NONE','TYPE_STELLAR','ITEM_GRASS_TERA_SHARD','FLAG_RETURNED_DEVON_GOODS','FLAG_RECEIVED_POKENAV','FLAG_LA_TERA_RESEARCH_INTRO','IN_BOX_COUNT','offsetof(struct PokemonSummaryScreenData,summary.teraType)','offsetof(struct PokemonSummaryScreenData,spriteIds)','sizeof(struct Sprite)','offsetof(struct Sprite,animNum)','SPRITE_ARR_ID_TYPE']
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "pokemon.h"\n#include "pokemon_summary_screen.h"\n#include "sprite.h"\n#include "pokemon_storage_system.h"\n#include <stddef.h>\n#define TYPE_ICON_SPRITE_COUNT (MAX_MON_MOVES + 1)\n#define MOVE_SELECTOR_SPRITES_COUNT 10\n'+enums+decl+'const unsigned v[]={'+','.join(names)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 c=dict(zip(names,struct.unpack('<'+str(len(names))+'I',(td/'c.bin').read_bytes())))
party=symbols['gParties'];scratch=0x0203fc00
for mode in [0,1]:
 start(0);invoke('StorageChangeMode',mode,1)
 for species,type_name in [('CHARMANDER','FIRE'),('WOOPER','WATER'),('MAGNEMITE','ELECTRIC')]:
  for pid in [2,3]:
   invoke('CreateMon',party,c['SPECIES_'+species],5,pid,0,0)
   check('primary_'+str((mode,species,pid)),invoke('GetMonData3',party,c['MON_DATA_TERA_TYPE'],0)==c['TYPE_'+type_name])
   wr(scratch,c['TYPE_NONE']);invoke('SetMonData',party,c['MON_DATA_TERA_TYPE'],scratch)
   check('unassigned_primary_'+str((mode,species,pid)),invoke('GetMonData3',party,c['MON_DATA_TERA_TYPE'],0)==c['TYPE_'+type_name])
 invoke('CreateMon',party,c['SPECIES_CHARMANDER'],5,2,0,0);wr(symbols['gPartiesCount'],1,1)
 for flag in ['FLAG_RETURNED_DEVON_GOODS','FLAG_RECEIVED_POKENAV','FLAG_LA_TERA_RESEARCH_INTRO']:invoke('FlagSet',c[flag])
 invoke('AddBagItem',c['ITEM_GRASS_TERA_SHARD'],50)
 wr(symbols['gSpecialVar_0x8004'],0,2);wr(symbols['gSpecialVar_0x8005'],3,2)
 invoke('LegendsCommitTeraChange')
 check('scientist_grass_'+str(mode),invoke('GetMonData3',party,c['MON_DATA_TERA_TYPE'],0)==c['TYPE_GRASS'])
 check('shards_consumed_'+str(mode),invoke('CountTotalItemQuantityInBag',c['ITEM_GRASS_TERA_SHARD'])==0)
 invoke('ShowPokemonSummaryScreen',0,party,0,0,symbols['CB2_ReturnToField']|1)
 wr(symbols['gMain']+4,symbols['CB2_InitSummaryScreen']|1);frames(180)
 summary=rd(symbols['sMonSummaryScreen'])
 check('summary_type_'+str(mode),rd(summary+c['offsetof(struct PokemonSummaryScreenData,summary.teraType)'],1)==c['TYPE_GRASS'])
 sprite_id=rd(summary+c['offsetof(struct PokemonSummaryScreenData,spriteIds)']+c['SPRITE_ARR_ID_TYPE']+2,1)
 sprite=symbols['gSprites']+sprite_id*c['sizeof(struct Sprite)']
 check('summary_badge_'+str(mode),rd(sprite+c['offsetof(struct Sprite,animNum)'],1)==c['TYPE_GRASS'])
 if mode==0:shutil.copy2(shot('tera_summary'),R/'docs/features/tera-summary.png')
 tap(2);frames(180)
 invoke('Debug_FillPCBoxes',0)
 for box in range(invoke('GetStorageBoxCount')):
  for slot in range(c['IN_BOX_COUNT']):
   species=invoke('GetBoxMonDataAt',box,slot,c['MON_DATA_SPECIES'])
   if not species:continue
   forced=rd(symbols['gSpeciesInfo']+species*c['sizeof(struct SpeciesInfo)']+c['offsetof(struct SpeciesInfo,forceTeraType)'],1)
   check('filled_primary_'+str((mode,box,slot)),invoke('GetBoxMonDataAt',box,slot,c['MON_DATA_TERA_TYPE'])==(forced or invoke('GetSpeciesType',species,0)))
 check('save_'+str(mode),invoke('TrySavingData',0)==1)
 check('reload_'+str(mode),invoke('LoadGameSave',0)==1)
 check('scientist_choice_survives_'+str(mode),invoke('GetMonData3',party,c['MON_DATA_TERA_TYPE'],0)==c['TYPE_GRASS'])
 lib.shutdown()
(R/'docs/features/primary-tera-validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'primary Tera and summary checks')
