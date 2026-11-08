from pathlib import Path
p=Path('/home/allan/projects/Legends-Awakening-Reborn');f=p/'tools/la_world/nuvema_exact_assets.py';s=f.read_text().replace("'deck','sign']","'deck','sign','earth','pool','pinkflowers']");f.write_text(s)
