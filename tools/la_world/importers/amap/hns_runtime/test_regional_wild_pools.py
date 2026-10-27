"""Exercise the actual linked ARM resolver in an isolated native mGBA instance."""
from probe import *
import hashlib, tempfile
D=R/'docs/la_world/wild_pools';D.mkdir(parents=True,exist_ok=True)
# Scratch lies beyond the linked EWRAM footprint; no user battery save is loaded.
BASE=0x0203f000
RULES=BASE+0x100
RESULT=BASE+0x180
assembly=r"""
.syntax unified
.thumb
.global start
start:
 push {r4,lr}
 ldr r0,arg0
 ldr r1,arg1
 ldr r2,arg2
 ldr r3,target
 bl call_r3
 ldr r1,result
 str r0,[r1]
 ldr r1,callback
 ldr r0,previous
 str r0,[r1]
 pop {r4}
 pop {r0}
 bx r0
call_r3:
 bx r3
.balign 4
arg0: .word 0
arg1: .word 0
arg2: .word 0
target: .word 0
result: .word 0
callback: .word 0
previous: .word 0
"""
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'invoke.s').write_text(assembly)
 subprocess.run(['arm-none-eabi-as','-mcpu=arm7tdmi','-o',str(td/'invoke.o'),str(td/'invoke.s')],check=True)
 subprocess.run(['arm-none-eabi-ld','-Ttext='+hex(BASE),'-e','start','-o',str(td/'invoke.elf'),str(td/'invoke.o')],check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary',str(td/'invoke.elf'),str(td/'invoke.bin')],check=True)
 code=(td/'invoke.bin').read_bytes()
 labels={z[2]:int(z[0],16) for line in subprocess.check_output(['arm-none-eabi-nm',str(td/'invoke.elf')],text=True).splitlines() if len(z:=line.split())==3}
def invoke(name,a=0,b=0,c=0):
 for i,v in enumerate(code):wr(BASE+i,v,1)
 for k,v in dict(arg0=a,arg1=b,arg2=c,target=symbols[name]|1,result=RESULT,callback=symbols['gMain']+4,previous=rd(symbols['gMain']+4)).items():wr(labels[k],v)
 wr(RESULT,0xdeadbeef)
 wr(symbols['gMain']+4,BASE|1)
 frames(1)
 assert rd(RESULT)!=0xdeadbeef,('native call did not return',name)
 return rd(RESULT)
checks=[]
def check(name,ok):
 assert ok,name
 checks.append(dict(test=name,passed=True))
def rules(entries,count=None,profiles=3):
 for i,row in enumerate(entries):
  for j,v in enumerate(row):wr(RULES+i*12+j*2,v,2)
 return invoke('ResolveDynamicEncounterRules',RULES,len(entries) if count is None else count,profiles)
def flag(n,on):
 a=rd(symbols['gSaveBlock1Ptr'])+0x1270+n//8
 wr(a,(rd(a,1)|(1<<(n%8))) if on else (rd(a,1)&~(1<<(n%8))),1)
assert lib.boot(str(R/'pokeemerald.gba').encode())
frames(600)
p=rd(symbols['gSaveBlock2Ptr'])
for i,v in enumerate([0xbb,0xcc,0xbf,0xc8,0xff,0,0,0]):wr(p+i,v,1)
wr(symbols['gMain']+4,symbols['CB2_NewGame']|1);frames(240)

import re
ids={n:int(v) for n,v in re.findall(r'\b(SPECIES_\w+)\s*=\s*(\d+)',(R/'include/constants/species.h').read_text())}
catalog=json.loads((D/'all_species_catalog.json').read_text())
banned={ids[n] for n,x in catalog.items() if x['excluded']}
flags_text=(R/'include/constants/flags.h').read_text()
# Expansion's system flag base is a constant native save offset.
system=0x860 # Native save flag ABI; asserted through cap/flag runtime checks below.
badge=system+7; clear=system+4
def stage(n,champion=False):
 for i in range(8):flag(badge+i,i<n)
 flag(clear,champion)
caps=[12,16,20,24,27,29,41,41,46]
for n,cap in enumerate(caps):
 stage(n)
 check('badge_stage_'+str(n),invoke('GetWildBadgeStage')==n)
 check('next_leader_lowest_level_'+str(n),invoke('GetWildProgressionCap')==cap)
stage(8,True)
check('post_league_cap_100',invoke('GetWildProgressionCap')==100)
for src,level,target in [
 ('CHARMANDER',15,'CHARMANDER'),('CHARMANDER',16,'CHARMELEON'),
 ('CHARMANDER',36,'CHARIZARD'),('CHARIZARD',5,'CHARMANDER'),
 ('CATERPIE',10,'BUTTERFREE'),('EEVEE',70,'EEVEE'),
 ('CURSOLA',5,'CORSOLA_GALAR'),('CURSOLA',38,'CURSOLA'),('KINGAMBIT',30,'PAWNIARD'),
 ('RAICHU',5,'PICHU'),('RAICHU',25,'PIKACHU'),('RAICHU',36,'RAICHU'),
 ('SILCOON',2,'WURMPLE'),('POIPOLE',100,'POIPOLE'),('PIKACHU',100,'PIKACHU')]:
 check('evolution_'+src+'_'+str(level),invoke('ResolveWildLevelSpecies',ids['SPECIES_'+src],level)==ids['SPECIES_'+target])
inventory=json.loads((D/'map_inventory.json').read_text())
for safe in ['LittlerootTown','OldaleTown','MauvilleCity_BikeShop','HnS_BlackthornCity_Gym','HnS_CeruleanCity_Gym']:
 check('safe_area_'+safe,not next(x for x in inventory if x['name']==safe)['eligible'])
count=rd(symbols['gWildMonHeaderCount'])
check('no_random_battles_before_starter',invoke('StandardWildEncounter',2,2)==0)
check('all_authored_maps_have_headers',count==json.loads((D/'coverage.json').read_text())['maps']+1)
sizes=[12,5,5,10,3]
compared=0
levels={}
range_rows=[]
map_names={ (x["group"],x["map_num"]):x["name"] for x in json.loads((D/"map_inventory.json").read_text())}
for n in range(9):
 stage(n)
 cap=caps[n]
 for index in range(count-1):
  for tod in range(4):
   view=invoke('GetEffectiveWildEncounterTypes',index,tod)
   for area,size in enumerate(sizes):
    info=rd(view+area*4)
    if not info:continue
    slots=rd(info+4)
    area_lows=[];area_highs=[]
    for j in range(size):
     lo,hi,sp=rd(slots+j*4,1),rd(slots+j*4+1,1),rd(slots+j*4+2,2)
     assert 1<=lo<=hi<=cap,(n,index,tod,area,j,lo,hi,cap)
     assert sp not in banned,(index,tod,sp)
     compared+=1
     area_lows.append(lo);area_highs.append(hi)
    h=symbols['gWildMonHeaders']+index*84
    range_rows.append(dict(map=map_names[(rd(h,1),rd(h+1,1))],badges=n,time=tod,method=area,min_level=min(area_lows),max_level=max(area_highs),cap=cap))
   if index==0 and tod==0:levels[n]=rd(rd(rd(view)+4),1)
check('all_linked_slots_obey_caps_and_exclusions',True)
check('route_ranges_rise_with_badges',levels[0]<=levels[4]<=levels[8])
# All four TOD pointers can be held together while land/water are inspected.
views=[invoke('GetEffectiveWildEncounterTypes',0,t) for t in range(4)]
check('four_time_views_have_distinct_storage',len(set(views))==4)
stage(0)
check('dexnav_bonus_cannot_exceed_cap',invoke('ClampWildBonusLevel',ids['SPECIES_PIKACHU'],99)==12)
stage(8,True)
check('dexnav_bonus_preserves_searched_species',invoke('ClampWildBonusLevel',ids['SPECIES_CHARMANDER'],99)==15)
check('poipole_does_not_auto_evolve_by_level',invoke('ResolveWildLevelSpecies',ids['SPECIES_POIPOLE'],100)==ids['SPECIES_POIPOLE'])
empty=invoke('GetEffectiveWildEncounterTypes',0xffff,0)
check('invalid_header_empty',all(rd(empty+j*4)==0 for j in range(5)))

reverse_ids={v:n for n,v in ids.items()}
# Route 101's night theme must survive evolution-stage adjustment.
route101=next(i for i in range(count-1) if rd(symbols['gWildMonHeaders']+i*84,1)==0 and rd(symbols['gWildMonHeaders']+i*84+1,1)==16)
weights=[20,20,10,10,10,10,5,5,4,4,1,1]
for n in [0,5,8]:
 stage(n)
 shares=[]
 for tod in [1,3]:
  view=invoke('GetEffectiveWildEncounterTypes',route101,tod);slots=rd(rd(view)+4)
  share=0
  for j,w in enumerate(weights):
   sp=reverse_ids[rd(slots+j*4+2,2)]
   if any(t in catalog[sp]['types'] for t in ('DARK','GHOST')):share+=w
  shares.append(share)
 check('night_route_theme_badges_'+str(n),shares[1]>shares[0])
# Verify safety in the real map/header lookup, not only in the authoring inventory.
sb=rd(symbols['gSaveBlock1Ptr'])
for name in ['LittlerootTown','OldaleTown','MauvilleCity_BikeShop','HnS_BlackthornCity_Gym']:
 row=next(x for x in inventory if x['name']==name)
 wr(sb+4,row['group'],1);wr(sb+5,row['map_num'],1)
 check('no_runtime_header_'+name,invoke('GetCurrentMapWildMonHeaderId')==0xffff)
# Exercise DexNav's actual level generator and actual wild Pokemon creation.
mon_enum=re.search(r'enum MonData\s*\{(.*?)\};',(R/'include/pokemon.h').read_text(),re.S)[1]
mon_ids={name:i for i,name in enumerate(re.findall(r'\bMON_DATA_\w+',re.sub(r'//[^\n]*','',mon_enum)))}
party_size=int(next(line.split()[1] for line in subprocess.check_output(
 ['arm-none-eabi-nm','-S',str(R/'pokeemerald.elf')],text=True).splitlines() if line.endswith(' gParties')),16)//4
opponent=symbols['gParties']+party_size
sb=rd(symbols['gSaveBlock1Ptr'])
wr(sb+4,0,1);wr(sb+5,16,1) # Route 101
for n in [0,2,5,8]:
 stage(n)
 header=invoke('GetCurrentMapWildMonHeaderId')
 tod=invoke('GetTimeOfDayForEncounters',header,0)
 view=invoke('GetEffectiveWildEncounterTypes',header,tod)
 slots=rd(rd(view)+4);species=rd(slots+2,2)
 for i in range(20):
  level=invoke('DexNavTryGenerateMonLevel',species,0)
  assert 1<=level<=caps[n],(n,level)
  assert invoke('ResolveWildLevelSpecies',species,level)==species
 invoke('CreateWildMon',species,level)
 check('dexnav_to_real_wild_mon_badges_'+str(n),
       invoke('GetMonData3',opponent,mon_ids['MON_DATA_SPECIES'])==species
       and invoke('GetMonData3',opponent,mon_ids['MON_DATA_LEVEL'])==level)
import csv
with (D/'badge_level_ranges.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(range_rows[0]));w.writeheader();w.writerows(range_rows)
lib.shutdown()
report=dict(rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),
 header_count=count,linked_slot_comparisons=compared,checks=checks,
 user_battery_save_loaded=False)
(D/'runtime_validation.json').write_text(json.dumps(report,indent=2)+'\n')
print('Native checks:',len(checks),'linked slots inspected:',compared)
