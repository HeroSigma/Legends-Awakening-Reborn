"""Native battle-back color loading and return-from-bag regression."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_dynamic_palettes.py').read_text().split('for gender,mode in [(0,0),(1,1)]:')[0],'helpers','exec'))
for gender in [0,1]:
 start(gender);invoke('ScriptGiveMon',4,16,0);invoke('DynamicPal_SetSelection',0x432)
 pic=c['TRAINER_PIC_MAY' if gender else 'TRAINER_PIC_BRENDAN']
 expected=pal(invoke('DynamicPal_TrainerPalette',pic,False))
 original=pal(symbols['gTrainerPalette_May' if gender else 'gTrainerPalette_Brendan'])
 check(f'battle_palette_custom_{gender}',expected!=original)
 invoke('CreateScriptedWildMon',261,3,0);invoke('BattleSetup_StartWildBattle')
 found=False
 for i in range(1200):
  frames(1)
  if any(pal(symbols['gPlttBufferUnfaded']+512+slot*32)==expected for slot in range(16)):
   found=True;break
 check(f'battle_loads_chosen_colors_{gender}',found)
 frames(30);capture(f'battle_back_{gender}')
 for i in range(1800):
  if rd(symbols['gBattleMainFunc'])==symbols['HandleTurnActionSelectionState']|1:frames(40);break
  frames(1,1 if i%30==0 else 0)
 else:raise AssertionError('battle action menu timeout')
 tap(16);tap(1);wait('Task_BagMenu_HandleInput',1200);frames(30);tap(2)
 for i in range(1500):
  frames(1)
  if rd(symbols['gBattleMainFunc'])==symbols['HandleTurnActionSelectionState']|1:break
 else:raise AssertionError('battle bag return timeout')
 check(f'bag_return_keeps_choice_{gender}',invoke('DynamicPal_GetSelection')==0x432)
 lib.shutdown()
(D/'battle-validation.json').write_text(json.dumps(dict(rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'battle palette checks',flush=True)
