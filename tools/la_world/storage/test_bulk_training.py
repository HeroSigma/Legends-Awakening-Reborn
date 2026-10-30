"""Bulk training limits, native effects and quantity UI, with isolated saves."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_preferred_follower.py').read_text().split('for mode in [0,1]:')[0],'helpers','exec'))
names=['ITEM_RARE_CANDY','ITEM_EXP_CANDY_XL','ITEM_PROTEIN','ITEM_HP_UP','ITEM_IRON','ITEM_CARBOS','ITEM_CALCIUM','ITEM_ZINC','MON_DATA_HP_EV','MON_DATA_ATK_EV','MON_DATA_DEF_EV','MON_DATA_SPEED_EV','MON_DATA_SPATK_EV','MON_DATA_SPDEF_EV','MON_DATA_LEVEL','FLAG_LA_RED_DEX_GIFTS','FLAG_SYS_POKEMON_GET']
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'b.c').write_text('#include "global.h"\n#include "pokemon.h"\n#include "constants/items.h"\n#include "constants/flags.h"\nconst unsigned v[]={'+','.join(names)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'b.c'),'-o',str(td/'b.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'b.o'),str(td/'b.bin')],check=True)
 c=dict(zip(names,struct.unpack('<'+str(len(names))+'I',(td/'b.bin').read_bytes())))
D=R/'docs/features/bulk-training';D.mkdir(exist_ok=True)
for mode in [0,1]:
 start(0);invoke('StorageChangeMode',mode,1);invoke('FlagSet',c['FLAG_LA_RED_DEX_GIFTS']);invoke('ScriptGiveMon',25,5,0)
 p=symbols['gParties'];a=0x0203fc00
 for item in names[:8]:invoke('AddBagItem',c[item],100)
 for item,ev in zip(['ITEM_HP_UP','ITEM_PROTEIN','ITEM_IRON','ITEM_CARBOS','ITEM_CALCIUM','ITEM_ZINC'],names[8:14]):
  for stat in names[8:14]:
   wr(a,0);invoke('SetMonData',p,c[stat],a)
  check('vitamin_max_'+str((mode,item)),invoke('TrainingItem_MaxQuantity',p,c[item])==26)
  check('vitamin_used_'+str((mode,item)),invoke('TrainingItem_Apply',p,c[item],0,100)==26)
  check('vitamin_252_'+str((mode,item)),invoke('GetMonData3',p,c[ev],0)==252)
  check('vitamin_full_'+str((mode,item)),invoke('TrainingItem_MaxQuantity',p,c[item])==0)
 # 508 total EVs: one item can use the final two points, never exceed 510.
 for stat in names[8:14]:
  wr(a,0);invoke('SetMonData',p,c[stat],a)
 for stat,value in [('MON_DATA_HP_EV',252),('MON_DATA_ATK_EV',252),('MON_DATA_DEF_EV',4)]:
  wr(a,value);invoke('SetMonData',p,c[stat],a)
 check('total_room_'+str(mode),invoke('TrainingItem_MaxQuantity',p,c['ITEM_IRON'])==1)
 check('total_used_'+str(mode),invoke('TrainingItem_Apply',p,c['ITEM_IRON'],0,100)==1)
 check('total_510_'+str(mode),invoke('GetMonEVCount',p)==510)
 check('rare_limit_'+str(mode),invoke('TrainingItem_MaxQuantity',p,c['ITEM_RARE_CANDY'])==11)
 check('rare_used_'+str(mode),invoke('TrainingItem_Apply',p,c['ITEM_RARE_CANDY'],0,100)==11)
 check('rare_cap_'+str(mode),invoke('GetMonData3',p,c['MON_DATA_LEVEL'],0)==16)
 check('no_candy_at_cap_'+str(mode),invoke('TrainingItem_Apply',p,c['ITEM_EXP_CANDY_XL'],0,10)==0)
 invoke('ScriptGiveMon',25,5,0)
 check('xl_limit_'+str(mode),invoke('TrainingItem_MaxQuantity',p+100,c['ITEM_EXP_CANDY_XL'])==1)
 check('xl_consumes_only_one_'+str(mode),invoke('TrainingItem_Apply',p+100,c['ITEM_EXP_CANDY_XL'],1,100)==1)
 check('xl_stops_at_cap_'+str(mode),invoke('GetMonData3',p+100,c['MON_DATA_LEVEL'],0)==16)
 lib.shutdown()
# Actual party quantity input: cancelling consumes nothing, confirming two Rare
# Candies consumes exactly two and uses the existing move/evolution flow.
start(0);invoke('FlagSet',c['FLAG_LA_RED_DEX_GIFTS']);invoke('FlagSet',c['FLAG_SYS_POKEMON_GET']);invoke('ScriptGiveMon',25,5,0)
p=symbols['gParties'];item=c['ITEM_RARE_CANDY'];invoke('AddBagItem',item,10)
wr(symbols['sStartMenuPage'],0,1);wr(symbols['sStartMenuCursorPos'],0,1)
tap(8);frames(45);tap(1);frames(150)
task=wait('Task_HandleChooseMonInput');wr(symbols['gSpecialVar_ItemId'],item,2)
invoke('ItemUseCB_RareCandy',task,symbols['Task_ReturnToChooseMonAfterText']|1);frames(180)
check('quantity_open',active('Task_GiveHowManyItemsHandleInput' if 'Task_GiveHowManyItemsHandleInput' in symbols else 'Task_BulkTrainingInput') is not None)
shutil.copy2(shot('bulk_quantity'),D/'quantity.png')
tap(2);frames(30)
check('cancel_keeps_items',invoke('CountTotalItemQuantityInBag',item)==10)
check('cancel_keeps_level',invoke('GetMonData3',p,c['MON_DATA_LEVEL'],0)==5)
invoke('ItemUseCB_RareCandy',task,symbols['Task_ReturnToChooseMonAfterText']|1);frames(180)
tap(64);frames(180)
tap(1);frames(180)
shutil.copy2(shot('bulk_result'),D/'result.png')
check('two_candies_consumed',invoke('CountTotalItemQuantityInBag',item)==8)
check('two_levels_gained',invoke('GetMonData3',p,c['MON_DATA_LEVEL'],0)==7)
lib.shutdown()
(D/'validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'bulk training checks')
