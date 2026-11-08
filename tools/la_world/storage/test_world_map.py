"""Exercise the connected atlas on native ARM with disposable SRAM."""
from pathlib import Path
import re,json,hashlib,shutil
R=Path('/home/allan/projects/Legends-Awakening-Reborn')
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'docs/art/regional_maps/runtime';D.mkdir(exist_ok=True)
checks=[]
def check(n,v):
 checks.append({'test':n,'passed':bool(v)})
 assert v,n
start(0)
invoke('ScriptContext_Init');invoke('UnlockPlayerFieldControls')
text=(R/'src/data/world_map_locations.h').read_text()
locs=re.findall(r'\{(\d+), (\d+), (\d+), (sWorldName\d+)\}',text)
for x,y,region,name in locs:
 check('location '+x+','+y,invoke('WorldMap_LocationAt',int(x),int(y))==symbols[name])
 check('region '+x+','+y,invoke('WorldMap_RegionAt',int(x),int(y))==int(region))
for x in range(2,29):
 for y in range(3,24):
  check('removed region '+str((x,y)),invoke('WorldMap_RegionAt',x,y)==0)
check('open sea' ,invoke('WorldMap_RegionAt',2,25)==0)
invoke('FieldInitRegionMap',symbols['CB2_ReturnToFieldWithOpenMenu']|1)
wr(symbols['gMain']+4,symbols['WorldMap_Update']|1);frames(40)
state=rd(symbols['sWorldMap']);check('allocated world map',state!=0)
check('BG0 UI / BG2 world enabled',rd(0x04000000,2)&0x500==0x500)
palette=(R/'data/world_map/palette.bin').read_bytes()
check('all atlas palette banks loaded',all(rd(0x05000000+i,2)==int.from_bytes(palette[i:i+2],'little') for i in range(0,len(palette),2)))
check('world tilemap block24',rd(0x0400000c,2)>>8&31==24)
shutil.copy2(shot('world_hoenn'),D/'hoenn.png')
oldx=rd(state+5,1);frames(1,16);frames(3);check('right moves cursor',rd(state+5,1)==oldx+1)
for region,name in [(2,'johto'),(1,'kanto')]:
 x,y,_,_=next(v for v in locs if int(v[2])==region)
 wr(state+5,int(x),1);wr(state+6,int(y),1);invoke('WorldMap_Refresh');frames(4)
 shutil.copy2(shot('world_'+name),D/(name+'.png'))
 check(name+' label region',invoke('WorldMap_RegionAt',int(x),int(y))==region)
wr(state+5,16,1);wr(state+6,12,1);invoke('WorldMap_Refresh');frames(4)
shutil.copy2(shot('world_open_sea'),D/'removed-sinnoh.png')
wr(state+5,61,1);wr(state+6,47,1);frames(2);frames(1,16|128);frames(2)
check('bottom right clamped',rd(state+5,1)==61 and rd(state+6,1)==47)
frames(1,2);frames(60)
check('map memory released',rd(symbols['sWorldMap'])==0)
check('return to game',rd(symbols['gMain']+4)!=symbols['WorldMap_Update']|1)
# Open the PokeNav normally, then select its first Map entry.
start(0)
invoke('ScriptContext_Init');invoke('UnlockPlayerFieldControls')
wr(symbols['gMain']+4,symbols['CB2_InitPokeNav']|1);frames(300)
check('PokeNav allocated',rd(symbols['gPokenavResources'])!=0)
frames(1,1);frames(220)
check('PokeNav Map opens world',rd(symbols['sWorldMap'])!=0)
check('PokeNav resources freed before world',rd(symbols['gPokenavResources'])==0)
shutil.copy2(shot('world_pokenav'),D/'pokenav.png')
frames(1,2);frames(60)
check('PokeNav map returns cleanly',rd(symbols['sWorldMap'])==0)
report={'passed':True,'checks':checks,'rom_sha256':hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest()}
(D/'validation.json').write_text(json.dumps(report,indent=2)+'\n')
print('PASS',len(checks),'native checks')
