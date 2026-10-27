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
 sub sp,#8
 ldr r4,arg4
 str r4,[sp]
 ldr r4,arg5
 str r4,[sp,#4]
 ldr r0,arg0
 ldr r1,arg1
 ldr r2,arg2
 ldr r3,arg3
 ldr r4,target
 bl call_r3
 ldr r1,result
 str r0,[r1]
 ldr r1,callback
 ldr r0,previous
 str r0,[r1]
 add sp,#8
 pop {r4}
 pop {r0}
 bx r0
call_r3:
 bx r4
.balign 4
arg0: .word 0
arg1: .word 0
arg2: .word 0
arg3: .word 0
arg4: .word 0
arg5: .word 0
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
def invoke(name,a=0,b=0,c=0,d=0,e=0,f=0):
 for i,v in enumerate(code):wr(BASE+i,v,1)
 for k,v in dict(arg0=a,arg1=b,arg2=c,arg3=d,arg4=e,arg5=f,target=symbols[name]|1,result=RESULT,callback=symbols['gMain']+4,previous=rd(symbols['gMain']+4)).items():wr(labels[k],v)
 wr(RESULT,0xdeadbeef)
 wr(symbols['gMain']+4,BASE|1)
 frames(1)
 assert rd(RESULT)!=0xdeadbeef,('native call did not return',name)
 return rd(RESULT)
D=R/'docs/art/protagonists/trainer_draft';D.mkdir(exist_ok=True)
import shutil
checks=[]
def check(n,v):
 assert v,n
 checks.append(dict(test=n,passed=True))
def capture(n):shutil.copy2(shot('full_protagonist_'+n),D/(n+'.png'))
rom=(R/'pokeemerald.gba').read_bytes()
def data_at(sym,n):
 a=symbols[sym]-0x08000000;return rom[a:a+n]
# Linked data must exactly encode the approved native sheets.
with tempfile.TemporaryDirectory() as td:
 for who,old in [('aren','Brendan'),('aria','May')]:
  for action,suffix in [('mach_bike','MachBike'),('acro_bike','AcroBike'),('surfing','Surfing'),('fishing','Fishing'),('watering','Watering'),('field_move','FieldMove'),('underwater','Underwater'),('decorating','Decorating')]:
   path=R/'graphics/object_events/pics/people'/who/(action+'.png');raw=Path(td)/(who+'_'+action+'.4bpp')
   cmd=[str(R/'tools/gbagfx/gbagfx'),str(path),str(raw)]
   if action!='decorating':cmd+=['-mwidth','4','-mheight','4']
   subprocess.run(cmd,check=True)
   expected=raw.read_bytes();check(who+'_'+action+'_linked_art',data_at('gObjectEventPic_'+old+suffix,len(expected))==expected)
for gender,name,old in [(0,'aren','Brendan'),(1,'aria','May')]:
 assert lib.boot(str(R/'pokeemerald.gba').encode());frames(600)
 p=rd(symbols['gSaveBlock2Ptr'])
 for i,v in enumerate([0xbb,0xcc,0xbf,0xc8,0xff,0,0,0]):wr(p+i,v,1)
 wr(p+8,gender,1);wr(symbols['gMain']+4,symbols['CB2_NewGame']|1);frames(240)
 for i in range(6000):
  if rd(rd(symbols['gSaveBlock1Ptr'])+0x139c+0x92*2,2)==11:break
  frames(1,1 if i%15==0 else 0)
 frames(120);capture(name+'_normal')
 o=next(symbols['gObjectEvents']+i*36 for i in range(16) if rd(symbols['gObjectEvents']+i*36,1)&1 and rd(symbols['gObjectEvents']+i*36+8,1)==255)
 normal=rd(o+4,2);table=symbols['gObjectEventGraphicsInfoPointers']
 for mode in ['Normal','MachBike','AcroBike','Surfing','Fishing','Watering','FieldMove','Underwater','Decorating']:
  info=symbols['gObjectEventGraphicsInfo_'+old+mode]
  gfx=next(i for i in range(512) if rd(table+i*4)==info)
  invoke('ObjectEventSetGraphicsId',o,gfx);frames(12)
  check(name+'_'+mode+'_runtime_graphics',rd(o+4,2)==gfx)
  check(name+'_'+mode+'_palette',rd(info+2,2)==(0x1115 if mode=='Underwater' else 0x1134+gender))
  capture(name+'_'+mode.lower())
 invoke('ObjectEventSetGraphicsId',o,normal);frames(12)
 pic=invoke('GetPlayerTrainerPic',gender,3)
 entry=symbols['gTrainerPicInfo']+pic*8;front=rd(entry);back=rd(entry+4)
 cap=name.capitalize()
 check(name+'_separate_front',rd(front)==symbols['gTrainerFrontPic_'+cap])
 check(name+'_separate_back',rd(back+4)==symbols['gTrainerBackPic_'+cap])
 check(name+'_trainer_palette',rd(front+4)==symbols['gTrainerPalette_'+cap] and rd(back+12)==symbols['gTrainerPalette_'+cap])
 # Original Emerald rival trainer fronts remain distinct from the player.
 original=symbols['gTrainerPicInfo']+(1+gender)*8
 check(name+'_native_rival_preserved',rd(rd(original))==symbols['gTrainerFrontPic_'+old])
 # Front sprite uses the same public native loader as trainer menus.
 front_sprite=invoke('CreateTrainerPicSprite',pic,1,120,64,14,0xffff)
 check(name+'_front_sprite_load',front_sprite<64)
 frames(30);capture(name+'_front_runtime')
 invoke('FreeAndDestroyTrainerPicSprite',front_sprite)
 # A disposable native wild battle exercises the trainer throw renderer.
 invoke('ScriptGiveMon',252,10,0);invoke('CreateScriptedWildMon',261,3,0)
 invoke('BattleSetup_StartWildBattle')
 for i in range(720):
  frames(1,1 if i%30==0 else 0)
  if i in [160,220,260,300,340,400]:capture(name+'_battle_'+str(i))
 print(name,'battle flags',hex(rd(symbols['gBattleTypeFlags'])),'party',rd(symbols['gPartiesCount'],1),'callback',hex(rd(symbols['gMain']+4)),flush=True)
 check(name+'_battle_controller_active',rd(symbols['gPartiesCount'],1)>0 and rd(symbols['gMain']+4)!=symbols['CB2_Overworld']|1)
 capture(name+'_battle_ready')
 lib.shutdown()
(D/'runtime_validation.json').write_text(json.dumps(dict(rom_sha256=hashlib.sha256(rom).hexdigest(),checks=checks),indent=2)+'\n')
print('Protagonist asset/runtime checks:',len(checks))
