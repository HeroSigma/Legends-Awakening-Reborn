"""Shared relic policy, Store and native Mart filtering/payment/save regressions."""
from pathlib import Path
import tempfile,struct,json,hashlib,re
R=Path.cwd()
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'docs/features/quest-relic-shops';D.mkdir(parents=True,exist_ok=True)
# Independent acquisition manifest from the approved relic plan and form audit.
explicit=['ITEM_'+x for x in [
 'RED_ORB','BLUE_ORB','SOUL_DEW','ADAMANT_ORB','LUSTROUS_ORB','GRISEOUS_ORB',
 'ADAMANT_CRYSTAL','LUSTROUS_GLOBE','GRISEOUS_CORE','RUSTED_SWORD','RUSTED_SHIELD',
 'WELLSPRING_MASK','HEARTHFLAME_MASK','CORNERSTONE_MASK','SCROLL_OF_DARKNESS','SCROLL_OF_WATERS',
 'METEORITE','GRACIDEA','REVEAL_GLASS','DNA_SPLICERS','ZYGARDE_CUBE','PRISON_BOTTLE',
 'N_SOLARIZER','N_LUNARIZER','REINS_OF_UNITY','EON_TICKET','MYSTIC_TICKET','AURORA_TICKET','OLD_SEA_MAP',
 'MEWTWONITE_X','MEWTWONITE_Y','LATIASITE','LATIOSITE','DIANCITE','ZYGARDITE',
 'HEATRANITE','DARKRANITE','ZERAORITE','MAGEARNITE','MEWNIUM_Z','TAPUNIUM_Z',
 'SOLGANIUM_Z','LUNALIUM_Z','MARSHADIUM_Z','ULTRANECROZIUM_Z']]

items=(R/'src/data/items.h').read_text()
classes={kind:re.findall(r'\[(ITEM_\w+)\]\s*=\s*\{[^}]*?\.sortType = ITEM_TYPE_'+kind,items,re.S) for kind in ['PLATE','MEMORY','DRIVE']}
reserved=list(dict.fromkeys(explicit+sum(classes.values(),[])))
ordinary=['ITEM_'+x for x in ['POTION','POKE_BALL','LIFE_ORB','FLAME_ORB','TOXIC_ORB','ADRENALINE_ORB','ADAMANT_MINT','MANECTITE','ELECTRIUM_Z','CHOICE_BAND','CHOICE_SPECS','CHOICE_SCARF','CHARCOAL','MYSTIC_WATER','RELIC_COPPER','DOME_FOSSIL','BOTTLE_CAP','GOLD_BOTTLE_CAP']]
names=list(dict.fromkeys(['FLAG_BADGE01_GET','FLAG_SYS_GAME_CLEAR','offsetof(struct SaveBlock1,money)']+reserved+ordinary))
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "item.h"\n#include "constants/flags.h"\n#include <stddef.h>\nconst unsigned v[]={'+','.join(names)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 c=dict(zip(names,struct.unpack('<'+str(len(names))+'I',(td/'c.bin').read_bytes())))
checks=[]
def check(n,v):checks.append(dict(test=n,passed=bool(v)));assert v,n
start(0)
check('17_Plates',len(classes['PLATE'])==17);check('17_Memories',len(classes['MEMORY'])==17);check('4_Drives',len(classes['DRIVE'])==4)
wallet=rd(symbols['gSaveBlock1Ptr'])+c['offsetof(struct SaveBlock1,money)'];invoke('SetMoney',wallet,999999)
for milestone in [0,8,9]:
 for i in range(8):invoke('FlagSet' if milestone>=8 else 'FlagClear',c['FLAG_BADGE01_GET']+i)
 if milestone==9:invoke('FlagSet',c['FLAG_SYS_GAME_CLEAR'])
 for x in reserved:
  item=c[x]
  check(f'{milestone}_{x}_classified',invoke('Item_IsQuestRelic',item)==1)
  check(f'{milestone}_{x}_not_listed',invoke('LegendsStore_ItemAllowed',item)==0)
  check(f'{milestone}_{x}_no_quoted_price',invoke('LegendsStore_Price',item,99)==0)
  before=invoke('CountTotalItemQuantityInBag',item)
  check(f'{milestone}_{x}_buy_refused',invoke('LegendsStore_Buy',item,1,99)==1 and invoke('CountTotalItemQuantityInBag',item)==before and invoke('GetMoney',wallet)==999999)
