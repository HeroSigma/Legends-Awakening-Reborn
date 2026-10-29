"""Author fixed trainer identities and specialist cores; no RNG or donor scripts.
Run after editing this source to regenerate the reviewed profile header and manifest.
Runtime resolves evolutions and legal role moves at the encounter's capped level.
"""
from pathlib import Path
import re,json
R=Path(__file__).resolve().parents[2]
# Six-member cores. Native aces and native teammates take priority for ordinary trainers.
CORES={
"Hiker":"GIGALITH EXCADRILL GASTRODON SKARMORY MUDSDALE GOLEM",
"Bug Catcher":"BUTTERFREE BEEDRILL DUSTOX BEAUTIFLY MASQUERAIN ARAQUANID",
"Bug Maniac":"GALVANTULA SCIZOR FORRETRESS VOLCARONA HERACROSS YANMEGA",
"Youngster":"LINOONE RATICATE SWELLOW LUXRAY MUDSDALE MIGHTYENA",
"Lass":"ROSERADE DELCATTY AZUMARILL TOGEKISS FURRET FLORGES",
"School Kid":"ALAKAZAM MAGNEZONE AZUMARILL BRELOOM CROBAT STOUTLAND",
"Rich Boy":"PERSIAN ARCANINE ROSERADE MILOTIC TOGEKISS STOUTLAND",
"Lady":"PERSIAN FLORGES MILOTIC ROSERADE ARCANINE DELCATTY",
"Gentleman":"STOUTLAND ARCANINE POLTEAGEIST MR_MIME ROSERADE PERSIAN",
"Beauty":"NINETALES ROSERADE MILOTIC LOPUNNY GARDEVOIR DELCATTY",
"Aroma Lady":"VILEPLUME ROSERADE SHIINOTIC TSAREENA WHIMSICOTT LILLIGANT",
"Camper":"SANDSLASH BRELOOM ARCANINE NOCTOWL QUAGSIRE LINOONE",
"Picnicker":"ROSERADE RAICHU AZUMARILL NINETALES ALTARIA WIGGLYTUFF",
"Pokefan":"RAICHU AZUMARILL CLEFABLE WIGGLYTUFF DELCATTY KANGASKHAN",
"Pkmn Breeder":"AUDINO ARCANINE AZUMARILL ROSERADE TOGEKISS KANGASKHAN",
"Fisherman":"PELIPPER BARRASKEWDA LUDICOLO WHISCASH GYARADOS TENTACRUEL",
"Swimmer M":"PELIPPER FLOATZEL LUDICOLO QWILFISH MANTINE SHARPEDO",
"Swimmer F":"PELIPPER LUDICOLO LANTURN GASTRODON GOREBYSS MILOTIC",
"Tuber M":"AZUMARILL LANTURN QUAGSIRE PELIPPER FLOATZEL LUDICOLO",
"Tuber F":"AZUMARILL DEWGONG LANTURN LUDICOLO PELIPPER GOREBYSS",
"Sailor":"PELIPPER POLIWRATH TENTACRUEL LANTURN MACHAMP GYARADOS",
"Sis And Bro":"PELIPPER LUDICOLO LANTURN MANTINE AZUMARILL GYARADOS",
"Parasol Lady":"PELIPPER LUDICOLO SEAKING DRAGALGE GASTRODON CASTFORM",
"Bird Keeper":"SKARMORY SWELLOW NOCTOWL TALONFLAME CORVIKNIGHT ALTARIA",
"Triathlete":"CROBAT MANECTRIC FLOATZEL DODRIO HITMONLEE SWELLOW",
"Guitarist":"GALVANTULA MANECTRIC ROTOM MAGNEZONE TOXTRICITY AMPED_RAICHU",
"Kindler":"NINETALES ARCANINE HOUNDOOM MAGCARGO TALONFLAME TORKOAL",
"Black Belt":"HITMONTOP HARIYAMA BRELOOM MACHAMP MIENSHAO LUCARIO",
"Battle Girl":"HITMONTOP MEDICHAM BRELOOM MIENSHAO HARIYAMA LUCARIO",
"Expert":"HITMONTOP MIENSHAO SLOWBRO SKARMORY ARCANINE HARIYAMA",
"Psychic":"MR_MIME GARDEVOIR BRONZONG SLOWBRO ESPEON ALAKAZAM",
"Hex Maniac":"SABLEYE COFAGRIGUS MISMAGIUS SPIRITOMB BANETTE GENGAR",
"Ninja Boy":"CROBAT SCOLIPEDE TENTACRUEL VENOMOTH SHIFTRY NINJASK",
"Ruin Maniac":"BRONZONG CLAYDOL CRADILY ARMALDO RUNERIGUS GOLEM",
"Pkmn Ranger":"ROSERADE ARCANINE LUDICOLO BRELOOM ALTARIA MANECTRIC",
"Dragon Tamer":"ALTARIA KINGDRA DRUDDIGON FLYGON HAXORUS SALAMENCE",
"Collector":"PORYGON2 CRADILY ARMALDO MAGNEZONE ROTOM DITTO",
"Pokemaniac":"SLOWBRO RHYPERIOR NIDOKING LICKILICKY AGGRON KANGASKHAN",
"Team Aqua":"PELIPPER MUK CROBAT CRAWDAUNT LANTURN SHARPEDO",
"Aqua Admin":"PELIPPER TENTACRUEL MUK LUDICOLO CRAWDAUNT SHARPEDO",
"Aqua Leader":"PELIPPER LUDICOLO TENTACRUEL GYARADOS CRAWDAUNT SHARPEDO",
"Team Magma":"TORKOAL WEEZING CROBAT SHIFTRY SANDSLASH CAMERUPT",
"Magma Admin":"TORKOAL WEEZING CROBAT SHIFTRY CLAYDOL CAMERUPT",
"Magma Leader":"TORKOAL SHIFTRY CROBAT CLAYDOL HOUNDOOM CAMERUPT",
"Twins":"PLUSLE MINUN CLEFAIRY HITMONTOP AZUMARILL TOGEKISS",
"Sr And Jr":"CLEFAIRY HITMONTOP MANECTRIC GYARADOS ROSERADE GARDEVOIR",
"Young Couple":"INDEEDEE_F ARCANINE WHIMSICOTT GALLADE TOGEKISS GARDEVOIR",
"Old Couple":"HITMONTOP SLOWBRO BRONZONG AMOONGUSS TORKOAL SNORLAX",
"Interviewer":"MAGNEZONE EXPLOUD PELIPPER LUDICOLO ARCANINE GARDEVOIR",
"Winstrate":"PELIPPER ROSERADE HITMONTOP GASTRODON MANECTRIC STOUTLAND",
"Cooltrainer":"ROTOM_WASH ARCANINE AMOONGUSS METAGROSS GARCHOMP TOGEKISS",
"Cooltrainer 2":"ROTOM_WASH ARCANINE AMOONGUSS METAGROSS GARCHOMP TOGEKISS",
"Rival":"PELIPPER LUXRAY BRELOOM GARDEVOIR SNORLAX ALTARIA",
"RS Protag":"PELIPPER LUXRAY BRELOOM GARDEVOIR SNORLAX ALTARIA",
}
# Correct explicit names rather than fuzzy donor-name guessing.
CORES['Guitarist']='GALVANTULA MANECTRIC ROTOM MAGNEZONE TOXTRICITY_AMPED RAICHU'
BOSSES={
'ROXANNE':('GIGALITH EXCADRILL CLAYDOL CRADILY ARMALDO PROBOPASS','sand',16),
'BRAWLY':('HITMONTOP SCRAFTY MEDICHAM TOXICROAK BRELOOM HARIYAMA','balance',20),
'WATTSON':('GALVANTULA LANTURN MAGNETON ROTOM EEL E_MANECTRIC','balance',26),
'FLANNERY':('TORKOAL SHIFTRY NINETALES TALONFLAME HOUNDOOM CAMERUPT','sun',32),
'NORMAN':('STARAPTOR LINOONE PORYGON2 TAUROS URSARING SLAKING','balance',37),
'WINONA':('PELIPPER GLISCOR SKARMORY TALONFLAME TROPIUS ALTARIA','rain',43),
'TATE_AND_LIZA':('BRONZONG CLAYDOL XATU SLOWBRO LUNATONE SOLROCK','trick',49),
'JUAN':('PELIPPER LUDICOLO GASTRODON TENTACRUEL GYARADOS KINGDRA','rain',56),
'SIDNEY':('KROOKODILE UMBREON SABLEYE SHIFTRY CRAWDAUNT ABSOL','balance',65),
'PHOEBE':('SABLEYE DUSCLOPS COFAGRIGUS MISMAGIUS BANETTE DUSKNOIR','trick',65),
'GLACIA':('ABOMASNOW FROSLASS MAMOSWINE LAPRAS GLALIE WALREIN','snow',65),
'DRAKE':('DRAGALGE ALTARIA KINGDRA FLYGON HAXORUS SALAMENCE','balance',65),
'WALLACE':('PELIPPER TENTACRUEL LUDICOLO GASTRODON GYARADOS MILOTIC','rain',65),
'STEVEN':('SKARMORY CLAYDOL CRADILY ARMALDO AGGRON METAGROSS','sand',65),
'WALLY':('ROSERADE MAGNEZONE ALTARIA AZUMARILL GALLADE GARDEVOIR','balance',65),
'RED':('PIKACHU LAPRAS SNORLAX VENUSAUR BLASTOISE CHARIZARD','balance',75),
'LEAF':('CLEFABLE NINETALES KANGASKHAN GYARADOS VICTREEBEL VENUSAUR','balance',75),
}
BOSSES['WATTSON']=('GALVANTULA LANTURN MAGNEZONE ROTOM EELEKTROSS MANECTRIC','balance',26)
# Map context takes priority over a generic class identity for Gym students.
GYM_CORES={
 'rock':('GOLEM ONIX PROBOPASS RHYDON CRADILY ARMALDO','sand'),
 'fighting':('MACHAMP MEDICHAM HERACROSS SCRAGGY HITMONTOP HARIYAMA','balance'),
 'electric':('RAICHU LANTURN MAGNEZONE ROTOM EELEKTROSS MANECTRIC','balance'),
 'fire':('TORKOAL NINETALES MAGCARGO HOUNDOOM TALONFLAME CAMERUPT','sun'),
 'normal':('LINOONE STOUTLAND FURRET PERSIAN TAUROS SLAKING','balance'),
 'flying':('PELIPPER SKARMORY SWELLOW NOCTOWL TROPIUS ALTARIA','rain'),
 'psychic':('BRONZONG CLAYDOL XATU SLOWBRO LUNATONE SOLROCK','trick'),
 'water':('PELIPPER LUDICOLO GASTRODON TENTACRUEL GYARADOS KINGDRA','rain'),
 'grass':('ROSERADE VILEPLUME BRELOOM TANGROWTH VICTREEBEL LILLIGANT','balance'),
 'poison':('CROBAT WEEZING MUK VENOMOTH TENTACRUEL DRAPION','balance'),
 'ground':('SANDSLASH RHYDON CLAYDOL MUDSDALE QUAGSIRE EXCADRILL','sand'),
 'bug':('BUTTERFREE BEEDRILL ARIADOS SCIZOR HERACROSS FORRETRESS','balance'),
 'ghost':('GENGAR MISMAGIUS BANETTE DUSCLOPS COFAGRIGUS SPIRITOMB','trick'),
 'steel':('MAGNEZONE STEELIX SKARMORY AGGRON FORRETRESS BRONZONG','balance'),
 'ice':('ABOMASNOW DEWGONG PILOSWINE JYNX GLALIE WALREIN','snow'),
 'dragon':('ALTARIA KINGDRA DRUDDIGON FLYGON HAXORUS SALAMENCE','balance'),
}
GYM_LOCATIONS={
 'RustboroCity_Gym':'rock','DewfordTown_Gym':'fighting','MauvilleCity_Gym':'electric',
 'LavaridgeTown_Gym':'fire','PetalburgCity_Gym':'normal','FortreeCity_Gym':'flying',
 'MossdeepCity_Gym':'psychic','SootopolisCity_Gym':'water',
 'PewterCity_Gym':'rock','CeruleanCity_Gym':'water','VermilionCity_Gym':'electric',
 'CeladonCity_Gym':'grass','FuchsiaCity_Gym':'poison','SaffronCity_Gym':'psychic',
 'CinnabarIsland_Gym':'fire','SeafoamIslands_Gym':'fire','ViridianCity_Gym':'ground',
 'VioletCity_Gym':'flying','AzaleaTown_Gym':'bug','GoldenrodCity_Gym':'normal',
 'EcruteakCity_Gym':'ghost','CianwoodGym':'fighting','OlivineCity_Gym':'steel',
 'MahoganyTown_Gym':'ice','BlackthornCity_Gym':'dragon',
}
BIOME_CORES={
 'forest':('BUTTERFREE BEEDRILL BRELOOM ROSERADE SHIFTRY MASQUERAIN','balance'),
 'cave':('GOLEM GOLBAT SABLEYE PROBOPASS EXCADRILL AGGRON','balance'),
 'mountain':('GOLEM SKARMORY MUDSDALE MACHAMP ALTARIA CAMERUPT','balance'),
 'coast':('PELIPPER LANTURN TENTACRUEL GASTRODON FLOATZEL LUDICOLO','rain'),
 'desert':('SANDSLASH CACTURNE FLYGON CLAYDOL KROOKODILE MARACTUS','sand'),
 'volcanic':('TORKOAL MAGCARGO CAMERUPT WEEZING SANDSLASH SKARMORY','sun'),
}
def location_theme(name):
 for gym,theme in GYM_LOCATIONS.items():
  if name.startswith(gym) or name.startswith('Kanto_'+gym) or name.startswith('HnS_'+gym) or name.startswith('HnSTest_'+gym):return 'gym:'+theme
 if any(x in name for x in ['Woods','Forest','SafariZone']):return 'forest'
 if name.startswith('Route111_Desert'):return 'desert'
 if any(x in name for x in ['FieryPath','MtChimney','JaggedPass','Route113']):return 'volcanic'
 if any(x in name for x in ['MtPyre','MeteorFalls','VictoryRoad','MtSilver','MtEmber']):return 'mountain'
 if any(x in name for x in ['Cave','Tunnel']):return 'cave'
 if name in ['Route105','Route106','Route107','Route108','Route109','Route124','Route125','Route126','Route127','Route128','Route129','Route130','Route131','Route132','Route133','Route134','DewfordTown']:return 'coast'
 return None
