"""Check source and linked encounters with disposable native saves."""
from pathlib import Path
R=Path.cwd()
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
import json, re, struct, tempfile, hashlib, collections
D=R/'docs/la_world/wild_pools'
cat=json.loads((D/'species_catalog.json').read_text())
allcat=json.loads((D/'all_species_catalog.json').read_text())
inv=json.loads((D/'map_inventory.json').read_text())
by_map={x['map']:x for x in inv}
by_num={(x['group'],x['map_num']):x for x in inv}
ids={n:int(v) for n,v in re.findall(r'\b(SPECIES_\w+)\s*=\s*(\d+)',(R/'include/constants/species.h').read_text())}
by_dex={x['national_dex']:x for x in cat.values() if not x.get('regional_form')}
allowed={ids[n]:cat.get(n,by_dex[x['national_dex']])['native_regions'] for n,x in allcat.items() if n in ids}
excluded={ids[n] for n,x in allcat.items() if x['excluded'] and n in ids}
source=json.loads((R/'src/data/wild_encounters.json').read_text())['wild_encounter_groups'][0]['encounters']
seen=set();source_slots=0
for e in source:
 row=by_map[e['map']]
 if row['region']=='REGION_UNOVA':continue
 for method,info in e.items():
  if not method.endswith('_mons'):continue
  for m in info['mons']:
   x=cat[m['species']]
   assert row['region'] in x['native_regions'],(row['name'],m['species'])
   assert not x['excluded']
   if x.get('regional_form'):
    import importlib.util
    if 'author_module' not in globals():
     spec=importlib.util.spec_from_file_location('author',R/'tools/la_world/encounters/author_pools.py');author_module=importlib.util.module_from_spec(spec);spec.loader.exec_module(author_module)
    assert author_module.biome(row) in x['allowed_biomes'],(row['name'],m['species'])
   seen.add(m['species']);source_slots+=1
assert seen=={n for n,x in cat.items() if not x['excluded']}
# Obtain exact structure offsets from the active compiler configuration.
names=['sizeof(struct WildPokemonHeader)','offsetof(struct WildPokemonHeader,encounterTypes)','FLAG_BADGE01_GET','FLAG_SYS_GAME_CLEAR']
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "wild_encounter.h"\n#include "constants/flags.h"\n#include <stddef.h>\nconst unsigned v[]={'+','.join(names)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 c=dict(zip(names,struct.unpack('<4I',(td/'c.bin').read_bytes())))
start(0)
form_seen=set()
count=rd(symbols['gWildMonHeaderCount']);compared=0;regions=collections.Counter()
for stage in range(10):
 for i in range(8):invoke('FlagSet' if i<stage else 'FlagClear',c['FLAG_BADGE01_GET']+i)
 invoke('FlagSet' if stage==9 else 'FlagClear',c['FLAG_SYS_GAME_CLEAR'])
 cap=invoke('GetWildProgressionCap')
 for i in range(count-1):
  h=symbols['gWildMonHeaders']+i*c['sizeof(struct WildPokemonHeader)']
  row=by_num[(rd(h,1),rd(h+1,1))]
  if row['region']=='REGION_UNOVA':continue
  for tod in range(4):
   view=invoke('GetEffectiveWildEncounterTypes',i,tod)
   for area,size in enumerate([12,5,5,10,3]):
    info=rd(view+area*4)
    if not info:continue
    slots=rd(info+4)
    for j in range(size):
     lo,hi,sp=rd(slots+j*4,1),rd(slots+j*4+1,1),rd(slots+j*4+2,2)
     assert 1<=lo<=hi<=cap,(stage,row['name'],lo,hi,cap)
     assert sp not in excluded,(row['name'],sp)
     assert row['region'] in allowed[sp],(stage,row['name'],sp)
     form_seen.add(sp)
     compared+=1
  if stage==0:regions[row['region']]+=1
 print('Validated badge stage',stage,'cap',cap,flush=True)
form_ids={ids[n] for n,x in cat.items() if x.get('regional_form')}
assert form_ids<=form_seen,('Forms never available after level resolution',[n for n in cat if ids[n] in form_ids-form_seen])
report=dict(source_slots=source_slots,ordinary_species=len(seen),regional_forms=sum(x.get('regional_form',False) for x in cat.values()),regional_maps=dict(regions),linked_slot_comparisons=compared,unova_required=False,user_save_loaded=False,rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest())
(D/'regional_assignment_validation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report),flush=True)
