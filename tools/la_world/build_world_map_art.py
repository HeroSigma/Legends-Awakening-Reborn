"""Build a continuous atlas, preserving original Hoenn pixels and exact GBA colors."""
from pathlib import Path
from PIL import Image
import struct,json,re,collections
R=Path(__file__).resolve().parents[2];A=R/'data/world_map';A.mkdir(exist_ok=True)
def decode(p):
 im=Image.open(p.with_suffix('.png')).convert('RGB');b=p.with_suffix('.bin').read_bytes();assert len(b)==4096
 out=Image.new('RGB',(512,512));cols=im.width//8
 for i,t in enumerate(b):
  assert t<cols*(im.height//8)
  out.paste(im.crop((t%cols*8,t//cols*8,t%cols*8+8,t//cols*8+8)),(i%64*8,i//64*8))
 return out
hoenn=decode(R/'graphics/pokenav/region_map/map');jk=decode(R/'assets/regional_maps/hns/pokenav/map_jk');sinnoh=decode(R/'assets/regional_maps/sinnoh_native/map')
sea=hoenn.crop((232,152,240,160));world=Image.new('RGB',(512,512))
for y in range(0,512,8):
 for x in range(0,512,8):world.paste(sea,(x,y))
for im,offset in [(jk,(248,24)),(sinnoh,(16,24))]:
 im=im.crop((0,0,240,160));pixels=im.load()
 for y in range(160):
  for x in range(240):
   red,green,blue=pixels[x,y]
   if blue>red+15 and blue>green+4:pixels[x,y]=world.getpixel((offset[0]+x,offset[1]+y))
 world.paste(im,offset)
world.paste(hoenn.crop((0,0,240,160)),(16,224))
def rgb555(c):return (c[0]>>3)|((c[1]>>3)<<5)|((c[2]>>3)<<10)
# Pack exact per-tile color sets into palette banks, rather than quantizing a
# whole region to sixteen colors. Hoenn's original pixel colors survive intact.
rawtiles=[]
for y in range(64):
 for x in range(64):rawtiles.append(tuple(rgb555(c) for c in world.crop((x*8,y*8,x*8+8,y*8+8)).getdata()))
banks=[]
for colors in sorted({frozenset(t) for t in rawtiles},key=lambda s:(-len(s),sorted(s))):
 assert len(colors)<=16,('Tile exceeds 4bpp palette',len(colors))
 candidates=[(len(set(b)|colors)-len(b),i) for i,b in enumerate(banks) if len(set(b)|colors)<=16]
 if candidates:
  _,i=min(candidates);banks[i]=sorted(set(banks[i])|colors)
 else:banks.append(sorted(colors))
assert len(banks)<=15,len(banks)
tiles=[];lookup={};grid=[]
for t in rawtiles:
 colors=set(t);bank=next(i for i,b in enumerate(banks) if colors<=set(b));indices=[banks[bank].index(c) for c in t];packed=bytes(indices[i]|indices[i+1]<<4 for i in range(0,64,2))
 if packed not in lookup:lookup[packed]=len(tiles);tiles.append(packed)
 grid.append(lookup[packed]|bank<<12)
assert len(tiles)<=1024,len(tiles)
tm=[0]*4096
for y in range(64):
 for x in range(64):tm[(y//32*2+x//32)*1024+(y%32)*32+x%32]=grid[y*64+x]
(A/'tiles.bin').write_bytes(b''.join(tiles));(A/'tilemap.bin').write_bytes(struct.pack('<4096H',*tm));(A/'palette.bin').write_bytes(b''.join(struct.pack('<16H',*(b+[0]*(16-len(b)))) for b in banks))
world.save(R/'docs/art/regional_maps/world-canvas.png')
# Keep the established Hoenn/Johto/Kanto hover geometry; append Sinnoh using
# its donor-authored grid, not guessed town positions.
header=R/'src/data/world_map_locations.h';s=header.read_text();s=s.split('// Sinnoh native map cells')[0]
# Rebuilding must not duplicate the generated Sinnoh cells.
s=re.sub(r'static const u8 sSinnohName\d+\[\].*?\n','',s)
s=re.sub(r'^    \{\d+, \d+, 4, sSinnohName.*?\n','',s,flags=re.M)
sections={x['id']:x.get('name',x['id'].removeprefix('MAPSEC_').replace('_',' ')).title() for x in json.loads((R/'assets/regional_maps/sinnoh_native/region_map_sections.json').read_text())['map_sections']}
lines=[];names={}
layout=(R/'assets/regional_maps/sinnoh_native/region_map_layout.h').read_text()
for y,row in enumerate(re.findall(r'\{([^{}]+)\}',layout)):
 for x,section in enumerate(re.findall(r'MAPSEC_\w+',row)):
  if section=='MAPSEC_NONE':continue
  name=sections.get(section,section.removeprefix('MAPSEC_').replace('_',' ').title())
  if name not in names:names[name]=len(names)
  lines.append(f'    {{{x+3}, {y+5}, 4, sSinnohName{names[name]}}}, // {section}\n')
declarations=''.join(f'static const u8 sSinnohName{i}[] = _("{n}");\n' for n,i in names.items())
s=s.replace('static const struct WorldLocation sWorldLocations[] = {',declarations+'static const struct WorldLocation sWorldLocations[] = {')
s=s.rsplit('};',1)[0]+''.join(lines)+'};\n';header.write_text(s)
# Group-level region hints disambiguate names shared by multiple regions.
groups=json.loads((R/'data/maps/map_groups.json').read_text());hints={}
manifest=json.loads((R/'docs/la_world/hns_regions/manifest.json').read_text())['maps'];hns={x['name']:x.get('source_region') for x in manifest}
for gi,g in enumerate(groups['group_order']):
 regions=[]
 for n in groups[g]:
  p=R/'data/maps'/n/'map.json'
  if p.exists():regions.append(hns.get(n) or json.loads(p.read_text()).get('region'))
 regions=[{'REGION_KANTO':1,'REGION_JOHTO':2,'REGION_HOENN':3,'REGION_SINNOH':4}.get(v,0) for v in regions]
 hints[gi]=collections.Counter(regions).most_common(1)[0][0] if regions else 0
(A/'region_groups.json').write_text(json.dumps(hints,indent=2)+'\n')
(R/'src/data/world_map_region_groups.h').write_text('static const u8 sWorldRegionByGroup[] = {\n'+''.join(f'    [{g}] = {v},\n' for g,v in hints.items())+'};\n')
report=dict(tiles=len(tiles),palette_banks=len(banks),sinnoh_cells=len(lines),sinnoh_names=len(names),hoenn_pixel_colors_preserved=True,canvas=[512,512])
(A/'build-report.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
