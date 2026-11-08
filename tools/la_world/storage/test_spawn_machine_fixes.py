"""Crowded-map spawn guard and blank-machine cleanup in isolated native mGBA."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
import tempfile,struct
names=['ITEM_TM01','ITEM_TM50','ITEM_TM51','ITEM_TM100','ITEM_HM01','ITEM_HM08','BAG_CATEGORIES_COUNT','BAG_MACHINES','ITEMS_COUNT','OBJECT_EVENTS_COUNT','sizeof(struct ObjectEvent)','OWE_RESERVED_OBJECT_SLOTS','OWE_SPAWNS_MAX','MAP_GROUP(MAP_ROUTE116)','MAP_NUM(MAP_ROUTE116)']
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "item.h"\n#include "bag_categories.h"\n#include "wild_encounter_ow.h"\n#include "constants/maps.h"\nconst unsigned v[]={'+','.join(names)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 c=dict(zip(names,struct.unpack('<'+str(len(names))+'I',(td/'c.bin').read_bytes())))
invalid=range(c['ITEM_TM51'],c['ITEM_TM100']+1)
valid=list(range(c['ITEM_TM01'],c['ITEM_TM50']+1))+list(range(c['ITEM_HM01'],c['ITEM_HM08']+1))
for mode in [0,1]:
 start(0);invoke('StorageChangeMode',mode,1);invoke('ClearBag')
 for item in invalid:invoke('AddBagItem',item,1)
 check('fill_machine_'+str(mode),invoke('Debug_FillBagCategory',c['BAG_MACHINES'])==len(valid))
 for item in invalid:check('blank_removed_'+str((mode,item)),invoke('CountTotalItemQuantityInBag',item)==0)
 for item in valid:check('valid_machine_'+str((mode,item)),invoke('CountTotalItemQuantityInBag',item)==1)
 invoke('Debug_FillBagCategory',c['BAG_CATEGORIES_COUNT'])
 check('all_category_count_'+str(mode),sum(invoke('BagCategory_Count',i) for i in range(c['BAG_CATEGORIES_COUNT']))==c['ITEMS_COUNT']-1-len(invalid))
 check('fill_repeat_'+str(mode),invoke('Debug_FillBagCategory',c['BAG_CATEGORIES_COUNT'])==0)
 check('save_'+str(mode),invoke('TrySavingData',0)==1)
 invoke('ClearBag');check('reload_'+str(mode),invoke('LoadGameSave',0)==1)
 check('machines_survive_'+str(mode),invoke('BagCategory_Count',c['BAG_MACHINES'])==len(valid))
 lib.shutdown()
start(0)
# Exercise the guard with every near-full object-table boundary. Restore before normal frames.
base=symbols['gObjectEvents'];size=c['sizeof(struct ObjectEvent)'];count=c['OBJECT_EVENTS_COUNT']
backup=bytes(rd(base+i,1) for i in range(size*count))
for free in [0,1,2,3,count]:
 for i in range(size*count):wr(base+i,0,1)
 for i in range(count-free):wr(base+i*size,1,1)
 check('free_slots_'+str(free),invoke('HasRoomForGeneratedOWE')==int(free>c['OWE_RESERVED_OBJECT_SLOTS']))
 for i,b in enumerate(backup):wr(base+i,b,1)
invoke('ScriptGiveMon',1,10,0);invoke('ScriptContext_Init');invoke('UnlockPlayerFieldControls')
warp(c['MAP_GROUP(MAP_ROUTE116)'],c['MAP_NUM(MAP_ROUTE116)'],10,12)
maximum=0
for _ in range(120):
 frames(30)
 n=invoke('GetNumberOfActiveOWEs',1);maximum=max(maximum,n)
 check('visible_limit_'+str(_),n<=c['OWE_SPAWNS_MAX'])
check('route_still_running',rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1)
lib.shutdown()
(R/'docs/features/spawn-machine-validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),maximum_route116_spawns=maximum,checks=checks),indent=2)+'\n')
print('PASS',len(checks),'spawn and machine checks; max wild spawns',maximum)
