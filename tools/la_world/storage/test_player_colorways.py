"""Expanded palette options, independent garment selection and legacy migration."""
from pathlib import Path
R=Path.cwd()
exec(compile((R/'tools/la_world/storage/test_player_outfits.py').read_text().split('for gender,mode in')[0],'palette_helpers','exec'))
D=R/'docs/features/player-outfits/palette-validation';D.mkdir(parents=True,exist_ok=True)
for gender in [0,1]:
 start(gender)
 invoke('VarSet',c['VAR_LA_PLAYER_OUTFIT'],0xC201)
 for color in range(16):
  choice=(color<<4)|(color<<8)
  invoke('DynamicPal_SetSelection',choice)
  check('palette_choice_'+str((gender,color)),invoke('DynamicPal_GetSelection')==choice)
  check('color_keeps_garment_'+str((gender,color)),invoke('PlayerOutfit_Get')==2)
 invoke('DynamicPal_SetSelection',0xAB0)
 tag=c['OBJ_EVENT_PAL_TAG_ARIA' if gender else 'OBJ_EVENT_PAL_TAG_AREN'];base=symbols['gObjectEventPal_May' if gender else 'gObjectEventPal_Brendan']
 actual=pal(invoke('DynamicPal_ObjectPalette',tag,base))
 for style,saved in [(0,0),(1,0xC101),(2,0xC201),(3,0xC202)]:
  invoke('VarSet',c['VAR_LA_PLAYER_OUTFIT'],saved)
  now=pal(invoke('DynamicPal_ObjectPalette',tag,base))
  check('independent_overrides_'+str((gender,style)),all(now[i]==actual[i] for i in [10,11,12,13]))
 for saved in [0xC102,0xC103,0xC104,0xC105]:
  invoke('VarSet',c['VAR_LA_PLAYER_OUTFIT'],saved)
  check('retired_colorway_rs_base_'+str((gender,saved)),invoke('PlayerOutfit_Get')==1)
 invoke('VarSet',c['VAR_LA_PLAYER_OUTFIT'],0xC201)
 check('save_palette_'+str(gender),invoke('TrySavingData',0)==1)
 invoke('VarSet',c['VAR_LA_PLAYER_OUTFIT'],0);invoke('DynamicPal_SetSelection',0)
 check('load_palette_'+str(gender),invoke('LoadGameSave',0)==1)
 check('preserved_'+str(gender),invoke('PlayerOutfit_Get')==2 and invoke('DynamicPal_GetSelection')==0xAB0)
 lib.shutdown()
(D/'validation.json').write_text(json.dumps(dict(passed=True,checks=checks,user_save_loaded=False),indent=2)+'\n')
print('PASS',len(checks),'palette and migration checks',flush=True)
