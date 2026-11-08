#!/usr/bin/env python3
"""Build native-scale WesleyFG Unova tiles, metatiles, palettes and Nuvema.
Source crops and placement are explicit; no resampling or AI artwork is used.
"""
from pathlib import Path
from PIL import Image, ImageDraw
import json,struct,shutil,hashlib,math,collections
P=Path(__file__).resolve().parents[2]
SRC=P/'graphics/unova_wesley/source'
OUT=P/'.la_work/unova_wesley';OUT.mkdir(parents=True,exist_ok=True)
DOC=P/'docs/la_world/unova_wesley';DOC.mkdir(parents=True,exist_ok=True)
PRI=P/'data/tilesets/primary/unova_general'
SEC=P/'data/tilesets/secondary/unova_nuvema'
N=Image.open(SRC/'bw_nature_tileset_by_wesleyfg_d45x0de.png').convert('RGB')
B=Image.open(SRC/'bw_buildings_tileset_by_wesleyfg_d45ygf8.png').convert('RGB')
T=Image.open(SRC/'nuvema_town_bw_by_wesleyfg_d3r861t.png').convert('RGB')
V=Image.open(SRC/'bw_velhices_by_wesleyfg_d45wzol.png').convert('RGB')
BG=N.getpixel((0,0));crops={}
def crop(sheet,box,name,transparent=False):
 im=sheet.crop(box).convert('RGBA')
 if transparent:
  bg=sheet.getpixel((0,0));im.putdata([(*c[:3],0 if c[:3]==bg else 255) for c in im.getdata()])
 crops[name]={'sheet':'buildings' if sheet is B else 'vehicles' if sheet is V else 'nuvema_reference' if sheet is T else 'nature','box':box,'native_size':im.size}
 return im

def pad(im,w=None,h=None,offset=(0,0)):
 w=w or math.ceil((im.width+offset[0])/16)*16;h=h or math.ceil((im.height+offset[1])/16)*16
 q=Image.new('RGBA',(w,h));q.alpha_composite(im,offset);return q

