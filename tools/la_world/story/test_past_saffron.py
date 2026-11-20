"""Native past-Saffron cast and battle checks. Disposable battery only."""
from pathlib import Path
R=Path.cwd()
exec(compile((R/'tools/la_world/story/test_ashes_silph.py').read_text().split('setup(6)')[0],'chapter_helpers','exec'))
import json,hashlib
manifest=json.loads((R/'docs/story/past-saffron/source-manifest.json').read_text())
setup(6)
invoke('VarSet',c['VAR_LA_ASHES_STATE'],4)
for i in range(8):invoke('FlagSet',0x290+i)
teams=[]
# Existing completed grunts retain their defeat state after relocation.
for o in manifest['objects']:
 if o['kind']!='trainer':continue
 floor=int(o['map'].split('_')[-1][:-1]);num={10:6,11:7}.get(floor,7+floor)
 warp(97,num,o['x'],o['y']+1);frames(90)
 check('floor_tile_'+o['script'],invoke('MapGridGetCollisionAt',o['x']+7,o['y']+7)==0)
 invoke('VarSet',c['VAR_LA_SILPH_OPPONENT'],o['profile'])
 t=invoke('LegendsTrainer_Get',c['TRAINER_GRUNT_UNUSED'],symbols['gTrainers']+c['TRAINER_GRUNT_UNUSED']*c['sizeof(struct Trainer)'])
 party=rd(t+c['offsetof(struct Trainer,party)'])
 teams.append(tuple(sorted(rd(party+j*c['sizeof(struct TrainerMon)']+c['offsetof(struct TrainerMon,species)'],2) for j in range(6))))
 for j in range(6):check('legal_'+o['script']+'_'+str(j),invoke('LegendsTrainer_MemberLegal',party+j*c['sizeof(struct TrainerMon)']))
 check('two_healing_items_'+o['script'],rd(t+c['offsetof(struct Trainer,items)'],2)!=0 and rd(t+c['offsetof(struct Trainer,items)']+2,2)!=0)
check('all_thirty_teams_distinct',len(set(teams))==30)
# All imported strings use actual linked font metrics.
for n in sorted(symbols):
 if not n.startswith(('LegendsPastSilph_','LegendsPastSaffron_','LegendsAshes_Grunt_')) or not n.endswith(('_Text','_Intro','_Post','_Defeat')):continue
 data=bytearray()
 for j in range(2200):
  b=rd(symbols[n]+j,1)
  if b==255:break
  data.append(b)
 for i,line in enumerate(re.split(b'[\xfe\xfb\xfa]',bytes(data))):
  if 0xfd in line:continue
  for j,b in enumerate(line+b'\xff'):wr(0x03007500+j,b,1)
  check('text_fit_'+n+'_'+str(i),invoke('GetStringWidth',1,0x03007500,0)<=208)
# Exercise ordinary Rocket and scientist battles, then their post-battle branch.
for o in [next(x for x in manifest['objects'] if x.get('profile')==1),next(x for x in manifest['objects'] if x.get('profile')==12)]:
 invoke('FlagClear',o['flag']);floor=int(o['map'].split('_')[-1][:-1]);warp(97,7+floor,o['x'],o['y']+1);frames(90)
 run(o['script']);waitfor(ready,'battle_'+o['script']);check('actual_six_'+o['script'],rd(symbols['gPartiesCount']+1,1)==6)
 win();finish('win_'+o['script']);check('defeat_saved_'+o['script'],invoke('FlagGet',o['flag']))
 run(o['script']);finish('repeat_'+o['script'])
# Hostage healing and Kirlia's interaction lead into Wally's real rescue conversation.
warp(97,16,3,16);frames(90)
run('LegendsPastSilph_F9_NPC2');finish('nurse')
run('LegendsPastSilph_Kirlia');finish('kirlia_hint');check('kirlia_leads_to_wally',f('FLAG_LA_SILPH_WALLY_FOUND'))
print(shot('past_silph_bedroom'),flush=True)
at('MAP_KANTOAR_3_10_SAFFRONCITY',33,33);finish('arrival');print(shot('past_saffron_occupation'),flush=True)
invoke('FlagSet',c['FLAG_LA_WALLY_RESCUED'])
warp(97,9,28,10);frames(90)
objects=json.loads((R/'data/maps/Kanto_SilphCo_2F/map.json').read_text())['object_events']
for i,o in enumerate(objects,1):
 warp(97,9,o['x'],o['y']+1);frames(90)
 present=invoke('GetObjectEventIdByLocalIdAndMap',i,9,97)<16
 check('cleared_cast_'+o['local_id'],present==(o['flag']=='0'))
check('save_occupation',invoke('TrySavingData',0)==1)
check('reload_occupation',invoke('LoadGameSave',0)==1)
p=R/'docs/story/past-saffron/validation.json';p.write_text(json.dumps(dict(passed=True,checks=checks,user_save_loaded=False,rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest()),indent=2)+'\n')
print('PASS',len(checks),'past-Saffron checks',flush=True)
