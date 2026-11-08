"""Isolated linked-ROM tests for the DexNav equipment bonus."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0], 'pc_helpers', 'exec'))
D=R/'.la_work/qol_features/dexnav-test';D.mkdir(parents=True,exist_ok=True)
start(0)
for chain,expected in [(0,0),(9,0),(10,10),(24,10),(25,20),(49,20),(50,35),(99,35),(100,50),(255,50),(9999,50)]:
 check('chance_'+str(chain),invoke('LegendsDexNavEquipmentChance',chain)==expected)
# Read native item enum values with the project's compiler instead of duplicating IDs.
import tempfile,struct
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "constants/items.h"\n#include "constants/species.h"\nconst unsigned values[]={ITEM_CHARIZARDITE_X,ITEM_CHARIZARDITE_Y,ITEM_FIRIUM_Z,ITEM_NORMALIUM_Z,NUM_SPECIES};\n')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 x,y,fire,electric,num=struct.unpack('<5I',(td/'c.bin').read_bytes())
for species,chain,caught in [(4,100,0),(4,9,1),(0,100,1),(num,100,1)]:
 check('ineligible_'+str((species,chain,caught)),invoke('LegendsChooseDexNavEquipment',species,chain,caught)==0)
for species,allowed in [(4,{0,x,y,fire}),(161,{0,electric})]:
 rolls=[invoke('LegendsChooseDexNavEquipment',species,100,1) for _ in range(500)]
 print("ROLLS",species,set(rolls),allowed,flush=True)
 check('species_appropriate_'+str(species),set(rolls)<=allowed)
 check('eligible_equipment_present_'+str(species),180<sum(bool(v) for v in rolls)<320)
 check('all_family_options_'+str(species),allowed<=set(rolls))
lib.shutdown()
(R/'docs/features/dexnav-equipment-chaining-validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'DexNav equipment checks')