def quant_colors(images,n):
 cs=[c[:3] for im in images for c in im.getdata() if c[3]]
 q=Image.new('RGB',(len(cs),1));q.putdata(cs);q=q.quantize(colors=n,method=Image.Quantize.MEDIANCUT);pal=q.getpalette()
 return list(dict.fromkeys(tuple(round(pal[i*3+k]*31/255)*255//31 for k in range(3)) for i in range(len(q.getcolors()))))

def rgb5(c):return tuple(round(v*31/255)*255//31 for v in c)
def finish_colors(cs):
 cs=list(dict.fromkeys(rgb5(c) for c in cs))[:15]
 while len(cs)<15:cs.append(cs[-1])
 return [(0,0,0)]+cs

assets={}
assets['grass']=crop(N,(104,64,120,80),'Grass')
assets['path_source']=crop(N,(121,64,169,112),'Path_3x3')
assets['tree_nature']=pad(crop(N,(40,16,72,64),'TreeNature',True))
assets['tree']=crop(T,(1,433,33,481),'TownForestEdge')
assets['forest_interior']=crop(T,(1,1,33,33),'TownForestInterior')
assets['cluster']=crop(T,(1,417,33,481),'TownForestCluster')
assets['earth']=crop(N,(216,64,264,112),'Earth_Cliff')
assets['pool']=crop(N,(265,64,313,112),'RockyShore_3x3')
assets['water']=crop(T,(161,529,177,545),'TownOcean')
assets['beach']=crop(T,(33,497,49,529),'TownSandyShore')
assets['coastal_cliff']=crop(T,(33,465,49,497),'TownCoastalCliff')
assets['sign']=pad(crop(N,(122,48,138,64),'StoneSign',True))
assets['board_sign']=pad(crop(N,(138,42,169,64),'TownSign',True))
assets['mailbox']=pad(crop(N,(106,34,122,64),'Mailbox',True),16,32)
assets['hedge']=pad(crop(N,(89,17,105,64),'Hedge',True),16,48,(0,1))
assets['flowers']=crop(N,(92,64,108,80),'WhiteFlowers')
assets['pinkflowers']=pad(crop(N,(72,72,88,96),'PinkFlowers',True),16,32)
assets['blue']=pad(crop(B,(14,10,84,97),'NuvemaBlueHouse',True),80,96,(1,5))
assets['lab']=pad(crop(B,(95,11,237,121),'NuvemaLaboratory',True),160,112,(8,0))
assets['dock_rail']=crop(T,(257,481,273,497),'TownBoardwalkFront')
assets['dock_back']=crop(T,(257,465,273,481),'TownBoardwalkBack')
assets['dock_post']=crop(T,(169,497,185,513),'TownBoardwalkSupport')
assets['deck']=crop(N,(464,1008,496,1040),'WoodenDeck')
assets['rail']=Image.new('RGBA',(16,16));assets['rail'].alpha_composite(crop(N,(198,52,214,64),'RailingHorizontal',True),(0,4))
assets['rail_vertical']=Image.new('RGBA',(16,16));assets['rail_vertical'].alpha_composite(crop(N,(190,32,198,48),'RailingVertical',True),(0,0))
assets['white_fence']=pad(crop(N,(704,338,736,354),'WhiteFence',True))
assets['rock']=pad(crop(N,(384,766,416,798),'CoastalRock',True))
# Stair treads have three separate native 8-pixel bands. Side panels are 48px tall.
assets['stairs_top']=crop(N,(288,40,336,48),'StairTread_Top_48x8',True)
assets['stairs_mid']=crop(N,(288,48,336,56),'StairTread_Middle_48x8',True)
assets['stairs_base']=crop(N,(288,56,336,64),'StairTread_Base_48x8',True)
assets['stairs']=Image.new('RGBA',(96,48))
assets['stairs'].alpha_composite(crop(N,(168,16,184,64),'StairLeftSide_16x48',True),(0,0))
assets['stairs'].alpha_composite(crop(N,(280,32,288,64),'StairLeftPost_8x32',True),(16,16))
assets['stairs'].alpha_composite(crop(N,(336,32,344,64),'StairRightPost_8x32',True),(72,16))
assets['stairs'].alpha_composite(crop(N,(344,16,360,64),'StairRightSide_16x48',True),(80,0))
for y,a in [(24,'stairs_top'),(32,'stairs_mid'),(40,'stairs_base')]:assets['stairs'].alpha_composite(assets[a],(24,y))
# User-prepared source sheets: preserve assembly dimensions and existing map IDs.
user_crops=json.loads((DOC/'user_sheet_crops.json').read_text())
for key in ['grass','path_source','pool','sign','hedge','blue','lab']:
 spec=user_crops[key];sheet=Image.open(SRC/spec['sheet']).convert('RGBA')
 assets[key]=pad(sheet.crop(tuple(spec['box'])),*spec['size'],tuple(spec['offset']))
 crops[key]={'sheet':spec['sheet'],'box':spec['box'],'native_size':spec['size']}

# Small native materials are palette families, never a global source-sheet reduction.
greens=quant_colors([assets['grass']],7)
dirt=quant_colors([assets['path_source'].crop((12,12,36,36))],8)
roofblue=assets['blue'].crop((0,0,96,56));rooforange=assets['lab'].crop((0,0,160,88))
pals={
 0:finish_colors(greens+[(255,255,239),(255,239,115),(222,165,222),(140,90,132),(255,214,173),(82,132,90),(198,230,140),(107,148,90)]),
 1:finish_colors(quant_colors([assets['forest_interior'],assets['forest_interior'],assets['tree'],assets['cluster']],15)),
 2:finish_colors(greens+dirt),
 3:finish_colors(quant_colors([assets['earth']],15)),
 4:finish_colors(quant_colors([assets['water'],assets['water'],assets['beach'],assets['pool']],15)),
 5:finish_colors(quant_colors([assets['sign'],assets['rail'],assets['stairs']],15)),
 6:finish_colors(quant_colors([roofblue],15)),
 7:finish_colors(quant_colors([rooforange],15)),
 8:finish_colors(quant_colors([assets['blue'].crop((0,48,96,96)),assets['lab'].crop((0,80,160,128))],15)),
 9:finish_colors(sorted({c[:3] for c in assets['mailbox'].getdata() if c[3]})+quant_colors([assets['board_sign'],assets['dock_rail']],5)),
 10:finish_colors(quant_colors([assets['deck'],assets['dock_rail'],assets['dock_post']],15)),
 11:finish_colors(greens+sorted({c[:3] for c in assets['hedge'].getdata() if c[3]})),
 12:finish_colors(quant_colors([assets['white_fence'],assets['board_sign']],15)),
}
for imname in ['blue','lab','tree','cluster','stairs','stairs_top','stairs_mid','stairs_base']:assets[imname].save(OUT/(imname+'-native.png'))

class Pack:
 def __init__(self):
  self.tiles={0:bytes(64)};self.lookup={bytes(64):0};self.next=[1,512];self.metas=[[],[]];self.attrs=[[],[]];self.names=[[],[]];self.errors=collections.defaultdict(list)
 def flip(self,pix,flag):
  rows=[pix[y*8:y*8+8] for y in range(8)]
  if flag&1024:rows=[r[::-1] for r in rows]
  if flag&2048:rows=rows[::-1]
  return b''.join(rows)
 def remember(self,pix,idx):
  self.tiles[idx]=pix
  for f in [0,1024,2048,3072]:self.lookup.setdefault(self.flip(pix,f),idx|f)
 def tile(self,im,slots,bank,forced=None):
  data=list(im.getdata());opts=[]
  for slot in slots:
   colors=pals[slot];pix=[];err=0
   for c in data:
    if c[3]==0:pix.append(0);continue
    n=min(range(1,16),key=lambda i:sum((c[k]-colors[i][k])**2 for k in range(3)))
    pix.append(n);err+=sum((c[k]-colors[n][k])**2 for k in range(3))
   opts.append((err,slot,bytes(pix)))
  err,slot,pix=min(opts);self.errors[slot].append(err)
  if forced is not None:self.tiles[forced]=pix;return forced|slot<<12
  if pix in self.lookup and (bank or (self.lookup[pix]&1023)<512):idx=self.lookup[pix]
  else:
   idx=self.next[bank];limit=384 if bank==0 else 1024
   assert idx<limit, f'Bank {bank} exceeds tile budget: {idx}'
   self.next[bank]+=1;self.remember(pix,idx)
  return idx|slot<<12
 def add(self,im,name,slots,bank=0,behavior=0,background=None,force=None):
  assert im.width%16==im.height%16==0,(name,im.size)
  pattern=[]
  for y in range(im.height//16):
   row=[]
   for x in range(im.width//16):
    refs=[]
    for j in range(4):
     q=im.crop((x*16+(j%2)*8,y*16+(j//2)*8,x*16+(j%2)*8+8,y*16+(j//2)*8+8))
     refs.append(self.tile(q,slots,bank,None if force is None else force+4*(y*(im.width//16)+x)+j))
    base=self.metas[0][background][:4] if background is not None else refs
    n=len(self.metas[bank])+bank*512
    assert len(self.metas[bank])<512,'metatile capacity'
    self.metas[bank].append(base+([0]*4 if background is None else refs));self.attrs[bank].append(behavior);self.names[bank].append(name+f'_{x}_{y}');row.append(n)
   pattern.append(row)
  return pattern
 def single(self,*a,**kw):return self.add(*a,**kw)[0][0]
pack=Pack();prefabs={}
grass=pack.single(assets['grass'],'Grass',[0]);grassvar=pack.single(assets['grass'].transpose(Image.Transpose.FLIP_LEFT_RIGHT),'GrassVariation',[0]);flower=pack.single(assets['flowers'],'Flowers',[0]);pink=pack.add(assets['pinkflowers'],'PinkFlowers',[0],background=grass)
# Organic 47-state blob autotiles. Native source corners/edges are preserved.
# Bits N,E,S,W,NE,SE,SW,NW; diagonal only matters when both adjoining edges connect.
PATH={}
def canonical(mask):
 for diag,a,b in [(4,0,1),(5,1,2),(6,2,3),(7,3,0)]:
  if not (mask>>a&1 and mask>>b&1):mask&=~(1<<diag)
 return mask
states=sorted({canonical(n) for n in range(256)})
assert len(states)==47
for mask in states:
 im=Image.new('RGBA',(16,16))
 for qx,qy,a,b,di in [(0,0,0,3,7),(1,0,0,1,4),(0,1,2,3,6),(1,1,2,1,5)]:
  va=bool(mask>>a&1);vb=bool(mask>>b&1);diag=bool(mask>>di&1)
  sx=0 if qx==0 else 32;sy=0 if qy==0 else 32


  sx=(16 if vb else sx)+(8 if qx else 0);sy=(16 if va else sy)+(8 if qy else 0)
  piece=assets['path_source'].crop((sx,sy,sx+8,sy+8))
  if va and vb and not diag:
   # Concave corner: retain source grass texture and a feathered native-color rim.
   for py in range(8):
    for px in range(8):
     dx=px if qx==0 else 7-px;dy=py if qy==0 else 7-py
     if dx*dx+dy*dy<10+((px+py)%3):piece.putpixel((px,py),assets['grass'].getpixel((px+qx*8,py+qy*8)))
  im.alpha_composite(piece,(qx*8,qy*8))
 PATH[mask]=pack.single(im,f'Path_{mask:02X}',[2])
prefabs['ForestInterior']=pack.add(assets['forest_interior'],'ForestInterior',[1],background=grass)
prefabs['Tree']=pack.add(assets['tree'],'Tree',[1],background=grass)
prefabs['TreeNature']=pack.add(assets['tree_nature'],'TreeNature',[1],background=grass)
prefabs['CoastalCliff']=pack.add(assets['coastal_cliff'],'CoastalCliff',[3],background=grass)
prefabs['SandyShore']=pack.add(assets['beach'],'SandyShore',[4],behavior=0x15)
prefabs['ForestVerticalCluster']=pack.add(assets['cluster'],'ForestVerticalCluster',[1],background=grass)
hcluster=Image.new('RGBA',(64,48));hcluster.alpha_composite(assets['tree'],(0,0));hcluster.alpha_composite(assets['tree'],(32,0));prefabs['ForestHorizontalCluster']=pack.add(hcluster,'ForestHorizontalCluster',[1],background=grass)
# Cropped half trees are useful at irregular inner and outer forest corners.
prefabs['ForestPartialLeft']=pack.add(assets['tree'].crop((0,0,16,48)),'ForestPartialLeft',[1],background=grass)
prefabs['ForestPartialRight']=pack.add(assets['tree'].crop((16,0,32,48)),'ForestPartialRight',[1],background=grass)
prefabs['EarthCliffs']=pack.add(assets['earth'],'EarthCliffs',[3])
prefabs['RockyShore']=pack.add(assets['pool'],'RockyShore',[3,4],behavior=0x15)
prefabs['CoastalRock']=pack.add(assets['rock'],'CoastalRock',[3,4],background=grass)
prefabs['StoneSign']=[[pack.single(assets['sign'],'StoneSign',[5],behavior=0x1d,background=grass)]]
prefabs['RailingHorizontal']=[[pack.single(assets['rail'],'RailingHorizontal',[5],background=grass)]]
prefabs['RailingVertical']=[[pack.single(assets['rail_vertical'],'RailingVertical',[5],background=grass)]]
prefabs['Stairs']=pack.add(assets['stairs'],'Stairs',[5],background=grass)
for name,pieces in [('TopMiddle',['stairs_top','stairs_mid']),('MiddleMiddle',['stairs_mid','stairs_mid']),('MiddleBase',['stairs_mid','stairs_base'])]:
 im=Image.new('RGBA',(48,16))
 for i,n in enumerate(pieces):im.alpha_composite(assets[n],(0,8*i))
 prefabs['Stairs'+name]=pack.add(im,'Stairs'+name,[5],background=grass)
# Four ocean phases occupy a private, contiguous animation range, never deduplicated.
def shifted(im,x,y):
 q=Image.new('RGBA',im.size)
 for py in range(im.height):
  for px in range(im.width):q.putpixel((px,py),im.getpixel(((px+x)%im.width,(py+y)%im.height)))
 return q
water32=Image.new('RGBA',(32,32))
for i,(dx,dy) in enumerate([(0,0),(3,5),(7,2),(10,9)]):water32.alpha_composite(shifted(assets['water'],dx,dy),((i%2)*16,(i//2)*16))
prefabs['Ocean']=pack.add(water32,'Ocean',[4],behavior=0x15,force=384)
for frame in range(4):
 im=shifted(water32,frame*2,frame*2);data=[]
 for y in range(2):
  for x in range(2):
   for j in range(4):
    q=im.crop((x*16+j%2*8,y*16+j//2*8,x*16+j%2*8+8,y*16+j//2*8+8));ref=pack.tile(q,[4],0,400+frame*16+y*8+x*4+j);data.extend(pack.tiles[ref&1023])
 # Build contiguous metatile-order 4bpp frames for the DMA callback.
 raw=bytes(u|v<<4 for u,v in zip(data[::2],data[1::2]));(OUT/f'water-{frame}.4bpp').write_bytes(raw)
# Remove temporary frame positions; only range 384..399 is live VRAM.
for i in range(400,464):pack.tiles.pop(i,None)
# Architecture is modular 16x16 roof, wall, door and trim pieces, with shared 8x8 patterns.
prefabs['BlueHouse']=pack.add(assets['blue'],'BlueHouse',[6,8],bank=1,background=grass)
prefabs['Laboratory']=pack.add(assets['lab'],'Laboratory',[7,8],bank=1,background=grass)
prefabs['Mailbox']=pack.add(assets['mailbox'],'Mailbox',[9],bank=1,background=grass)
prefabs['Hedge']=pack.add(assets['hedge'],'Hedge',[11],bank=1,background=grass)
prefabs['TownSign']=pack.add(assets['board_sign'],'TownSign',[9,12],bank=1,background=grass)
prefabs['GardenFence']=pack.add(assets['white_fence'],'GardenFence',[11,12],bank=1,background=grass)
prefabs['BoardwalkBack']=pack.add(assets['dock_back'],'BoardwalkBack',[0,3,9,10],bank=1,background=grass)
prefabs['BoardwalkDeck']=pack.add(assets['deck'],'BoardwalkDeck',[10],bank=1)
prefabs['BoardwalkFront']=pack.add(assets['dock_rail'],'BoardwalkFront',[9,10],bank=1,background=prefabs['Ocean'][0][0])
prefabs['BoardwalkSupport']=pack.add(assets['dock_post'],'BoardwalkSupport',[9,10],bank=1,background=prefabs['Ocean'][1][0])
# Door metatiles remain unique so their behavior does not leak to wall pieces.
blue_door=prefabs['BlueHouse'][5][2];lab_door=prefabs['Laboratory'][6][5]
pack.attrs[1][blue_door-512]=0x60;pack.attrs[1][lab_door-512]=0x60

# Archive the existing map before the visual-layer replacement.
backup=OUT/'original';backup.mkdir(exist_ok=True)
layoutfile=P/'data/layouts/layouts.json';layouts=json.loads(layoutfile.read_text());layout=next(l for l in layouts['layouts'] if l['id']=='LAYOUT_AMAP_3_0_NUVEMA_TOWN_LAYOUT')
for rel in ['data/maps/Unova_NuvemaTown/map.json','data/layouts/layouts.json',layout['blockdata_filepath'],layout['border_filepath'],'data/maps/Unova_Route1/map.json']:
 dst=backup/rel;dst.parent.mkdir(parents=True,exist_ok=True)
 if not dst.exists():shutil.copy2(P/rel,dst)

W,H=40,40
blocks=[grass|0x3000]*(W*H);kind=['grass']*(W*H)
def setblock(x,y,n,collision=0,elevation=3,k='grass'):
 if 0<=x<W and 0<=y<H:blocks[y*W+x]=n|collision<<10|elevation<<12;kind[y*W+x]=k

def stamp(pat,x,y,k,collision=1):
 for j,row in enumerate(pat):
  for i,n in enumerate(row):setblock(x+i,y+j,n,collision,k=k)
# Placement follows the user-supplied native 640x576 town reference; four additional
# ocean rows provide depth without changing the scale of a single source pixel.
for y in range(30,H):
 for x in range(W):setblock(x,y,prefabs['Ocean'][y%2][x%2],0,1,'water')
for x in list(range(9))+list(range(30,W)):
 stamp(prefabs['CoastalCliff'],x,29,'cliff')
 stamp(prefabs['SandyShore'],x,31,'shore',0)
# Native forest top/middle/base pieces are staggered around the clearing.
for y in range(-2,28,2):
 for x in range(-1,W,2):
  if x<9 or x>=30 or y<1 or (19<=x<25 and y<6):stamp(prefabs['ForestInterior'],x,y,'forest')
for x in range(0,9,2):stamp(prefabs['Tree'],x,27,'forest')
for x in range(30,W,2):stamp(prefabs['Tree'],x,27,'forest')
# Forest edge partials avoid a single repeated straight seam everywhere.
for x,y in [(8,4),(8,18),(29,8),(29,22),(21,5)]:
 if x==8:stamp(prefabs['ForestPartialRight'],x,y,'forest')
 else:stamp(prefabs['ForestPartialLeft'],x,y,'forest')
paths=set()
def rect(x1,y1,x2,y2):
 for y in range(y1,y2+1):
  for x in range(x1,x2+1):paths.add((x,y))
rect(13,9,27,10);rect(13,9,15,19);rect(25,0,27,19);rect(13,17,27,19)
rect(18,18,20,28);rect(11,26,27,28);rect(14,25,15,28);rect(25,25,26,28)
rect(13,7,15,10)
for x,y in list(paths):
 if y<9 and 25<=x<=27:
  for dx in [-1,0,1]:setblock(x+dx,y,grass,0,3,'grass')
for x,y in paths:
 mask=0
 for bit,(dx,dy) in enumerate([(0,-1),(1,0),(0,1),(-1,0),(1,-1),(1,1),(-1,1),(-1,-1)]):
  if (x+dx,y+dy) in paths or (y==0 and dy==-1 and 25<=x+dx<=27):mask|=1<<bit
 setblock(x,y,PATH[canonical(mask)],0,3,'path')
houses=[('Laboratory',10,1,(15,7)),('BlueHouse',19,11,(21,16)),('BlueHouse',12,20,(14,25)),('BlueHouse',23,20,(25,25))]
for name,x,y,door in houses:
 stamp(prefabs[name],x,y,'building')
 setblock(*door,lab_door if name=='Laboratory' else blue_door,0,3,'door')
 art=assets['lab' if name=='Laboratory' else 'blue']
 for by in range(art.height//16):
  for bx in range(art.width//16):
   if not art.crop((bx*16,by*16,bx*16+16,by*16+16)).getbbox():setblock(x+bx,y+by,grass,0,3,'grass')
 if name=='BlueHouse':
  hedge_x=x+5 if x==12 else x-1
  stamp(prefabs['Hedge'],hedge_x,y+2,'hedge');stamp(prefabs['Mailbox'],x-1,y+4,'mailbox')
# Central island remains open as in the final reference; flower/fence prefabs are
# available in Porymap for future gardens without forcing an enclosure into this town.
stamp(prefabs['StoneSign'],12,10,'sign');stamp(prefabs['TownSign'],21,19,'sign')
for x,y in [(10,14),(10,15),(11,16),(11,17),(10,24),(28,27),(29,28),(28,29)]:
 if kind[y*W+x]=='grass':setblock(x,y,flower,0,3,'flowers')
for x in range(9,30):
 setblock(x,29,prefabs['BoardwalkBack'][0][0],0,3,'boardwalk')
 setblock(x,30,prefabs['BoardwalkFront'][0][0],1,3,'railing')
 if x in (10,23):setblock(x,31,prefabs['BoardwalkSupport'][0][0],1,3,'support')
rockwater=pack.add(assets['rock'],'CoastalRockWater',[3,4],background=prefabs['Ocean'][0][0])
# Keep the reference's open ocean; coastal rocks remain available as reusable tiles.
# NPCs and active warps are preserved, then moved only if their landing is obstructed.
mapfile=P/'data/maps/Unova_NuvemaTown/map.json';m=json.loads((backup/'data/maps/Unova_NuvemaTown/map.json').read_text());event_moves=[];occupied={(19,23)}
for obj in m['object_events']:
 old=(obj['x'],obj['y']);nearest=min((q for q in paths if kind[q[1]*W+q[0]]=='path' and q not in occupied),key=lambda q:(abs(q[0]-old[0])+abs(q[1]-old[1]),q[1],q[0]));obj['x'],obj['y']=nearest;obj['elevation']=3;occupied.add(nearest)
 if old!=nearest:event_moves.append({'local_id':obj['local_id'],'old':old,'new':nearest})
# No active doors existed in the restored BWA exterior; do not silently activate pending donor warps.
# Keep those records, and update their source coordinates to the new corresponding doors.
for warp in m.get('warp_events',[]):
 old=(warp['x'],warp['y']);near=min([h[3] for h in houses],key=lambda q:abs(q[0]-old[0])+abs(q[1]-old[1]));warp['x'],warp['y']=near;warp['elevation']=3
m.update(map_type='MAP_TYPE_TOWN',allow_running=True,allow_cycling=True)
# Route 1's southern path x=22..24 aligns with new Nuvema x=25..27.
for c in m.get('connections') or []:
 if c['map']=='MAP_BWA_3_19_ROUTE_1':c['offset']=3
rfile=P/'data/maps/Unova_Route1/map.json';r=json.loads(rfile.read_text())
for c in r.get('connections') or []:
 if c['map']==m['id']:c['offset']=-3

# Write the native GBA tileset files and 16-color JASC palettes.
for bank,directory in enumerate([PRI,SEC]):
 directory.mkdir(parents=True,exist_ok=True);(directory/'palettes').mkdir(exist_ok=True)
 raw=bytearray()
 for i in range(bank*512,(bank+1)*512):
  pix=pack.tiles.get(i,bytes(64));raw.extend(u|v<<4 for u,v in zip(pix[::2],pix[1::2]))
 (directory/'tiles.4bpp').write_bytes(raw)
 png=Image.new('P',(128,256));png.putpalette([i*17 for i in range(16) for _ in range(3)]+[0]*720)
 for i in range(512):
  pix=pack.tiles.get(bank*512+i,bytes(64));t=Image.new('P',(8,8));t.putdata(pix);png.paste(t,((i%16)*8,(i//16)*8))
 png.save(directory/'tiles.png')
 meta=pack.metas[bank]+[[0]*8]*(512-len(pack.metas[bank]));attrs=pack.attrs[bank]+[0]*(512-len(pack.attrs[bank]))
 (directory/'metatiles.bin').write_bytes(struct.pack('<4096H',*(v for row in meta for v in row)))
 (directory/'metatile_attributes.bin').write_bytes(struct.pack('<512H',*attrs))
 for slot in range(16):
  colors=pals.get(slot,[(0,0,0)]*16);(directory/f'palettes/{slot:02}.pal').write_text('JASC-PAL\n0100\n16\n'+'\n'.join(' '.join(map(str,c)) for c in colors)+'\n')
  (directory/f'palettes/{slot:02}.gbapal').write_bytes(struct.pack('<16H',*[sum((c[k]>>3)<<(5*k) for k in range(3)) for c in colors]))
 (directory/'prefabs.json').write_text(json.dumps({k:v for k,v in prefabs.items() if bool(v[0][0]>=512)==bool(bank)},indent=2)+'\n')
 if bank==0:
  (directory/'anim/water').mkdir(parents=True,exist_ok=True)
  for i in range(4):shutil.copy2(OUT/f'water-{i}.4bpp',directory/f'anim/water/{i}.4bpp')
layout.update(width=W,height=H,primary_tileset='gTileset_UnovaGeneral_Primary',secondary_tileset='gTileset_UnovaNuvema_Secondary')
(P/layout['blockdata_filepath']).write_bytes(struct.pack('<'+str(W*H)+'H',*blocks))
(P/layout['border_filepath']).write_bytes(struct.pack('<4H',*[prefabs['Ocean'][y][x]|0x1c00 for y in range(2) for x in range(2)]))
layoutfile.write_text(json.dumps(layouts,indent=2)+'\n');mapfile.write_text(json.dumps(m,indent=2)+'\n');rfile.write_text(json.dumps(r,indent=2)+'\n')
f=P/'data/scripts/la_teleport_scientist.inc';f.write_text(f.read_text().replace('warp MAP_AMAP_3_0_NUVEMA_TOWN, 16, 22','warp MAP_AMAP_3_0_NUVEMA_TOWN, 19, 23'))
# Export vehicles as native RGBA source assets only; no tileset capacity is spent.
vehicles=SRC.parent/'vehicles';vehicles.mkdir(exist_ok=True)
vehicleboxes={'Castelia_BoatBlue':(123,25,240,88),'Castelia_BoatBlack':(127,91,240,151),'Castelia_BoatYellow':(129,159,238,224),'Driftveil_Truck':(273,24,427,87),'Driftveil_Loader':(7,110,88,180),'Mistralton_Aircraft':(266,106,407,235),'Castelia_CargoShipHorizontal':(553,20,760,121),'Castelia_CargoShipVertical':(450,24,542,227)}
for name,box in vehicleboxes.items():crop(V,box,name,True).save(vehicles/(name+'.png'))

report={'tilesets':['gTileset_UnovaGeneral_Primary','gTileset_UnovaNuvema_Secondary'],'map_dimensions':[W,H],'primary_graphics_tiles':pack.next[0]+16,'secondary_graphics_tiles':pack.next[1]-512,'primary_graphics_free':512-pack.next[0]-16,'secondary_graphics_free':1024-pack.next[1],'primary_metatiles':len(pack.metas[0]),'secondary_metatiles':len(pack.metas[1]),'primary_metatiles_free':512-len(pack.metas[0]),'secondary_metatiles_free':512-len(pack.metas[1]),'palettes':{str(i):n for i,n in enumerate(['grass/accent','dark trees','grass/dirt','earth/cliffs','ocean/foam','stone/stairs/fences','blue roofs','orange roofs','wood/windows','metal/mailboxes','boardwalk wood','hedges/flowers','white fence/signs'])},'path_blob_states':47,'stair_bands':{'top':[288,40,336,48],'middle':[288,48,336,56],'base':[288,56,336,64],'assembly':'TopMiddle, MiddleMiddle, MiddleBase: 16px metatiles; middle repeatable. Side panels remain separate native 16x48 assets.'},'water_animation':{'frames':4,'tiles':16,'destination':384,'ticks_per_frame':16},'event_moves':event_moves,'active_warps':len(m['warp_events']),'pending_donor_warps_activated':False,'route_offsets':[3,-3],'vehicle_assets':vehicleboxes,'source_crops':crops,'limitations':['GBA RGB5 and 15 opaque colors per material palette; quantization is local to named materials.','Source sheets contain single still ocean texture; four native-pixel scroll phases provide subtle animation.','Vehicles are prepared RGBA source art for later sprite conversion; not active object graphics.']}
(DOC/'report.json').write_text(json.dumps(report,indent=2)+'\n');(DOC/'prefabs.json').write_text(json.dumps(prefabs,indent=2)+'\n');(DOC/'path_autotiles.json').write_text(json.dumps({f'{k:02X}':v for k,v in PATH.items()},indent=2)+'\n');(DOC/'collision_grid.json').write_text(json.dumps({'width':W,'height':H,'kind':kind,'doors':[[h[3][0],h[3][1]] for h in houses]},indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ['source_crops','vehicle_assets','palettes','event_moves']},indent=2))

