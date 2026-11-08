"""Regression: colliding personality/OT keys must not select an earlier species."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_preferred_follower.py').read_text().split('for mode in [0,1]:')[0],'follower_helpers','exec'))
for mode in [0,1]:
 start(0);invoke('StorageChangeMode',mode,1)
 species=[256,657,811,559,903,679]
 p=symbols['gParties'];scratch=0x0203fc00
 for sp in species:invoke('ScriptGiveMon',sp,20,0)
 # Compact/debug Pokémon can share these values. Match the user's party order.
 template=bytes(rd(p+j,1) for j in range(100))
 for slot,sp in enumerate(species):
  for j,value in enumerate(template):wr(p+slot*100+j,value,1)
  wr(scratch,sp);invoke('SetMonData',p+slot*100,c['MON_DATA_SPECIES'],scratch)
  invoke('CalculateMonStats',p+slot*100)
 for slot in range(6):
  check('choose_'+str((mode,slot)),invoke('PreferredFollower_Set',slot)==1)
  check('exact_slot_'+str((mode,slot)),invoke('GetFirstLiveMon')==p+slot*100)
  check('species_'+str((mode,slot)),invoke('GetMonData3',invoke('GetFirstLiveMon'),c['MON_DATA_SPECIES'],0)==species[slot])
 invoke('PreferredFollower_Set',4)
 # Sneasler still follows after swapping its slot with Scraggy.
 before=[bytes(rd(p+i*100+j,1) for j in range(100)) for i in [3,4]]
 for slot,mon in zip([4,3],before):
  for j,value in enumerate(mon):wr(p+slot*100+j,value,1)
 check('sneasler_after_swap_'+str(mode),invoke('GetFirstLiveMon')==p+300)
 check('save_'+str(mode),invoke('TrySavingData',0)==1)
 invoke('PreferredFollower_Automatic')
 check('load_'+str(mode),invoke('LoadGameSave',0)==1)
 check('sneasler_after_reload_'+str(mode),invoke('GetFirstLiveMon')==p+300)
 lib.shutdown()
(D/'collision-validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'collision checks')
