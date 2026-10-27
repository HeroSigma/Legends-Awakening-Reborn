"""Build the user's named donor NPC roster without importing donor gameplay.
Only walking/standard NPC animation contracts are bound; player avatars and
NPC bike/surf/field actions retain their existing specialized definitions.
"""
from pathlib import Path
import json,hashlib,struct,re,shutil
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parents[4]
DOC=R/'docs/art/npc_roster';OUT=R/'graphics/object_events/pics/people/la_roster'
HYPER={'Red':230,'Blue':79,'Green':231,'Brendan':0,'May':89,'Birch':64,'Silver':77,'Elio':115,'Wally':135,'Hilda':145,'Rosa':149,'Serena':150,'Lyra':151,'Kris':152,'Lucas':153,'Selene':144,'Hilbert':157,'Nate':158,'Hugh':159,'Calem':160,'Ash':161,'Alain':162,'Barry':164,'Gladion':165,'Zinnia':166,'Archie':195,'Maxie':196,'N':201,'Iris':202}
SELECTION=[(n,'hyper',v) for n,v in HYPER.items()]+[(n,'swsh',v) for n,v in {'Gloria':7,'Bede':14,'Marnie':15,'Hop':72}.items()]+[('Cheren','bwa',72)]+[('Ethan','hyper_legacy_variants',76),('Oak','aestheticred',71),('RandomPortals','swsh',91),('Juniper','bwa',71),('Cynthia','hyper',183),('HoopaRing','hyper',4)]
ALIASES={'Ethan':['OBJ_EVENT_GFX_HNS_GOLD_NORMAL_HNS'],'Oak':['OBJ_EVENT_GFX_PROF_OAK','OBJ_EVENT_GFX_HNS_PROF_OAK_HNS'],'Red':['OBJ_EVENT_GFX_RED','OBJ_EVENT_GFX_HNS_RED_NORMAL_HNS'],'Blue':['OBJ_EVENT_GFX_BLUE','OBJ_EVENT_GFX_HNS_BLUE_HNS'],'Brendan':['OBJ_EVENT_GFX_RIVAL_BRENDAN_NORMAL'],'May':['OBJ_EVENT_GFX_RIVAL_MAY_NORMAL'],'Birch':['OBJ_EVENT_GFX_PROF_BIRCH'],'Silver':['OBJ_EVENT_GFX_HNS_SILVER_HNS'],'Kris':['OBJ_EVENT_GFX_HNS_KRIS_NORMAL_HNS'],'Wally':['OBJ_EVENT_GFX_WALLY'],'Archie':['OBJ_EVENT_GFX_ARCHIE'],'Maxie':['OBJ_EVENT_GFX_MAXIE']}
def write(p,s):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s)
def replace_block(path,start,end,content):
 p=R/path;s=p.read_text();s=re.sub(re.escape(start)+r'.*?'+re.escape(end)+'\n?','',s,flags=re.S);write(p,s.rstrip()+'\n\n'+start+'\n'+content+'\n'+end+'\n')
