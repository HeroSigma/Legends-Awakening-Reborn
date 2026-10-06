#!/usr/bin/env python3
"""Add Porymap parser support to inactive donor editor projects only."""
import json,shutil
from pathlib import Path

def prepare(repo,editor):
    editor=editor.resolve();allowed=(repo/'.la_work/amap').resolve()
    assert editor.is_relative_to(allowed) and editor.name=='editor'
    for rel in ['include/fieldmap.h','include/global.fieldmap.h','include/global.h']:
        p=editor/rel;p.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(repo/rel,p)
    def emit(rel,obj):
        p=editor/rel;p.parent.mkdir(parents=True,exist_ok=True)
        if not p.exists():p.write_text(json.dumps(obj,indent=2)+'\n')
    emit('src/data/region_map/region_map_sections.json',{'map_sections':[{'id':'MAPSEC_NONE','name':'DONOR ASSET PREVIEW','x':0,'y':0,'width':1,'height':1}]})
    emit('src/data/heal_locations.json',{'heal_locations':[]})
    emit('src/data/wild_encounters.json',{'wild_encounter_groups':[]})
    for rel in ['data/event_scripts.s','src/pokemon_icon.c','src/event_object_movement.c','src/wild_encounter.c','src/data/graphics/pokemon.h','src/data/object_events/object_event_graphics_info_pointers.h','src/data/object_events/object_event_graphics_info.h','src/data/object_events/object_event_pic_tables.h','src/data/object_events/object_event_graphics.h']:
        p=editor/rel;p.parent.mkdir(parents=True,exist_ok=True)
        if not p.exists():p.write_text('// Empty editor reference: no gameplay implementation.\n' if rel.endswith(('.c','.h')) else '@ No gameplay scripts.\n')
    # Porymap supports INCBIN universally; graphics paths resolve to editable PNG/PAL.
    p=editor/'src/data/tilesets/graphics.h'
    s=p.read_text();import re
    s=re.sub(r'INCGFX_U32\("([^"]+)/tiles.png", ".4bpp"\)',r'INCBIN_U32("\1/tiles.4bpp")',s)
    s=re.sub(r'INCGFX_U16\("([^"]+)\.pal", ".gbapal"\)',r'INCBIN_U16("\1.gbapal")',s);p.write_text(s)
    for rel in ['src/data/region_map/region_map_sections.json','src/data/heal_locations.json','include/fieldmap.h','include/global.fieldmap.h']:
        assert (editor/rel).exists()
    print('Prepared',editor)
if __name__=='__main__':
    repo=Path(__file__).resolve().parents[4]
    for editor in [repo/'.la_work/amap/bwa_selected_assets/editor',repo/'.la_work/amap/donor_preservation/bwa/editor',repo/'.la_work/amap/donor_preservation/swsh/editor']:
        if editor.exists():prepare(repo,editor)
