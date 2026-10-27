"""Read-only ROM experiment; all RAM edits belong to an isolated mGBA core.
No user battery save is opened and no donor code is imported into Reborn.
"""
from pathlib import Path
import sys,json,hashlib
R=Path('/home/allan/projects/Legends-Awakening-Reborn')
sys.path.insert(0,str(R/'tools/la_world/importers/amap/hns_runtime'))
helper=R/'tools/la_world/importers/amap/hns_runtime/test_protagonist_assets.py'
exec(compile(helper.read_text().split("D=R/'docs/art/protagonists/trainer_draft'")[0].replace('BASE=0x0203f000','BASE=0x03007000'),'native_call_helper','exec'))
rom=Path('/mnt/c/Users/aadair/Downloads/Quetzal English Alpha 9v1.gba')
symbols={'gMain':0x03002660,'BoxCount':0x08137f00,'StorageMode':0x08137ed4,'RichRecords':0x08137898}
assert lib.boot(str(rom).encode());frames(600)
fake=0x02030000
for i in range(0x400):wr(fake+i,0,1)
wr(0x030055c0,fake)
results=[]
for format_mode in [0,1]:
 for reduced_metadata in [0,1]:
  wr(fake+0x2bb,format_mode,1);wr(fake+0x2c6,reduced_metadata,1)
  row=dict(format_mode=format_mode,metadata_gate_byte=reduced_metadata,reported_mode=invoke('StorageMode'),rich_records=invoke('RichRecords'),boxes=invoke('BoxCount'))
  row['slots']=row['boxes']*30;results.append(row)
lib.shutdown()
out=R/'docs/la_world/quetzal_reference/alpha9v1_storage/runtime_results.json'
out.write_text(json.dumps(dict(rom_sha256=hashlib.sha256(rom.read_bytes()).hexdigest(),isolated_core=True,user_save_loaded=False,results=results),indent=2)+'\n');print(json.dumps(results,indent=2))
