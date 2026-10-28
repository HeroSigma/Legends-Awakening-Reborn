"""Native move-free field skill regression; isolated emulator, no player save."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
helpers=(R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0]
helpers=helpers.replace("R=Path('/home/allan/projects/Legends-Awakening-Reborn')",'R=Path('+repr(str(R))+')')
exec(compile(helpers,'pc_helpers','exec'))
D=R/'.la_work/field-move-test';D.mkdir(parents=True,exist_ok=True)
proof=R/'docs/features/field-move-unlocks';proof.mkdir(exist_ok=True)
start(0);invoke('ScriptGiveMon',151,10,0)
party=symbols['gParties'];A=0x0203f000;V=A+0x300
for slot in range(4):invoke('SetMonMoveSlot',party,0,slot)
# Compiler resolves enum/ABI constants, including the native badge per skill.
import tempfile,struct
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "field_move.h"\n#include "pokemon.h"\n#include "script.h"\n#include "constants/flags.h"\n#include "constants/items.h"\n#include "constants/moves.h"\n#include "constants/species.h"\n#include <stddef.h>\nconst unsigned values[]={FLAG_RECEIVED_HM_CUT,FLAG_RECEIVED_HM_FLASH,FLAG_RECEIVED_HM_ROCK_SMASH,FLAG_RECEIVED_HM_STRENGTH,FLAG_RECEIVED_HM_SURF,FLAG_RECEIVED_HM_FLY,FLAG_RECEIVED_HM_DIVE,FLAG_RECEIVED_HM_WATERFALL,FLAG_BADGE01_GET,ITEM_HM03,MON_DATA_IS_EGG,FLAG_SYS_POKEMON_GET,offsetof(struct ScriptContext,scriptPtr),MON_DATA_MOVE1,MOVE_SURF,SPECIES_VENIPEDE};\n')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 constants=struct.unpack('<16I',(td/'c.bin').read_bytes())
flags=constants[:8];badge0,surfHM,eggField,partyFlag,scriptOffset,moveField,surfMove,climber=constants[8:]
badges=[badge0+i for i in [0,1,2,3,4,5,6,7]]
for mode in [0,1]:
 invoke('StorageChangeMode',mode,1)
 for skill in range(8):
  for badge,acquired in [(False,False),(True,False),(False,True),(True,True)]:
   invoke('FlagSet' if badge else 'FlagClear',badges[skill]);invoke('FlagSet' if acquired else 'FlagClear',flags[skill])
   expected=0 if badge and acquired else 6
   check('find_user_'+str((mode,skill,badge,acquired)),invoke('FieldMove_FindUser',skill)==expected)
   # Exercise the actual bytecode command, including its default no-badge-check form.
   for do_check in [0,1]:
    wr(A+0x200,skill,1);wr(A+0x201,do_check,1);wr(A+scriptOffset,A+0x200)
    invoke('ScrCmd_checkfieldmove',A)
    check('script_'+str((mode,skill,badge,acquired,do_check)),rd(symbols['gSpecialVar_Result'],2)==expected)
  invoke('FlagClear',flags[skill]);invoke('FlagClear',badges[skill])
 # Older saves holding the HM can unlock without a historical received flag.
 invoke('FlagSet',badges[4]);invoke('AddBagItem',surfHM,1)
 check('owned_hm_fallback_'+str(mode),invoke('FieldMove_FindUser',4)==0)
 invoke('RemoveBagItem',surfHM,1);invoke('FlagClear',badges[4])
# Learned HMs cannot bypass the acquisition requirement either.
invoke('FlagSet',badges[4]);invoke('FlagClear',flags[4]);invoke('SetMonMoveSlot',party,surfMove,0)
check('learned_move_cannot_bypass_acquisition',invoke('FieldMove_FindUser',4)==6)
invoke('SetMonMoveSlot',party,0,0)
# Egg and incapable species must not become invisible field-move users.
for f in flags+tuple(badges):invoke('FlagSet',f)
wr(V,1,1);invoke('SetMonData',party,eggField,V)
check('surf_checker_rejects_eggs',invoke('PartyHasMonWithSurf')==0)
check('eggs_rejected',invoke('FieldMove_FindUser',4)==6)
wr(V,0,1);invoke('SetMonData',party,eggField,V)
check('surf_checker_without_move',invoke('PartyHasMonWithSurf')==1)
check('restored_non_egg',invoke('FieldMove_FindUser',4)==0)
invoke('CreateRandomMon',party,10,10)
check('surf_checker_rejects_incapable',invoke('PartyHasMonWithSurf')==0)
check('incapable_species_rejected',invoke('FieldMove_FindUser',4)==6)
invoke('CreateRandomMon',party,climber,5)
for slot in range(4):invoke('SetMonMoveSlot',party,0,slot)
check('natural_rock_climber_without_move',invoke('FieldMove_FindUser',14)==0)
invoke('HyperSinnoh_RockClimbSelectMon')
check('sinnoh_climb_uses_shared_selector',rd(symbols['gSpecialVar_0x8004'],2)==0)
invoke('CreateRandomMon',party,151,10)
for slot in range(4):invoke('SetMonMoveSlot',party,0,slot)
check('invalid_skill',invoke('FieldMove_FindUser',255)==6)
check('unrelated_move_still_requires_knowledge',invoke('FieldMove_FindUser',8)==6)
# All four actual move slots remain empty; no move is taught by unlocking.
for slot in range(4):check('moves_unchanged_'+str(slot),invoke('GetBoxMonData3',party,moveField+slot,0)==0)
# Real party menu: paged skills avoid overflowing the native action buffer.
invoke('FlagSet',partyFlag);wr(symbols['gMain']+4,symbols['CB2_PartyMenuFromStartMenu']|1);frames(240);tap(1);frames(30)
check('party_context',active('Task_HandleSelectionMenuInput') is not None)
tap(128);tap(1);frames(30);shutil.copy2(shot('field_skills_first'),proof/'page_1.png')
check('skills_menu',active('Task_HandleSelectionMenuInput') is not None and invoke('Menu_GetCursorPos')==0)
for _ in range(6):tap(128)
tap(1);frames(30);shutil.copy2(shot('field_skills_second'),proof/'page_2.png')
check('second_page',active('Task_HandleSelectionMenuInput') is not None and invoke('Menu_GetCursorPos')==0)
tap(2);frames(30);tap(2);frames(30);tap(2);frames(180)
check('party_exit',rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1)
lib.shutdown()
(R/'docs/features/field-move-unlocks-validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'field-move unlock checks')
