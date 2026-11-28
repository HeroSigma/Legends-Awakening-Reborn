"""Native Store milestone gates and Wattson's first Mega configuration."""
from pathlib import Path
import tempfile,struct,json,hashlib,re
R=Path.cwd()
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'docs/features/gimmick-shop-milestones';D.mkdir(parents=True,exist_ok=True)
items_source=(R/'src/data/items.h').read_text()
mega=re.findall(r'\[(ITEM_\w+)\]\s*=\s*\{[^}]*?\.sortType = ITEM_TYPE_MEGA_STONE',items_source,re.S)
z=re.findall(r'\[(ITEM_\w+)\]\s*=\s*\{[^}]*?\.sortType = ITEM_TYPE_Z_CRYSTAL',items_source,re.S)
reserved=['ITEM_'+x for x in ['MEWTWONITE_X','MEWTWONITE_Y','LATIASITE','LATIOSITE','DIANCITE','ZYGARDITE','HEATRANITE','DARKRANITE','ZERAORITE','MAGEARNITE','MEWNIUM_Z','TAPUNIUM_Z','SOLGANIUM_Z','LUNALIUM_Z','MARSHADIUM_Z','ULTRANECROZIUM_Z']]
names=['FLAG_BADGE01_GET','FLAG_BADGE02_GET','FLAG_BADGE03_GET','FLAG_SYS_GAME_CLEAR','FLAG_LA_RED_DEX_GIFTS','TRAINER_WATTSON_1','TRAINER_WATTSON_2','SPECIES_MANECTRIC','ITEM_MANECTITE','sizeof(struct Trainer)','sizeof(struct TrainerMon)','offsetof(struct Trainer,party)','offsetof(struct TrainerMon,species)','offsetof(struct TrainerMon,heldItem)','offsetof(struct SaveBlock1,money)']+mega+z
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "data.h"\n#include "item.h"\n#include "constants/opponents.h"\n#include "constants/flags.h"\n#include <stddef.h>\nconst unsigned v[]={'+','.join(names)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 c=dict(zip(names,struct.unpack('<'+str(len(names))+'I',(td/'c.bin').read_bytes())))
checks=[]
def check(n,v):checks.append(dict(test=n,passed=bool(v)));assert v,n
start(0)
wallet=rd(symbols['gSaveBlock1Ptr'])+c['offsetof(struct SaveBlock1,money)'];invoke('SetMoney',wallet,999999)
for badges in [0,1,2,3,4,8]:
 for i in range(8):invoke('FlagSet' if i<badges else 'FlagClear',c['FLAG_BADGE01_GET']+i)
 for item in mega+z:
  allowed=item not in reserved and badges>=(3 if item in mega else 2)
  check(f'{badges}_{item}_catalog',bool(invoke('LegendsStore_ItemAllowed',c[item]))==allowed)
  if not allowed:
   before=invoke('CountTotalItemQuantityInBag',c[item])
   check(f'{badges}_{item}_purchase_blocked',invoke('LegendsStore_Buy',c[item],1,99)==1 and invoke('GetMoney',wallet)==999999 and invoke('CountTotalItemQuantityInBag',c[item])==before)
invoke('FlagSet',c['FLAG_SYS_GAME_CLEAR'])
check('Champion_relics_stay_reserved',all(invoke('LegendsStore_ItemAllowed',c[x])==0 for x in reserved))
# Pre-owned reserved relics are retained: only acquisition through the Store changes.
invoke('AddBagItem',c['ITEM_MEWTWONITE_X'],1)
check('owned_relic_retained',invoke('CheckBagHasItem',c['ITEM_MEWTWONITE_X'],1)==1)
lib.shutdown()
start(0);invoke('FlagSet',c['FLAG_LA_RED_DEX_GIFTS']);invoke('FlagSet',c['FLAG_BADGE01_GET']);invoke('FlagSet',c['FLAG_BADGE02_GET'])
id=c['TRAINER_WATTSON_1'];base=symbols['gTrainers']+id*c['sizeof(struct Trainer)']
for i in range(24):
 invoke('LegendsTrainer_RollGymGimmick',id)
 check(f'first_attempt_{i}_Mega',invoke('LegendsTrainer_Gimmick',id)==4)
 t=invoke('LegendsTrainer_Get',id,base);team=rd(t+c['offsetof(struct Trainer,party)']);ace=team+5*c['sizeof(struct TrainerMon)']
 check(f'first_attempt_{i}_Manectric_stone',rd(ace+c['offsetof(struct TrainerMon,species)'],2)==c['SPECIES_MANECTRIC'] and rd(ace+c['offsetof(struct TrainerMon,heldItem)'],2)==c['ITEM_MANECTITE'])
 check(f'first_attempt_{i}_legal_team',all(invoke('LegendsTrainer_MemberLegal',team+j*c['sizeof(struct TrainerMon)']) for j in range(6)))
invoke('FlagSet',c['FLAG_BADGE03_GET']);seen=set()
for i in range(100):
 invoke('LegendsTrainer_RollGymGimmick',id);seen.add(invoke('LegendsTrainer_Gimmick',id))
check('post_badge_rotates_all_four',seen=={1,2,3,4})
lib.shutdown()
(D/'validation.json').write_text(json.dumps(dict(checks=checks,ordinary_mega_stones=len(mega)-10,ordinary_Z_crystals=len(z)-6,reserved=reserved,user_save_loaded=False,rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest()),indent=2)+'\n')
print('PASS',len(checks),'gimmick Store and Wattson checks',flush=True)
