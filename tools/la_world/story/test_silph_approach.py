"""Native Rocket sight, approach, defeat persistence and scientist exclusion."""
from pathlib import Path
R=Path.cwd()
h=(R/'tools/la_world/story/test_ashes_silph.py').read_text().split('setup(6)')[0]
h=h.replace("names=[", "names=['sizeof(struct ObjectEvent)','offsetof(struct ObjectEvent,currentCoords)',",1)
exec(compile(h,'helpers','exec'))
import json,hashlib
manifest=json.loads((R/'docs/story/past-saffron/source-manifest.json').read_text())
gr=[o for o in manifest['objects'] if o['kind']=='trainer' and 'Grunt' in o['source']]
setup(6);invoke('VarSet',c['VAR_LA_ASHES_STATE'],4)
for o in manifest['objects']:
 if o['kind']!='trainer':continue
 d=json.loads((R/'data/maps'/o['map']/'map.json').read_text());obj=next(x for x in d['object_events'] if x['script']==o['script'])
 check('sight_mode_'+o['script'],obj['trainer_type']==('TRAINER_TYPE_NORMAL' if o in gr else 'TRAINER_TYPE_NONE'))
for o in gr:
 warp(97,{10:6,11:7}.get(int(o['map'].split('_')[-1][:-1]),7+int(o['map'].split('_')[-1][:-1])),o['x'],o['y']);frames(30)
 invoke('FlagClear',o['flag']);check('fresh_'+o['script'],not invoke('LegendsAshes_GruntAlreadyDefeated',symbols[o['script']]))
 invoke('FlagSet',o['flag']);check('beaten_'+o['script'],invoke('LegendsAshes_GruntAlreadyDefeated',symbols[o['script']]))
setup(6);invoke('VarSet',c['VAR_LA_ASHES_STATE'],4)
for defeated in gr:invoke('FlagSet',defeated['flag'])
# Use the third-floor west-facing grunt: all approach tiles must be open.
o=next(o for o in gr if o['script']=='LegendsAshes_Grunt_1')
invoke('FlagClear',o['flag']);warp(97,10,22,8);frames(60)
for x in [22,23,24]:check('approach_path_'+str(x),invoke('MapGridGetCollisionAt',x+7,9+7)==0)
obj=invoke('GetObjectEventIdByLocalIdAndMap',2,10,97)
check('grunt_loaded',obj<16)
def trainerpos():
 a=symbols['gObjectEvents']+obj*c['sizeof(struct ObjectEvent)']+c['offsetof(struct ObjectEvent,currentCoords)'];return rd(a,2)-7,rd(a+2,2)-7
before=trainerpos();check('starts_outside_sight',before==(25,9))
frames(40,128);frames(80);check('normal_sight_detected',rd(symbols['gNoOfApproachingTrainers'],1)==1);print(shot('silph_grunt_approaching'),flush=True)
check('walked_to_player',trainerpos()!=before and abs(trainerpos()[0]-pos()[0])+abs(trainerpos()[1]-pos()[1])==1)
waitfor(ready,'sight_battle');check('six_enemies_after_approach',rd(symbols['gPartiesCount']+1,1)==6)
for j in range(6):wr(symbols['gParties']+600+j*100+86,0,2)
win();finish('sight_win');check('sight_victory_saved',invoke('FlagGet',o['flag']))
warp(97,10,22,9);frames(60);check('defeated_no_rechallenge',not invoke('CheckForTrainersWantingBattle'))
check('save_sight_win',invoke('TrySavingData',0)==1);check('reload_sight_win',invoke('LoadGameSave',0)==1)
warp(97,10,22,9);frames(60);check('saved_defeat_no_rechallenge',not invoke('CheckForTrainersWantingBattle'))
# Direct conversation still gives the defeated trainer's post-battle response.
run(o['script']);finish('post_battle_talk')
# A scientist in front of the player never registers as an approaching trainer.
warp(97,10,4,11);frames(60);check('scientist_does_not_approach',not invoke('CheckForTrainersWantingBattle'))
# Other maps never inherit this chapter's custom defeat policy.
at('MAP_MAUVILLE_CITY',10,10);check('other_maps_unaffected',not invoke('LegendsAshes_GruntAlreadyDefeated',symbols[o['script']]))
p=R/'docs/story/past-saffron/grunt-approach-validation.json';p.write_text(json.dumps(dict(passed=True,checks=checks,user_save_loaded=False,rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest()),indent=2)+'\n')
print('PASS',len(checks),'grunt approach checks',flush=True)
