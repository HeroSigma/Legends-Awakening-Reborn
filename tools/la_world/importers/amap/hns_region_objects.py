"""Port HnS visual object closure without copying event or trainer logic."""
import re,struct,hashlib
from pathlib import Path
from PIL import Image
from hns_region_assets import R,S,A,c_defs,tokens,blob,palette,graphics
class ObjectPort:
 def __init__(self):
  self.ptr=(S/'src/data/object_events/object_event_graphics_info_pointers.h').read_text()
  self.info=(S/'src/data/object_events/object_event_graphics_info.h').read_text()
  self.tables=c_defs((S/'src/data/object_events/object_event_pic_tables.h').read_text())
  self.tables.update(c_defs((S/'src/data/object_events/berry_tree_graphics_tables.h').read_text()))
  self.tables.update(c_defs((S/'src/data/field_effects/field_effect_objects.h').read_text()))
  self.pics=c_defs((S/'src/data/object_events/object_event_graphics.h').read_text())
  self.pics.update(c_defs((S/'src/graphics.c').read_text()))
  self.anims=c_defs((S/'src/data/object_events/object_event_anims.h').read_text())
  self.subs=c_defs((S/'src/data/object_events/object_event_subsprites.h').read_text())
  self.palmap=dict((tag,sym) for sym,tag in re.findall(r'\{\s*(gObjectEventPal\w+)\s*,\s*(OBJ_EVENT_PAL_TAG_\w+)\s*\}',(S/'src/event_object_movement.c').read_text()))
  self.native_anims=(R/'src/data/object_events/object_event_anims.h').read_text()
  self.native_subs=(R/'src/data/object_events/object_event_subsprites.h').read_text()
  self.native_oam=(R/'src/data/object_events/base_oam.h').read_text()
  self.picture_done=set();self.info_done=set();self.mapping={};self.palettes={};self.assets=[];self.pending={};self.defines=[];self.externs=[];self.pointer_entries=[];self.graphics=[];self.picdefs=[];self.infodefs=[];self.pal_entries=[];self.aux=[];self.aux_done=set()
 def aux_symbol(self,name):
  if name in self.native_anims or name in self.native_subs or name in self.native_oam:return name
  if name in self.aux_done:return 'HnsRegion_'+name
  defs=self.anims if name in self.anims else self.subs
  assert name in defs,('unsupported graphical support',name)
  self.aux_done.add(name);text=defs[name]
  for token in tokens(text):
   if token!=name and (token in self.anims or token in self.subs):
    new=self.aux_symbol(token);text=re.sub(r'\b'+re.escape(token)+r'\b',new,text)
  text=re.sub(r'\b'+re.escape(name)+r'\b','HnsRegion_'+name,text);self.aux.append(text)
  return 'HnsRegion_'+name
 def pal(self,tag):
  assert tag in self.palmap,('missing source palette tag',tag)
  source=self.palmap[tag];assert source in self.pics,source
  path=re.search(r'"([^"]+\.gbapal)"',self.pics[source])[1]
  palpath=(S/path).with_suffix('.pal')
  if not palpath.exists():
   candidates=list((S/'graphics/object_events/palettes').glob(palpath.name));assert len(candidates)==1,(source,path);palpath=candidates[0]
  lines=palpath.read_text().splitlines();rgb=[list(map(int,line.split())) for line in lines[3:] if line.strip()]
  assert 0<len(rgb)<=16,(source,len(rgb))
  rgb += [[0,0,0]]*(16-len(rgb))
  b=b''.join(struct.pack('<H',(a>>3)|((b>>3)<<5)|((c>>3)<<10)) for a,b,c in rgb);digest=hashlib.sha256(b).hexdigest()
  if digest not in self.palettes:
   n=len(self.palettes);sym='gHnsObjectPalette_'+digest[:16];dest=A/'objects/palettes'/f'{digest[:16]}.gbapal';blob(dest,b);dest.with_suffix('.pal').write_text(palpath.read_text());native_tag=0xda00+n
   self.graphics.append(f'const u16 {sym}[] = INCBIN_U16("{dest.relative_to(R).as_posix()}");')
   self.pal_entries.append(f'    {{{sym}, 0x{native_tag:04X}}},');self.palettes[digest]=native_tag
  return self.palettes[digest]
 def picture(self,name,w,h):
  assert name in self.pics,('missing source picture',name)
  paths=re.findall(r'"([^"]+\.4bpp)"',self.pics[name]);assert paths,(name,self.pics[name])
  result=b'';frame_count=0
  for path in paths:
   im=Image.open((S/path).with_suffix('.png'));assert im.mode=='P';assert im.width%w==im.height%h==0,(name,im.size,w,h)
   for y in range(0,im.height,h):
    for x in range(0,im.width,w):
     # Each frame must be stored contiguously, not as a sheet of interleaved rows.
     frame=im.crop((x,y,x+w,y+h));px=frame.load()
     for ty in range(h//8):
      for tx in range(w//8):
       for yy in range(8):
        for xx in range(0,8,2):
         a,b=px[tx*8+xx,ty*8+yy],px[tx*8+xx+1,ty*8+yy];assert a<16 and b<16;result+=bytes([a|(b<<4)])
     frame_count+=1
  digest=hashlib.sha256(result).hexdigest();sym='gHnsObjectPicture_'+digest[:16];dest=A/'objects/pictures'/f'{digest[:16]}.4bpp'
  if digest not in self.picture_done:
   self.picture_done.add(digest)
   blob(dest,result);self.graphics.append(f'const u32 {sym}[] = INCBIN_U32("{dest.relative_to(R).as_posix()}");')
   # Original indexed PNG is useful for Porymap and visual review.
   (A/'objects/pictures').mkdir(parents=True,exist_ok=True);Image.open((S/paths[0]).with_suffix('.png')).save(dest.with_suffix('.png'))
  return sym,frame_count,str(dest.relative_to(R)),digest
 def gfx(self,source):
  if source in self.mapping:return self.mapping[source]
  shiny=re.fullmatch(r'OBJ_EVENT_MON\s*\+\s*SPECIES_(\w+)\s*\+\s*OBJ_EVENT_MON_SHINY',source)
  if shiny:
   result='OBJ_EVENT_GFX_SPECIES_SHINY('+shiny[1]+')';self.mapping[source]=result;return result
  mon=re.fullmatch(r'OBJ_EVENT_GFX_MON_BASE\s*\+\s*SPECIES_(\w+)',source)
  if mon:
   result='OBJ_EVENT_GFX_SPECIES('+mon[1]+')';self.mapping[source]=result;return result
  match=re.search(r'\[\s*'+re.escape(source)+r'\s*\]\s*=\s*&(\w+)',self.ptr)
  assert match,('missing source graphics identity',source)
  name=match[1];match=re.search(r'const struct ObjectEventGraphicsInfo\s+'+name+r'\s*=\s*\{(.*?)\};',self.info,re.S);assert match,name
  body=match[1]
  fields=['tileTag','paletteTag','reflectionPaletteTag','size','width','height','paletteSlot','shadowSize','inanimate','compressed','tracks','oam','subspriteTables','anims','images','affineAnims']
  if '.tileTag' in body:
   values={k:v.strip() for k,v in re.findall(r'\.(\w+)\s*=\s*([^,]+)',body)}
  else:
   parts=[v.strip() for v in body.split(',') if v.strip()];assert len(parts)==len(fields),(name,len(parts),parts);values=dict(zip(fields,parts))
  w,h=int(values['width'],0),int(values['height'],0);table=values['images'];assert table in self.tables,(name,table)
  text=self.tables[table];images=set(re.findall(r'(?:overworld_frame|overworld_ascending_frames|obj_frame_tiles)\(\s*(\w+)',text));assert images,(name,table,text)
  frame_metadata=[];renamed=table+'HnsRegion'
  for image in images:
   # Standard pic tables explicitly record source frame dimensions.
   spec=re.search(r'(?:overworld_frame|overworld_ascending_frames)\(\s*'+image+r'\s*,\s*(\d+)\s*,\s*(\d+)',text)
   fw,fh=(int(spec[1])*8,int(spec[2])*8) if spec else (w,h)
   pic,count,path,digest=self.picture(image,fw,fh);text=re.sub(r'\b'+image+r'\b',pic,text);frame_metadata.append(dict(source=image,frames=count,path=path,sha256=digest))
  text=re.sub(r'\b'+re.escape(table)+r'\b',renamed,text)
  if renamed not in self.pending:self.picdefs.append(text);self.pending[renamed]=True
  palette_tag=self.pal(values['paletteTag']);values['tileTag']='TAG_NONE';values['paletteTag']=hex(palette_tag);values['reflectionPaletteTag']='OBJ_EVENT_PAL_TAG_NONE';values['images']=renamed
  for field in ['subspriteTables','anims','oam']:
   symbol=values[field].lstrip('&')
   if symbol not in ['NULL','gDummySpriteAffineAnimTable']:
    actual=self.aux_symbol(symbol);values[field]=('&' if values[field].startswith('&') else '')+actual
  info='gHnsRegionInfo_'+name
  if info not in self.info_done:self.infodefs.append('const struct ObjectEventGraphicsInfo '+info+' = {\n'+''.join(f' .{k}={v},\n' for k,v in values.items())+'};')
  self.info_done.add(info)
  identifier='OBJ_EVENT_GFX_HNS_'+re.sub(r'^OBJ_EVENT_GFX_','',source);number=0x3000+len(self.assets);assert number<0x3800
  self.defines.append(f'#define {identifier} 0x{number:04X}')
  self.externs.append(f'extern const struct ObjectEventGraphicsInfo {info};')
  self.pointer_entries.append(f'    [{identifier}] = &{info},')
  self.assets.append(dict(source=source,identifier=identifier,number=number,info=info,width=w,height=h,palette_tag=palette_tag,picture_data=frame_metadata))
  self.mapping[source]=identifier;return identifier
 def output(self):
  constants='#ifndef GUARD_HNS_OBJECT_GRAPHICS_H\n#define GUARD_HNS_OBJECT_GRAPHICS_H\n#define OBJ_EVENT_GFX_HNS_BASE 0x3000\n#define OBJ_EVENT_GFX_HNS_END '+hex(0x3000+len(self.assets))+'\n'+'\n'.join(self.defines)+'\n#endif\n'
  return dict(constants=constants,graphics='\n'.join(self.graphics)+'\n',picdefs='\n'.join(self.picdefs)+'\n',infos='\n'.join(self.aux+self.infodefs)+'\n',externs='\n'.join(self.externs)+'\n',pointers='\n'.join(self.pointer_entries)+'\n',palettes='\n'.join(self.pal_entries)+'\n')
