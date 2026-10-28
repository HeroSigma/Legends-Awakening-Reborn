"""Full Nurse Joy healing in normal and collection mode; no player save used."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_training_scientist.py').read_text().split('for mode in [0,1]:')[0],'training_helpers','exec'))
D=R/'docs/la_world/compact_pc/nurse';D.mkdir(exist_ok=True)
mg=json.loads((R/'data/maps/map_groups.json').read_text())
for mode in [0,1]:
 start(0);invoke('StorageChangeMode',mode,1);invoke('ScriptGiveMon',4,8,0)
 # A marker in the final slot catches accidental loss or profile resets.
 invoke('SetBoxMonAt',59 if mode else 13,29,symbols['gParties'])
 for name in ['OldaleTown_PokemonCenter_1F','PetalburgCity_PokemonCenter_1F','LilycoveCity_PokemonCenter_1F']:
  for group,gname in enumerate(mg['group_order']):
   if name in mg[gname]:mapnum=mg[gname].index(name);break
  data=json.loads((R/'data/maps'/name/'map.json').read_text())
  nurse=next(o for o in data['object_events'] if 'Nurse' in o['script'])
  warp(group,mapnum,nurse['x'],nurse['y']+2)
  setdata('MON_DATA_HP',1)
  frames(12,64);frames(8);tap(1)
  blocked=False;healed=False;started=False
  for frame in range(14000):
   pointer=rd(symbols['sGlobalScriptContext']+8)
   if symbols['LaCollection_Blocked']<=pointer<symbols['LaCollection_Blocked']+40:blocked=True
   if task('Task_HandleYesNoInput') is not None:started=True
   if frame%120==0 and get('MON_DATA_HP')>1:healed=True
   if started and healed and rd(symbols['sGlobalScriptContextStatus'],1)==2:break
   frames(1,1 if frame%20==0 else 0)
  else:raise AssertionError(('nurse did not finish',mode,name,blocked,healed))
  check('nurse_no_warning_'+str((mode,name)),not blocked)
  check('nurse_heals_'+str((mode,name)),healed)
  check('storage_mode_preserved_'+str((mode,name)),invoke('GetStorageBoxCount')==(60 if mode else 14))
  check('stored_marker_preserved_'+str((mode,name)),invoke('GetBoxMonDataAt',59 if mode else 13,29,c['MON_DATA_SPECIES'])==4)
  if mode==1:shutil.copy2(shot('nurse_'+name),D/(name+'.png'))
 # Every blocked special must resolve to its current named ELF symbol.
 gates=json.loads((R/'docs/la_world/compact_pc/retired_feature_gates.json').read_text())
 for entry in gates['specials']:
  check('named_gate_'+str(mode)+'_'+entry['name'],invoke('LaPcBlockedSpecial',symbols['SPECIAL_'+entry['name']])==mode)
 for name in ['HealPlayerParty','CountPlayerTrainerStars','IsPokerusInParty','PlayerNotAtTrainerHillEntrance','BufferUnionRoomPlayerName','LegendsTraining_Menu','LegendsTraining_Commit']:
  check('ordinary_service_'+str(mode)+'_'+name,invoke('LaPcBlockedSpecial',symbols['SPECIAL_'+name])==0)
 lib.shutdown()
(D/'validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),checks=checks,rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest()),indent=2)+'\n')
print('PASS',len(checks),'Nurse Joy/collection guard checks')
