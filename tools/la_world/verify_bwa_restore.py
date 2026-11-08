from pathlib import Path
import json,hashlib
P=Path('/home/allan/projects/Legends-Awakening-Reborn');old=P/'.la_work/unova_wesley/original';l=next(v for v in json.loads((P/'data/layouts/layouts.json').read_text())['layouts'] if v['id']=='LAYOUT_AMAP_3_0_NUVEMA_TOWN_LAYOUT');proof={}
for rel in ['data/maps/Unova_NuvemaTown/map.json',l['blockdata_filepath'],l['border_filepath']]:
 a=(P/rel).read_bytes();b=(old/rel).read_bytes();assert a==b;proof[rel]=hashlib.sha256(a).hexdigest()
out=Path('/mnt/c/Users/aadair/Downloads/Legends-Awakening-Reborn/Nuvema-BWA-restored');(out/'Restoration.json').write_text(json.dumps({'active_map':'Unova_NuvemaTown','layout':l,'restored_from':'Pre-Wesley BWA backup','verified_original_files_sha256':proof,'custom_sources_preserved':True},indent=2)+'\n');(P/'docs/la_world/unova_wesley/CURRENT-STATE.md').write_text('Nuvema has been reverted to its original BWA map and tileset pair at the user request. Wesley/user source assets and tools are archived and retained for future work. They are not the active Nuvema map. Do not rerun the recreation scripts without a new user request.\n')
