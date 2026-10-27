from pathlib import Path
P=Path('/home/allan/projects/Legends-Awakening-Reborn');f=P/'tools/la_world/build_nuvema_exact.py';s=f.read_text();needle="body=s[s.index('pack=Pack();'):s.index('# Archive the existing map')]";replacement=needle+'''
start=body.index('for mask in states:');end=body.index("prefabs['ForestInterior']")
body=body[:start]+"""for mask in states:
 sx=0 if not mask&8 else 32 if not mask&2 else 16
 sy=0 if not mask&1 else 32 if not mask&4 else 16
 im=assets['path_source'].crop((sx,sy,sx+16,sy+16))
 # Native 16px corners retain the complete source curve, without recombining
 # disconnected 8px samples or drawing new feathered rims.
 PATH[mask]=pack.single(im,f'Path_{mask:02X}',[2])
"""+body[end:]
''';assert needle in s;s=s.replace(needle,replacement);f.write_text(s)