def hoopa_animations(folder):
 """Port visual AnimCmds only; never donor scripts/callback addresses."""
 rom=Path('/mnt/c/Users/aadair/Downloads/tools/Donor Roms/HypEm v5.7 EN+QoL.gba').read_bytes()
 assert hashlib.sha256(rom).hexdigest()=='73d6faeb29bcc15e1627a6f237e99e11ddea8429ed31ec30057560ee069a546f'
 table=0x5090b0;decls=[];reference=[]
 for anim in range(20):
  ptr=struct.unpack_from('<I',rom,table+anim*4)[0];commands=[];raw=[]
  for index in range(64):
   a,b=struct.unpack_from('<HH',rom,ptr-0x08000000+index*4);raw.append([a,b])
   if a==0xffff:commands.append('    ANIMCMD_END,');break
   if a==0xfffe:commands.append(f'    ANIMCMD_JUMP({b&63}),');break
   assert a<7 and not b&0xff00,(anim,index,a,b)
   commands.append(f'    ANIMCMD_FRAME({a}, {b&63}, .hFlip = {int(bool(b&64))}, .vFlip = {int(bool(b&128))}),')
  else:raise AssertionError('unterminated visual animation')
  decls.append(f'static const union AnimCmd sLaHoopaDonorAnim{anim:02}[] = {{\n'+'\n'.join(commands)+'\n};')
  reference.append(dict(index=anim,source_pointer=f'0x{ptr:08X}',commands=raw))
 decls.append('static const union AnimCmd sLaHoopaEmerge[] = {\n'+''.join(f'    ANIMCMD_FRAME({frame}, {duration}),\n' for frame,duration in [(6,5),(5,5),(4,5),(3,5),(0,20),(1,32)])+'    ANIMCMD_END,\n};')
 decls.append('static const union AnimCmd *const sAnimTable_LaHoopaCombined[] = {\n'+''.join(f'    sLaHoopaDonorAnim{i:02},\n' for i in range(20))+'    sLaHoopaEmerge,\n};')
 write(DOC/'hoopa_visual_animations.json',json.dumps(dict(source_table='0x085090B0',donor_animations=reference,project_emergence_animation=20,project_sequence=[[6,5],[5,5],[4,5],[3,5],[0,20],[1,32]],graphics_count=1,source_frames_retained=7,gameplay_imported=False),indent=2)+'\n')
 return '\n'.join(decls)

