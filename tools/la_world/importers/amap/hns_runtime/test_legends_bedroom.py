"""Isolated native mGBA prologue test; never opens a user battery save."""
from probe import *
import hashlib, shutil
D=R/'docs/story/bedroom_prologue'
(D/'screenshots').mkdir(exist_ok=True)
checks=[]
def check(name, passed):
 checks.append(dict(test=name,passed=bool(passed)))
 assert passed,(name,stage(),location(),pos())
def capture(name):
 shutil.copy2(shot(name),D/'screenshots'/(name+'.png'))
def stage():
 return rd(rd(symbols['gSaveBlock1Ptr'])+0x139c+0x92*2,2)
def flag(n):
 return bool(rd(rd(symbols['gSaveBlock1Ptr'])+0x1270+n//8,1)&(1<<(n%8)))
def tera_count():
 pocket=symbols['gBagPockets']+4*8
 ptr=rd(pocket);capacity=rd(pocket+4,1)
 key=rd(rd(symbols['gSaveBlock2Ptr'])+0xac,2)
 return sum(rd(ptr+i*4+2,2)^key for i in range(capacity) if rd(ptr+i*4,2)==772)
def location():
 p=rd(symbols['gSaveBlock1Ptr']);return rd(p+4,1),rd(p+5,1)
def tap(k):
 frames(2);frames(1,k);frames(8)
def move(k,n):
 frames(n*16,k);frames(8)
def advance(target=None,limit=14000):
 if target is None:frames(30)
 for i in range(limit):
  if target==7 and stage()==15:
   pointer=rd(symbols['sGlobalScriptContext']+8)
   for name in ['LegendsDownstairs_Watch','LegendsDownstairs_AfterReport']:
    # Scene snapshots are supplemental; assertions below validate completion.
    if name in symbols and symbols[name] <= pointer < symbols[name]+12:
     capture('rift_report_'+str(gender))
  if target is None and rd(symbols["sGlobalScriptContextStatus"],1)==2:
   frames(20);return
  if target is not None and stage()==target:
   frames(120);return
  active=[rd(symbols['gTasks']+j*40) for j in range(16) if rd(symbols['gTasks']+j*40+4,1)]
  if symbols['Task_SetClock_HandleConfirmInput']|1 in active:
   tap(64);tap(1)
  else:frames(1,1 if i%15==0 else 0)
 if target is not None:raise AssertionError(('stage timeout',target,stage(),location(),pos()))
def start(gender):
 assert lib.boot(str(R/'pokeemerald.gba').encode())
 frames(600)
 p=rd(symbols['gSaveBlock2Ptr'])
 name=[0xbb,0xcc,0xc3,0xbb] if gender else [0xbb,0xcc,0xbf,0xc8]
 for i,v in enumerate(name+[0xff,0,0,0]):wr(p+i,v,1)
 wr(p+8,gender,1)
 wr(symbols['gMain']+4,symbols['CB2_NewGame']|1)
 frames(240);capture('dream_'+str(gender))
 advance(11)
 check('bedroom_spawn_'+str(gender),location()==(1,3 if gender else 1))
 check('wake_and_no_exploration_supplies_'+str(gender),pos()==(6 if gender else 2,5) and rd(symbols["gPartiesCount"],1)==0)
 capture('awake_'+str(gender))
def save_reload(gender):
 expected=(stage(),location(),pos())
 tap(8);frames(90)
 tap(128);tap(128);tap(1)
 for i in range(1800):frames(1,64 if i%30==0 else 1 if i%30==5 else 0)
 capture('saved_'+str(gender))
 frames(20,15);frames(600)
 for i in range(2400):
  if rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1:break
  frames(1,8 if i%120==0 else 1 if i%120==60 else 0)
 else:raise AssertionError('continue did not return to overworld')
 frames(120)
 if (stage(),location(),pos())!=expected:print('SAVE EXPECTED',expected,'ACTUAL',(stage(),location(),pos()),flush=True)
 check('native_save_softreset_continue_'+str(gender),(stage(),location(),pos())==expected)
 capture('reloaded_'+str(gender))
for gender in [0,1]:
 start(gender)
 # Try the stairs before the PC: trigger must push back and leave map unchanged.
 move(64,3);move(32 if gender else 16,3);tap(64);tap(1);advance(limit=600)
 # Inspect the clock early: it must defer to the unread PC message.
 check('clock_cannot_skip_pc_'+str(gender),stage()==11 and not flag(0x51))
 move(32 if gender else 16,2);advance(limit=600)
 check('stairs_block_pc_'+str(gender),pos()==(1 if gender else 7,3) and stage()==11)
 capture('stairs_block_'+str(gender))
 # Walk to the PC, read the delivery notice, then verify persistence mid-intro.
 move(16 if gender else 32,7);move(64,1);tap(1);advance(12)
 check('pc_message_recorded_'+str(gender),flag(0x22))
 capture('pc_read_'+str(gender))
 save_reload(gender)
 # Reach staircase again while clock remains unset.
 move(32 if gender else 16,7);advance(limit=600)
 check('stairs_block_clock_'+str(gender),stage()==12 and location()==(1,3 if gender else 1))
 # Return to clock on row 2.
 move(16 if gender else 32,2);move(64,1);tap(1)
 # Female clock x3; male clock x5. The gate pushed us to x1/7,y3.
 advance(7)
 check('gift_complete_'+str(gender),flag(0x23) and flag(0x25) and flag(0x24))
 check('tera_orb_exactly_once_'+str(gender),tera_count()==1)
 capture('package_complete_'+str(gender))
 save_reload(gender)
 # Stair is now usable, and returning upstairs cannot replay the parcel.
 move(16 if not gender else 32,2);move(64,1);frames(180)
 check('stairs_unlocked_'+str(gender),location()==(1,2 if gender else 0))
 # The next story scene owns the first downstairs entry.
 advance(7,24000)
 check('rift_report_completed_'+str(gender),flag(0x26))
 check('tv_staging_position_'+str(gender),pos()==(6 if gender else 4,5))
 capture('rift_report_complete_'+str(gender))
 move(32 if gender else 16,1)
 check('control_restored_after_report_'+str(gender),pos()==(5,5))
 save_reload(gender)
 check('rift_report_persists_after_continue_'+str(gender),flag(0x26))
 warp(1,3 if gender else 1,3 if gender else 5,2);frames(180)
 check('no_cutscene_replay_'+str(gender),stage()==7 and flag(0x25))
 capture('returned_'+str(gender))
 check('no_duplicate_orb_after_reload_'+str(gender),tera_count()==1)
 # The ordinary bedroom PC is restored, including its normal menu.
 warp(1,3 if gender else 1,8 if gender else 0,2);tap(64);tap(1)
 for i in range(1500):
  if any(rd(symbols['gTasks']+j*40)==symbols['PlayerPCProcessMenuInput']|1 for j in range(16) if rd(symbols['gTasks']+j*40+4,1)):break
  frames(1,1 if i%15==0 else 0)
 else:raise AssertionError('normal PC menu was not restored')
 check('normal_pc_restored_'+str(gender),True)
 capture('normal_pc_'+str(gender));tap(2);frames(120)
 # Existing next-door progression must still advance after our new report.
 warp(1,0 if gender else 2,9 if gender else 1,8)
 advance(limit=12000)
 house_var=0x4082 if gender else 0x408c
 value=rd(rd(symbols['gSaveBlock1Ptr'])+0x139c+(house_var-0x4000)*2,2)
 check('native_rival_family_progression_'+str(gender),value==2 and flag(0x26))
 warp(1,1 if gender else 3,4,4);frames(120)
 value=rd(rd(symbols['gSaveBlock1Ptr'])+0x139c+0x8d*2,2)
 check('both_rivals_introduction_complete_'+str(gender),value==3 and flag(0x29))

 lib.shutdown()
(D/'runtime_validation.json').write_text(json.dumps(dict(rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print(json.dumps(checks,indent=2))
