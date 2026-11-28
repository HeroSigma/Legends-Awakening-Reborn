"""Native TM mapping, compatibility, Store and actual Bag teaching regression."""
from pathlib import Path
import json,hashlib,tempfile,struct,subprocess,shutil
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'docs/features/tm-expansion';D.mkdir(parents=True,exist_ok=True)
checks=[]
def check(n,v):
 checks.append(dict(test=n,passed=bool(v)));assert v,n
rows=json.loads((D/'tm51-100.json').read_text())
# Independent canonical learnables determine a compatible sample for every move.
import re
learn=json.loads((R/'src/data/pokemon/all_learnables.json').read_text());species=(R/'include/constants/species.h').read_text()
preferred=['CHARIZARD','VENUSAUR','BLASTOISE','PIKACHU','ALAKAZAM','GENGAR','SCYTHER','CLEFABLE','GYARADOS','SNORLAX','GARCHOMP','DRAGONITE','STEELIX','LUCARIO','GARDEVOIR','TOGEKISS','LAPRAS','CORVIKNIGHT']
for v in rows:v['test_species']=next(x for x in preferred+list(learn) if 'MOVE_'+v['move'] in learn.get(x,[]) and re.search(r'\bSPECIES_'+re.escape(x)+r'\b',species))
names=['NUM_TECHNICAL_MACHINES','NUM_HIDDEN_MACHINES','ITEM_TM01','ITEM_TM50','ITEM_TM51','ITEM_TM100','ITEM_HM01','ITEM_HM08','BAG_MACHINES','ITEMMENULOCATION_FIELD','SPECIES_CHARIZARD','SPECIES_MAGIKARP','MON_DATA_MOVE1','offsetof(struct SaveBlock1,money)']
for v in rows:names+=['ITEM_TM_'+v['move'],'MOVE_'+v['move'],'SPECIES_'+v['test_species']]
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "item.h"\n#include "item_menu.h"\n#include "bag_categories.h"\n#include "pokemon.h"\n#include <stddef.h>\nconst unsigned v[]={'+','.join(names)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 c=dict(zip(names,struct.unpack('<'+str(len(names))+'I',(td/'c.bin').read_bytes())))
start(0)
check('100_TMs',c['NUM_TECHNICAL_MACHINES']==100)
check('8_HMs',c['NUM_HIDDEN_MACHINES']==8)
check('stable_item_IDs',[c[x] for x in ['ITEM_TM01','ITEM_TM50','ITEM_TM51','ITEM_TM100','ITEM_HM01','ITEM_HM08']]==[582,631,632,681,682,689])
for v in rows:
 tag='TM'+str(v['tm']);item=c['ITEM_TM_'+v['move']];move=c['MOVE_'+v['move']]
 check(tag+'_move',invoke('ItemIdToBattleMoveId',item)==move)
 check(tag+'_learnable',invoke('CanLearnTeachableMove',c['SPECIES_'+v['test_species']],move)==1)
 check(tag+'_description',rd(invoke('GetItemDescription',item),1)!=0xac) # '?' is 0xAC
 check(tag+'_price',invoke('GetItemPrice',item)==v['base_price'])
 check(tag+'_icon',invoke('GetItemIconPic',item)!=0 and invoke('GetItemIconPalette',item)!=0)
 check(tag+'_reusable',invoke('GetItemImportance',item)==1)
 check(tag+'_machine_pocket',invoke('GetItemBagCategory',item)==c['BAG_MACHINES'])
 check(tag+'_store',invoke('LegendsStore_ItemAllowed',item)==1)
 cat=c['BAG_MACHINES'];regular=invoke('LegendsStore_Price',item,99);sale=invoke('LegendsStore_Price',item,cat)
 check(tag+'_sale',sale==v['base_price'] and regular>sale)
 invoke('SetMoney',rd(symbols['gSaveBlock1Ptr'])+c['offsetof(struct SaveBlock1,money)'],999999)
 check(tag+'_purchase',invoke('LegendsStore_Buy',item,1,99)==0)
 check(tag+'_sold_out',invoke('LegendsStore_Buy',item,1,99)==1 and invoke('CountTotalItemQuantityInBag',item)==1)
for item in range(c['ITEM_HM01'],c['ITEM_HM08']+1):check('HM_excluded_'+str(item),invoke('LegendsStore_ItemAllowed',item)==0)
check('no_blank_TM_moves',all(invoke('ItemIdToBattleMoveId',item)!=0 for item in range(c['ITEM_TM01'],c['ITEM_TM100']+1)))
check('Magikarp_not_Roost',invoke('CanLearnTeachableMove',c['SPECIES_MAGIKARP'],c['MOVE_ROOST'])==0)
check('Magikarp_not_Moonblast',invoke('CanLearnTeachableMove',c['SPECIES_MAGIKARP'],c['MOVE_MOONBLAST'])==0)
# Teach Roost from the real Bag, with an empty move slot to avoid replacement.
invoke('ClearBag');invoke('AddBagItem',c['ITEM_TM_ROOST'],1);invoke('ScriptGiveMon',c['SPECIES_CHARIZARD'],25,0)
party=symbols['gParties'];V=0x03007600;wr(V,0)
for i in range(4):invoke('SetMonData',party,c['MON_DATA_MOVE1']+i,V)
check('empty_move_slot_ready',invoke('GetMonData3',party,c['MON_DATA_MOVE1'],0)==0)
invoke('GoToBagMenu',c['ITEMMENULOCATION_FIELD'],c['BAG_MACHINES'],symbols['CB2_ReturnToField'])
wr(symbols['gMain']+0x438,0,1);wr(symbols['gMain']+4,symbols['CB2_Bag']|1)
wait('Task_BagMenu_HandleInput',900);frames(60);shutil.copy2(shot('tm_roost_bag'),D/'roost-bag.png');tap(1);frames(30);tap(1)
frames(180)
for i in range(30):
 tap(1);frames(90)
 if invoke('GetMonData3',party,c['MON_DATA_MOVE1'],0)==c['MOVE_ROOST']:break
else:raise AssertionError('Roost Bag teaching timed out')
frames(45);shutil.copy2(shot('tm_roost_taught'),D/'roost-taught.png')
check('actual_Bag_teaches_Roost',invoke('GetMonData3',party,c['MON_DATA_MOVE1'],0)==c['MOVE_ROOST'])
check('TM_retained_after_teaching',invoke('CountTotalItemQuantityInBag',c['ITEM_TM_ROOST'])==1)
lib.shutdown()
(D/'validation.json').write_text(json.dumps(dict(checks=checks,user_save_loaded=False,rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest()),indent=2)+'\n')
print('PASS',len(checks),'TM expansion checks',flush=True)
