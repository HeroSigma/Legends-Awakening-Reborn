"""Native mGBA chapter tests. All saves are disposable; no player battery is opened."""
from pathlib import Path
import hashlib,json,subprocess,shutil,re
exec(compile(Path(__file__).with_name('test_legends_bedroom.py').read_text().split('for gender in [0,1]:')[0],'bedroom_helpers','exec'))
# Saving relocates EWRAM save blocks; keep the isolated call helper in unused IWRAM.
exec(compile(Path(__file__).with_name('test_protagonist_assets.py').read_text().split("D=R/'docs/art/protagonists/trainer_draft'")[0].replace('BASE=0x0203f000','BASE=0x03007000'),'arm_helpers','exec'))
D=R/'docs/story/route102_timeless_call';(D/'screenshots').mkdir(parents=True,exist_ok=True)
_event_ids=(R/'include/constants/map_event_ids.h').read_text()
def route_id(name):return int(re.search(r'#define LOCALID_LA_ROUTE103_'+name+r'\s+(\d+)',_event_ids)[1])
R_RED,R_PIKA,R_BRENDAN,R_MAY=[route_id(n) for n in ['RED','PIKACHU','BRENDAN','MAY']]
checks=[]
def check(n,v):
 checks.append(dict(test=n,passed=bool(v)))
 assert v,(n,location(),pos(),var(0x4083),var(0x4084))
def capture(n):shutil.copy2(shot('littleroot_arc_'+n),D/'screenshots'/(n+'.png'))
def var(n,value=None):
 a=rd(symbols['gSaveBlock1Ptr'])+0x139c+(n-0x4000)*2
 if value is not None:wr(a,value,2)
 return rd(a,2)
def setflag(n,on=True):
 a=rd(symbols['gSaveBlock1Ptr'])+0x1270+n//8
 wr(a,rd(a,1)|(1<<(n%8)) if on else rd(a,1)&~(1<<(n%8)),1)
def actors():
 return {rd(symbols['gObjectEvents']+i*36+8,1):rd(symbols['gObjectEvents']+i*36+4,2) for i in range(16) if rd(symbols['gObjectEvents']+i*36,1)&1}
def itemcount(item):
 key=rd(rd(symbols['gSaveBlock2Ptr'])+0xac,2);total=0
 for pocket in range(5):
  a=symbols['gBagPockets']+pocket*8;ptr=rd(a);cap=rd(a+4,1)
  total+=sum(rd(ptr+i*4+2,2)^key for i in range(cap) if rd(ptr+i*4,2)==item)
 return total