for x in ordinary:
 check(x+'_ordinary_classification',invoke('Item_IsQuestRelic',c[x])==0)
 check(x+'_Champion_still_sold',invoke('LegendsStore_ItemAllowed',c[x])==1)
# Script/quest awards and old ownership stay possible, and survive save/load.
for x in reserved:check(x+'_can_be_awarded',invoke('AddBagItem',c[x],1)==1)
check('save',invoke('TrySavingData',0)==1)
for x in reserved:invoke('RemoveBagItem',c[x],1)
check('reload',invoke('LoadGameSave',0)==1)
for x in reserved:check(x+'_ownership_persists',invoke('CheckBagHasItem',c[x],1)==1)
# Exercise the real shared dynamic Mart list, including an all-relic empty list.
A=0x03007400;P=0x03007600;N=P+4
for label,source in [('mixed',reserved+ordinary),('empty',reserved)]:
 for i,x in enumerate(source):wr(A+i*2,c[x],2)
 wr(A+len(source)*2,0,2);wr(P,A);wr(N,len(source),2)
 invoke('TryBuildDynamicShopItemList',P,N)
 count=rd(N,2);ptr=rd(P);found=[rd(ptr+i*2,2) for i in range(count)]
 expected=[c[x] for x in source if x not in reserved]
 check(label+'_native_Mart_catalog',found==expected and rd(ptr+count*2,2)==0)
 invoke('TryFreeDynamicShopItemList',P)
 check(label+'_original_catalog_restored',rd(P)==A)
lib.shutdown()
# Live native Mart: a forbidden ID injected at payment must fail without charging.
start(0);wallet=rd(symbols['gSaveBlock1Ptr'])+c['offsetof(struct SaveBlock1,money)'];invoke('SetMoney',wallet,999999)
for i,x in enumerate(['ITEM_POTION','ITEM_RED_ORB','ITEM_LIFE_ORB']):wr(A+i*2,c[x],2)
wr(A+6,0,2);invoke('CreatePokemartMenu',A);frames(40);tap(1);frames(240)
tid=wait('Task_BuyMenu',1200)
# Native MartInfo ABI: callback, menuActions, itemList pointer, itemCount.
mi=symbols['sMartInfo'];ptr=rd(mi+8);count=rd(mi+12,2)
check('live_Mart_hides_RedOrb',count==2 and [rd(ptr+i*2,2) for i in range(count)]==[c['ITEM_POTION'],c['ITEM_LIFE_ORB']])
shutil.copy2(shot('relic_filtered_Mart'),D/'ordinary-mart.png')
wr(symbols['gTasks']+tid*40+8+5*2,c['ITEM_RED_ORB'],2);wr(symbols['gTasks']+tid*40+8+1*2,1,2)
invoke('BuyMenuTryMakePurchase',tid);frames(120)
check('live_Mart_injected_relic_refused',invoke('CountTotalItemQuantityInBag',c['ITEM_RED_ORB'])==0 and invoke('GetMoney',wallet)==999999)
lib.shutdown()
(D/'validation.json').write_text(json.dumps(dict(checks=checks,reserved_items=reserved,class_counts={k:len(v) for k,v in classes.items()},user_save_loaded=False,rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest()),indent=2)+'\n')
print('PASS',len(checks),'relic shop checks;',len(reserved),'reserved items',flush=True)
