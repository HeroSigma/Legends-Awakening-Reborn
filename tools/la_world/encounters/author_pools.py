#!/usr/bin/env python3
"""Reproducible encounter authoring from the current Emerald build configuration."""
import argparse, collections, csv, hashlib, json, re, struct, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'docs/la_world/wild_pools'
SPECIAL = ('isRestrictedLegendary', 'isSubLegendary', 'isMythical', 'isUltraBeast', 'isParadox')
TEMPORARY = ('isTotem', 'isMegaEvolution', 'isPrimalReversion', 'isUltraBurst', 'isGigantamax', 'isTeraForm')
def blocks(text, pattern):
    for m in re.finditer(pattern, text):
        start = m.end()-1
        # Remove quoted text before counting braces (descriptions contain punctuation).
        tail = text[start:]
        depth = 0
        for t in re.finditer(r'"(?:\\.|[^"\\])*"|[{}]', tail):
            if t.group() == '{': depth += 1
            elif t.group() == '}':
                depth -= 1
                if not depth:
                    yield m.group(1), tail[:t.end()]
                    break
ALL_SPECIES={}
def catalog():
    text = subprocess.check_output(['arm-none-eabi-cpp', '-iquote', 'include',
        '-Wno-trigraphs', '-DMODERN=1', '-DTESTING=0', '-DEMERALD', '-std=gnu17',
        'src/pokemon.c'], cwd=ROOT, text=True)
    entries={};dex_names={}
    for name,body in blocks(text,r'\[(SPECIES_\w+)\]\s*=\s*\{'):
        dex=re.search(r'\.natDexNum\s*=\s*NATIONAL_DEX_(\w+)',body)
        if not dex or dex[1]=='NONE':continue
        flags=[f for f in SPECIAL+TEMPORARY if re.search(r'\.'+f+r'\s*=\s*1\b',body)]
        types=re.search(r'\.types\s*=\s*\{([^}]+)',body)
        evo=re.findall(r'\{\s*EVO_LEVEL\s*,\s*(\d+)\s*,\s*(SPECIES_\w+)',body)
        targets=re.findall(r'\{\s*EVO_(\w+)\s*,\s*([^,{}]+)\s*,\s*(SPECIES_\w+)',body)
        value=dict(species=name,types=re.findall(r'TYPE_(\w+)',types[1]) if types else [],
            excluded=bool(flags) and name!='SPECIES_POIPOLE',exclusion_flags=flags,
            evolution_targets=[dict(method=m,param=p.strip(),species=t) for m,p,t in targets],
            level_evolutions=[dict(level=int(l),species=t) for l,t in evo])
        ALL_SPECIES[name]=value
        # The wild source catalog uses one ordinary representative per Dex entry.
        # All ordinary forms remain available as ancestry for regional evolutions.
        if dex[1] in dex_names:
            if name!='SPECIES_'+dex[1]:continue
            del entries[dex_names[dex[1]]]
        dex_names[dex[1]]=name;entries[name]=value
    assert len(entries)==1025,len(entries)
    assert entries['SPECIES_NAGANADEL']['excluded']
    assert not entries['SPECIES_POIPOLE']['excluded']
    assert entries['SPECIES_MEW']['excluded'] and entries['SPECIES_IRON_VALIANT']['excluded']
    lineage={}
    for n,x in ALL_SPECIES.items():
        for e in x['evolution_targets']:
            lineage[e['species']]=n
    for n,x in ALL_SPECIES.items():
        root=n;seen=set()
        while root in lineage and root not in seen:
            seen.add(root);root=lineage[root]
        x['family_root_types']=ALL_SPECIES.get(root,x)['types']
    return entries
