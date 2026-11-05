"""Native rendered-width audit for Rustboro's May/Silver dialogue."""
from pathlib import Path
import json,re,tempfile,struct,subprocess
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'docs/story/rustboro_silver'
checks=[]
text_labels=set()
for file in ['data/scripts/legends_rustboro_rivals.inc','data/maps/RustboroCity/scripts.inc']:
 for label in re.findall(r'^(\w+):', (R/file).read_text(),re.M):
  if label.startswith(('LegendsRustboroRivals_Text_','RustboroCity_Text_May','RustboroCity_Text_RegisteredMay')):text_labels.add(label)
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
