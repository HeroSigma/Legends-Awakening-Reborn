"""Rendered text widths and story-command preservation for the completed chapter."""
from pathlib import Path
import json,re,tempfile,struct,subprocess
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'docs/story/completed-story-polish'
changes=json.loads((D/'dialogue-changes.json').read_text())
files=set(x['file'] for x in changes)
full={f'data/scripts/legends_{name}.inc' for name in ['bedroom','downstairs','nextdoor','littleroot_arc','petalburg','spoken_dialogue']}
files |= full | {'data/maps/Hoenn_Timeless_Woods/scripts.inc'}
text_labels=set(x['label'] for x in changes)
checks=[]
def check(n,v):
 checks.append(dict(test=n,passed=bool(v)));assert v,n
# Only dialogue, speaker tags and their text_labels may differ from the preceding release.
def commands(s):
 return [line.strip() for line in s.splitlines() if line.strip() and not line.lstrip().startswith(('@','.string','setspeaker ','msgbox ')) and not re.match(r'^[A-Za-z_][A-Za-z_0-9]*:',line)]
for f in sorted(files):
 before=subprocess.check_output(['git','show','4b4d20d2e3:'+f],cwd=R,text=True)
 check('story_commands_unchanged_'+f,commands(before)==commands((R/f).read_text()))
 original_messages=re.findall(r'^\s*msgbox (\w+)',before,re.M)
 messages=re.findall(r'^\s*msgbox (\w+)',(R/f).read_text(),re.M)
 new_messages={'LegendsPetalburg_Text_WallyBorrow','LegendsPetalburg_Text_NormanBall'}
 check('message_order_unchanged_'+f,original_messages==[m for m in messages if m not in new_messages])
 label=''
 for line in (R/f).read_text().splitlines():
  if re.match(r'^[A-Za-z_][A-Za-z_0-9]*:',line):label=line.split(':')[0]
  if '.string ' in line and (f in full or (f not in {'data/scripts/legends_tera.inc','data/scripts/legends_pokevial.inc'} and label.startswith(('Legends','TimelessWoods_Text_','Route102_Text_Timeless')))):text_labels.add(label)
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "text.h"\n#include "constants/characters.h"\nconst unsigned v[]={FONT_NORMAL,CHAR_W};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 font,charw=struct.unpack('<2I',(td/'c.bin').read_bytes())
start(0)
name=rd(symbols['gSaveBlock2Ptr'])
for i,v in enumerate([charw]*7+[255]):wr(name+i,v,1)
invoke('StringCopy',symbols['gStringVar1'],invoke('GetSpeciesName',invoke('GetStarterPokemon',8)))
failures=[];widths=[]
for label in sorted(text_labels):
 invoke('StringExpandPlaceholders',symbols['gStringVar4'],symbols[label])
 lines=[[]]
 for i in range(1800):
  value=rd(symbols['gStringVar4']+i,1)
  if value==255:break
  if value in [250,251,254]:lines.append([])
  else:lines[-1].append(value)
 for row,line in enumerate(lines):
  for i,value in enumerate(line+[255]):wr(0x03007400+i,value,1)
  width=invoke('GetStringWidth',font,0x03007400,0)
  widths.append(dict(label=label,row=row,width=width))
  if width>208:failures.append(dict(label=label,row=row,width=width))
  checks.append(dict(test=f'width_{label}_{row}',passed=width<=208))
lib.shutdown()
(D/'text-validation.json').write_text(json.dumps(dict(rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks,text_labels=len(text_labels),max_width=208,player_name='WWWWWWW',starter='Rockruff',failures=failures),indent=2)+'\n')
print('Widths:',len(widths),'text_labels:',len(text_labels),'failures:',json.dumps(failures),flush=True)
assert not failures
