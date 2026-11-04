"""Invalid legacy IDs must not reach bag item metadata assertions."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_bag_categories.py').read_text().split('for mode in [0,1]:')[0],'helpers','exec'))
D=R/'docs/fixes/intro-bag';D.mkdir(parents=True,exist_ok=True)
checks=[]
for mode in [0,1]:
 start(0);invoke('StorageChangeMode',mode,1);invoke('ClearBag');invoke('ScriptGiveMon',4,16,0)
 invoke('AddBagItem',874,1)
 for item in [0,8249,65535,c['ITEMS_COUNT']]:
  check(f'invalid_category_{mode}_{item}',invoke('GetItemBagCategory',item)==c['BAG_CATEGORIES_COUNT'])
 # Inject the reported malformed ID into an isolated legacy slot. Keep an
 # adjacent valid Pokévial and verify browsing does not discard that item.
 invoke('ExpandedBag_Suspend')
 slots=rd(symbols['gBagPockets']);wr(slots,8249,2)
 for category_id in range(c['BAG_CATEGORIES_COUNT']):invoke('BagCategory_Count',category_id)
 openbag();closebag()
 check(f'legacy_invalid_does_not_reset_{mode}',rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1)
 invoke('ExpandedBag_Resume')
 check(f'vial_preserved_{mode}',invoke('CountTotalItemQuantityInBag',874)==1)
 for i in range(c['BAG_CATEGORIES_COUNT']):openbag(i);closebag()
 check(f'vial_still_preserved_{mode}',invoke('CountTotalItemQuantityInBag',874)==1)
 lib.shutdown()
(D/'bag-invalid-validation.json').write_text(json.dumps(dict(rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'invalid bag slot checks',flush=True)
