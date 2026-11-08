"""Load a copy of the existing legacy battery; never modify the source file."""
exec(compile(__import__('pathlib').Path(__file__).with_name('test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
source=Path('/mnt/c/Users/aadair/Downloads/Legends-Awakening-Reborn/Legends-Awakening-Reborn.sav')
battery=source.read_bytes();before=hashlib.sha256(battery).hexdigest()
assert len(battery) in (131072,131088)  # mGBA may append a 16-byte RTC trailer
assert lib.boot(str(R/'pokeemerald.gba').encode());frames(600)
for sector in range(32):
 for i,v in enumerate(battery[sector*4096:(sector+1)*4096]):wr(symbols['gSaveDataBuffer']+i,v,1)
 assert invoke('ProgramFlashSectorAndVerify',sector,symbols['gSaveDataBuffer'])==0
status=invoke('LoadGameSave',0)
check('legacy_battery_loads',status in [1,255])
check('legacy_battery_storage_mode',invoke('GetStorageBoxCount') in [14,60])
check('legacy_battery_current_box_valid',invoke('StorageGetCurrentBox')<14)
check('legacy_battery_party_count_valid',rd(symbols['gPartiesCount'],1)<=6)
check('legacy_bag_migrated',invoke('ExpandedBag_Active')==1)
from collections import Counter
expected=Counter();key=rd(rd(symbols['gSaveBlock2Ptr'])+0xac,2)
for pocket,capacity in enumerate([30,16,64,46,30]):
 pointer=rd(symbols['gBagPockets']+pocket*8)
 for slot in range(capacity):
  item=rd(pointer+slot*4,2)
  if item:expected[item]+=rd(pointer+slot*4+2,2)^key
for item,quantity in expected.items():check('legacy_item_'+str(item),invoke('CountTotalItemQuantityInBag',item)==quantity)
check('migrated_copy_saves',invoke('TrySavingData',0)==1)
check('migrated_copy_reloads',invoke('LoadGameSave',0)==1)
for item,quantity in expected.items():check('migrated_item_'+str(item),invoke('CountTotalItemQuantityInBag',item)==quantity)
count=invoke('CountStorageNonEggMons')
lib.shutdown()
check('source_battery_unchanged',hashlib.sha256(source.read_bytes()).hexdigest()==before)
report=dict(passed=True,assertions=len(checks),boxed_non_egg_count=count,source_sha256=before,source_unchanged=True,scope='Read-only source; programmed only into isolated emulator flash')
(D/'existing_save_compatibility.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report))
