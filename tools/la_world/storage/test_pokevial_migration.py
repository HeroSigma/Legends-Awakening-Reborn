"""Round-trip inventories from the pre-Pokevial build, without opening a player save.
Requires .la_work/pokevial/before.{gba,elf}, archived before this feature's build.
"""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'.la_work/pokevial';proof=R/'docs/features/pokevial';proof.mkdir(exist_ok=True)
current=dict(symbols)
def syms(path):return {z[2]:int(z[0],16) for line in subprocess.check_output(['arm-none-eabi-nm','--defined-only',str(path)],text=True).splitlines() if len(z:=line.split())==3}
old=syms(D/'before.elf');real_boot=lib.boot
symbols.clear();symbols.update(old)
lib.boot=lambda ignored:real_boot(str(D/'before.gba').encode())
items=[(6,17),(49,999),(873,1)]
images={}
for mode in [0,1]:
 start(0);invoke('StorageChangeMode',mode,1);invoke('ScriptGiveMon',4,16,0)
 for item,count in items:assert invoke('AddBagItem',item,count)
 assert invoke('StorageWriteMon',59 if mode else 13,29,symbols['gParties'])
 assert invoke('TrySavingData',0)==1
 image=bytearray()
 for sector in range(32):
  invoke('ReadFlash',sector,0,symbols['gSaveDataBuffer'],4096)
  image.extend(rd(symbols['gSaveDataBuffer']+i,1) for i in range(4096))
 images[mode]=bytes(image)
 lib.shutdown()
lib.boot=real_boot;symbols.clear();symbols.update(current)
for mode,image in images.items():
 assert lib.boot(str(R/'pokeemerald.gba').encode());frames(600)
 for sector in range(32):
  for i,v in enumerate(image[sector*4096:(sector+1)*4096]):wr(symbols['gSaveDataBuffer']+i,v,1)
  assert invoke('ProgramFlashSectorAndVerify',sector,symbols['gSaveDataBuffer'])==0
 check('old_save_loads_'+str(mode),invoke('LoadGameSave',0)==1)
 check('old_mode_'+str(mode),invoke('GetStorageBoxCount')==(60 if mode else 14))
 check('old_bag_active_'+str(mode),invoke('ExpandedBag_Active')==1)
 for item,count in items:check('old_item_'+str((mode,item)),invoke('CountTotalItemQuantityInBag',item)==count)
 check('new_item_starts_empty_'+str(mode),invoke('CountTotalItemQuantityInBag',874)==0)
 check('old_last_box_'+str(mode),invoke('GetBoxMonDataAt',59 if mode else 13,29,18)==4)
 invoke('AddBagItem',874,1);invoke('LegendsPokevialGrant')
 check('new_format_saves_'+str(mode),invoke('TrySavingData',0)==1)
 check('new_format_loads_'+str(mode),invoke('LoadGameSave',0)==1)
 for item,count in items:check('new_item_preserved_'+str((mode,item)),invoke('CountTotalItemQuantityInBag',item)==count)
 check('vial_saved_'+str(mode),invoke('CountTotalItemQuantityInBag',874)==1)
 check('boxed_saved_'+str(mode),invoke('GetBoxMonDataAt',59 if mode else 13,29,18)==4)
 lib.shutdown()
(proof/'migration-validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),old_rom_sha256=hashlib.sha256((D/'before.gba').read_bytes()).hexdigest(),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'old/new save checks')
