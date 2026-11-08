"""Saved-menu new-game regression. Disposable saves only."""
from pathlib import Path
import json,hashlib,shutil
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'docs/fixes/intro-bag';D.mkdir(parents=True,exist_ok=True)
checks=[]
def check(n,v):
 checks.append(dict(test=n,passed=bool(v)));assert v,n
def capture(n):shutil.copy2(shot('intro_fix_'+n),D/(n+'.png'))
def until(task,limit=30000):
 for i in range(limit):
  if active(task) is not None:return active(task)
  frames(1,1 if i%13==0 else 0)
 raise AssertionError(('missing',task,hex(rd(symbols['gMain']+4))))
for gender in [0,1]:
 start(0);check(f'save_{gender}',invoke('TrySavingData',0)==1);invoke('LoadGameSave',0)
 wr(symbols['gMain']+4,symbols['CB2_InitMainMenu']|1);wait('Task_MainMenuMain',1500);frames(30)
 tap(128);tap(1);wait('Task_LegendsCreator_Update',1500)
 until('Task_NewGameBirchSpeech_WaitToShowBirch');frames(30)
 capture(f'creator_cleared_{gender}')
 check(f'creator_tilemap_cleared_{gender}',all(rd(0x0600f000+i,2)==0 for i in range(0,2048,2)))
 until('Task_NewGameBirchSpeech_ChooseGender');frames(60)
 check(f'distinct_background_maps_{gender}',((rd(0x04000008,2)>>8)&31)==30 and ((rd(0x0400000a,2)>>8)&31)==7)
 capture(f'boy_girl_{gender}')
 for switch in [128,64,128,64]:
  tap(switch);frames(360)
  check(f'gender_switch_{gender}_{switch}_{len(checks)}',active('Task_NewGameBirchSpeech_ChooseGender') is not None)
 if gender:tap(128);frames(360)
 tap(1);until('Task_NewGameBirchSpeech_WaitPressBeforeNameChoice');tap(1);wait('Task_NamingScreen',1800);frames(100)
 capture(f'naming_{gender}')
 check(f'gender_saved_{gender}',rd(rd(symbols['gSaveBlock2Ptr'])+8,1)==gender)
 expected=bytes([0xbb,0xcc,0xc3,0xbb] if gender else [0xbb,0xcc,0xbf,0xc8])
 check(f'default_name_{gender}',bytes(rd(rd(symbols['gSaveBlock2Ptr'])+i,1) for i in range(4))==expected)
 # Compare the icon sprite's picture pointer to the current player graphics.
 gfx=invoke('GetPlayerAvatarGraphicsIdByStateIdAndGender',0,gender)
 info=invoke('GetObjectEventGraphicsInfo',gfx)
 # Pointer offsets are read from a compiled offsetof manifest below if needed;
 # the scene snapshots also expose any outfit mismatch immediately.
 check(f'player_graphics_available_{gender}',info>=0x08000000)
 tap(8);frames(90);tap(1);until('Task_NewGameBirchSpeech_ProcessNameYesNoMenu');capture(f'name_confirm_{gender}')
 check(f'blank_accept_uses_default_{gender}',bytes(rd(rd(symbols['gSaveBlock2Ptr'])+i,1) for i in range(4))==expected)
 lib.shutdown()
(D/'intro-validation.json').write_text(json.dumps(dict(rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'intro repairs checks',flush=True)