locations={}
for path in sorted((R/'data/maps').glob('*/scripts.inc')):
 theme=location_theme(path.parent.name)
 if not theme:continue
 for tid in set(tid for line in re.findall(r'^\s*trainerbattle_\w+[^\n]*',path.read_text(),re.M) for tid in re.findall(r'\bTRAINER_\w+',line)):
  locations.setdefault(tid,[]).append((path.parent.name,theme))
LOCATION_CLASSES={'Youngster','Lass','School Kid','Camper','Picnicker','Cooltrainer','Cooltrainer 2','Pkmn Ranger','Hiker','Bug Catcher','Bug Maniac','Ruin Maniac','Ninja Boy','Bird Keeper','Fisherman','Swimmer M','Swimmer F','Sailor','Black Belt','Battle Girl','Hex Maniac','Psychic','Tuber M','Tuber F'}
def context_core(key,cls):
 sources=locations.get(key,[])
 gyms={theme for _,theme in sources if theme.startswith('gym:')}
 if len(gyms)==1:
  theme=next(iter(gyms));return theme,GYM_CORES[theme[4:]],sources
 if gyms or cls not in LOCATION_CLASSES:return None
 themes={theme for _,theme in sources}
 if len(themes)!=1:return None # Shared cross-area trainers keep their explicit class identity.
 theme=next(iter(themes))
 # Specialists retain a relevant role within the environment.
 if theme=='forest' and cls in ['Bug Catcher','Bug Maniac','Ninja Boy','Bird Keeper']:return theme,(CORES[cls],'balance'),sources
 if theme=='coast' and cls in ['Fisherman','Swimmer M','Swimmer F','Sailor','Tuber M','Tuber F']:return theme,(CORES[cls],'rain'),sources
 return theme,BIOME_CORES[theme],sources
