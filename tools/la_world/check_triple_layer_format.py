from pathlib import Path
import re
P=Path(__file__).resolve().parents[2]
if '#define NUM_TILES_PER_METATILE 12' not in (P/'include/fieldmap.h').read_text():raise SystemExit('Triple layer format check: engine must use 12 entries.')
paths=dict(re.findall(r'const u(?:16|32)\s+(\w+)\[\]\s*=\s*INCBIN_U(?:16|32)\("([^"]+)"\)',(P/'src/data/tilesets/metatiles.h').read_text()));checked=set()
for name,body in re.findall(r'const struct Tileset\s+(\w+)\s*=\s*\{(.*?)\};',(P/'src/data/tilesets/headers.h').read_text(),re.S):
 m=re.search(r'\.metatiles\s*=\s*(\w+)',body);a=re.search(r'\.metatileAttributes\s*=\s*(\w+)',body)
 if not m or not a:continue
 rel=paths[m[1]]
 if rel in checked:continue
 size=(P/rel).stat().st_size;asize=(P/paths[a[1]]).stat().st_size
 if not asize or size%24 or size not in (asize*6,asize*12):raise SystemExit(f'{rel}: expected 12-entry metatiles. An older importer may have written two-layer data; convert that tileset before building.')
 checked.add(rel)
print('Triple layer format:',len(checked),'registered tileset files valid.')