def main():
 OUT.mkdir(parents=True,exist_ok=True);DOC.mkdir(parents=True,exist_ok=True)
 graphics=[];pictures=[];infos=[];pointers=[];externs=[];palentries=[];pals={};rows=[]
 existing=(R/'include/constants/event_objects.h').read_text()+(R/'include/constants/hns_object_graphics.h').read_text()
 for name,donor,gid in SELECTION:
  folder=R/'assets/donor_npcs'/('hyper' if name=='Ethan' else donor)/'sprites'/f'gfx_{gid:03}';m=json.loads((folder/'sprite.json').read_text());assert m['palette_status']=='rom' and (m['project_import_safe'] or (name=='HoopaRing' and m['standard_frame_stride'] and m['frame_count']==7))
  width,height=m['width'],m['height'];fw,fh=width//8,height//8;raw=(folder/'palette.gbapal').read_bytes();digest=hashlib.sha256(raw).hexdigest()
  if digest not in pals:
   index=len(pals);tag=0xDB40+index;symbol=f'gObjectEventPal_LaRoster{index:02}';palpath=R/'graphics/object_events/palettes'/f'la_roster_{index:02}.gbapal';palpath.write_bytes(raw)
   graphics.append(f'const u16 {symbol}[] = INCBIN_U16("{palpath.relative_to(R).as_posix()}");')
   palentries.append(f'    {{{symbol}, 0x{tag:04X}}},');pals[digest]=(tag,symbol)
  tag,_=pals[digest]
  colors=[tuple((((v>>sh)&31)<<3)|(((v>>sh)&31)>>2) for sh in [0,5,10]) for (v,) in struct.iter_unpack('<H',raw)]
  count=m['frame_count'];cols=3;sheet=Image.new('P',(width*cols,height*((count+cols-1)//cols)),0);sheet.putpalette(sum((list(c) for c in colors),[])+[0]*720)
  pixel_frames=[]
  for i in range(count):
   im=Image.open(folder/'frames'/f'frame_{i:02}.png').convert('RGBA')
   if name=='Ethan':
    backup=Image.open(R/'assets/donor_npcs/hyper_legacy_variants/amap/gfx_076.rgba-backup.png').convert('RGBA');columns=backup.width//width;im=backup.crop(((i%columns)*width,(i//columns)*height,(i%columns+1)*width,(i//columns+1)*height))
   assert im.size==(width,height)
   indices=[]
   for px in im.getdata():
    if px[3]==0:indices.append(0)
    else:
     matches=[j for j,c in enumerate(colors) if j and c==px[:3]];assert matches,(name,px);indices.append(matches[0])
   frame=Image.new('P',(width,height));frame.putpalette(sheet.getpalette());frame.putdata(indices);sheet.paste(frame,((i%cols)*width,(i//cols)*height));pixel_frames.append(indices)
  png=OUT/(name.lower()+'.png');sheet.save(png,bits=4,transparency=0)
  sym='LaRoster'+name;gfx='OBJ_EVENT_GFX_LA_ROSTER_'+name.upper();info='gObjectEventGraphicsInfo_'+sym
  graphics.append(f'const u32 gObjectEventPic_{sym}[] = INCGFX_U32("{png.relative_to(R).as_posix()}", ".4bpp", "-mwidth {fw} -mheight {fh}");')
  pictures.append(f'static const struct SpriteFrameImage sPicTable_{sym}[] = {{\n'+''.join(f'    overworld_frame(gObjectEventPic_{sym}, {fw}, {fh}, {i}),\n' for i in range(count))+'};')
  anim_table='sAnimTable_Standard'
  if name=='HoopaRing':pictures.append(hoopa_animations(folder));anim_table='sAnimTable_LaHoopaCombined'
  effect=name in ['HoopaRing','RandomPortals']
  infos.append(f"""const struct ObjectEventGraphicsInfo {info} = {{
 .tileTag = TAG_NONE, .paletteTag = 0x{tag:04X},
 .reflectionPaletteTag = OBJ_EVENT_PAL_TAG_NONE,
 .size = {width*height//2}, .width = {width}, .height = {height},
 .paletteSlot = 5, .shadowSize = 1, .inanimate = {"TRUE" if effect else "FALSE"},
 .compressed = FALSE, .tracks = {"TRACKS_NONE" if effect else "TRACKS_FOOT"},
 .oam = &gObjectEventBaseOam_{width}x{height},
 .subspriteTables = sOamTables_{width}x{height},
 .anims = {anim_table}, .images = sPicTable_{sym},
 .affineAnims = gDummySpriteAffineAnimTable,
}};""")
  externs.append(f'extern const struct ObjectEventGraphicsInfo {info};');pointers.append(f'    [{gfx}] = &{info},')
  aliases=[a for a in ALIASES.get(name,[]) if a in existing]
  for alias in aliases:pointers.append(f'    [{alias}] = &{info},')
  rows.append(dict(name=name,donor=donor,source_id=gid,source_sha256=hashlib.sha256((folder/'sprite.json').read_bytes()).hexdigest(),graphics_id=gfx,info_symbol=info,frames=count,width=width,height=height,palette_tag=tag,palette_sha256=digest,editor_sheet=str(png.relative_to(R)),aliases=aliases,kind="combined_hoopa_ring" if name=="HoopaRing" else "visual_effect" if effect else "npc",emergence_animation=20 if name=="HoopaRing" else None,source_variant="assets/donor_npcs/hyper_legacy_variants/amap/gfx_076.rgba-backup.png" if name=="Ethan" else None,source_variant_sha256=hashlib.sha256((R/"assets/donor_npcs/hyper_legacy_variants/amap/gfx_076.rgba-backup.png").read_bytes()).hexdigest() if name=="Ethan" else None))
 # Existing table entries are rewritten once for editor support; runtime resolves
 # these role aliases before legacy per-map Hyper visual bindings.
 p=R/'src/data/object_events/object_event_graphics_info_pointers.h';s=p.read_text()
 for row in rows:
  for alias in row['aliases']:
   s=re.sub(r'(?m)^\s*\['+re.escape(alias)+r'\]\s*=.*?\n','',s)
 p.write_text(s)
 p=R/'include/constants/event_objects.h';s=p.read_text();s=re.sub(r'(?m)^    OBJ_EVENT_GFX_LA_ROSTER_\w+,\n','',s);s=s.replace('    NUM_OBJ_EVENT_GFX,',''.join('    '+row['graphics_id']+',\n' for row in rows)+'    NUM_OBJ_EVENT_GFX,');p.write_text(s)
 for path,kind,body in [('src/data/object_events/object_event_graphics.h','GRAPHICS','\n'.join(graphics)),('src/data/object_events/object_event_pic_tables.h','PICTURES','\n'.join(pictures)),('src/data/object_events/object_event_graphics_info.h','INFO','\n'.join(infos))]:replace_block(path,'/* LA_NPC_ROSTER_'+kind+'_BEGIN */','/* LA_NPC_ROSTER_'+kind+'_END */',body)
 # Externs must precede the graphics pointer table; generated entries live inside it.
 p=R/'src/data/object_events/object_event_graphics_info_pointers.h';s=p.read_text();s=re.sub(r'/\* LA_NPC_ROSTER_EXTERNS_BEGIN \*/.*?/\* LA_NPC_ROSTER_EXTERNS_END \*/\n?','',s,flags=re.S);s=re.sub(r'/\* LA_NPC_ROSTER_POINTERS_BEGIN \*/.*?/\* LA_NPC_ROSTER_POINTERS_END \*/\n?','',s,flags=re.S)
 s='/* LA_NPC_ROSTER_EXTERNS_BEGIN */\n'+'\n'.join(externs)+'\n/* LA_NPC_ROSTER_EXTERNS_END */\n'+s
 s=s.replace('gObjectEventGraphicsInfoPointers[] = {','gObjectEventGraphicsInfoPointers[] = {\n/* LA_NPC_ROSTER_POINTERS_BEGIN */\n'+'\n'.join(pointers)+'\n/* LA_NPC_ROSTER_POINTERS_END */');p.write_text(s)
 cases=[]
 for row in rows:
  for alias in row['aliases']:cases.append(f'    case {alias}: return &{row["info_symbol"]};')
 override='/* NPC roles only: no player-avatar IDs and no donor gameplay. */\nstatic const struct ObjectEventGraphicsInfo *GetLaNpcRosterGraphics(u16 graphicsId)\n{\n    switch (graphicsId)\n    {\n'+'\n'.join(cases)+'\n    default: return NULL;\n    }\n}\n'
 write(R/'src/data/object_events/npc_roster_overrides.inc',override)
 p=R/'src/event_object_movement.c';s=p.read_text();needle='#include "data/object_events/hyper_assets.inc"';inc='#include "data/object_events/npc_roster_overrides.inc"'
 if inc not in s:s=s.replace(needle,needle+'\n'+inc)
 hook="""    /* Selected NPC roles override old map-specific visual substitutions. */
    const struct ObjectEventGraphicsInfo *rosterGraphics = GetLaNpcRosterGraphics(graphicsId);
    if (rosterGraphics != NULL)
        return rosterGraphics;

"""
 if 'rosterGraphics = GetLaNpcRosterGraphics' not in s:s=s.replace('    if (graphicsId >= OBJ_EVENT_GFX_HNS_BASE',hook+'    if (graphicsId >= OBJ_EVENT_GFX_HNS_BASE',1)
 needle='#include "data/object_events/hyper_palettes.inc"';s=re.sub(r'/\* LA_NPC_ROSTER_PALETTES_BEGIN \*/.*?/\* LA_NPC_ROSTER_PALETTES_END \*/\n?','',s,flags=re.S);s=s.replace(needle,needle+'\n/* LA_NPC_ROSTER_PALETTES_BEGIN */\n'+'\n'.join(palentries)+'\n/* LA_NPC_ROSTER_PALETTES_END */');p.write_text(s)
 write(DOC/'manifest.json',json.dumps(dict(selection_count=len(rows),npc_only=True,new_map_placements=0,gameplay_imported=False,characters=rows),indent=2)+'\n')
 # Enlarged, labelled first-frame review sheet.
 canvas=Image.new('RGB',(680,((len(rows)+5)//6)*118),'#293b42');draw=ImageDraw.Draw(canvas)
 for i,row in enumerate(rows):
  p=R/row['editor_sheet'];im=Image.open(p).convert('RGBA').crop((0,0,row['width'],row['height']));im=im.resize((row['width']*2,row['height']*2),Image.Resampling.NEAREST);x=(i%6)*113+15;y=(i//6)*118+5;canvas.paste(im,(x,y),im);draw.text((x,y+70),row['name'],fill='white');draw.text((x,y+85),f'{row["donor"]} {row["source_id"]:03}',fill='#b5cdd4')
 canvas.save(DOC/'roster.png');print('Named NPC selections registered:',len(rows),'palette banks:',len(pals))
if __name__=='__main__':main()
