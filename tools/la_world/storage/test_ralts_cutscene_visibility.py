"""Check that Ralts contributes visible pixels above the dialogue window."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
from PIL import Image,ImageChops
D=R/'.la_work/petalburg-story-test/visibility';D.mkdir(parents=True,exist_ok=True)
import re
raltsid=int(re.search(r'#define LOCALID_LA_ROUTE102_RALTS (\d+)',(R/'include/constants/map_event_ids.h').read_text()).group(1))
start(0);warp(0,17,5,5)
invoke('ScriptContext_SetupScript',symbols['LegendsPetalburg_RaltsApproach']);frames(220)
obj=invoke('GetObjectEventIdByLocalIdAndMap',raltsid,17,0)
check('ralts_spawned',obj<16)
a=Image.open(shot('ralts_visible_dialogue')).convert('RGB').copy()
invoke('SetObjectInvisibility',raltsid,17,0,1);frames(2)
b=Image.open(shot('ralts_hidden_comparison')).convert('RGB').copy()
# Compare only the target's area above the message box, excluding text and actors.
area=(136,32,170,110)
diff=ImageChops.difference(a.crop(area),b.crop(area))
changed=sum(any(px) for px in diff.getdata())
check('ralts_visible_above_dialogue',changed>=15)
a.save(R/'docs/story/petalburg_rift/ralts_visible_dialogue.png')
lib.shutdown()
(R/'docs/story/petalburg_rift/visibility-validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),visible_pixel_difference=changed,rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'Ralts visibility checks;',changed,'visible pixels')
