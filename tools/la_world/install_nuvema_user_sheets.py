from pathlib import Path
import json
P=Path('/home/allan/projects/Legends-Awakening-Reborn');f=P/'tools/la_world/rebuild_unova_wesley.py';s=f.read_text();marker='# Small native materials'
block='''# User-prepared source sheets: preserve assembly dimensions and existing map IDs.
user_crops=json.loads((DOC/'user_sheet_crops.json').read_text())
for key in ['grass','path_source','pool','sign','hedge','blue','lab']:
 spec=user_crops[key];sheet=Image.open(SRC/spec['sheet']).convert('RGBA')
 assets[key]=pad(sheet.crop(tuple(spec['box'])),*spec['size'],tuple(spec['offset']))
 crops[key]={'sheet':spec['sheet'],'box':spec['box'],'native_size':spec['size']}
'''
if '# User-prepared source sheets:' not in s:s=s.replace(marker,block+'\n'+marker);f.write_text(s)
print('Registered both user sheets; town assembly and map IDs preserved.')
