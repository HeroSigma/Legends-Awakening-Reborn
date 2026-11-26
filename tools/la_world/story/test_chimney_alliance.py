"""Native Mt Chimney gauntlet, actor staging and partner validation."""
from pathlib import Path
R=Path.cwd()
h=(R/'tools/la_world/story/test_blue_chimney.py').read_text().split('start(0);')[0]
h=h.replace("names=[", "names=['VAR_LA_CHIMNEY_GAUNTLET','VAR_LA_SILPH_OPPONENT','FLAG_LA_CHIMNEY_MAGMA_BEATEN','FLAG_LA_CHIMNEY_AQUA_BEATEN','FLAG_LA_CHIMNEY_ROCKET_BEATEN','LOCALID_LA_CHIMNEY_RED','LOCALID_LA_CHIMNEY_PIKACHU','LOCALID_LA_CHIMNEY_CHARIZARD','LOCALID_LA_CHIMNEY_SHARPEDO','LOCALID_ASHES_CHIMNEY_MAY','LOCALID_LA_CHIMNEY_MAY_PARTNER',",1)
exec(compile(h,'alliance_helpers','exec'))
def progress():return invoke('VarGet',c['VAR_LA_CHIMNEY_GAUNTLET'])
def actor(n):
 i=invoke('GetObjectEventIdByLocalIdAndMap',c[n],c['MAP_MT_CHIMNEY']&255,c['MAP_MT_CHIMNEY']>>8)
 check('present_'+n,i<16)
 a=symbols['gObjectEvents']+i*36
 return (rd(a+0x10,2)-7,rd(a+0x12,2)-7)
def battle():return rd(symbols['gMain']+4)==symbols['BattleMainCB2']|1 and rd(symbols['gBattleMainFunc'])==symbols['HandleTurnActionSelectionState']|1
start(0)
sb=rd(symbols['gSaveBlock2Ptr']);wr(sb+0x14,(rd(sb+0x14,1)&~7)|2,1)
invoke('FlagSet',c['FLAG_LA_RED_DEX_GIFTS'])
for i in range(3):invoke('FlagSet',c['FLAG_BADGE01_GET']+i)
for sp in [1,4,7,25,133,155]:invoke('ScriptGiveMon',sp,30,0)
for n in ['FLAG_LA_BLUE_CHIMNEY_BRIEFED','FLAG_LA_BLUE_CABLE_MET','FLAG_LA_BLUE_CHIMNEY_BOARDED','FLAG_LA_COZMO_BRIEFED']:invoke('FlagSet',c[n])
invoke('VarSet',c['VAR_LA_ASHES_STATE'],2)
for n in sorted(symbols):
 if not n.startswith('ChimneyAlliance_Text_'):continue
 data=bytearray()
 for i in range(2400):
  b=rd(symbols[n]+i,1)
  if b==255:break
  data.append(b)
 for i,line in enumerate(re.split(b'[\xfe\xfb\xfa]',bytes(data))):
  if 253 in line:continue
  for j,b in enumerate(line+b'\xff'):wr(0x03007500+j,b,1)
  check('fit_'+n+'_'+str(i),invoke('GetStringWidth',1,0x03007500,0)<=208)
at('MAP_MT_CHIMNEY',25,22);frames(36,128);finish('automatic_briefing')
check('phone_call_saved',progress()==1)
for n,xy in [('LOCALID_LA_BLUE_CHIMNEY',(20,20)),('LOCALID_LA_CHIMNEY_CHARIZARD',(21,20)),('LOCALID_LA_CHIMNEY_SHARPEDO',(23,20))]:check('standoff_'+n,actor(n)==xy)
frames(40,64)
for slot in [34,35,36]:
 waitfor(battle,'battle_'+str(slot))
 check('profile_'+str(slot),invoke('VarGet',c['VAR_LA_SILPH_OPPONENT'])==slot)
 wr(symbols['gBattleOutcome'],1,1);wr(symbols['gBattleMainFunc'],symbols['HandleEndTurn_BattleWon']|1)
 if slot<36:frames(180)
finish('backup_arrival')
check('gauntlet_completed',progress()==5)
for n,xy in [('LOCALID_LA_CHIMNEY_RED',(26,20)),('LOCALID_LA_CHIMNEY_PIKACHU',(27,20)),('LOCALID_ASHES_CHIMNEY_MAY',(23,21)),('LOCALID_LA_CHIMNEY_MAY_PARTNER',(24,21))]:check('arrival_'+n,actor(n)==xy)
print(shot('chimney_alliance_arrived'),flush=True)
at('MAP_MT_CHIMNEY',25,22);finish('stage5_reload')
check('no_replayed_gauntlet',progress()==5)
at('MAP_MT_CHIMNEY',13,7);tap(64);tap(1);waitfor(battle,'maxie')
wr(symbols['gBattleOutcome'],1,1);wr(symbols['gBattleMainFunc'],symbols['HandleEndTurn_BattleWon']|1)
finish('full_summit_aftermath')
check('native_completion',flag('FLAG_DEFEATED_EVIL_TEAM_MT_CHIMNEY'))
check('hoopa_continuity',flag('FLAG_LA_CHIMNEY_RESONANCE'))
for n,xy in [('LOCALID_LA_CHIMNEY_RED',(14,7)),('LOCALID_LA_CHIMNEY_PIKACHU',(15,7))]:check('summit_'+n,actor(n)==xy)
print(shot('chimney_alliance_summit'),flush=True)
# Real west stairs also align the player without crossing the ace standoff.
invoke('FlagClear',c['FLAG_DEFEATED_EVIL_TEAM_MT_CHIMNEY'])
invoke('VarSet',c['VAR_LA_CHIMNEY_GAUNTLET'],0)
for n in ['FLAG_LA_CHIMNEY_MAGMA_BEATEN','FLAG_LA_CHIMNEY_AQUA_BEATEN','FLAG_LA_CHIMNEY_ROCKET_BEATEN']:invoke('FlagClear',c[n])
at('MAP_MT_CHIMNEY',17,22);frames(36,64);finish('west_briefing')
check('west_entry_calls_backup',progress()==1 and pos()==(25,23))
# Simulate a saved first victory, then lose the second fight: the first stays won.
invoke('VarSet',c['VAR_LA_CHIMNEY_GAUNTLET'],2)
invoke('FlagSet',c['FLAG_LA_CHIMNEY_MAGMA_BEATEN'])
at('MAP_MT_CHIMNEY',18,22);frames(36,64)
waitfor(battle,'west_aqua_retry')
check('west_stairs_resumes_aqua',invoke('VarGet',c['VAR_LA_SILPH_OPPONENT'])==35)
wr(symbols['gBattleOutcome'],2,1);wr(symbols['gBattleMainFunc'],symbols['HandleEndTurn_BattleLost']|1)
finish('guard_whiteout')
check('loss_keeps_prior_win',progress()==2 and flag('FLAG_LA_CHIMNEY_MAGMA_BEATEN'))
check('loss_does_not_defeat_aqua',not flag('FLAG_LA_CHIMNEY_AQUA_BEATEN'))
check('save_progress',invoke('TrySavingData',0)==1)
check('reload_progress',invoke('LoadGameSave',0)==1)
check('saved_first_win_retained',progress()==2)
p=R/'docs/story/chimney-alliance/validation.json' ;p.parent.mkdir(parents=True,exist_ok=True)
p.write_text(json.dumps(dict(passed=True,checks=checks,user_save_loaded=False),indent=2)+'\n')
print('PASS',len(checks),'Chimney alliance checks',flush=True)
