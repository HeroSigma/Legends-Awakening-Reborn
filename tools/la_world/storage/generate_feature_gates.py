"""Regenerate collection-mode legacy activity gates from current registries."""
from pathlib import Path
import json, re
R=Path(__file__).resolve().parents[3]
SPECIAL_PATTERN=r'Contest|TrainerHill|BattleFrontier|BattleTower|BattleTent|BattlePike|BattleDome|BattlePalace|BattleFactory|BattleArena|BattlePyramid|SecretBase|Decoration|BerryBlender|RecordMix|MysteryGift|UnionRoom|LilycoveLady|PokemonJump|BerryCrush|BerryPick|BattleRecords'
# These support ordinary map initialization/identity, not activity entry.
# InitUnionRoom itself checks whether the current map needs wireless setup.
ALLOWED_SETUP_SPECIALS={'InitUnionRoom','SetLilycoveLadyGfx','Script_GetLilycoveLadyId','PlayerNotAtTrainerHillEntrance','BufferUnionRoomPlayerName'}
MAP_PATTERN=r'BattleFrontier|BattleTent|TrainerHill|SecretBase|Contest|BerryBlender|UnionRoom|RecordCorner'

def generate(check=False):
    names=re.findall(r'^\s*def_special\s+(\w+)',(R/'data/specials.inc').read_text(),re.M)
    blocked=[(i,n) for i,n in enumerate(names) if re.search(SPECIAL_PATTERN,n) and n not in ALLOWED_SETUP_SPECIALS]
    groups=json.loads((R/'data/maps/map_groups.json').read_text());maps=[]
    for group in groups['group_order']:
        for name in groups[group]:
            path=R/'data/maps'/name/'map.json'
            if re.search(MAP_PATTERN,name) and name!='BattleFrontier_Outside' and path.exists():maps.append(json.loads(path.read_text())['id'])
    p=R/'src/la_pc_features.c';s=p.read_text()
    a=s.index('static const u16 sRetiredMaps[] = {');b=s.index('};',a)+2
    updated=s[:a]+'static const u16 sRetiredMaps[] = {\n'+''.join('    '+n+',\n' for n in maps)+'};'+s[b:]
    # Reference linker-defined SPECIAL symbols rather than baking mutable table
    # indices into C. Appending/inserting a special can never retarget a gate.
    a=updated.index('// BEGIN NAMED COLLECTION SPECIAL GATES') if '// BEGIN NAMED COLLECTION SPECIAL GATES' in updated else updated.index('bool32 LaPcBlockedSpecial(u32 id)')
    b=updated.index('bool32 LaPcBlockWarp',a)
    block='// BEGIN NAMED COLLECTION SPECIAL GATES\n'
    block+=''.join('extern const u8 SPECIAL_'+name+'[];\n' for _,name in blocked)
    block+='static const u32 sRetiredSpecials[] = {\n'
    block+=''.join('    (u32)SPECIAL_'+name+',\n' for _,name in blocked)
    block+='};\nbool32 LaPcBlockedSpecial(u32 id)\n{\n    if (!StorageIsCollectionMode()) return FALSE;\n    // Ordinary pickups query their location before closing the item header.\n    if (id == (u32)SPECIAL_CallBattlePyramidFunction\n        && gSpecialVar_0x8004 == BATTLE_PYRAMID_FUNC_CURRENT_LOCATION) return FALSE;\n    for (u32 i=0;i<ARRAY_COUNT(sRetiredSpecials);i++)\n        if (id==sRetiredSpecials[i]) return TRUE;\n    return FALSE;\n}\n// END NAMED COLLECTION SPECIAL GATES\n'
    updated=updated[:a]+block+updated[b:]
    if check:
        assert updated==s,'collection feature gates need regeneration'
    else:
        p.write_text(updated)
        (R/'docs/la_world/compact_pc/retired_feature_gates.json').write_text(json.dumps(dict(maps=maps,specials=[dict(index=i,name=n) for i,n in blocked]),indent=2)+'\n')
    return len(maps),len(blocked)
if __name__=='__main__':
    import sys
    print(generate('--check' in sys.argv))
