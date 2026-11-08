"""Native Petalburg story run: both protagonists, tutorial battle and saved progression."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'.la_work/petalburg-story-test';D.mkdir(parents=True,exist_ok=True)
proof=R/'docs/story/petalburg_rift';proof.mkdir(parents=True,exist_ok=True)
import tempfile,struct
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "constants/flags.h"\n#include "constants/vars.h"\n#include "constants/map_event_ids.h"\nconst unsigned v[]={FLAG_LA_TIMELESS_WOODS_CONSPIRACY_SEEN,FLAG_LA_REPORTED_WOODS_TO_NORMAN,FLAG_LA_NORMAN_CONTACTED_BIRCH,FLAG_LA_WALLY_RALTS_BOND,FLAG_LA_WOODS_EXIT_THOUGHT,FLAG_HIDE_PETALBURG_GYM_NORMAN,FLAG_HIDE_PETALBURG_GYM_WALLY,VAR_PETALBURG_GYM_STATE,VAR_PETALBURG_CITY_STATE,VAR_LA_PETALBURG_ARC,FLAG_LA_INTRO_ACTIVE,VAR_LITTLEROOT_INTRO_STATE,LOCALID_PETALBURG_GYM_NORMAN,VAR_FACING,DIR_NORTH};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 seen,report,relay,bond,exitflag,normanhide,wallyhide,gym,city,arc,introflag,introvar,norman,facing,north=struct.unpack('<15I',(td/'c.bin').read_bytes())
def v(n): return rd(rd(symbols["gSaveBlock1Ptr"])+0x139c+(n-0x4000)*2,2)
def f(n): return (rd(rd(symbols["gSaveBlock1Ptr"])+0x1270+n//8,1)>>(n%8))&1
def until(predicate,limit=20000):
 for i in range(limit):
  if predicate():frames(20);return
  pointer=rd(symbols['sGlobalScriptContext']+8)
  if symbols['LegendsPetalburg_RaltsApproach'] <= pointer < symbols['LegendsPetalburg_RaltsCaught'] and i%40==0:
   shutil.copy2(shot('ralts_approach'),proof/'ralts_approach.png')
  frames(1,1 if i%16==0 else 0)
 raise AssertionError(('scene timed out',location(),pos(),v(gym),v(city),hex(rd(symbols['sGlobalScriptContext']+8))))
def setup(gender,mode):
 start(gender);invoke('FlagClear',introflag);invoke('VarSet',introvar,7)
 invoke('ScriptGiveMon',4,8,0);invoke('StorageChangeMode',mode,1)
 invoke('FlagClear',normanhide);invoke('FlagSet',wallyhide)
 invoke('FlagSet',seen);invoke('VarSet',gym,0);invoke('VarSet',city,0)
def norman_talk():
 wr(symbols['gSpecialVar_LastTalked'],norman,2)
 obj=invoke('GetObjectEventIdByLocalIdAndMap',norman,1,8)
 wr(symbols['gSelectedObjectEvent'],obj,1);invoke('VarSet',facing,north)
 invoke('ScriptContext_SetupScript',symbols['PetalburgCity_Gym_EventScript_Norman'])
for gender,mode in [(0,0),(1,1)]:
 setup(gender,mode)
 # West exit is queued once, only after witnessing the Woods meeting.
 warp(0,17,6,4)
 until(lambda:f(exitflag)==1)
 check('exit_thought_'+str(gender),invoke('FlagGet',exitflag)==1)
 until(lambda:rd(symbols['sGlobalScriptContextStatus'],1)==2)
 # Validate Ralts' added approach cells against the actual imported geometry.
 warp(0,17,5,5)
 for x,y in [(5,5),(5,6),(6,5),(7,5)]:
  check('tutorial_cell_'+str((gender,x,y)),invoke('MapGridGetCollisionAt',x+7,y+7)==0)
 warp(8,1,4,108)
 before=bytes(rd(symbols['gParties']+i,1) for i in range(100))
 norman_talk()
 until(lambda:f(report)==1)
 check('report_saved_'+str(gender),invoke('VarGet',arc)==1)
 shutil.copy2(shot('norman_report'),proof/('report_'+str(gender)+'.png'))
 until(lambda:v(gym)==2 and f(relay)==1)
 until(lambda:rd(symbols['sGlobalScriptContextStatus'],1)==2)
 check('full_outing_completed_'+str(gender),location()==(8,1) and invoke('VarGet',city)==3)
 check('ralts_bond_'+str(gender),invoke('FlagGet',bond)==1)
 check('birch_contacted_'+str(gender),invoke('VarGet',arc)==3)
 check('wally_leaves_'+str(gender),invoke('FlagGet',wallyhide)==1)
 check('party_restored_'+str(gender),before==bytes(rd(symbols['gParties']+i,1) for i in range(100)))
 shutil.copy2(shot('norman_followup'),proof/('followup_'+str(gender)+'.png'))
 check('story_save_'+str(gender),invoke('TrySavingData',0)==1)
 invoke('FlagClear',report);invoke('FlagClear',relay);invoke('VarSet',arc,0)
 check('story_load_'+str(gender),invoke('LoadGameSave',0)==1)
 check('story_persisted_'+str(gender),invoke('FlagGet',relay)==1 and invoke('FlagGet',report)==1 and invoke('VarGet',arc)==3)
 warp(8,1,4,108);norman_talk();until(lambda:rd(symbols['sGlobalScriptContextStatus'],1)==2)
 check('no_tutorial_repeat_'+str(gender),invoke('VarGet',gym)==2 and invoke('VarGet',arc)==3)
 lib.shutdown()
# Leaving through another Woods gate must not trigger the western-exit thought.
setup(0,0);warp(0,17,24,3);frames(90)
check('east_gate_no_exit_thought',f(exitflag)==0)
invoke('FlagClear',seen);warp(0,17,6,4);frames(90)
check('unseen_meeting_no_exit_thought',f(exitflag)==0)
lib.shutdown()
# Existing saves that finished Wally before seeing the Woods receive a late report.
setup(0,0);invoke('VarSet',gym,2);invoke('VarSet',city,3)
warp(8,1,4,108);norman_talk();until(lambda:rd(symbols['sGlobalScriptContextStatus'],1)==2)
check('late_report_supported',invoke('FlagGet',relay)==1 and invoke('VarGet',gym)==2)
check('late_report_does_not_invent_capture',invoke('FlagGet',bond)==0)
lib.shutdown()
(R/'docs/story/petalburg_rift/validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'Petalburg story checks')
