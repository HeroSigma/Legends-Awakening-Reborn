from pathlib import Path
p=Path('/home/allan/projects/Legends-Awakening-Reborn');f=p/'porymap.project.cfg';s=f.read_text();s=s.replace('prefabs_filepath=\n','prefabs_filepath=data/tilesets/unova_wesley_prefabs.json\n');f.write_text(s)
f=p/'graphics/unova_wesley/source/CREDITS.md';s=f.read_text();line='\nNuvema.png and Nuvema Second.png: user-arranged native WesleyFG source sheets, supplied October 7, 2026. Green-roof structure is a gatehouse. Gatehouse and Pokemon Center are retained in the source sheet for future use; Nuvema uses the blue house and laboratory.\n'
if 'user-arranged native' not in s:f.write_text(s+line)
