from probe import *
import hashlib,shutil
D=R/'docs/story/intro_draft1';captures=D/'screenshots';captures.mkdir(exist_ok=True)
introfuncs={a|1:n for n,a in symbols.items() if n.startswith(('Task_NewGameBirchSpeech_','Task_LegendsCreator_'))}
def current():
 for i in range(16):
  a=symbols['gTasks']+i*40
  if rd(a+4,1) and rd(a) in introfuncs:return introfuncs[rd(a)],i
 return '',-1
def capture(name):
 path=shot(name);shutil.copy2(path,captures/(name+'.png'))
def until(suffix,limit=40000):
 for tick in range(limit):
  name,i=current()
  if name.endswith(suffix):return i
  frames(1,1 if tick%10==0 else 0)
 raise AssertionError((suffix,current(),hex(rd(symbols['gMain']+4))))
def naming():
 for tick in range(12000):
  name,i=current()
  if name.endswith(('SoItsPlayerName','CreateNameYesNo','ProcessNameYesNoMenu')):return
  frames(1,8 if tick%60==0 else 1 if tick%12==0 else 0)
 raise AssertionError(('naming did not return',current()))
assert lib.boot(str(R/'pokeemerald.gba').encode())
frames(600);frames(1,8);frames(180);frames(1,8);frames(180);frames(1,1);frames(180);frames(1,1);frames(180)
assert current()[0]=='Task_LegendsCreator_Update';capture('creator');state('legends_intro_baseline')
results=[]
for gender in [0,1,0]:
 custom = len(results) >= 3
 state('legends_intro_baseline',True)
 until('ThisIsAPokemon');frames(100);capture('birch_'+str(gender))
 until('ChooseGender');capture('selection_'+str(gender))
 if gender:
  frames(120);frames(1,128)
  for wait in range(400):
   frames(1)
   if current()[0].endswith('ChooseGender'):break
  capture('aria_selection')
 frames(2);frames(1,1);frames(10)
 until('WaitPressBeforeNameChoice');frames(1,1);frames(90);naming()
 if custom:
  address=rd(symbols['gSaveBlock2Ptr'])
  for index,value in enumerate(bytes([0xca,0xc6,0xbb,0xd3,0xbf,0xcc,0xd2,0xff])):wr(address+index,value,1)
 until('ProcessNameYesNoMenu');capture('name_confirmation_'+str(gender))
 if gender==1:
  # Rejection returns to selection without repeating the Creator.
  frames(1,2);frames(20);until('ChooseGender')
  results.append(dict(test='reject_name_returns_to_selection',passed=current()[0].endswith('ChooseGender')))
  # The native rejection menu starts with its first entry; select Aria again.
  frames(120);frames(1,128)
  for wait in range(400):
   frames(1)
   if current()[0].endswith('ChooseGender'):break
  capture('aria_reselected')
  frames(2);frames(1,1);frames(12);until('WaitPressBeforeNameChoice');frames(1,1);frames(90);naming();until('ProcessNameYesNoMenu')
 frames(1,1);frames(8)
 until('WaitForSpriteFadeInAndTextPrinter');frames(65);capture('recognition_'+str(gender))
 if not custom:
  frames(2);frames(1,1);frames(100);frames(2);frames(1,1);frames(100)
  capture('recognition_line_'+str(gender))
 if custom:
  expanded=bytes(rd(symbols['gStringVar4']+i,1) for i in range(700))
  results.append(dict(test='custom_seven_character_name_expands',passed=bytes([0xca,0xc6,0xbb,0xd3,0xbf,0xcc,0xd2]) in expanded))
 for i in range(1500):
  if rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1:break
  frames(5);frames(8,1);frames(5)
 else:raise AssertionError(('did not hand off',current()))
 p=rd(symbols['gSaveBlock2Ptr']);actual=rd(p+8,1);name=bytes(rd(p+i,1) for i in range(8)).hex();capture('handoff_'+str(gender))
 results.append(dict(test='complete_intro',gender=gender,actual_gender=actual,encoded_name=name,passed=actual==gender))
 print(results[-1],flush=True)
assert all(x['passed'] for x in results),results
(D/'runtime_validation.json').write_text(json.dumps(dict(rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=results),indent=2)+'\n')
lib.shutdown()
