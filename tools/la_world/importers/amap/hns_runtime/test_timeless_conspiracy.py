"""Native, isolated-save tests for the project-owned Timeless Woods scene."""
from pathlib import Path
import json,hashlib,shutil
helpers=Path(__file__).with_name('test_timeless_call.py').read_text().split('\nfor gender in [0,1]:')[0]
exec(compile(helpers,'timeless_helpers','exec'))
D=R/'docs/story/timeless_woods_conspiracy';(D/'screenshots').mkdir(parents=True,exist_ok=True)
checks=[]
groups=json.loads((R/'data/maps/map_groups.json').read_text())
GROUP=groups['group_order'].index('gMapGroup_Hoenn_Forests');MID=groups['gMapGroup_Hoenn_Forests'].index('Hoenn_Timeless_Woods')
ENTERED,SEEN,TAKEN=0x3a,0x3b,0x3c
def actor(local):
 for i in range(16):
  p=symbols['gObjectEvents']+i*36
  if rd(p,1)&1 and rd(p+8,1)==local:return p
 return None
def axy(local):
 a=actor(local);return (rd(a+16,2)-7,rd(a+18,2)-7) if a else None
def facing(local):return rd(actor(local)+24,1)&15

def run_scene(gender):
 seen=set();maxx={1:0,2:0};camera=False
 texts=['Familiar','Voices','Discovery','Resonance','Stabilize','Plan','Secrecy','Recognition']
 for i in range(16000):
  if actor(127):camera=True
  for local in [1,2]:
   if actor(local):maxx[local]=max(maxx[local],axy(local)[0])
  message=bytes(rd(symbols['gStringVar4']+j,1) for j in range(16))
  for name in texts:
   ptr=symbols['TimelessWoods_Text_'+name]
   expected=bytes(rd(ptr+j,1) for j in range(12))
   if name not in seen and any(message[offset:offset+12]==expected for offset in range(4)):
    seen.add(name)
    if name=='Discovery':
     check('camera_at_meeting_'+str(gender),axy(127)==(24,12))
     check('giovanni_position_and_facing_'+str(gender),axy(1)==(25,12) and facing(1)==3)
     check('cyrus_position_and_facing_'+str(gender),axy(2)==(23,12) and facing(2)==4)
     check('ball_between_them_'+str(gender),axy(3)==(24,12))
     frames(240);capture('meeting_'+str(gender))
    if name=='Stabilize':
     check('giovanni_picks_up_ball_'+str(gender),not actor(3) and flag(TAKEN) and axy(1)==(24,12))
     frames(240);capture('item_taken_'+str(gender))
    if name=='Recognition':
     check('camera_removed_on_return_'+str(gender),not actor(127))
     check('villains_left_'+str(gender),not actor(1) and not actor(2))
     frames(240);capture('player_recognition_'+str(gender))
  if flag(SEEN) and not actor(127) and rd(symbols['sGlobalScriptContextStatus'],1)==2:
   check('dialogue_and_camera_completed_'+str(gender),camera and set(texts[1:]).issubset(seen))
   check('both_walked_to_right_edge_'+str(gender),maxx[1]>=33 and maxx[2]>=33)
   check('player_not_teleported_'+str(gender),pos()==(16,13))
   return
  frames(1,1 if i%20==0 else 0)
 capture('timeout_'+str(gender))
 raise AssertionError(('scene timeout',gender,seen,axy(1),axy(2),axy(127),pos(),hex(rd(symbols['sGlobalScriptContext']+8))))
for gender in [0,1]:
 print('CASE',gender,'map',GROUP,MID,flush=True)
 start(gender);setflag(0x860);invoke('ScriptGiveMon',252,5,0)
 warp(GROUP,MID,15 if gender==0 else 17,13)
 for i in range(2200):
  if flag(ENTERED) and rd(symbols['sGlobalScriptContextStatus'],1)==2:break
  frames(1,1 if i%20==0 else 0)
 else:raise AssertionError('arrival scene timeout')
 check('arrival_completed_'+str(gender),flag(ENTERED) and not flag(SEEN))
 capture('arrival_'+str(gender))
 for i in range(100):
  if pos()==(16,13):break
  frames(1,16 if gender==0 else 32)
 check('coordinate_trigger_reached_'+str(gender),pos()==(16,13))
 run_scene(gender)
 warp(GROUP,MID,15,13);frames(100)
 check('actors_stay_hidden_on_reentry_'+str(gender),not actor(1) and not actor(2) and not actor(3))
 check('arrival_does_not_repeat_'+str(gender),rd(symbols['sGlobalScriptContextStatus'],1)==2)
 frames(18,16);frames(60)
 check('meeting_does_not_repeat_'+str(gender),not actor(127) and rd(symbols['sGlobalScriptContextStatus'],1)==2)
 # Native save and soft reset, using only this runner's disposable battery.
 cb1=rd(symbols['gMain']);wr(symbols['gMain'],0)
 def safe_invoke(name,*args):
  try:return invoke(name,*args)
  except AssertionError:
   for i in range(900):
    frames(1)
    if rd(RESULT)!=0xdeadbeef:return rd(RESULT)
   raise
 safe_invoke('SavePlayerParty');saved=safe_invoke('TrySavingData',0);wr(symbols['gMain'],cb1)
 check('native_save_success_'+str(gender),saved==1)
 frames(20,15);frames(600)
 for i in range(3000):
  if rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1:break
  frames(1,8 if i%120==0 else 1 if i%120==60 else 0)
 frames(120)
 check('saved_scene_flags_persist_'+str(gender),flag(ENTERED) and flag(SEEN) and flag(TAKEN))
 check('saved_actors_stay_hidden_'+str(gender),not actor(1) and not actor(2) and not actor(3))
 lib.shutdown()
(D/'runtime_validation.json').write_text(json.dumps(dict(checks=checks,all_passed=all(x['passed'] for x in checks),user_save_loaded=False,rom_sha256=hashlib.sha256((R/"pokeemerald.gba").read_bytes()).hexdigest()),indent=2)+'\n')
print('Timeless conspiracy checks:',len(checks),flush=True)
