from pathlib import Path
import json,re
P=Path(__file__).resolve().parents[2]
def block(file,tag,text):
 f=P/file;s=f.read_text();start='// BEGIN '+tag;end='// END '+tag;s=re.sub(re.escape(start)+r'.*?'+re.escape(end)+r'\n?', '',s,flags=re.S);s=s.rstrip()+'\n\n'+start+'\n'+text.rstrip()+'\n'+end+'\n';f.write_text(s)
graphics=[];metas=[];headers=[]
for name,path,sec in [('UnovaGeneral_Primary','data/tilesets/primary/unova_general',False),('UnovaNuvema_Secondary','data/tilesets/secondary/unova_nuvema',True)]:
 graphics.append(f'const u32 gTilesetTiles_{name}[] = INCBIN_U32("{path}/tiles.4bpp.lz");\nconst u16 gTilesetPalettes_{name}[][16] = {{\n'+''.join(f'    INCBIN_U16("{path}/palettes/{i:02}.gbapal"),\n' for i in range(16))+'};')
 metas.append(f'const u16 gMetatiles_{name}[] = INCBIN_U16("{path}/metatiles.bin");\nconst u16 gMetatileAttributes_{name}[] = INCBIN_U16("{path}/metatile_attributes.bin");')
 headers.append(f'const struct Tileset gTileset_{name} =\n{{\n    .isCompressed = TRUE,\n    .isSecondary = {"TRUE" if sec else "FALSE"},\n    .tiles = gTilesetTiles_{name},\n    .palettes = gTilesetPalettes_{name},\n    .metatiles = gMetatiles_{name},\n    .metatileAttributes = gMetatileAttributes_{name},\n    .callback = {"NULL" if sec else "InitTilesetAnim_UnovaGeneral"},\n}};')
block('src/data/tilesets/graphics.h','WESLEY_UNOVA_GRAPHICS','\n\n'.join(graphics));block('src/data/tilesets/metatiles.h','WESLEY_UNOVA_METATILES','\n\n'.join(metas));block('src/data/tilesets/headers.h','WESLEY_UNOVA_HEADERS','\n\n'.join(headers))
f=P/'include/tileset_anims.h';s=f.read_text();decl='void InitTilesetAnim_UnovaGeneral(void);\n'
if decl not in s:s=s.replace('#endif // GUARD_TILESET_ANIMS_H',decl+'\n#endif // GUARD_TILESET_ANIMS_H');f.write_text(s)
f=P/'src/tileset_anims.c';s=f.read_text();inc='#include "unova_tileset_anims.inc"\n'
if inc not in s:f.write_text(s.rstrip()+'\n\n'+inc)
anim='''// WesleyFG ocean texture: four native-pixel phases, isolated from all other tile banks.
'''+''.join(f'static const u16 sUnovaOceanFrame{i}[] = INCBIN_U16("data/tilesets/primary/unova_general/anim/water/{i}.4bpp");\n' for i in range(4))+'''
static const u16 *const sUnovaOceanFrames[] = {
    sUnovaOceanFrame0, sUnovaOceanFrame1, sUnovaOceanFrame2, sUnovaOceanFrame3
};

static void TilesetAnim_UnovaGeneral(u16 timer)
{
    if (timer % 16 == 0)
        AppendTilesetAnimToBuffer(sUnovaOceanFrames[(timer / 16) % 4],
            (u16 *)(BG_VRAM + TILE_OFFSET_4BPP(384)), 16 * TILE_SIZE_4BPP);
}

void InitTilesetAnim_UnovaGeneral(void)
{
    sPrimaryTilesetAnimCounter = 0;
    sPrimaryTilesetAnimCounterMax = 64;
    sPrimaryTilesetAnimCallback = TilesetAnim_UnovaGeneral;
}
''';(P/'src/unova_tileset_anims.inc').write_text(anim)
# Emerald's regular border is only 2x2. Nuvema samples its outer terrain instead,
# so north/west/east stay forest or rocky coast while the south stays ocean.
f=P/'src/fieldmap.c';s=f.read_text();tag='    // Wesley Nuvema: extend each edge\'s own terrain rather than a forest below the sea.\n'
if tag not in s:
 needle='const struct MapLayout *mapLayout = gMapHeader.mapLayout;\n\n    if (mapLayout->isFrlg)'
 replacement='''const struct MapLayout *mapLayout = gMapHeader.mapLayout;

'''+tag+'''    if (gMapHeader.mapLayoutId == LAYOUT_AMAP_3_0_NUVEMA_TOWN_LAYOUT)
    {
        s32 edgeX = x - MAP_OFFSET;
        s32 edgeY = y - MAP_OFFSET;
        if (edgeX < 0) edgeX = 0;
        if (edgeY < 0) edgeY = 0;
        if (edgeX >= mapLayout->width) edgeX = mapLayout->width - 1;
        if (edgeY >= mapLayout->height) edgeY = mapLayout->height - 1;
        return mapLayout->map[edgeX + edgeY * mapLayout->width] | MAPGRID_IMPASSABLE;
    }

    if (mapLayout->isFrlg)'''
 assert needle in s;s=s.replace(needle,replacement,1);f.write_text(s)
# Labels and prefab patterns are exposed without changing Porymap's global defaults.
report=json.loads((P/'docs/la_world/unova_wesley/report.json').read_text());prefabs=json.loads((P/'docs/la_world/unova_wesley/prefabs.json').read_text());paths=json.loads((P/'docs/la_world/unova_wesley/path_autotiles.json').read_text());labels=[]
for name,pattern in prefabs.items():
 for y,row in enumerate(pattern):
  for x,n in enumerate(row):labels.append(f'#define METATILE_UnovaWesley_{name}_{x}_{y} 0x{n:03X}')
for mask,n in paths.items():labels.append(f'#define METATILE_UnovaWesley_Path_{mask} 0x{n:03X}')
block('include/constants/metatile_labels.h','WESLEY_UNOVA_LABELS','\n'.join(labels))
print('Registered both tilesets, ocean callback, labels and regional edge borders.')
