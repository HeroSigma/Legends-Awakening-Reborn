"""Native next-door scene checks; isolated mGBA, no user save loaded."""
from pathlib import Path
import json,hashlib,shutil
prefix=Path(__file__).with_name('test_legends_bedroom.py').read_text().split('for gender in [0,1]:')[0]
exec(compile(prefix,'bedroom_test_helpers','exec'))
original_shot=shot
def shot(name):return original_shot('nextdoor_'+name)
D=R/'docs/story/nextdoor';(D/'screenshots').mkdir(exist_ok=True)
checks=[]
def setflag(n,on=True):
 a=rd(symbols['gSaveBlock1Ptr'])+0x1270+n//8
 wr(a,rd(a,1)|(1<<(n%8)) if on else rd(a,1)&~(1<<(n%8)),1)
def variable(n,value=None):
 a=rd(symbols['gSaveBlock1Ptr'])+0x139c+(n-0x4000)*2
 if value is not None:wr(a,value,2)
 return rd(a,2)
def objects():
 result={}
 for i in range(16):
  a=symbols['gObjectEvents']+i*0x24
  if rd(a,1)&1:
   result[rd(a+8,1)]=dict(gfx=rd(a+4,2),visible=not bool(rd(a+1,1)&0x20),
       x=rd(a+16,2)-7,y=rd(a+18,2)-7,facing=rd(a+24,1)&15)
 return result
for gender in [0,1]:
 for upgrade in [False,True]:
  start(gender)
  for n in [0x22,0x23,0x24,0x25,0x26,0x51]:setflag(n)
  variable(0x4092,7)
  housevar=0x4082 if gender else 0x408c
  variable(housevar,2 if upgrade else 1)
  variable(0x408d,3 if upgrade else 0)
  suffix=str(gender)+'_'+str(int(upgrade))
  warp(1,0 if gender else 2,(9 if gender else 1) if upgrade else (8 if gender else 2),6 if upgrade else 8)
  frames(120)
  actors=objects()
  check('both_rivals_visible_'+suffix,all(i in actors and actors[i]['visible'] for i in [8,9]))
  check('distinct_rival_graphics_'+suffix,actors[8]['gfx']!=actors[9]['gfx'])
  for local,who in [(8,'Brendan'),(9,'May')]:
   check('native_'+who.lower()+'_sprite_'+suffix,
         rd(symbols['gObjectEventGraphicsInfoPointers']+actors[local]['gfx']*4)==symbols['gObjectEventGraphicsInfo_Rival'+who+'Normal'])
  before=(location(),pos())
  captured=set()
  for i in range(16000):
   for who,index in [('hazel',4),('brendan',5),('may',8)]:
    if who in captured:continue
    address=symbols['LegendsNextDoor_Text_'+str(index)]
    if all(rd(symbols['gStringVar4']+k,1)==rd(address+k,1) for k in range(12)):
     frames(360);capture(who+'_'+suffix);captured.add(who)
     if who=='hazel':
      hz=objects()[4];px,py=pos()
      dx,dy=px-hz['x'],py-hz['y']
      expected=([4 if dx>0 else 3] if abs(dx)>abs(dy) else [1 if dy>0 else 2])
      check('hazel_faces_player_'+suffix,hz['facing'] in expected)
     if who=='brendan' and not upgrade:
      current=objects()
      expected={8:(7 if gender else 3,8),9:(8 if gender else 2,7)}
      check('rivals_adjacent_to_player_'+suffix,all((current[k]['x'],current[k]['y'])==xy for k,xy in expected.items()))
      px,py=pos()
      check('both_rivals_within_one_step_'+suffix,all(abs(current[k]['x']-px)+abs(current[k]['y']-py)==1 for k in [8,9]))
   if i in [300,800,1500]:
    capture('scene_'+suffix+'_'+str(i))
   if flag(0x29) and rd(symbols['sGlobalScriptContextStatus'],1)==2:
    frames(120);break
   frames(1,1 if i%15==0 else 0)
  else:raise AssertionError(('scene timeout',suffix,objects(),variable(0x408d)))
  check('all_three_named_speakers_displayed_'+suffix,len(captured)==3)
  check('scene_complete_'+suffix,flag(0x29) and variable(0x408d)==3 and variable(housevar)==2)
  check('birch_field_progression_ready_'+suffix,variable(0x4050)==1)
  actors=objects()
  check('both_ground_floor_rivals_departed_'+suffix,8 not in actors and 9 not in actors)
  check('player_position_preserved_'+suffix,(location(),pos())==before)
  capture('complete_'+suffix)
  # Save and reload the completed story state; no duplicate meeting on entry.
  save_reload(gender)
  check('meeting_persists_after_continue_'+suffix,flag(0x29) and variable(0x408d)==3)
  warp(1,1 if gender else 3,7 if gender else 1,1);frames(180)
  # Watch the resident arrive at the PC once, then verify persistence.
  for i in range(1800):
   if flag(0x2b) and rd(symbols['sGlobalScriptContextStatus'],1)==2:break
   frames(1)
  else:raise AssertionError(('PC movement timeout',suffix,objects()))
  actors=objects()
  check('resident_rival_at_pc_'+suffix,1 in actors and (actors[1]['x'],actors[1]['y'])==(0 if gender else 8,2))
  check('no_repeat_rival_introduction_'+suffix,variable(0x408d)==3)
  capture('resident_pc_'+suffix)
  save_reload(gender)
  actors=objects()
  check('pc_state_survives_save_continue_'+suffix,flag(0x2b) and 1 in actors and (actors[1]['x'],actors[1]['y'])==(0 if gender else 8,2) and rd(symbols['sGlobalScriptContextStatus'],1)==2)
  warp(1,1 if gender else 3,7 if gender else 1,1);frames(300)
  check('pc_walk_does_not_replay_'+suffix,flag(0x2b) and rd(symbols['sGlobalScriptContextStatus'],1)==2)
  warp(1,0 if gender else 2,9 if gender else 1,8);frames(180)
  check('scene_does_not_replay_'+suffix,rd(symbols['sGlobalScriptContextStatus'],1)==2)
  # Simulate native Birch rescue and confirm the temporary house actors disappear.
  setflag(0x52)
  warp(1,0 if gender else 2,9 if gender else 1,8);frames(180)
  check('temporary_rivals_removed_after_rescue_'+suffix,8 not in objects() and 9 not in objects())
  lib.shutdown()
(D/'runtime_validation.json').write_text(json.dumps(dict(rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks,user_save_loaded=False),indent=2)+'\n')
print('Next-door checks:',len(checks))
