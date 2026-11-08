"""BW navigation and gimmick selection in isolated native battles."""
from pathlib import Path
import tempfile,struct
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'docs/features/bw-battle-ui';D.mkdir(parents=True,exist_ok=True)
checks=[]
def check(n,v):
 checks.append(dict(test=n,passed=bool(v)));assert v,n
names=['MON_DATA_MOVE1','MON_DATA_MOVE2','MON_DATA_MOVE3','MON_DATA_MOVE4','MOVE_THUNDER_SHOCK','MOVE_GROWL','MOVE_QUICK_ATTACK','MOVE_THUNDER_WAVE','ITEM_MEGA_RING','ITEM_CHARIZARDITE_X','ITEM_ELECTRIUM_Z','ITEM_Z_POWER_RING','ITEM_TERA_ORB','GIMMICK_MEGA','GIMMICK_Z_MOVE','GIMMICK_TERA','GIMMICK_DYNAMAX','GIMMICK_ULTRA_BURST','ABILITY_STATIC','offsetof(struct BattleStruct,gimmick.usableGimmick)','offsetof(struct BattleStruct,gimmick.playerSelect)','offsetof(struct Sprite,data)','sizeof(struct Sprite)']
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "pokemon.h"\n#include "battle.h"\n#include "battle_gimmick.h"\n#include "sprite.h"\n#include <stddef.h>\nconst unsigned v[]={'+','.join(names)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 c=dict(zip(names,struct.unpack('<'+str(len(names))+'I',(td/'c.bin').read_bytes())))
def capture(n):shutil.copy2(shot('bw_'+n),D/(n+'.png'))
for label,species,held,key,gimmick in [('normal',25,0,0,0),('mega',6,c['ITEM_CHARIZARDITE_X'],c['ITEM_MEGA_RING'],c['GIMMICK_MEGA']),('zmove',25,c['ITEM_ELECTRIUM_Z'],c['ITEM_Z_POWER_RING'],c['GIMMICK_Z_MOVE']),('tera',25,0,c['ITEM_TERA_ORB'],c['GIMMICK_TERA'])]:
 start(0);invoke('StorageChangeMode',1,1);invoke('ScriptGiveMon',species,20,held)
 if key:invoke('AddBagItem',key,1)
 for slot,move in enumerate(['MOVE_THUNDER_SHOCK','MOVE_GROWL','MOVE_QUICK_ATTACK','MOVE_THUNDER_WAVE']):
  wr(0x03007400,c[move],2);invoke('SetMonData',symbols['gParties'],c['MON_DATA_MOVE'+str(slot+1)],0x03007400)
 invoke('CreateScriptedWildMon',113,10,0);invoke('BattleSetup_StartWildBattle')
 for i in range(1800):
  frames(1,1 if i%30==0 else 0)
  if rd(symbols['gBattleMainFunc'])==symbols['HandleTurnActionSelectionState']|1:frames(40);break
 check('battle_ready_'+label,i<1799);capture(label+'_actions')
 tap(1);frames(60);capture(label+'_moves')
 check('choose_move_'+label,rd(symbols['gBattlerControllerFuncs'])==symbols['HandleInputChooseMove']|1)
 check('four_moves_'+label,rd(symbols['gNumberOfMovesToChoose'],1)==4)
 if gimmick:
  bs=rd(symbols['gBattleStruct']);check('gimmick_available_'+label,rd(bs+c['offsetof(struct BattleStruct,gimmick.usableGimmick)'],1)==gimmick)
  tap(8);frames(45);capture(label+'_selected')
  check('gimmick_selected_'+label,rd(bs+c['offsetof(struct BattleStruct,gimmick.playerSelect)'],1)==1)
  tap(8);frames(30);check('gimmick_deselected_'+label,rd(bs+c['offsetof(struct BattleStruct,gimmick.playerSelect)'],1)==0)
 else:
  for button,expected in [(16,1),(128,3),(32,2),(64,0)]:
   tap(button);frames(10);check('move_cursor_'+str(expected),rd(symbols['gMoveSelectionCursor'],1)==expected)
  tap(512);frames(30);capture('description');tap(512);frames(30);capture('description_closed')
  tap(2);frames(60);capture('back_actions');check('back_to_actions',rd(symbols['gBattle_BG0_Y'],2)==160)
  tap(1);frames(30)
  for kind in ['GIMMICK_DYNAMAX','GIMMICK_ULTRA_BURST']:
   # UI-only fixture: do not grant or activate a locked gameplay mechanic.
   bs=rd(symbols['gBattleStruct']);wr(bs+c['offsetof(struct BattleStruct,gimmick.usableGimmick)'],c[kind],1)
   invoke('DestroyGimmickTriggerSprite');invoke('CreateGimmickTriggerSprite',0)
   check('preview_trigger_'+kind,invoke('IsGimmickTriggerSpriteActive'))
   if kind=='GIMMICK_DYNAMAX':
    wr(bs+c['offsetof(struct BattleStruct,gimmick.playerSelect)'],1,1);invoke('BattleUI_DisplayMoveBox',0)
   frames(30);capture(kind.lower()+'_preview')
 lib.shutdown()
(D/'validation.json').write_text(json.dumps(dict(rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks,user_save_loaded=False),indent=2)+'\n')
print('PASS',len(checks),'BW UI checks',flush=True)
