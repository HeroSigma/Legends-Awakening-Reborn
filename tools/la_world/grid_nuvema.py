from pathlib import Path
from PIL import Image,ImageDraw
p=Path('/home/allan/projects/Legends-Awakening-Reborn');im=Image.open(p/'graphics/unova_wesley/source/Nuvema.png').convert('RGBA').resize((1024,1024),Image.Resampling.NEAREST);d=ImageDraw.Draw(im)
for v in range(0,256,16):
 d.line((v*4,0,v*4,1024),fill='red');d.line((0,v*4,1024,v*4),fill='red');d.text((v*4+1,0),str(v),fill='white');d.text((0,v*4+1),str(v),fill='white')
im.save('/mnt/c/Users/aadair/Downloads/nuvema-grid-audit.png')
