"""Real wild-battle party selection, cancellation and switching."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'docs/features/swsh-party-menu';D.mkdir(parents=True,exist_ok=True)
for mode in [0,1]:
 start(0);invoke('StorageChangeMode',mode,1)
 invoke('ScriptGiveMon',25,10,0);invoke('ScriptGiveMon',7,10,0)
 invoke('CreateScriptedWildMon',261,3,0);invoke('BattleSetup_StartWildBattle')
 for i in range(1200):
  frames(1,1 if i%30==0 else 0)
  if rd(symbols['gBattleMainFunc'])==symbols['HandleTurnActionSelectionState']|1:
   frames(40);break
 check('wild_battle_started_'+str(mode),rd(symbols['gMain']+4)!=symbols['CB2_Overworld']|1)
 tap(128);tap(1);frames(180)
 check('battle_party_open_'+str(mode),active('Task_HandleChooseMonInput') is not None)
 shutil.copy2(shot('swsh-battle-'+str(mode)),D/('battle-'+str(mode)+'.png'))
 tap(2);frames(200)
 check('cancel_returns_to_battle_'+str(mode),active('Task_HandleChooseMonInput') is None)
 # Action cursor remains Pokemon after cancelling.
 tap(1);frames(180)
 check('battle_party_reopens_'+str(mode),active('Task_HandleChooseMonInput') is not None)
 tap(128);tap(1);frames(30)
 shutil.copy2(shot('swsh-battle-actions-'+str(mode)),D/('battle-actions-'+str(mode)+'.png'))
 tap(1)
 for i in range(600):frames(1,1 if i%30==0 else 0)
 check('switch_returns_to_battle_'+str(mode),active('Task_HandleChooseMonInput') is None)
 check('battle_uses_selected_slot_'+str(mode),rd(symbols['gBattlerPartyIndexes'],2)==1)
 lib.shutdown()
(D/'battle-validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'battle party checks')