def money():return rd(rd(symbols['gSaveBlock1Ptr'])+0x490)^rd(rd(symbols['gSaveBlock2Ptr'])+0xac)
def advance_arc(target,suffix,limit=22000):
 loss=False;lab_battle=False;multi=False;names=set();snap=set()
 for i in range(limit):
  phase=var(0x4083)
  if rd(symbols['gMain']+4)==symbols['BattleMainCB2']|1:
   if flag(0x37):
    lab_battle=True
    if 'lab' not in snap:
     frames(220);capture('lab_battle_'+suffix);snap.add('lab')
     check('lab_normal_trainer_not_birch_tutorial_'+suffix,not (rd(symbols['gBattleTypeFlags'])&16))
     check('red_uses_riolu_level_10_'+suffix,rd(symbols['gBattleMons']+140,2)==447 and rd(symbols['gParties']+600+84,1)==10)
   if flag(0x38):
    multi=True
    if 'multi' not in snap:
     frames(220);capture('double_battle_'+suffix);snap.add('multi')
     required=(1<<0)|(1<<6)|(1<<15)|(1<<22)
     check('true_four_trainer_battle_'+suffix,(rd(symbols['gBattleTypeFlags'])&required)==required and rd(symbols['gBattlersCount'],1)==4)
     check('red_is_battle_partner_'+suffix,rd(symbols['gPartnerTrainerId'],2)==866)
     check('red_battles_with_riolu_not_pikachu_'+suffix,rd(symbols['gBattleMons']+280,2)==447)
  if flag(0x37) and rd(symbols['gBattleOutcome'],1)==2:loss=True
  for key in ['BirchRecognizes','PortalArrival','PlayerIntroduction','KeepStarter','RioluGift','RedCongratulates','BrendanRecognizes','NationalDexGift','DexNavGift','ElaraThought']:
   label=symbols['LegendsArc_Text_'+key]
   if key not in names and all(rd(symbols['gStringVar4']+k,1)==rd(label+k,1) for k in range(10)):
    names.add(key);frames(120);capture(key+'_'+suffix)
    def actor(local):
     return next(symbols['gObjectEvents']+j*36 for j in range(16) if rd(symbols['gObjectEvents']+j*36,1)&1 and rd(symbols['gObjectEvents']+j*36+8,1)==local)
    if key in ['BirchRecognizes','PortalArrival','RioluGift','KeepStarter','NationalDexGift','DexNavGift']:
     facing=3 if key in ['BirchRecognizes','PortalArrival','RioluGift'] else 1
     check('birch_faces_speaker_'+key+'_'+suffix,rd(actor(2)+24,1)&15==facing)
    if key=='BirchRecognizes':
     check('red_faces_birch_at_opening_'+suffix,rd(actor(7)+24,1)&15==4)
    if key=='PortalArrival':
     red=actor(7)
     check('red_stays_with_pikachu_for_birch_'+suffix,(rd(red+16,2)-7,rd(red+18,2)-7)==(5,4) and rd(red+24,1)&15==4)
    if key=='PlayerIntroduction':
     red=actor(7);pika=actor(8)
     check('lab_red_approached_'+key+'_'+suffix,(rd(red+16,2)-7,rd(red+18,2)-7)==(5,5))
     check('lab_red_faces_player_'+key+'_'+suffix,rd(red+24,1)&15==4)
     check('lab_pikachu_faces_conversation_'+key+'_'+suffix,rd(pika+24,1)&15==4)
    if key=='BrendanRecognizes':
     check('route_player_walks_to_brendan_'+suffix,pos()==(10,4))
     red=actor(R_RED);pika=actor(R_PIKA)
     check('route_red_in_front_of_may_'+suffix,(rd(red+16,2)-7,rd(red+18,2)-7)==(11,4) and rd(red+24,1)&15==2)
     check('route_pikachu_at_right_facing_group_'+suffix,(rd(pika+16,2)-7,rd(pika+18,2)-7)==(12,4) and rd(pika+24,1)&15==3)
  if phase==target and rd(symbols['sGlobalScriptContextStatus'],1)==2:
   frames(60);return dict(lost=loss,lab=lab_battle,multi=multi,text=sorted(names))
  active=[rd(symbols['gTasks']+j*40) for j in range(16) if rd(symbols['gTasks']+j*40+4,1)]
  key=2 if symbols['Task_HandleYesNoInput']|1 in active else 1
  frames(1,key if i%15==0 else 0)
 raise AssertionError(('arc timeout',target,suffix,var(0x4083),var(0x4084),location(),pos(),hex(rd(symbols['gMain']+4)),actors()))
def step_to_strip():
 for i in range(180):
  if pos()[1]==8:frames(4);return
  frames(1,64)
 raise AssertionError(('could not step onto strip',pos()))
ALLEN=333
STATE=0x408b
SEEN=0x39
def scene_run(suffix,limit=14000):
 pan=False;heard=False;battle=False;voice=False
 for i in range(limit):
  if rd(symbols['gMain']+4)==symbols['BattleMainCB2']|1:battle=True
  for j in range(16):
   obj=symbols['gObjectEvents']+j*36
   if rd(obj,1)&1 and rd(obj+8,1)==127 and (rd(obj+16,2)-7,rd(obj+18,2)-7)==(6,3):
    if not pan:frames(60);capture('woods_'+suffix)
    pan=True
  name=bytes(rd(rd(symbols['gSaveBlock2Ptr'])+j,1) for j in range(4))
  message=bytes(rd(symbols['gStringVar4']+j,1) for j in range(100))
  if name in message:voice=True
  if flag(SEEN) and var(STATE)==2 and rd(symbols['sGlobalScriptContextStatus'],1)==2:
   frames(30);return dict(pan=pan,battle=battle,voice=voice)
  frames(1,1 if i%20==0 else 0)
 capture('timeout_'+suffix)
 raise AssertionError(('scene timeout',suffix,location(),pos(),var(STATE),flag(SEEN),battle,rd(symbols['gBattleOutcome'],1),hex(rd(symbols['sGlobalScriptContext']+8))))
