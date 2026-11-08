from pathlib import Path
import json,struct,shutil,collections
from PIL import Image
P=Path(__file__).resolve().parents[2];f=P/'tools/la_world/rebuild_unova_wesley.py';s=f.read_text();OUT=P/'.la_work/unova_wesley';backup=OUT/'before-exact-user';backup.mkdir(exist_ok=True)
for rel in ['data/tilesets/primary/unova_general','data/tilesets/secondary/unova_nuvema','data/layouts/AMap_3_0_Nuvema_Town_Layout','docs/la_world/unova_wesley']:
 dst=backup/rel
 if not dst.exists():shutil.copytree(P/rel,dst)
ns={'__file__':str(f)};prefix=s[:s.index('class Pack:')];prefix=prefix.replace('# Small native materials',"exec((P/'tools/la_world/nuvema_exact_assets.py').read_text())\n# Small native materials")
exec(prefix,ns);exec(s[s.index('class Pack:'):s.index('pack=Pack();')],ns)
required={'Grass','GrassVariation','Flowers','ForestInterior','Tree','TreeNature','CoastalCliff','SandyShore','ForestVerticalCluster','ForestHorizontalCluster','ForestPartialLeft','ForestPartialRight','StoneSign','Ocean','BlueHouse','Laboratory','Mailbox','Hedge','TownSign','BoardwalkBack','BoardwalkDeck','BoardwalkFront','BoardwalkSupport'}
def isrequired(n):return n.startswith('Path_') or n in required
Pack=ns['Pack'];originaladd=Pack.add;calls=[];name=''
def add(self,im,n,*a,**kw):
 global name
 name=n
 return originaladd(self,im,n,*a,**kw)
def collect(self,im,slots,bank,forced=None):
 if isrequired(name):calls.append((name,im.copy()))
 if forced is not None:self.tiles[forced]=bytes(64);return forced
 return 0
Pack.add=add;Pack.tile=collect
body=s[s.index('pack=Pack();'):s.index('# Archive the existing map')]
start=body.index('for mask in states:');end=body.index("prefabs['ForestInterior']")
body=body[:start]+"""for mask in states:
 sx=0 if not mask&8 else 32 if not mask&2 else 16
 sy=0 if not mask&1 else 32 if not mask&4 else 16
 im=assets['path_source'].crop((sx,sy,sx+16,sy+16))
 # Native 16px corners retain the complete source curve, without recombining
 # disconnected 8px samples or drawing new feathered rims.
 PATH[mask]=pack.single(im,f'Path_{mask:02X}',[2])
"""+body[end:]

exec(body,ns)
sets=list(set(frozenset(tuple(v>>3 for v in c[:3]) for c in im.getdata() if c[3]) for _,im in calls));sets=[c for c in sets if c and not any(c<d for d in sets)];bins=[]
for cs in sorted(sets,key=lambda c:(-len(c),sorted(c))):
 assert len(cs)<=15
 opts=[(len(cs-b),i) for i,b in enumerate(bins) if len(cs|b)<=15]
 if opts:bins[min(opts)[1]]|=cs
 else:bins.append(set(cs))
print('Exact palettes required:',len(bins));assert len(bins)<=13,'Exact palette budget exceeded; no colours were reduced.'
pals={i:[(0,0,0)]+[tuple(v<<3 for v in c) for c in sorted(b)]+[(0,0,0)]*(15-len(b)) for i,b in enumerate(bins)}
for i in range(13):pals.setdefault(i,[(0,0,0)]*16)
ns['pals']=pals;calls=[]
def exacttile(self,im,slots,bank,forced=None):
 if not isrequired(name):return 0
 cs={tuple(v>>3 for v in c[:3]) for c in im.getdata() if c[3]};slot=next(i for i,b in enumerate(bins) if cs<=b);colors=pals[slot];lookup={tuple(v>>3 for v in c):i for i,c in enumerate(colors) if i};pix=bytes(lookup[tuple(v>>3 for v in c[:3])] if c[3] else 0 for c in im.getdata());calls.append((name,im.copy(),slot,pix))
 if forced is not None:self.tiles[forced]=pix;return forced|slot<<12
 if pix in self.lookup and (bank or (self.lookup[pix]&1023)<512):idx=self.lookup[pix]
 else:
  idx=self.next[bank];assert idx<(384 if bank==0 else 1024),(name,idx);self.next[bank]+=1;self.remember(pix,idx)
 return idx|slot<<12
Pack.tile=exacttile;exec(body,ns)
# Keep existing metatile IDs, layout and user edits; only source artwork/palettes change.
old=json.loads((P/'docs/la_world/unova_wesley/prefabs.json').read_text());assert ns['prefabs']==old
exec("rockwater=pack.add(assets['rock'],'CoastalRockWater',[3,4],background=prefabs['Ocean'][0][0])",ns)
exec(s[s.index('for bank,directory in enumerate([PRI,SEC]):'):s.index('layout.update(width=W,height=H')],ns)
for n,im,slot,pix in calls:
 for c,index in zip(im.getdata(),pix):
  assert (not c[3] and index==0) or (c[3] and index and tuple(v>>3 for v in c[:3])==tuple(v>>3 for v in pals[slot][index]))
rfile=P/'docs/la_world/unova_wesley/report.json';r=json.loads(rfile.read_text());pack=ns['pack'];r.update(primary_graphics_tiles=pack.next[0]+16,secondary_graphics_tiles=pack.next[1]-512,primary_graphics_free=512-pack.next[0]-16,secondary_graphics_free=1024-pack.next[1]);r['exact_user_art']={'source_sheets':['Nuvema.png','Nuvema Second.png'],'palettes':len(bins),'checked_8x8_tiles':len(calls),'colour_reduction':False,'colour_conversion':'RGB888 to GBA RGB555 only; no nearest-colour replacement.','unused_previous_prefabs':'Blanked; only Nuvema-used assemblies are packed.'};rfile.write_text(json.dumps(r,indent=2)+'\n')
f=P/'data/tilesets/unova_wesley_prefabs.json';catalog=json.loads(f.read_text());catalog=[v for v in catalog if any(k.lower() in v['name'].lower().replace(' ','') for k in required if k not in ['Grass','Tree'])];f.write_text(json.dumps(catalog,indent=2)+'\n')
print('Exact pixel validation passed:',len(calls),'8x8 tiles. Graphics used:',r['primary_graphics_tiles'],r['secondary_graphics_tiles'])