FACILITIES={'Salon Maiden','Dome Ace','Palace Maven','Arena Tycoon','Factory Head','Pike Queen','Pyramid King'}
S=(R/'src/data/trainers.party').read_text();S=re.sub(r'/\*.*?\*/','',S,flags=re.S)
P=re.split(r'^=== (TRAINER_\w+) ===\s*$',S,flags=re.M)
# Read exact species tokens from generated native parties (trainerproc resolves display names).
H=(R/'src/data/trainers.h').read_text()
blocks=re.split(r'\[DIFFICULTY_NORMAL\]\[(TRAINER_\w+)\] =',H)
native={blocks[i]:re.findall(r'\.species = SPECIES_(\w+)',blocks[i+1]) for i in range(1,len(blocks),2)}
# Promote native ordinary team members through their canonical family, then let
# the runtime resolve the highest ancestor legal at the encounter's capped level.
parents=re.findall(r'\[SPECIES_(\w+)\] = \{ SPECIES_(\w+), \d+ \}',(R/'src/data/wild_level_parents.h').read_text())
order={name:i for i,name in enumerate(re.findall(r'SPECIES_(\w+)\s*(?:=|,)',(R/'include/constants/species.h').read_text()))}
children={}
for child,parent in parents:
 if '_' not in child and child not in ['MEWTWO','MEW']:
  children.setdefault(parent,[]).append(child)
