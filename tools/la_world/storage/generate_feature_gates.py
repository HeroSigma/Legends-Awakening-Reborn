"""Regenerate collection-mode legacy activity gates from current registries."""
from pathlib import Path
import json, re
R=Path(__file__).resolve().parents[3]
SPECIAL_PATTERN=r'Contest|TrainerHill|BattleFrontier|BattleTower|BattleTent|BattlePike|BattleDome|BattlePalace|BattleFactory|BattleArena|BattlePyramid|SecretBase|Decoration|BerryBlender|RecordMix|MysteryGift|UnionRoom|LilycoveLady|PokemonJump|BerryCrush|BerryPick|BattleRecords'
# These support ordinary map initialization/identity, not activity entry.
# InitUnionRoom itself checks whether the current map needs wireless setup.
ALLOWED_SETUP_SPECIALS={'InitUnionRoom','SetLilycoveLadyGfx','Script_GetLilycoveLadyId'}
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
    a=updated.index('    switch(id) {');b=updated.index('        return TRUE;',a)
    updated=updated[:a]+'    switch(id) {\n'+''.join('    case %d: // %s\n'%(i,n) for i,n in blocked)+updated[b:]
    if check:
        assert updated==s,'collection feature gates need regeneration'
    else:
        p.write_text(updated)
        (R/'docs/la_world/compact_pc/retired_feature_gates.json').write_text(json.dumps(dict(maps=maps,specials=[dict(index=i,name=n) for i,n in blocked]),indent=2)+'\n')
    return len(maps),len(blocked)
if __name__=='__main__':
    import sys
    print(generate('--check' in sys.argv))
