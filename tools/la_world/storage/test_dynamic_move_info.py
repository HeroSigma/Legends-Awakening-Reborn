"""Native battle preview calculations and state-preservation checks."""
from pathlib import Path
import tempfile,struct
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'docs/features/dynamic-move-info';D.mkdir(exist_ok=True)
fields=['sizeof(struct BattlePokemon)','sizeof(struct BattleStruct)','offsetof(struct BattlePokemon,ability)','offsetof(struct BattlePokemon,item)','offsetof(struct BattlePokemon,status1)','offsetof(struct BattlePokemon,hp)','offsetof(struct BattlePokemon,maxHP)','offsetof(struct BattlePokemon,moves)']
consts=['MOVE_TACKLE','MOVE_THUNDER','MOVE_FACADE','MOVE_ACROBATICS','MOVE_SWORDS_DANCE','MOVE_LOW_KICK','MOVE_KNOCK_OFF','MOVE_MACH_PUNCH','ABILITY_TECHNICIAN','ABILITY_COMPOUND_EYES','ABILITY_NO_GUARD','ABILITY_IRON_FIST','ABILITY_TOUGH_CLAWS','ITEM_WIDE_LENS','ITEM_MUSCLE_BAND','ITEM_ORAN_BERRY','STATUS1_BURN','B_WEATHER_SUN','B_WEATHER_RAIN','MON_DATA_MOVE1','GIMMICK_DYNAMAX','GIMMICK_NONE']
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "battle.h"\n#include "battle_gimmick.h"\n#include "pokemon.h"\n#include <stddef.h>\nconst unsigned v[]={'+','.join(fields+consts)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 c=dict(zip(fields+consts,struct.unpack('<'+'I'*len(fields+consts),(td/'c.bin').read_bytes())))
start(0);invoke('ScriptContext_Init');invoke('UnlockPlayerFieldControls');invoke('ScriptGiveMon',25,20,0)
scratch=0x0203fc00
wr(scratch,c['MOVE_FACADE'],2);invoke('SetMonData',symbols['gParties'],c['MON_DATA_MOVE1'],scratch)
invoke('CreateScriptedWildMon',261,3,0);invoke('BattleSetup_StartWildBattle')
for i in range(1600):
 frames(1,1 if i%30==0 else 0)
 if rd(symbols['gBattleMainFunc'])==symbols['HandleTurnActionSelectionState']|1:
  frames(40);break
check('real battle ready',i<1599)
mon=symbols['gBattleMons'];size=c[fields[0]]
def setf(field,value,n=2):wr(mon+c['offsetof(struct BattlePokemon,'+field+')'],value,n)
def preview(move,ability=0,item=0,status=0,weather=0):
 setf('ability',ability);setf('item',item);setf('status1',status,4);wr(symbols['gBattleWeather'],weather,4)
 wr(symbols['sRngLoopUnlocked'],0,1)
 wr(0x03007300,0x4770,2);wr(symbols['gMain']+4,0x03007301)
 before={n:rd(symbols[n]) for n in ['gRngValue','gRng2Value','gBattleMovePower','gPotentialItemEffectBattler'] if n in symbols}
 bs=rd(symbols['gBattleStruct']);raw=bytes(rd(bs+j,1) for j in range(c[fields[1]]));mons=bytes(rd(mon+j,1) for j in range(size*4))
 invoke('GetMoveDescriptionPreview',0,move,scratch)
 check('no scratch or RNG changes '+str((move,ability,item,status,weather)),all(rd(symbols[n])==v for n,v in before.items()))
 check('no battle-state changes '+str((move,ability,item,status,weather)),raw==bytes(rd(bs+j,1) for j in range(len(raw))) and mons==bytes(rd(mon+j,1) for j in range(len(mons))))
 return rd(scratch,2),rd(scratch+2,2)
for name,args,expected in [
 ('plain tackle',(c['MOVE_TACKLE'],),(40,100)),
 ('Technician',(c['MOVE_TACKLE'],c['ABILITY_TECHNICIAN']),(60,100)),
 ('Iron Fist',(c['MOVE_MACH_PUNCH'],c['ABILITY_IRON_FIST']),(48,100)),
 ('Tough Claws',(c['MOVE_TACKLE'],c['ABILITY_TOUGH_CLAWS']),(52,100)),
 ('Wide Lens',(c['MOVE_THUNDER'],0,c['ITEM_WIDE_LENS']),(110,77)),
 ('Compound Eyes',(c['MOVE_THUNDER'],c['ABILITY_COMPOUND_EYES']),(110,91)),
 ('No Guard',(c['MOVE_THUNDER'],c['ABILITY_NO_GUARD']),(110,0)),
 ('sun Thunder',(c['MOVE_THUNDER'],0,0,0,c['B_WEATHER_SUN']),(110,50)),
 ('rain Thunder',(c['MOVE_THUNDER'],0,0,0,c['B_WEATHER_RAIN']),(110,0)),
 ('burned Facade',(c['MOVE_FACADE'],0,0,c['STATUS1_BURN']),(140,100)),
 ('empty Acrobatics',(c['MOVE_ACROBATICS'],),(110,100)),
 ('held Acrobatics',(c['MOVE_ACROBATICS'],0,c['ITEM_ORAN_BERRY']),(55,100)),
 ('status move',(c['MOVE_SWORDS_DANCE'],),(0,0)),
 ('unknown weight fallback',(c['MOVE_LOW_KICK'],),(1,100)),
 ('Knock Off fallback',(c['MOVE_KNOCK_OFF'],),(65,100)),
 ('Muscle Band',(c['MOVE_TACKLE'],0,c['ITEM_MUSCLE_BAND']),(44,100)),
]:check(name,preview(*args)==expected)
# Max moves retain their own authored power/category instead of ordinary boosts.
invoke('SetActiveGimmick',0,c['GIMMICK_DYNAMAX'])
check('Max Strike',preview(c['MOVE_TACKLE'])==(90,0))
check('Max Guard',preview(c['MOVE_SWORDS_DANCE'])==(0,0))
invoke('SetActiveGimmick',0,c['GIMMICK_NONE'])
# Enemy ability/item knowledge must not influence the estimate.
wr(mon+size+c['offsetof(struct BattlePokemon,ability)'],c['ABILITY_NO_GUARD'],2)
check('hidden target ability ignored',preview(c['MOVE_THUNDER'])==(110,70))
check('invalid move safe',preview(65535)==(0,0))
wr(mon+size+c['offsetof(struct BattlePokemon,ability)'],0,2)
wr(symbols['sRngLoopUnlocked'],1,1)
wr(symbols['gMain']+4,symbols['BattleMainCB2']|1)
# The move-description panel is reached through its normal Fight/L controls.
setf('ability',0);setf('item',0);setf('status1',c['STATUS1_BURN'],4);wr(symbols['gBattleWeather'],0,4)
frames(1,1);frames(45);frames(1,512);frames(30)
shutil.copy2(shot('dynamic_facade'),D/'facade.png')
check('positive preview palette',rd(0x05000000+(5*16+6)*2,2)==(3|(19<<5)|(6<<10)))
check('UI remains in battle',rd(symbols['gMain']+4)!=symbols['CB2_Overworld']|1)
(D/'validation.json').write_text(json.dumps({'passed':True,'checks':checks,'rom_sha256':hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest()},indent=2)+'\n')
print('PASS',len(checks),'dynamic move checks')
