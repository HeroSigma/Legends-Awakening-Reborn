"""Exercise native starter selection, actual loss and Red rescue; disposable saves only."""
from pathlib import Path
import json,hashlib,re,shutil
helpers=Path(__file__).with_name('test_legends_bedroom.py').read_text().split('for gender in [0,1]:')[0]
exec(compile(helpers,'bedroom_helpers','exec'))
D=R/'docs/story/birch_red_rescue';(D/'screenshots').mkdir(parents=True,exist_ok=True)
checks=[]
def capture(name):shutil.copy2(shot('red_rescue_'+name),D/'screenshots'/(name+'.png'))
def check(name,value):
 checks.append(dict(test=name,passed=bool(value)))
 assert value,(name,location(),pos())
def setflag(n,on=True):
 a=rd(symbols['gSaveBlock1Ptr'])+0x1270+n//8
 wr(a,rd(a,1)|(1<<(n%8)) if on else rd(a,1)&~(1<<(n%8)),1)
def var(n,value=None):
 a=rd(symbols['gSaveBlock1Ptr'])+0x139c+(n-0x4000)*2
 if value is not None:wr(a,value,2)
 return rd(a,2)
mon_enum=(R/'include/pokemon.h').read_text().split('enum MonData {')[1].split('};')[0]
mon_keys=re.findall(r'MON_DATA_[A-Z_0-9]+',mon_enum)
def mon(p,key):return rd(p+{'MON_DATA_LEVEL':84,'MON_DATA_HP':86,'MON_DATA_MAX_HP':88}[key],1 if key=='MON_DATA_LEVEL' else 2)
battle_mon_size=next(int(z[1],16)//4 for l in subprocess.check_output(['arm-none-eabi-nm','-S',str(R/'pokeemerald.elf')],text=True).splitlines() if len(z:=l.split())==4 and z[3]=='gBattleMons')
for gender in [0,1]:
 for starter in [0,1,2]:
  start(gender);suffix=str(gender)+'_'+str(starter)
  setflag(0x29);var(0x4050,1);var(0x4060,2)
  money_before=rd(rd(symbols['gSaveBlock1Ptr'])+0x490)^rd(rd(symbols['gSaveBlock2Ptr'])+0xac)
  warp(0,16,7,15);frames(90);tap(64);tap(1)
  for i in range(1800):
   active=[rd(symbols['gTasks']+j*40) for j in range(16) if rd(symbols['gTasks']+j*40+4,1)]
   if symbols['Task_HandleStarterChooseInput']|1 in active:break
   frames(1,1 if i%30==0 else 0)
  else:raise AssertionError(('starter menu timeout',suffix,var(0x404e)))
  if starter!=1:tap(32 if starter==0 else 16)
  tap(1)
  for i in range(3000):
   if rd(symbols['gMain']+4)==symbols['BattleMainCB2']|1:break
   frames(1,1 if i%20==0 else 0)
  else:raise AssertionError(('battle timeout',suffix))
  frames(200);capture('battle_'+suffix)
  enemy=symbols['gParties']+600
  check('iron_valiant_'+suffix,rd(symbols['gBattleMons']+battle_mon_size,2)==1399)
  check('level_100_'+suffix,mon(enemy,'MON_DATA_LEVEL')==100)
  check('starter_level_5_'+suffix,mon(symbols['gParties'],'MON_DATA_LEVEL')==5)
  saw_departure=set();saw_loss=False;saw_red=False;saw_strike=False;saw_bolt=False;last=None;entry_captured=False;clearing_captured=False
  for i in range(18000):
   if not saw_bolt and any(rd(symbols['gTasks']+j*40)==symbols['Task_RescueLightning']|1 and rd(symbols['gTasks']+j*40+4,1) and rd(symbols['gTasks']+j*40+8,2)==10 for j in range(16)):
    capture('thunderbolt_'+suffix);saw_bolt=True
   if var(0x404e)==2:
    red=next((symbols['gObjectEvents']+j*36 for j in range(16) if rd(symbols['gObjectEvents']+j*36,1)&1 and rd(symbols['gObjectEvents']+j*36+8,1)==7),None)
    if red:
     xy=(rd(red+16,2)-7,rd(red+18,2)-7)
     if xy==(11,10) and not entry_captured:capture('north_entry_'+suffix);entry_captured=True
     if xy==(9,11) and not clearing_captured:capture('clearing_'+suffix);clearing_captured=True
   for j in range(16):
    obj=symbols['gObjectEvents']+j*36
    if rd(obj,1)&1 and rd(obj+8,1) in [7,8] and rd(obj+18,2)-7>=15:
     saw_departure.add(rd(obj+8,1))
   current=(location(),var(0x404e),rd(symbols['gBattleOutcome'],1))
   if current!=last:print(suffix,i,current,hex(rd(symbols['gMain']+4)),flush=True);last=current
   if rd(symbols['gBattleOutcome'],1)==2:saw_loss=True
   if var(0x404e)==2 and not saw_strike:
    capture('rescue_'+suffix);saw_strike=True
   if not saw_red and all(rd(symbols['gStringVar4']+k,1)==rd(symbols['Route101_Text_RedIntroduces']+k,1) for k in range(16)):
    frames(180);capture('red_introduces_'+suffix);saw_red=True
    actors={rd(symbols['gObjectEvents']+j*36+8,1):(rd(symbols['gObjectEvents']+j*36+16,2)-7,rd(symbols['gObjectEvents']+j*36+18,2)-7) for j in range(16) if rd(symbols['gObjectEvents']+j*36,1)&1}
    check('northern_path_arrival_'+suffix,actors.get(7)==(6,12) and actors.get(8)==(7,12))
    pika=next(symbols['gObjectEvents']+j*36 for j in range(16) if rd(symbols['gObjectEvents']+j*36,1)&1 and rd(symbols['gObjectEvents']+j*36+8,1)==8)
    check('encounter_style_pikachu_'+suffix,rd(pika+4,2)==(16384+25))
   if var(0x404e)==3 and location()==(1,4):break
   frames(1,1 if i%15==0 else 0)
  else:raise AssertionError(('rescue timeout',suffix,var(0x404e),location(),pos()))
  frames(120)
  check('both_companions_walk_south_'+suffix,saw_departure=={7,8})
  check('actual_battle_lost_'+suffix,saw_loss)
  check('thunderbolt_effect_ran_'+suffix,saw_bolt)
  check('no_money_loss_'+suffix,(rd(rd(symbols['gSaveBlock1Ptr'])+0x490)^rd(rd(symbols['gSaveBlock2Ptr'])+0xac))==money_before)
  check('offscreen_rescue_then_red_intro_'+suffix,saw_strike and saw_red)
  check('met_red_persistent_'+suffix,flag(0x2c))
  check('battle_guard_cleared_'+suffix,not flag(0x2e))
  check('red_actors_hidden_'+suffix,flag(0x2d))
  check('native_birch_progression_'+suffix,flag(0x52) and var(0x4084)==2)
  check('starter_retained_and_healed_'+suffix,rd(symbols['gPartiesCount'],1)==1 and mon(symbols['gParties'],'MON_DATA_HP')==mon(symbols['gParties'],'MON_DATA_MAX_HP'))
  capture('lab_'+suffix)
  warp(0,16,10,19);frames(180)
  check('route_revisit_no_replay_'+suffix,var(0x404e)==3 and var(0x4060)==3 and flag(0x2c) and flag(0x2d) and not flag(0x2e))
  lib.shutdown()
(D/'runtime_validation.json').write_text(json.dumps(dict(rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks,user_save_loaded=False),indent=2)+'\n')
print('Birch / Red rescue checks:',len(checks))