def final_form(sp):
 for _ in range(5):
  options=children.get(sp,[])
  if not options:break
  sp=min(options,key=lambda n:order.get(n,99999))
 return sp
profiles={};excluded={};out=['// Generated by tools/la_world/author_competitive_trainers.py. Fixed identities, no RNG.','static const struct LegendsTeamProfile sFullProfiles[TRAINERS_COUNT] = {']
for i in range(1,len(P),2):
 key,body=P[i:i+2]
 def field(n):
  m=re.search('^'+re.escape(n)+r': (.*)$',body,re.M);return m.group(1) if m else ''
 cls=field('Class');name=field('Name');species=native.get(key,[])
 if not species or cls in FACILITIES or key.startswith('TRAINER_LA_') or key.endswith('_PLACEHOLDER'):
  excluded[key]='scripted tutorial/partner, empty placeholder, or separate facility rules';continue
 if cls not in CORES and key!='TRAINER_GRUNT_PETALBURG_WOODS' and not any(k in key for k in BOSSES):raise ValueError((key,cls))
 boss=next((k for k in BOSSES if re.match('TRAINER_'+k+r'(?:_\d+)?$',key)),None)
 core,weather,level=BOSSES[boss] if boss else (CORES.get(cls,CORES['Team Aqua']),'balance',0)
 if boss and re.search(r'_[2-5]$',key):level=100
 if not boss:species=list(dict.fromkeys(final_form(sp) for sp in species))
 pool=core.split();ace=pool[-1] if boss else species[-1]
 # Ordinary native identities take priority, then complement from an authored class core.
 team=[] if boss else [sp for sp in dict.fromkeys(species[:-1]) if sp!=ace][:5]
 for sp in pool:
  if len(team)>=5:break
  if sp!=ace and sp not in team:team.append(sp)
 if len(team)<5:
  for sp in species+pool:
   if len(team)>=5:break
   team.append(sp)
 team=team[:5]+[ace]
 if not boss:
  original=max(map(int,re.findall(r'^Level: (\d+)',body,re.M)))
  old=[15,19,24,29,31,33,42,46,58,100];new=[16,20,26,32,37,43,49,56,65,100]
  stage=next(j for j,v in enumerate(old) if original<=v);level=new[stage]
  weather='rain' if cls in ['Fisherman','Swimmer M','Swimmer F','Sailor','Team Aqua','Aqua Admin','Aqua Leader','Parasol Lady','Sis And Bro'] else 'sun' if cls in ['Kindler','Team Magma','Magma Admin','Magma Leader','Aroma Lady'] else 'sand' if cls=='Hiker' else 'trick' if cls in ['Old Couple','Ruin Maniac','Psychic'] else 'balance'
 context=None if boss or cls in ['Rival','RS Protag','Team Aqua','Team Magma','Aqua Admin','Aqua Leader','Magma Admin','Magma Leader'] or key=='TRAINER_GRUNT_PETALBURG_WOODS' else context_core(key,cls)
 if context:
  location,(local_core,weather),sources=context
  pool=local_core.split()
  # Different students lead with different members; the entire roster stays thematic.
  offset=sum(key.encode())%len(pool)
  team=pool[offset:]+pool[:offset]
 major=bool(boss or cls in ['Rival','RS Protag','Aqua Admin','Aqua Leader','Magma Admin','Magma Leader'])
 choice=bool(boss and boss not in ['WALLY','RED','LEAF','STEVEN'])
 if key=='TRAINER_GRUNT_PETALBURG_WOODS':
  team=['PAWNIARD','ZUBAT','KOFFING','SNEASEL','ZORUA','ABSOL'];weather='balance';level=16;major=True;choice=False
 profiles[key]=dict(name=name,trainer_class=cls,species=team,theme=weather,level=level,shiny_ace=major,format_choice=choice)
 if context:profiles[key].update(location_theme=context[0],location_sources=[name for name,_ in context[2]])
 out.append('    ['+key+'] = {{'+','.join('SPECIES_'+sp for sp in team)+'}, '+str(level)+', THEME_'+weather.upper()+', '+str(int(major))+', '+str(int(choice))+'},')
out+=['};']
(R/'src/data/legends_trainer_profiles.h').write_text('\n'.join(out)+'\n')
(R/'docs/features/competitive-trainer-profiles.json').write_text(json.dumps(dict(profiles=profiles,excluded=excluded),indent=2)+'\n')
print('Authored',len(profiles),'profiles;',len(excluded),'protected entries')
