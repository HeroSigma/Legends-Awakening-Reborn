"""Native font, speaker and full summit-dialogue validation. Disposable save only."""
from pathlib import Path
R=Path.cwd()
h=(R/'tools/la_world/story/test_blue_chimney.py').read_text().split('start(0);')[0]
h=h.replace("names=[","names=['SP_NAME_PLAYER','SP_NAME_MAXIE','SP_NAME_ARCHIE','SP_NAME_MAGMA_TABITHA','SP_NAME_TEAM_MAGMA',",1)
h=h.replace(r'#include "global.h"\n',r'#include "global.h"\n#include "constants/speaker_names.h"\n',1)
exec(compile(h,'summit_helpers','exec'))
revised_labels=json.loads((R/'docs/story/chimney-villain-dialogue/revised-labels.json').read_text())
start(0)
sb=rd(symbols['gSaveBlock2Ptr']);wr(sb+0x14,(rd(sb+0x14,1)&~7)|2,1)
invoke('FlagSet',c['FLAG_LA_RED_DEX_GIFTS'])
for i in range(3):invoke('FlagSet',c['FLAG_BADGE01_GET']+i)
for sp in [1,4,7,25,133,155]:invoke('ScriptGiveMon',sp,30,0)
for n in ['FLAG_LA_BLUE_CHIMNEY_BRIEFED','FLAG_LA_BLUE_CABLE_MET','FLAG_LA_BLUE_CHIMNEY_BOARDED','FLAG_LA_COZMO_BRIEFED']:invoke('FlagSet',c[n])
invoke('VarSet',c['VAR_LA_ASHES_STATE'],2)
for n in revised_labels:
 data=bytearray()
 for j in range(2400):
  b=rd(symbols[n]+j,1)
  if b==255:break
  data.append(b)
 for i,line in enumerate(re.split(b'[\xfe\xfb\xfa]',bytes(data))):
  for j,b in enumerate(line+b'\xff'):wr(0x03007500+j,b,1)
  check('fit_'+n+'_'+str(i),invoke('GetStringWidth',1,0x03007500,0)<=208)
for n,speaker in [('MtChimney_Text_TabithaIntro','SP_NAME_MAGMA_TABITHA'),('MtChimney_Text_Grunt1Intro','SP_NAME_TEAM_MAGMA'),('MtChimney_Text_Grunt2Intro','SP_NAME_TEAM_MAGMA')]:
 check('inline_speaker_'+n,bytes(rd(symbols[n]+i,1) for i in range(3))==bytes([0xfc,0x19,c[speaker]]))
 check('speaker_resolves_'+n,invoke('IsSpeakerBuffered',symbols[n]) and rd(symbols['gSpeakerName'])==rd(symbols['gSpeakerNamesTable']+c[speaker]*4))
def seen(n):
 pre=bytes(rd(symbols[n]+i,1) for i in range(16));return pre in bytes(rd(symbols['gStringVar4']+i,1) for i in range(48))
def speaker(n):return rd(symbols['gSpeakerName'])==rd(symbols['gSpeakerNamesTable']+c[n]*4)
at('MAP_MT_CHIMNEY',13,7);tap(64);frames(20);tap(1)
for label,sp in [('ChimneyVillains_Text_PlayerDemand','SP_NAME_PLAYER'),('ChimneyVillains_Text_MaxieChallenge','SP_NAME_MAXIE')]:
 waitfor(lambda:seen(label),label);check('active_speaker_'+label,speaker(sp));frames(160);print(shot(label),flush=True)
waitfor(lambda:rd(symbols['gMain']+4)==symbols['BattleMainCB2']|1 and rd(symbols['gBattleMainFunc'])==symbols['HandleTurnActionSelectionState']|1,'maxie_battle')
wr(symbols['gBattleOutcome'],1,1);wr(symbols['gBattleMainFunc'],symbols['HandleEndTurn_BattleWon']|1)
for label,sp in [('MtChimney_Text_ArchieThankYou','SP_NAME_ARCHIE'),('ChimneyVillains_Text_PlayerMissing','SP_NAME_PLAYER'),('ChimneyVillains_Text_ArchieWithdrawal','SP_NAME_ARCHIE')]:
 waitfor(lambda:seen(label),label);check('active_speaker_'+label,speaker(sp));frames(160);print(shot(label),flush=True)
finish('summit_and_hoopa')
check('summit_still_completed',flag('FLAG_DEFEATED_EVIL_TEAM_MT_CHIMNEY'))
check('hoopa_lead_still_available',flag('FLAG_LA_CHIMNEY_RESONANCE'))
check('speaking_protagonist_returns_control',ended())
check('speaker_cleared_after_scene',rd(symbols['gSpeakerName'])==0)
p=R/'docs/story/chimney-villain-dialogue/validation.json';p.write_text(json.dumps(dict(passed=True,checks=checks,user_save_loaded=False,rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest()),indent=2)+'\n')
print('PASS',len(checks),'Chimney villain checks',flush=True)
