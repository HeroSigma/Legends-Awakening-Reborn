"""Keep ordinary Pokemon Center transition setup usable in collection mode.
Uses isolated emulator RAM/flash; never opens the player's battery save.
"""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0], 'pc_helpers', 'exec'))
D=R/'docs/la_world/compact_pc/map_initializers';D.mkdir(parents=True,exist_ok=True)
start(0)
groups=json.loads((R/'data/maps/map_groups.json').read_text())
name='LilycoveCity_PokemonCenter_1F'
group=next(i for i,g in enumerate(groups['group_order']) if name in groups[g])
num=groups[groups['group_order'][group]].index(name)
for mode in [0,1]:
 check('mode_'+str(mode),invoke('StorageChangeMode',mode,1)==1)
 for special in ['InitUnionRoom','SetLilycoveLadyGfx','Script_GetLilycoveLadyId']:
  check('initializer_allowed_'+str(mode)+'_'+special,invoke('LaPcBlockedSpecial',symbols['SPECIAL_'+special])==0)
 for lady in range(3):
  save2=rd(symbols['gSaveBlock2Ptr'])
  wr(save2+0xA,lady*2,2);invoke('InitLilycoveLady')
  check('lady_variant_'+str(mode)+'_'+str(lady),invoke('GetLilycoveLadyId')==lady)
  warp(group,num,8,8)
  check('center_loaded_'+str(mode)+'_'+str(lady),location()==(group,num))
  check('center_overworld_'+str(mode)+'_'+str(lady),rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1)
  check('no_unavailable_dialog_'+str(mode)+'_'+str(lady),rd(symbols['sGlobalScriptContext']+1,1)==0)
  check('initializer_result_'+str(mode)+'_'+str(lady),rd(symbols['gSpecialVar_Result'],2)==(lady==2))
  check('lady_identity_allowed_'+str(mode)+'_'+str(lady),invoke('LaPcBlockedSpecial',symbols['SPECIAL_Script_GetLilycoveLadyId'])==0)
  invoke('Script_GetLilycoveLadyId')
  check('lady_identity_result_'+str(mode)+'_'+str(lady),rd(symbols['gSpecialVar_Result'],2)==lady)
  if mode==1 and lady==2:shutil.copy2(shot('lilycove_collection_fixed'),D/'lilycove_collection_fixed.png')
 for special in ['OpenPokeblockCaseForContestLady','CallBattleTowerFunc','CallTrainerHillFunction']:
  check('retired_activity_'+str(mode)+'_'+special,invoke('LaPcBlockedSpecial',symbols['SPECIAL_'+special])==mode)
lib.shutdown()
(D/'validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'map-initializer regression checks')
