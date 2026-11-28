"""Post-Brawly scientist kit: actual script, decline/retry and saved claim."""
from pathlib import Path
R=Path.cwd()
source=(R/'tools/la_world/storage/test_summary_stat_editor.py').read_text().split('for mode in [0,1]:')[0]
source=source.replace("names=[", "names=['FLAG_LA_TRAINING_CAP_KIT',")
exec(compile(source,'kit_helpers','exec'))
D=R/'docs/features/cap-training';D.mkdir(parents=True,exist_ok=True)
def quantity(item):return invoke('CountTotalItemQuantityInBag',c['ITEM_'+item])
def visit(accept=None):
 invoke('ScriptContext_SetupScript',symbols['LegendsTraining_Scientist'])
 offered=False
 for i in range(8000):
  if active('Task_HandleYesNoInput') is not None:
   offered=True;frames(30);capture('kit_offer');tap(1 if accept else 2);frames(40)
  if active('Task_HandleChooseMonInput') is not None:
   frames(90);tap(2);frames(240);return offered
  frames(1,1 if i%17==0 else 0)
 raise AssertionError('Scientist did not return to party selection')
start(0);invoke('ScriptGiveMon',4,16,0);invoke('FlagSet',c['FLAG_BADGE01_GET'])
check('no_kit_before_Brawly',not visit() and quantity('BOTTLE_CAP')==0 and quantity('GOLD_BOTTLE_CAP')==0)
invoke('FlagSet',c['FLAG_BADGE02_GET'])
check('offered_after_Brawly',visit(False))
check('decline_no_claim',invoke('FlagGet',c['FLAG_LA_TRAINING_CAP_KIT'])==0 and quantity('GOLD_BOTTLE_CAP')==0)
check('declined_can_retry',visit(True))
check('one_of_each',quantity('BOTTLE_CAP')==1 and quantity('GOLD_BOTTLE_CAP')==1)
check('claim_flag',invoke('FlagGet',c['FLAG_LA_TRAINING_CAP_KIT'])==1)
check('no_repeat_offer',not visit())
check('no_duplicate',quantity('BOTTLE_CAP')==1 and quantity('GOLD_BOTTLE_CAP')==1)
check('save',invoke('TrySavingData',0)==1)
invoke('FlagClear',c['FLAG_LA_TRAINING_CAP_KIT']);invoke('RemoveBagItem',c['ITEM_GOLD_BOTTLE_CAP'],1)
check('reload',invoke('LoadGameSave',0)==1)
check('saved_claim_and_caps',invoke('FlagGet',c['FLAG_LA_TRAINING_CAP_KIT'])==1 and quantity('GOLD_BOTTLE_CAP')==1)
lib.shutdown()
(D/'kit-validation.json').write_text(json.dumps(dict(checks=checks,user_save_loaded=False,rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest()),indent=2)+'\n')
print('PASS',len(checks),'starter kit checks',flush=True)
