"""Scientist nature effects must appear on the actual Summary memo."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_training_scientist.py').read_text().split('for mode in [0,1]:')[0],'helpers','exec'))
D=R/'.la_work/nature-summary';D.mkdir(exist_ok=True)
for mode in [0,1]:
 start(0);invoke('StorageChangeMode',mode,1);invoke('ScriptGiveMon',4,16,0)
 setdata('MON_DATA_HIDDEN_NATURE',2)
 original=get('MON_DATA_PERSONALITY')
 check('initial_effects_brave_'+str(mode),get('MON_DATA_HIDDEN_NATURE')==2)
 apply(4,0,10)
 check('effective_timid_'+str(mode),get('MON_DATA_HIDDEN_NATURE')==10)
 check('identity_unchanged_'+str(mode),get('MON_DATA_PERSONALITY')==original)
 invoke('ShowPokemonSummaryScreen',0,symbols['gParties'],0,0,symbols['CB2_ReturnToField']|1)
 wr(symbols['gMain']+4,symbols['CB2_InitSummaryScreen']|1)
 frames(180)
 memo=bytes(rd(symbols['gStringVar4']+i,1) for i in range(256))
 check('summary_says_timid_'+str(mode),bytes([0xCE,0xDD,0xE1,0xDD,0xD8]) in memo)
 if mode==0:shutil.copy2(shot('timid_summary'),R/'docs/features/timid-summary.png')
 tap(2);frames(180)
 check('summary_returns_'+str(mode),rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1)
 lib.shutdown()
(R/'docs/features/summary-effective-nature-validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'effective nature checks')
