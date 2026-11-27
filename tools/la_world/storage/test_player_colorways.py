"""Native style cycling, palette overrides, identity colors and persistence."""
from pathlib import Path
R=Path.cwd()
h=(R/'tools/la_world/storage/test_player_outfits.py').read_text().split('for gender,mode in')[0]
exec(compile(h,'wardrobe_helpers','exec'))
D=R/'docs/features/player-outfits/colorways';D.mkdir(parents=True,exist_ok=True)
def setstyle(style):invoke('VarSet',c['VAR_LA_PLAYER_OUTFIT'],0xC100+style if style else 0)
for gender in [0,1]:
 start(gender);invoke('ScriptGiveMon',3,20,0)
 g='MAY' if gender else 'BRENDAN'
 tag=c['OBJ_EVENT_PAL_TAG_ARIA' if gender else 'OBJ_EVENT_PAL_TAG_AREN']
 base=symbols['gObjectEventPal_May' if gender else 'gObjectEventPal_Brendan']
 setstyle(1);invoke('DynamicPal_SetSelection',0)
 rs=pal(invoke('DynamicPal_ObjectPalette',tag,base))
 for style in range(6):
  setstyle(style);invoke('DynamicPal_SetSelection',0)
  check('style_'+str((gender,style)),invoke('PlayerOutfit_Get')==style)
  for state in ['NORMAL','MACH_BIKE','ACRO_BIKE','SURFING','UNDERWATER','FIELD_MOVE','FISHING','WATERING','DECORATING']:
   check('complete_animation_'+str((gender,style,state)),images(c['OBJ_EVENT_GFX_'+g+'_'+state])!=0)
  actual=pal(invoke('DynamicPal_ObjectPalette',tag,base))
  if style>=2:
   check('identity_palette_preserved_'+str((gender,style)),all(actual[i]==rs[i] for i in range(16) if i not in [10,11,12,13]))
   check('inspired_colorway_visible_'+str((gender,style)),actual!=rs)
  check('save_style_'+str((gender,style)),invoke('TrySavingData',0)==1)
  setstyle(0);invoke('LoadGameSave',0)
  check('restore_style_'+str((gender,style)),invoke('PlayerOutfit_Get')==style)
 # Every 4-bit palette selection remains independently available with every style.
 for color in range(16):
  choice=(color<<4)|(color<<8)
  invoke('DynamicPal_SetSelection',choice)
  check('palette_choice_'+str((gender,color)),invoke('DynamicPal_GetSelection')==choice)
 # With explicit colors, style defaults never replace the player's choices.
 invoke('DynamicPal_SetSelection',0xAB0)
 setstyle(1);custom=pal(invoke('DynamicPal_ObjectPalette',tag,base))
 for style in range(2,6):
  setstyle(style)
  check('manual_overrides_'+str((gender,style)),pal(invoke('DynamicPal_ObjectPalette',tag,base))==custom)
 # Actual PC controls: wrap backward/forward through all six, then cancel.
 setstyle(0);invoke('DynamicPal_SetSelection',0);openpc();tap(64);tap(32)
 check('left_wrap_'+str(gender),invoke('PlayerOutfit_Get')==5)
 tap(16);check('right_wrap_'+str(gender),invoke('PlayerOutfit_Get')==0)
 for style in range(1,6):
  tap(16);frames(30)
  check('ui_style_'+str((gender,style)),invoke('PlayerOutfit_Get')==style)
  if style>=2:capture('g'+str(gender)+'_style'+str(style))
 finishpc(2)
 check('cancel_style_and_colors_'+str(gender),invoke('PlayerOutfit_Get')==0 and invoke('DynamicPal_GetSelection')==0)
 # Intro customization also retains the selection only on commit.
 invoke('DynamicPal_BeginIntro');openpc();tap(64);tap(16);tap(16);tap(16);invoke('DynamicPal_SetSelection',0xED0);finishpc(1);invoke('DynamicPal_CommitIntro')
 check('intro_commit_'+str(gender),invoke('PlayerOutfit_Get')==3 and invoke('DynamicPal_GetSelection')==0xED0)
 lib.shutdown()
(D/'validation.json').write_text(json.dumps(dict(passed=True,checks=checks,user_save_loaded=False,rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest()),indent=2)+'\n')
print('PASS',len(checks),'wardrobe checks',flush=True)