for gender in [0,1]:
 for x in [12,13,14]:
  print('CASE',gender,x,flush=True)
  start(gender);setflag(0x860);invoke('ScriptGiveMon',252,5,0)
  invoke('SetTrainerFlag',ALLEN)
  warp(0,17,x,9);frames(120)
  print('FIELD',hex(rd(symbols['gMain']+4)),pos(),flush=True)
  step_to_strip();result=scene_run(str(gender)+'_'+str(x))
  check('camera_shows_woods_'+str(gender)+'_'+str(x),result['pan'])
  check('voice_calls_player_'+str(gender)+'_'+str(x),result['voice'])
  check('not_forced_battle_'+str(gender)+'_'+str(x),not result['battle'])
  check('player_stays_on_trigger_'+str(gender)+'_'+str(x),pos()==(x,8))
  warp(0,17,x,9);frames(120);frames(8,64);frames(90)
  check('no_repeat_'+str(gender)+'_'+str(x),var(STATE)==2 and rd(symbols['sGlobalScriptContextStatus'],1)==2)
  warp(0,17,x,9);frames(120);frames(8,64);frames(90)
  check('map_reentry_no_repeat_'+str(gender)+'_'+str(x),flag(SEEN) and var(STATE)==2 and rd(symbols['sGlobalScriptContextStatus'],1)==2)
  lib.shutdown()
# No defeated-trainer prerequisite: pass beside Allen without fighting.
start(0);setflag(0x860);invoke('ScriptGiveMon',252,5,0);invoke('ClearTrainerFlag',ALLEN)
warp(0,17,12,9);frames(120);step_to_strip();result=scene_run('unbeaten_bypass')
check('unbeaten_allen_does_not_gate_scene',flag(SEEN) and not result['battle'])
lib.shutdown()
# When Allen spots the player on the strip, his native battle and dialogue come first.
start(0);setflag(0x860)
for f in range(0x867,0x86f):setflag(f)
invoke('ScriptGiveMon',493,100,0)
invoke('SetMonMoveSlot',symbols['gParties'],332,0)
for slot in [1,2,3]:invoke('SetMonMoveSlot',symbols['gParties'],0,slot)
invoke('ClearTrainerFlag',ALLEN)
warp(0,17,13,8);frames(60);tap(64);tap(1)
result=scene_run('after_allen_battle')
check('actual_youngster_battle_before_scene',result['battle'] and rd(symbols['gBattleOutcome'],1)==1)
check('scene_after_battle_at_same_tile',flag(SEEN) and pos()==(13,8) and result['pan'])
cb1=rd(symbols['gMain']);wr(symbols['gMain'],0)
try:invoke('SavePlayerParty')
except AssertionError:
 for i in range(120):
  frames(1)
  if rd(RESULT)!=0xdeadbeef:break
 assert rd(RESULT)!=0xdeadbeef, 'party-save helper timeout'
try:saved=invoke('TrySavingData',0)
except AssertionError:
 for i in range(600):
  frames(1)
  if rd(RESULT)!=0xdeadbeef:break
 saved=rd(RESULT)
check('native_save_success',saved==1)
wr(symbols['gMain'],cb1)
frames(20,15);frames(600)
for i in range(3000):
 if rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1:break
 frames(1,8 if i%120==0 else 1 if i%120==60 else 0)
frames(120)
check('saved_scene_completion_persists',flag(SEEN) and var(STATE)==2)
warp(0,17,13,9);frames(60);frames(8,64);frames(90)
check('saved_scene_does_not_replay',rd(symbols['sGlobalScriptContextStatus'],1)==2)
lib.shutdown()
(D/'runtime_validation.json').write_text(json.dumps({'checks':checks,'all_passed':all(c['passed'] for c in checks),'user_save_loaded':False},indent=2)+'\n')
print('Timeless Woods call checks:',len(checks),flush=True)
