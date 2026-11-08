"""Preserve donor object art without linking it or changing any map/gameplay data.
Run with python3 tools/la_world/importers/amap/preserve_npc_library.py.
Source sheets and metadata are copied byte-for-byte; uncertain palettes/frames
remain review candidates. This archive intentionally includes props and creatures.
"""
from pathlib import Path
import csv, hashlib, json, shutil, html, re
from collections import Counter
from PIL import Image, ImageDraw
from sprite_catalog import ObjectSpriteCatalog
R=Path(__file__).resolve().parents[4]
OUT=R/'assets/donor_npcs'
DOC=R/'docs/la_world/donor_npcs'
OLD=Path('/home/allan/projects/Legends-Awakening')
HNS=Path('/home/allan/la-scratch/pokehns-canary-source')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,v):
 p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,indent=2)+'\n')
def rel(p): return p.relative_to(R).as_posix()
def main():
 OUT.mkdir(parents=True,exist_ok=True);DOC.mkdir(parents=True,exist_ok=True)
 files=[];rows=[];coverage=[]
 def copy(src,dst):
  dst.parent.mkdir(parents=True,exist_ok=True)
  digest=sha(src)
  if not dst.exists() or sha(dst)!=digest: shutil.copy2(src,dst)
  assert sha(dst)==digest
  files.append(dict(source=str(src),path=rel(dst),sha256=digest,bytes=dst.stat().st_size))
 def tree(src,dst,extensions=None):
  for p in sorted(src.rglob('*')):
   if p.is_file() and (extensions is None or p.suffix.lower() in extensions):copy(p,dst/p.relative_to(src))
 def row(donor,key,p,status,**kw):
  with Image.open(p) as im:
   im.load();w,h=im.size;mode=im.mode;colors=len(set(im.getdata()))
  rows.append(dict(donor=donor,key=key,name='',kind='unclassified_object_art',status=status,sheet=rel(p),width=w,height=h,image_mode=mode,used_colors=colors,**kw))
 # Recover the entire Hyper static table, including sprites unused by exported maps.
 hyper_rom=Path('/mnt/c/Users/aadair/Downloads/tools/Donor Roms/HypEm v5.7 EN+QoL.gba')
 assert sha(hyper_rom)=='73d6faeb29bcc15e1627a6f237e99e11ddea8429ed31ec30057560ee069a546f'
 hc=ObjectSpriteCatalog(hyper_rom.read_bytes(),OUT/'hyper');hc.discover();hc.extract(range(hc.static_count+10))
 coverage.append(dict(donor='hyper',rom_sha256=sha(hyper_rom),static_count=hc.static_count,warnings=hc.warnings))
 sources=[('hyper',OUT/'hyper')]
 sources += [(d,R/'.la_work/amap/donor_preservation'/d/'object_art_candidates') for d in ['bwa','swsh','aestheticred']]
 # Mercury is no longer an active region donor; preserve its art only.
 mercury=R/'.la_work/amap/mercury_full_v11/manifest.json'
 if mercury.exists():
  info=json.loads(mercury.read_text())['rom'];rom=Path(info['path']);dest=OUT/'mercury'
  if rom.exists():
   assert sha(rom)==info['sha256'],'Mercury ROM hash mismatch'
   cat=ObjectSpriteCatalog(rom.read_bytes(),dest);cat.discover()
   ids=set(range(cat.static_count))
   for p in (mercury.parent/'maps').glob('*/map.json'):
    m=json.loads(p.read_text());ids.update(x['graphics_id'] for x in m.get('npcs',[]) if isinstance(x.get('graphics_id'),int))
   cat.extract(ids);sources.append(('mercury',dest))
   coverage.append(dict(donor='mercury',rom_sha256=info['sha256'],static_count=cat.static_count,warnings=cat.warnings,palette_caution='Most slots use fallback grayscale and remain manual review; table discovery alone does not confirm character identity.',policy='archive only; removed region remains inactive'))
  else:coverage.append(dict(donor='mercury',status='MISSING_SOURCE',expected=str(rom)))
 for donor,src in sources:
  dest=OUT/donor
  if src!=dest:tree(src/'sprites',dest/'sprites')
  count=0
  for p in sorted((dest/'sprites').glob('*/sprite.json')):
   m=json.loads(p.read_text());sheet=p.parent/'sheet.png'
   if not sheet.exists():continue
   status='ASSET_CANDIDATE' if m.get('palette_status')=='rom' and m.get('project_import_safe') else 'MANUAL_REVIEW'
   row(donor,m['key'],sheet,status,graphics_id=m['id'],frame_width=m.get('width'),frame_height=m.get('height'),frame_count=m.get('frame_count'),palette_status=m.get('palette_status'),metadata=rel(p))
   count+=1
  coverage.append(dict(donor=donor,preserved_sheets=count,source=str(src),status='PRESERVED_EXPORT',scope='all recovered static object sheets; unresolved IDs retained in source catalog'))
  for name in ['manifest.json']:
   p=src/'sprites'/name
   if p.exists() and src!=dest:copy(p,dest/'sprites'/name)
 # Exact older sheets, including artist-edited indexed art and RGBA backups.
 for folder in ['amap','amap_sheet_backups']:
  src=OLD/'graphics/object_events/pics'/folder;dest=OUT/'hyper_legacy_variants'/folder
  if not src.exists():continue
  tree(src,dest)
  for p in sorted(dest.rglob('*.png')):row('hyper_legacy_variants',folder+'/'+p.name,p,'VARIANT_REVIEW',metadata='')
 # Source-native HnS art retains its palette files and visual declarations.
 if HNS.exists():
  src=HNS/'graphics/object_events';dest=OUT/'hns/graphics/object_events'
  tree(src,dest,{'.png','.pal','.gbapal','.bin'})
  for p in sorted((dest/'pics').rglob('*.png')):row('hns',p.relative_to(dest/'pics').as_posix(),p,'SOURCE_ASSET',metadata='assets/donor_npcs/hns/visual_reference')
  refs=['include/constants/event_objects.h','src/data/object_events/object_event_graphics.h','src/data/object_events/object_event_graphics_info.h','src/data/object_events/object_event_graphics_info_pointers.h','src/data/object_events/object_event_pic_tables.h','src/data/object_events/object_event_anims.h','src/data/object_events/object_event_subsprites.h']
  for name in refs:
   p=HNS/name
   if p.exists():copy(p,OUT/'hns/visual_reference'/name)
  coverage.append(dict(donor='hns',status='PRESERVED_SOURCE',source=str(HNS),scope='object pictures, palettes and visual definitions; definitions are reference-only'))
 # GS export currently has no extracted object sheets and its original ROM is absent.
 gs=R/'.la_work/amap/gs_chronicles_full/manifest.json'
 if gs.exists():
  m=json.loads(gs.read_text());coverage.append(dict(donor='gs_chronicles',status='MISSING_SOURCE',rom=m.get('rom'),reason='Original ROM path absent; map/tileset export does not contain object sheets. No completeness claim.'))
 # Named Hyper identities: map-object linkage is reference evidence, never script ownership.
 identities={81:('Giovanni','35.4',1,'0x098046CC','0x0837A394','I am Giovanni, leader of Team Rainbow Rocket.'),96:('Cyrus','35.4',5,'0x09804A14','0x0837F561','I leave the present world to Giovanni; I shall create a universe of my own.')}
 evidence=[]
 for gid,(name,mapid,local,script,text,paraphrase) in identities.items():
  for v in rows:
   if v['donor']=='hyper' and v.get('graphics_id')==gid:v.update(name=name,kind='named_human_npc')
  evidence.append(dict(name=name,donor='hyper',graphics_id=gid,map=mapid,object_local_id=local,script_pointer_reference=script,text_pointer_reference=text,dialogue_summary=paraphrase,confidence='HIGH',evidence='ROM-linked object script, boss appearance and donor locations; dialogue inspected as reference only'))
 dump(DOC/'named_characters.json',evidence)
 artifacts=[dict(path=rel(p),sha256=sha(p),bytes=p.stat().st_size) for p in sorted(OUT.rglob('*')) if p.is_file()]
 dump(DOC/'manifest.json',dict(artifacts=artifacts,format='LA donor NPC preservation v1',linked_into_rom=False,map_placements_added=0,gameplay_imported=False,scope='Overworld object art; trainer battle portraits are a separate asset class.',coverage=coverage,assets=rows,files=files,limitations=['Dynamic graphics variables are not executed.','Palette fallbacks, unusual frame layouts and source animation ownership need review before future registration.','Names are assigned only where supported by evidence; props/creatures retained rather than silently discarded.','GS Chronicles object recovery remains pending its original ROM.','Animation and subsprite definitions/pointers are preserved as reference, not asserted runtime-ready.']))
 fields=sorted(set().union(*(v.keys() for v in rows)))
 with (DOC/'inventory.csv').open('w',newline='') as f:
  writer=csv.DictWriter(f,fields);writer.writeheader();writer.writerows(rows)
 # A local gallery works without registering graphics into Porymap or the ROM.
 cards=[]
 for v in rows:
  url='../../../'+v['sheet'];label=html.escape(v['donor']+' / '+v['key']+' '+v['name'])
  cards.append(f'<article><a href="{url}"><img loading="lazy" src="{url}"></a><p>{label}</p><small>{v["status"]}</small></article>')
 (DOC/'gallery.html').write_text('<!doctype html><meta charset="utf-8"><title>Donor NPC library</title><style>body{background:#20262b;color:white;font:14px sans-serif}main{display:flex;flex-wrap:wrap;gap:10px}article{width:260px;background:#343d44;padding:10px;overflow:auto}img{image-rendering:pixelated;max-width:240px;min-height:64px;object-fit:contain}p{overflow-wrap:anywhere}</style><h1>Donor object art library</h1><p>Staged assets only. Click a sheet for the original. Uncertain art needs review before use.</p><main>'+''.join(cards)+'</main>')
 counts=Counter(v['donor'] for v in rows);states=Counter(v['status'] for v in rows)
 report=['# Donor NPC asset library','', 'Hyper Giovanni: **gfx_081**. Hyper Cyrus: **gfx_096**. Both are preserved with original graphics metadata and palettes.','', '| Donor / source | Sheets |','|---|---:|']+[f'| {k} | {v} |' for k,v in counts.items()]
 report+=['','Sheets include NPCs, creatures, effects and props; these are not counts of unique human characters. Legacy variants are intentionally counted separately.','','## Use and validation','','Open `gallery.html` to browse, or open individual PNGs in LibreSprite. `inventory.csv` lists assets and their review status; `manifest.json` records original source paths and exact file hashes. HnS palettes and visual declarations are retained beside its art.','','These files are staged under `assets/donor_npcs`, outside the build. They do not assign runtime graphics IDs or create map events. Existing HnS Giovanni is already available as `OBJ_EVENT_GFX_HNS_GIOVANNI_HNS`; the Hyper versions remain separate.','','Source copies are hash-checked and all indexed sheets are decoded. Fallback palettes and unusual frame strides remain in manual review. Runtime animation, palette-slot and subsprite validation is required when a character is selected for use.','','## Remaining source gaps','','GS Chronicles: original ROM is missing at its recorded path, and its map export contains no sprite catalog. Recovery remains pending; no source art is invented. Mercury is archived only and is not reactivated. BW3G / Rainbow Mistralton were single-map asset experiments without complete NPC exports, so this pass makes no full donor coverage claim for them.','','## Status counts','']+[f'- {k}: {v}' for k,v in states.items()]
 (DOC/'review.md').write_text('\n'.join(report)+'\n')
 # Focused identity preview from actual extracted pixels.
 canvas=Image.new('RGB',(400,200),'#34454a');draw=ImageDraw.Draw(canvas)
 for x,gid in [(40,81),(240,96)]:
  p=OUT/'hyper/sprites'/f'gfx_{gid:03}'/'frames/frame_00.png'
  im=Image.open(p).convert('RGBA');im=im.resize((im.width*4,im.height*4),Image.Resampling.NEAREST);canvas.paste(im,(x,30),im);draw.text((x,170),identities[gid][0]+f' / {gid:03}',fill='white')
 canvas.save(DOC/'giovanni_cyrus.png')
 print(json.dumps(dict(sheets=len(rows),files=len(files),donors=counts,statuses=states,report=str(DOC/'review.md')),indent=2))
if __name__=='__main__':main()
