"""Native indexed-pixel authoring trial; never writes playable assets."""
from pathlib import Path
from PIL import Image
R=Path(__file__).resolve().parents[4]
D=Path(__file__).parent
# Shared color roles: transparency, skin x3, warm outline, hair x3,
# dark outline, white shadow, green x2, clothing x2, pale highlight, black.
PALETTES={
'aren':[(115,197,164),(255,213,180),(247,180,139),(206,132,99),(105,65,59),(91,94,112),(54,57,76),(31,35,48),(24,28,38),(192,204,209),(105,205,105),(39,128,70),(46,57,65),(73,86,91),(244,247,239),(13,20,25)],
'aria':[(115,197,164),(255,222,205),(232,172,148),(201,130,112),(106,65,59),(141,104,83),(98,69,60),(63,45,44),(31,27,32),(199,207,208),(105,205,105),(39,128,70),(42,53,60),(72,85,83),(245,236,211),(13,20,25)]}
HAIR={
'aren':[
['0000000700000000','0007007760700000','0076777777607000','0007677ee7676000','007677eee7777600','076677ee97777670','007777ee77777700','0007779777777000'],
['0000000700000000','0007007760700000','0076777777607000','0007677ee7676000','007677eee7777600','0766777e97777670','0077777777777700','0007777777777000'],
['0000000070000000','0000700776700000','0007677777607000','007677ee77777600','07677eee77777760','0077ee9777777770','0077e97777777700','0007777777777000']],
'aria':[
['0000007777700000','0000776666670000','0007666655667000','0076666556666700','076666e66666ab70','07666ee766667b70','0776ee7776676770','0777e77777776770'],
['0000007777700000','0000776666670000','0007666655667000','0076666556666700','07ab6666666e6670','07b66666666ee670','077666666666e770','0777666666667770'],
['0000007777700000','0000776666670000','0007666655667000','00766665566ab670','07666e666667b670','0766ee7666666670','077ee77766666770','077e777766666770']]}
# Native frame order and bobbing reference taken directly from playable sheets.
DIRECTION=[0,1,2,0,0,1,1,2,2]
for who,base in [('aren','brendan'),('aria','may')]:
 src=Image.open(R/'graphics/object_events/pics/people'/base/'walking.png')
 out=Image.new('P',(144,32),0);pal=PALETTES[who]
 out.putpalette([v for c in pal for v in c]+[0]*720)
 for frame,direction in enumerate(DIRECTION):
  native=src.crop((frame*16,0,frame*16+16,32));fr=Image.new('P',(16,32),0)
  mapping=({0:0,1:1,2:2,3:3,4:4,5:6,6:7,7:8,8:7,9:9,10:10,11:11,12:10,13:11,14:14,15:15} if who=='aren' else {0:0,1:1,2:2,3:3,4:4,5:13,6:12,7:6,8:7,9:9,10:10,11:11,12:10,13:11,14:14,15:15})
  for y in range(32):
   for x in range(16):fr.putpixel((x,y),mapping[native.getpixel((x,y))])
  # Rebuild the head at the existing pixel coordinates; no scaling involved.
  for y in range(10,18):
   for x in range(16):fr.putpixel((x,y),int(HAIR[who][direction][y-10][x],16))
  if who=='aren' and direction==1:
   # Remove the remaining native hat band below the custom hair.
   for y in range(18,21):
    for x in range(4,12):
     if fr.getpixel((x,y))!=0:fr.putpixel((x,y),7 if x in [4,11] or y==20 else 6)
  if who=='aria':
   # Hair replaces May's side locks and extends behind the jacket.
   for y in range(18,24):
    for x in ([1,2,13,14] if direction<2 else [12,13,14]):
     if fr.getpixel((x,y))==0 or x in [1,14]:fr.putpixel((x,y),7 if x in [1,14] else 6)
   if direction==1:
    for y in range(18,23):
     for x in range(4,12):fr.putpixel((x,y),6 if x<10 else 7)
    for y in range(18,22):fr.putpixel((10,y),14 if y<20 else 9)
  # Replace red uniforms with white jacket panels and green trim.
  if direction<2:
   for x,y in [(5,23),(10,23),(5,24),(10,24)]:
    if fr.getpixel((x,y))!=0:fr.putpixel((x,y),14)
   for x,y in [(6,24),(9,24),(6,25),(9,25)]:
    if fr.getpixel((x,y))!=0:fr.putpixel((x,y),9)
   for x,y in [(7,26),(8,26)]:
    if fr.getpixel((x,y))!=0:fr.putpixel((x,y),11)
  else:
   for x,y in [(6,24),(7,24),(6,25)]:
    if fr.getpixel((x,y))!=0:fr.putpixel((x,y),14)
  if who=='aren':
   # Long dark trousers instead of Brendan's shorts.
   for y in [27,28,29]:
    for x in range(16):
     if native.getpixel((x,y)) in [1,2,3,4,12,13]:fr.putpixel((x,y),12)
  out.paste(fr,(frame*16,0))
 out.info['transparency']=0;out.save(D/(who+'_walking.png'))
 out.crop((0,0,48,32)).resize((384,256),Image.Resampling.NEAREST).save(D/(who+'_idle_8x.png'))
 # Loop native left/idle/right/idle poses for south, north and west separately.
 for direction,indices in [('south',[3,0,4,0]),('north',[5,1,6,1]),('west',[7,2,8,2])]:
  frames=[out.crop((i*16,0,i*16+16,32)).resize((128,256),Image.Resampling.NEAREST) for i in indices]
  frames[0].save(D/(who+'_'+direction+'.gif'),save_all=True,append_images=frames[1:],duration=160,loop=0,transparency=0,disposal=2)