def terrain_sources():
    # Resolve the exact attributes referenced by the editable layout, including donor banks.
    text = '\n'.join(p.read_text() for p in (ROOT/'src/data/tilesets').glob('*.h'))
    bins = dict(re.findall(r'const u(?:16|32)\s+(\w+)\[\]\s*=\s*INCBIN_U(?:16|32)\("([^"]+)"\)',text))
    tiles = {}
    for name,body in blocks(text,r'const struct Tileset\s+(\w+)\s*=\s*\{'):
        m = re.search(r'\.metatileAttributes\s*=\s*(\w+)',body)
        if m and m[1] in bins:
            raw=(ROOT/bins[m[1]]).read_bytes()
            tiles[name]=list(struct.unpack('<'+'H'*(len(raw)//2),raw))
    behavior_text=(ROOT/'include/constants/metatile_behaviors.h').read_text()
    names=re.findall(r'\b(MB_\w+)\s*,',behavior_text)
    ids={n:i for i,n in enumerate(names)}
    behavior=(ROOT/'src/metatile_behavior.c').read_text()
    land=set(); water=set()
    for n,v in re.findall(r'\[(MB_\w+)\]\s*=\s*([^,\n]+)',behavior):
        if n not in ids: continue
        if 'TILE_FLAG_SURFABLE' in v:water.add(ids[n])
        elif 'TILE_FLAG_HAS_ENCOUNTERS' in v:land.add(ids[n])
    return tiles,land,water
def inventory():
    rules=json.loads(Path(__file__).with_name('area_rules.json').read_text())
    water_towns={re.sub('[^A-Z0-9]','',x.upper()) for x in rules['water_only_settlements']}
    groups=json.loads((ROOT/'data/maps/map_groups.json').read_text())
    layouts={x['id']:x for x in json.loads((ROOT/'data/layouts/layouts.json').read_text())['layouts']}
    baseline=json.loads(Path(__file__).with_name('baseline_wild_encounters.json').read_text())
    previous={}
    for e in baseline['wild_encounter_groups'][0]['encounters']:
        key=re.sub('[^A-Z0-9]','',e['map'].removeprefix('MAP_'))
        previous.setdefault(key,set()).update(k for k in e if k.endswith('_mons'))
    hns={x['name']:x for x in json.loads((ROOT/'docs/la_world/hns_regions/manifest.json').read_text())['maps']}
    tiles,land,water=terrain_sources()
    rows=[]
    for gi,g in enumerate(groups['group_order']):
        for mi,name in enumerate(groups[g]):
            p=ROOT/'data/maps'/name/'map.json'
            if not p.exists():continue
            m=json.loads(p.read_text()); region=m.get('region','')
            active=False
            if gi <= 34 or 75 <= gi <= 80:active=region=='REGION_HOENN'
            elif 98<=gi<=108:active=True
            elif name in hns:active=not hns[name]['reference_only']
            if not active:continue
            if name in hns:region=hns[name]['source_region']
            if 104<=gi<=108:region='REGION_UNOVA'
            if 98<=gi<=103:region='REGION_SINNOH'
            layout=layouts[m['layout']]
            counts=collections.Counter();error=''
            try:
                attrs=tiles[layout['primary_tileset']]+[0]*max(0,512-len(tiles[layout['primary_tileset']]))
                attrs=attrs[:512]+tiles[layout['secondary_tileset']]
                raw=(ROOT/layout['blockdata_filepath']).read_bytes()
                for (cell,) in struct.iter_unpack('<H',raw):
                    idx=cell&1023
                    if idx>=len(attrs):continue
                    b=attrs[idx]&255
                    if b in land:counts['land']+=1
                    if b in water:counts['water']+=1
            except (KeyError,FileNotFoundError) as e:error=str(e)
            source_name=hns[name]['source'].removesuffix('_hns') if name in hns else name
            old_key=re.sub('[^A-Z0-9]','',source_name.upper())
            original_methods=sorted(previous.get(old_key,set()))
            settlement_key=old_key.removeprefix('SINNOH').removeprefix('HNS')
            if settlement_key in water_towns:original_methods=['water_mons','fishing_mons']
            map_type=m.get('map_type')
            allowed=map_type in ('MAP_TYPE_ROUTE','MAP_TYPE_UNDERGROUND','MAP_TYPE_UNDERWATER','MAP_TYPE_OCEAN_ROUTE')
            urban=map_type in ('MAP_TYPE_CITY','MAP_TYPE_TOWN') or bool(re.search(r'(City|Town)(?:_|$)',source_name))
            indoor=map_type=='MAP_TYPE_INDOOR'
            wild_name=bool(re.search(r'cave|woods|forest|ruins|temple|tower|safari|park|lake|marsh|mount|pyre|summit|den|pillar|mine|chamber',name,re.I))
            if urban:allowed=bool(original_methods)
            if indoor:allowed=bool(original_methods) or (wild_name and not urban)
            if re.search(r'gym|mart|shop|harbor|portinside|lighthouse|house|center|hotel|museum|rocket|galactic|hq|sstidal|ssaqua',name,re.I):
                allowed=bool(original_methods)
            if gi<=34:allowed=bool(original_methods)
            if name in rules['wild_areas']:
                allowed=True;urban=False;indoor=False
            if name in rules['no_encounters']:allowed=False
            excluded=bool(re.search('BattleFrontier|BattlePike|BattlePyramid|SecretBase|SafariZone_RestHouse|BirthIsland|NavelRock|FarawayIsland|SouthernIsland|HallOfOrigin|Distortion|Outer_Space|Test|Unused',name,re.I))
            # HnSTest is a validated canonical map prefix, not a debug-map designation.
            if name.startswith('HnSTest_'):excluded=False
            rows.append(dict(map=m['id'],name=name,group=gi,map_num=mi,region=region,
                map_type=m['map_type'],land_cells=counts['land'],water_cells=counts['water'],
                eligible=allowed and not excluded and region is not None and (
                    (counts['land'] and (not urban or 'land_mons' in original_methods)) or
                    (counts['water'] and (not urban or 'water_mons' in original_methods or 'fishing_mons' in original_methods))),terrain_error=error,
                layout=m['layout'],original_methods=original_methods,urban=urban,indoor=indoor,
                decision='intended wild area' if allowed else 'safe town/building or unconfirmed wild area'))
    return rows

def biome(row):
    n=row['name'].lower()
    for b,terms in [
        ('snow',('snow','acuity','217','216','shoal','icepath','ice_path','seafom','seafoam')),
        ('volcanic',('fiery','chimney','jagged','magma','stark','ember','scorched')),
        ('desert',('desert','miragetower','route111')),
        ('haunted',('pyre','cemetery','losttower','oldchateau','sprouttower','burnedtower')),
        ('forest',('forest','woods','park','pinwheel','ilex')),
        ('mountain',('coronet','silver','victory','meteor','mountain','rocktunnel')),
        ('cave',('cave','tunnel','den','ruins','chamber','underground')),
        ('marsh',('marsh','safari','route119','route212')),
        ('coast',('sea','ocean','island','beach','cianwood','pacifidlog'))]:
        if any(t in n for t in terms):return b
    if row['map_type']=='MAP_TYPE_UNDERWATER' or row['water_cells']>max(1,row['land_cells'])*3:return 'coast'
    return 'meadow'
HABITAT_TYPES={
 'snow':('ICE','WATER','NORMAL','ROCK'),
 'volcanic':('FIRE','ROCK','GROUND','STEEL'),
 'desert':('GROUND','ROCK','FIRE','BUG'),
 'haunted':('GHOST','DARK','PSYCHIC','POISON'),
 'forest':('GRASS','BUG','FAIRY','FLYING','NORMAL'),
 'mountain':('ROCK','GROUND','STEEL','DRAGON','FIGHTING'),
 'cave':('ROCK','GROUND','POISON','DARK','STEEL','FIGHTING'),
 'marsh':('WATER','GRASS','BUG','POISON','GROUND'),
 'coast':('WATER','FLYING','ROCK','NORMAL'),
 'meadow':('NORMAL','FLYING','GRASS','BUG','ELECTRIC','FAIRY','FIGHTING','PSYCHIC')}
def score(species,row,method,time):
    types=species['types']; habitat=row['biome']
    night_types=species.get('family_root_types',types)
    if species['species']=='SPECIES_POIPOLE' and (habitat not in ('forest','haunted') or time!='Night'):return None
    aquatic='WATER' in types
    if method in ('water_mons','fishing_mons'):
        if not aquatic:return None
        value=5
    else:
        if aquatic and not any(t in types for t in ('GRASS','GROUND','BUG','FLYING','FIGHTING','POISON','ICE')):return None
        value=sum(t in HABITAT_TYPES[habitat] for t in types)
        if time=='Night' and any(t in night_types for t in ('DARK','GHOST')):value+=3
        if not value:return None
    if time=='Night':
        value+=2*any(t in night_types for t in ('DARK','GHOST','PSYCHIC','POISON'))
    elif time=='Morning':
        value+=2*any(t in types for t in ('FLYING','BUG','GRASS','FAIRY'))
    elif time=='Day':
        value+=any(t in types for t in ('FIRE','NORMAL','FIGHTING','ELECTRIC'))
    return value
def digest(*parts):
    return int(hashlib.sha256('|'.join(map(str,parts)).encode()).hexdigest(),16)
def author(species,maps):
    path=ROOT/'src/data/wild_encounters.json'
    backup=Path(__file__).with_name('baseline_wild_encounters.json')
    data=json.loads(backup.read_text())
    group=next(x for x in data['wild_encounter_groups'] if x['label']=='gWildMonHeaders')
    old=collections.defaultdict(dict)
    for e in group['encounters']:
        for method in ('land_mons','water_mons','rock_smash_mons','fishing_mons'):
            if method in e:old[e['map']][method]=e[method]
    rows=[dict(x,biome=biome(x)) for x in maps if x['eligible'] and x['region'] is not None]
    eligible={n:x for n,x in species.items() if not x['excluded']}
    counts=collections.Counter()
    records=[];entries=[]
    for row in rows:
        for time in ('Morning','Day','Evening','Night'):
            entry=dict(map=row['map'],base_label='gLA_'+row['name']+'_'+time)
            methods=[]
            if row['land_cells'] and (not row['urban'] or 'land_mons' in row['original_methods']):methods.append(('land_mons',12,20))
            if row['water_cells'] and (not row['urban'] or 'water_mons' in row['original_methods'] or 'fishing_mons' in row['original_methods']):methods.extend([('water_mons',5,4),('fishing_mons',10,25)])
            if 'rock_smash_mons' in old[row['map']]:methods.append(('rock_smash_mons',5,20))
            for method,size,rate in methods:
                choices=[(n,score(x,row,method,time)) for n,x in eligible.items()]
                choices=[(n,v) for n,v in choices if v is not None]
                assert choices,(row['name'],method)
                # Stable ecological ranking; least-used eligible species fill rare slots
                # so every permitted National Dex species has a documented home.
                local=sorted([x for x in choices if x[0]!='SPECIES_POIPOLE'],key=lambda nv:(-nv[1],digest(row['map'],time,method,nv[0])))
                mons=[]
                existing=old[row['map']].get(method,{}).get('mons',[])
                for slot in range(size):
                    native=existing[slot%len(existing)] if existing else None
                    if slot<min(3,size) and native and native['species'] in eligible and (time!='Night' or any(t in eligible[native['species']]['types'] for t in ('DARK','GHOST'))):
                        n=native['species']
                    elif time=='Night' and slot<min(4,size):
                        n=local[slot%len(local)][0]
                    elif slot>=size-3:
                        n=min(choices,key=lambda nv:(counts[nv[0]],-nv[1],digest(row['map'],time,slot,nv[0])))[0]
                    else:
                        n=local[(digest(row['map'],time,method,slot)%min(45,len(local)))][0]
                    counts[n]+=1
                    base=existing[slot%len(existing)] if existing else {}
                    if not base and method=='fishing_mons':
                        base=dict(min_level=5 if slot<2 else 10 if slot<5 else 20,
                                  max_level=8 if slot<2 else 15 if slot<5 else 25)
                    lo=base.get('min_level',8 if row['biome']=='meadow' else 15)
                    hi=base.get('max_level',lo+3)
                    if row['name']=='Route101':lo,hi=2,3
                    mons.append(dict(min_level=lo,max_level=max(lo,hi),species=n))
                    records.append(dict(map=row['map'],name=row['name'],region=row['region'],biome=row['biome'],
                        time=time,method=method,slot=slot,species=n,min_level=lo,max_level=max(lo,hi)))
                entry[method]=dict(encounter_rate=old[row['map']].get(method,{}).get('encounter_rate',rate),mons=mons)
            entries.append(entry)
    missing=sorted(set(eligible)-set(counts))
    # A missing habitat must be fixed explicitly, never silently put a fish in grass.
    assert not missing, 'Unplaced species: '+','.join(missing)
    group['encounters']=entries
    path.write_text(json.dumps(data,indent=2)+'\n')
    parents={}
    for n,x in ALL_SPECIES.items():
        if x['excluded']:continue
        for e in x['evolution_targets']:
            if e['species'] in ALL_SPECIES and not ALL_SPECIES[e['species']]['excluded']:
                level=int(e['param']) if e['method']=='LEVEL' and e['param'].isdigit() and int(e['param'])>1 else None
                parents[e['species']]=(n,level)
    def depth(n,seen=()):
        if n not in parents or n in seen:return 0
        return 1+depth(parents[n][0],seen+(n,))
    # Species without a natural level requirement receive explicit wild-availability
    # gates; this does not grant their evolution to player-owned Pokemon.
    parents={n:(p,level or (20 if depth(n)==1 else 36 if depth(n)==2 else 50))
             for n,(p,level) in parents.items()}
    def minimum(n,seen=()):
        if n not in parents or n in seen:return 0
        p,level=parents[n]
        return max(level,minimum(p,seen+(n,)))
    parents={n:(p,minimum(n)) for n,(p,level) in parents.items()}
    (ROOT/'src/data/wild_level_parents.h').write_text(
        '// Generated by tools/la_world/encounters/author_pools.py; Wild availability ancestry. Special evolutions use authored 20/36/50 level gates.\n'
        'static const struct WildLevelParent sWildLevelParents[NUM_SPECIES] = {\n'
        + ''.join(f'    [{n}] = {{ {p}, {level} }},\n' for n,(p,level) in sorted(parents.items()))+'};\n')
    with (OUT/'encounter_slots.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(records[0]));w.writeheader();w.writerows(records)
    summary=dict(policy='all active regions follow Hoenn badges temporarily',maps=len(rows),
        time_tables=len(entries),slots=len(records),eligible_species=len(eligible),unplaced=missing,
        regional_maps=dict(collections.Counter(x['region'] for x in rows)),
        form_policy='One ordinary representative per National Dex entry; battle-only forms excluded.',
        source_sha256=hashlib.sha256(path.read_bytes()).hexdigest())
    (OUT/'coverage.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary))

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    species=catalog();maps=inventory()
    if '--write' in __import__('sys').argv: author(species,maps)
    (OUT/'all_species_catalog.json').write_text(json.dumps(ALL_SPECIES,indent=2)+'\n')
    (OUT/'species_catalog.json').write_text(json.dumps(species,indent=2)+'\n')
    (OUT/'map_inventory.json').write_text(json.dumps(maps,indent=2)+'\n')
    with (OUT/'map_inventory.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(maps[0]));w.writeheader();w.writerows(maps)
    print(json.dumps(dict(base_species=len(species),eligible_species=sum(not x['excluded'] for x in species.values()),
        active_maps=len(maps),encounter_maps=sum(x['eligible'] for x in maps),
        missing_terrain=sum(bool(x['terrain_error']) for x in maps),regions=dict(collections.Counter(x['region'] for x in maps)))))
if __name__=='__main__':main()
