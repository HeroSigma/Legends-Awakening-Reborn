"""Check real battle obedience against every Hoenn training cap in isolated mGBA."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0], 'helpers', 'exec'))
D=R/'.la_work/obedience-test';D.mkdir(exist_ok=True)
import tempfile,struct
with tempfile.TemporaryDirectory() as td:
 td=Path(td)
 (td/'c.c').write_text('#include "global.h"\n#include "pokemon.h"\n#include "battle.h"\n#include "battle_util.h"\n#include "constants/flags.h"\n#include <stddef.h>\nconst unsigned v[]={offsetof(struct BattlePokemon,level),offsetof(struct BattlePokemon,otId),offsetof(struct BattlePokemon,otName),FLAG_LA_RED_DEX_GIFTS,FLAG_BADGE01_GET,FLAG_BADGE02_GET,FLAG_BADGE03_GET,FLAG_BADGE04_GET,FLAG_BADGE05_GET,FLAG_BADGE06_GET,FLAG_BADGE07_GET,FLAG_BADGE08_GET,FLAG_IS_CHAMPION,OBEYS};\n')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 values=struct.unpack('<14I',(td/'c.bin').read_bytes())
level,otid,otname,dex,*rest=values
badges=rest[:-1];obeys=rest[-1]
start(0)
wr(symbols['gBattlerAttacker'],0,1);wr(symbols['gBattleTypeFlags'],0)
mon=symbols['gBattleMons']
for f in badges:invoke('FlagClear',f)
for unlocked in [False,True]:
 invoke('FlagSet' if unlocked else 'FlagClear',dex)
 for step,cap in enumerate(([16] if not unlocked else [16,20,26,32,37,43,49,56,65,100])):
  if step:invoke('FlagSet',badges[step-1])
  if unlocked:check('cap_'+str(step),invoke('GetCurrentLevelCap')==cap)
  for traded in [False,True]:
   save2=rd(symbols['gSaveBlock2Ptr'])
   wr(mon+otid,0x12345678 if traded else rd(save2+10))
   for i in range(8):wr(mon+otname+i,rd(save2+i,1),1)
   for lvl in [1,cap-1,cap]:
    wr(mon+level,lvl,1);wr(mon+otid+4,lvl,1)
    for repeat in range(16):
     check('obeys_'+str((unlocked,step,traded,lvl,repeat)),invoke('GetAttackerObedienceForAction')==obeys)
lib.shutdown()
(R/'docs/features/obedience-level-cap-validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'obedience checks')
