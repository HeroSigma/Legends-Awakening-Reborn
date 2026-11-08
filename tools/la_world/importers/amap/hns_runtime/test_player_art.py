from probe import *
import shutil
D=R/'docs/art/protagonists';checks=[]
def check(n,v):
 checks.append(dict(test=n,passed=bool(v)))
 assert v,n
for gender,name in [(0,'aren'),(1,'aria')]:
 assert lib.boot(str(R/'pokeemerald.gba').encode());frames(600)
 p=rd(symbols['gSaveBlock2Ptr'])
 for i,v in enumerate([0xbb,0xcc,0xbf,0xc8,0xff,0,0,0]):wr(p+i,v,1)
 wr(p+8,gender,1);wr(symbols['gMain']+4,symbols['CB2_NewGame']|1);frames(240)
 # Let the wake scene reach the first free-control state.
 for i in range(5000):
  stage=rd(rd(symbols['gSaveBlock1Ptr'])+0x139c+0x92*2,2)
  if stage==11:break
  frames(1,1 if i%15==0 else 0)
 frames(120)
 shutil.copy2(shot('player_art_'+name),D/(name+'_bedroom.png'))
 # Print actual player palette and expected palette for visual audit.
 player=rd(symbols['gPlayerAvatar']+5,1)
 print(name,'avatar bytes',[rd(symbols['gPlayerAvatar']+i,1) for i in range(12)],flush=True)
 for i in range(16):
  o=symbols['gObjectEvents']+i*36
  if rd(o,1)&1 and rd(o+8,1)==255:
   gfx=rd(o+4,2);info=rd(symbols['gObjectEventGraphicsInfoPointers']+gfx*4)
   tag=rd(info+2,2);print('player gfx',gfx,'tag',hex(tag),flush=True)
   check(name+'_isolated_palette',tag==0x1134+gender)
   sprite=rd(o+0x23,1);print('sprite',sprite,flush=True)
   break
 else:raise AssertionError('no player object')
 for k in [16,64,32,128]:frames(16,k);frames(4)
 shutil.copy2(shot('player_art_walk_'+name),D/(name+'_walking_runtime.png'))
 lib.shutdown()
(D/'player_validation.json').write_text(json.dumps(checks,indent=2))
