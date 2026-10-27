"""Exercise the actual linked ARM resolver in an isolated native mGBA instance."""
from probe import *
import hashlib, tempfile
D=R/'docs/la_world/pool_framework';D.mkdir(parents=True,exist_ok=True)
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
import shutil
D=R/'docs/art/protagonists/standing_32_trial';output=D/'in_project';output.mkdir(exist_ok=True)
INFO=BASE+0x500;IMAGES=BASE+0x600;PIXELS=BASE+0x200;PAL=BASE+0x700
captures=[]
def capture(n):
 path=Path(shot('standing32_'+n));shutil.copy2(path,output/(n+'.png'));captures.append(n)
 for scale in [3]:
  Image.open(path).resize((240*scale,160*scale),Image.Resampling.NEAREST).save(output/(n+'_3x.png'))
def load_art(who):
 with tempfile.TemporaryDirectory() as td:
  raw=Path(td)/'stand.4bpp';subprocess.run([str(R/'tools/gbagfx/gbagfx'),str(D/(who+'_standing_32.png')),str(raw),'-mwidth','4','-mheight','4'],check=True)
  data=raw.read_bytes();assert len(data)==512
  for i,v in enumerate(data):wr(PIXELS+i,v,1)
 im=Image.open(D/(who+'_standing_32.png'));pal=im.getpalette()
 for i in range(16):
  red,green,blue=pal[i*3:i*3+3];wr(PAL+i*2,(red>>3)|((green>>3)<<5)|((blue>>3)<<10),2)
def show_trial(gender,who):
 o=next(symbols['gObjectEvents']+i*36 for i in range(16) if rd(symbols['gObjectEvents']+i*36,1)&1 and rd(symbols['gObjectEvents']+i*36+8,1)==255)
 source=symbols['gObjectEventGraphicsInfo_'+('Brendan' if gender==0 else 'May')+'Normal']
 load_art(who)
 for i in range(36):wr(INFO+i,rd(source+i,1),1)
 wr(INFO+6,512,2);wr(INFO+8,32,2);wr(INFO+10,32,2)
 wr(INFO+16,symbols['gObjectEventBaseOam_32x32']);wr(INFO+20,symbols['sOamTables_32x32']);wr(INFO+28,IMAGES)
 for i in range(18):
  wr(IMAGES+i*8,PIXELS);wr(IMAGES+i*8+4,512,2);wr(IMAGES+i*8+6,0,2)
 invoke('ObjectEventSetGraphics',o,INFO)
 invoke('ObjectEventTurn',o,1)
 sprite=symbols['gSprites']+rd(o+0x23,1)*68
 palette=(rd(sprite+4,2)>>12)&15
 invoke('LoadPalette',PAL,256+palette*16,32)
 frames(20)
 assert rd(INFO+8,2)==32 and rd(sprite+12)==IMAGES
for gender,who in [(0,'aren'),(1,'aria')]:
 assert lib.boot(str(R/'pokeemerald.gba').encode());frames(600)
 p=rd(symbols['gSaveBlock2Ptr'])
 for i,v in enumerate([0xbb,0xcc,0xbf,0xc8,0xff,0,0,0]):wr(p+i,v,1)
 wr(p+8,gender,1);wr(symbols['gMain']+4,symbols['CB2_NewGame']|1);frames(240)
 for i in range(6000):
  if rd(rd(symbols['gSaveBlock1Ptr'])+0x139c+0x92*2,2)==11:break
  frames(1,1 if i%15==0 else 0)
 frames(120);capture(who+'_bedroom_current')
 show_trial(gender,who);capture(who+'_bedroom_trial')
 # Show the same static down-facing draft in the existing canonical outdoor map.
 wr(rd(symbols['gSaveBlock1Ptr'])+0x139c+0x92*2,7,2)
 warp(0,10,14,13);frames(90);capture(who+'_oldale_current')
 show_trial(gender,who);capture(who+'_oldale_trial')
 lib.shutdown()
(output/'preview_validation.json').write_text(json.dumps(dict(rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),method='RAM-only 32x32 graphics override in isolated native mGBA; one down-facing static draft, no ROM or save writes',captures=captures),indent=2)+'\n')
print('Captured actual in-project static sprite trials for both characters')
