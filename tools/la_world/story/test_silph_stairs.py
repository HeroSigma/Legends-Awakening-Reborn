"""Walk every Silph staircase both ways using native movement and map warps."""
from pathlib import Path
R=Path.cwd()
exec(compile((R/'tools/la_world/story/test_silph_security.py').read_text().split('start(0);')[0],'stair_helpers','exec'))
start(0)
invoke('FlagSet',c['FLAG_LA_RED_DEX_GIFTS']);invoke('VarSet',c['VAR_LA_ASHES_STATE'],4)
up={1:31,2:28,3:30,4:28,5:30,6:14,7:27,8:16,9:18,10:6}
down={2:30,3:28,4:30,5:28,6:26,7:19,8:28,9:16,10:8,11:7}
for direction,stairs in [('down',down),('up',up)]:
 for floor,x in stairs.items():
  expected=floor+(-1 if direction=='down' else 1)
  at(floor,x,3)
  check('walkable_'+direction+'_'+str(floor),invoke('MapGridGetCollisionAt',x+7,9)==0)
  check('stair_behavior_'+direction+'_'+str(floor),invoke('MapGridGetMetatileBehaviorAt',x+7,9)!=0)
  behavior=invoke('MapGridGetMetatileBehaviorAt',x+7,9)
  right=behavior in [0xEB,0xED]
  at(floor,x-1 if right else x+1,2)
  frames(40,16 if right else 32);frames(180)
  target=c['MAP_KANTOAR_1_'+str(46+expected)+'_SILPHCO_'+str(expected)+'F']
  check('walk_'+direction+'_'+str(floor),location()==(target>>8,target&255))
  # Walk off the arrival tile: prove the player is not trapped after the warp.
  before=pos();frames(32,128);frames(10)
  check('arrival_can_leave_'+direction+'_'+str(floor),pos()!=before)
  if floor in [2,11] and direction=='down':print(shot('silph_down_stairs_'+str(floor)),flush=True)
# Saving does not lose the repaired behavior when the current floor reloads.
check('save',invoke('TrySavingData',0)==1)
check('reload',invoke('LoadGameSave',0)==1)
at(2,29,2);frames(40,16);frames(180)
check('saved_game_down_stairs',location()==(97,8))
p=R/'docs/story/silph-security/stairs-validation.json'
p.write_text(json.dumps(dict(passed=True,checks=checks,user_save_loaded=False,rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest()),indent=2)+'\n')
print('PASS',len(checks),'Silph stair checks',flush=True)
