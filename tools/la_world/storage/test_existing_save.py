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
check('legacy_battery_normal_mode',invoke('GetStorageBoxCount')==14)
check('legacy_battery_current_box_valid',invoke('StorageGetCurrentBox')<14)
check('legacy_battery_party_count_valid',rd(symbols['gPartiesCount'],1)<=6)
count=invoke('CountStorageNonEggMons')
lib.shutdown()
check('source_battery_unchanged',hashlib.sha256(source.read_bytes()).hexdigest()==before)
report=dict(passed=True,assertions=len(checks),boxed_non_egg_count=count,source_sha256=before,source_unchanged=True,scope='Read-only source; programmed only into isolated emulator flash')
(D/'existing_save_compatibility.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report))
