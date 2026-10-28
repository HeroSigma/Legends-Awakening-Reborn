"""Production PC/save/menu integration tests. Uses an isolated emulator battery."""
from pathlib import Path
import sys, json, hashlib, shutil, re
R=Path('/home/allan/projects/Legends-Awakening-Reborn')
H=R/'tools/la_world/importers/amap/hns_runtime'
sys.path.insert(0,str(H))
exec(compile((H/'test_legends_bedroom.py').read_text().split('for gender in [0,1]:')[0],'bedroom_helpers','exec'))
exec(compile((H/'test_protagonist_assets.py').read_text().split("D=R/'docs/art/protagonists/trainer_draft'")[0].replace('BASE=0x0203f000','BASE=0x03007000').replace('frames(1)\n assert rd(RESULT)', 'frames(1)\n for retry in range(3600):\n  if rd(RESULT)!=0xdeadbeef:break\n  frames(1)\n assert rd(RESULT)'),'arm_helpers','exec'))
D=R/'docs/la_world/compact_pc/integration';D.mkdir(parents=True,exist_ok=True)
checks=[]
def check(n,v):
 checks.append(dict(test=n,passed=bool(v)))
 assert v,n
def capture(n):shutil.copy2(shot('pc_'+n),D/(n+'.png'))
def active(name):return next((j for j in range(16) if rd(symbols['gTasks']+j*40+4,1) and rd(symbols['gTasks']+j*40)==symbols[name]|1),None)
def wait(name,limit=500):
 for i in range(limit):
  if active(name) is not None:return active(name)
  frames(1)
 raise AssertionError(('missing task',name,hex(rd(symbols['gMain']+4))))
def open_options(callback='CB2_ReturnToField'):
 wr(symbols['gMain']+8,symbols[callback]|1)
 wr(symbols['gMain']+0x438,0,1);wr(symbols['gMain']+4,symbols['CB2_InitOptionMenu']|1)
 tid=wait('Task_OptionMenuProcessInput')
 for i in range(6):tap(128)
 return tid
start(0)
check('normal_default_14',invoke('GetStorageBoxCount')==14)
invoke('ScriptGiveMon',265,10,0)
A=0x0203fc00;B=A+0x100;V=A+0x200
party=symbols['gParties']
for i in range(80):wr(A+i,rd(party+i,1),1)
wr(V,5);invoke('SetBoxMonData',A,8,V)
# Cancellation in Options must preserve a specimen and the current profile.
invoke('StorageWriteMon',0,0,A)
open_options();capture('options_14');tap(1);frames(20);capture('warning_1');tap(2);frames(20)
check('cancel_keeps_mode',invoke('GetStorageBoxCount')==14)
check('cancel_keeps_mon',invoke('GetBoxMonDataAt',0,0,18)==265)
# New mode is enabled through the real two-stage warning, not a test-only switch.
tap(1);frames(15);tap(1);frames(15);capture('warning_erase');tap(1);frames(15);capture('enabled_60');tap(1);frames(20)
check('options_enable_60',invoke('GetStorageBoxCount')==60)
check('confirmed_clears_boxes',invoke('GetBoxMonDataAt',0,0,18)==0)
tap(2);frames(180)
# Fill every native accessor slot; verify identities using per-slot friendship.
for index in range(1800):
 wr(V,index%256);invoke('SetBoxMonData',A,39,V)
 invoke('StorageWriteMon',index//30,index%30,A)
scan_before=rd(symbols['gMain']+0x24)
check('all_1800_filled',invoke('CountStorageNonEggMons')==1800)
scan_frames=(rd(symbols['gMain']+0x24)-scan_before)&0xffffffff
print('FULL PC SCAN FRAMES',scan_frames,flush=True)
check('full_pc_scan_under_200ms',scan_frames<12)
check('full_pc_has_no_free_slot',invoke('CheckFreePokemonStorageSpace')==0)
check('last_box_accessible',invoke('GetBoxMonDataAt',59,29,18)==265)
check('last_slot_trait',invoke('GetBoxMonDataAt',59,29,39)==1799%256)
check('flush',invoke('StorageFlush')==1)
# Exercise the real PC screen at the final box and wrap through its boundaries.
wr(rd(symbols['gPokemonStoragePtr']),59,1)
invoke('ShowPokemonStorageSystemPC');frames(90);tap(128);tap(128);tap(1)
wait('Task_PokeStorageMain',900);frames(90);capture('pc_box60')
check('pc_last_box_display',invoke('StorageGetCurrentBox')==59)
tap(64);tap(16);frames(120);capture('pc_wrap_box1')
check('pc_wrap_forward',invoke('StorageGetCurrentBox')==0)
tap(32);frames(120);tap(128)
check('pc_wrap_backward',invoke('StorageGetCurrentBox')==59)
# Leave PC through its normal exit prompt and restore overworld control.
tap(2);frames(30);tap(1);frames(240);tap(2);frames(180)
check('pc_visit_keeps_all_slots',invoke('CountStorageNonEggMons')==1800)

# Native save-memory relocation must not drop the decoded box cache.
ptr=invoke('GetBoxedMonPtr',59,29);wr(V,237);invoke('SetBoxMonData',ptr,39,V)
invoke('MoveSaveBlocks_ResetHeap')
check('aslr_preserves_cache_edits',invoke('GetBoxMonDataAt',59,29,39)==237)
check('collection_save',invoke('TrySavingData',0)==1)
capture('collection_saved')
# Loading must choose the expanded profile and restore all slots.
invoke('StorageInitialize')
check('ram_reset_normal',invoke('GetStorageBoxCount')==14)
check('load_collection',invoke('LoadGameSave',0)==1)
check('loaded_60',invoke('GetStorageBoxCount')==60)
check('collection_markings_persist',invoke('GetBoxMonDataAt',59,29,8)==5)
check('loaded_count_1800',invoke('CountStorageNonEggMons')==1800)
for index in range(1800):
 expected=237 if index==1799 else index%256
 check('loaded_slot_'+str(index),invoke('GetBoxMonDataAt',index//30,index%30,39)==expected)
wr(V,222);invoke('SetBoxMonDataAt',0,0,39,V)
check('second_collection_save',invoke('TrySavingData',0)==1)
# Corrupt a sector in the newest bank; recover the previous complete save.
latest_counter=rd(symbols['gSaveCounter'])
sector=(latest_counter%2)*16+(latest_counter%16)
invoke('ReadFlash',sector,0,symbols['gSaveDataBuffer'],4096)
backup=bytes(rd(symbols['gSaveDataBuffer']+i,1) for i in range(4096))
wr(symbols['gSaveDataBuffer']+256,backup[256]^1,1)
check('inject_corrupt_sector',invoke('ProgramFlashSectorAndVerify',sector,symbols['gSaveDataBuffer'])==0)
check('recover_previous_bank',invoke('LoadGameSave',0)==1)
check('recovery_uses_previous_generation',rd(symbols['gSaveCounter'])==latest_counter-1)
check('recovery_keeps_previous_trait',invoke('GetBoxMonDataAt',0,0,39)==0)
for i,v in enumerate(backup):wr(symbols['gSaveDataBuffer']+i,v,1)
check('restore_test_sector',invoke('ProgramFlashSectorAndVerify',sector,symbols['gSaveDataBuffer'])==0)
check('restored_latest_load',invoke('LoadGameSave',0)==1)
check('latest_trait_after_restore',invoke('GetBoxMonDataAt',0,0,39)==222)
# An independent host decoder must agree with the live flash layout.
from collection_format import newest, decode_slot
image=bytearray()
for sector_id in range(32):
 invoke('ReadFlash',sector_id,0,symbols['gSaveDataBuffer'],4096)
 image.extend(rd(symbols['gSaveDataBuffer']+j,1) for j in range(4096))
schema=json.loads((R/'docs/la_world/compact_pc/layout_audit.json').read_text())
bank,decoded=newest(schema,bytes(image))
check('independent_flash_decoder',decoded['counter']==latest_counter and len(decoded['pc'])==56804)
check('independent_profile_header',decoded['pc'][1:4]==bytes([1,2,0]))


# Continue after a real soft reset uses the same profile detection.
frames(20,15);frames(600)
for i in range(5000):
 if rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1:break
 frames(1,8 if i%120==0 else 1 if i%120==60 else 0)
else:raise AssertionError('collection continue timed out')
frames(90);capture('continued_60')
check('continue_60',invoke('GetStorageBoxCount')==60)
check('continue_all_slots',invoke('CountStorageNonEggMons')==1800)
# Switch back through the tested core, save, and load original-format storage.
check('switch_back_normal',invoke('StorageChangeMode',0,1)==1)
check('normal_conversion_save',invoke('TrySavingData',0)==1)
check('normal_reload',invoke('LoadGameSave',0)==1)
check('normal_mode_restored',invoke('GetStorageBoxCount')==14)
check('normal_boxed_cleared',invoke('CountStorageNonEggMons')==0)
for i in range(80):wr(A+i,rd(party+i,1),1)
invoke('StorageWriteMon',13,29,A)
check('normal_save_again',invoke('TrySavingData',0)==1)
for i in range(80):wr(B+i,0,1)
invoke('StorageWriteMon',13,29,B)
check('normal_load_again',invoke('LoadGameSave',0)==1)
check('normal_legacy_metadata_and_boxes',invoke('GetBoxMonDataAt',13,29,18)==265)
gates=json.loads((R/'docs/la_world/compact_pc/retired_feature_gates.json').read_text())
for special in gates['specials']:
 check('special_id_'+special['name'],symbols['SPECIAL_'+special['name']]==special['index'])
 check('normal_activity_'+special['name'],invoke('LaPcBlockedSpecial',special['index'])==0)
check('enable_for_activity_gates',invoke('StorageChangeMode',1,1)==1)
for special in gates['specials']:check('collection_activity_'+special['name'],invoke('LaPcBlockedSpecial',special['index'])==1)

# Eggs retain hatch progress and both native egg flags through live saving.
fields={n:i for i,n in enumerate(re.findall(r'\bMON_DATA_[A-Z0-9_]+\b',(R/'include/pokemon.h').read_text().split('enum MonData {')[1].split('};')[0]))}
invoke('ScriptGiveEgg',133)
party_count=rd(symbols['gPartiesCount'],1)
for i in range(80):wr(A+i,rd(party+(party_count-1)*100+i,1),1)
hatch_progress=invoke('GetBoxMonData3',A,fields['MON_DATA_FRIENDSHIP'],0)
invoke('StorageWriteMon',59,29,A)
check('egg_flag',invoke('GetBoxMonDataAt',59,29,fields['MON_DATA_IS_EGG'])==1)
check('egg_sanity_flag',invoke('GetBoxMonDataAt',59,29,fields['MON_DATA_SANITY_IS_EGG'])==1)
check('egg_not_counted_as_non_egg',invoke('CountStorageNonEggMons')==0)
check('egg_collection_save_after_native_odd_bank',invoke('TrySavingData',0)==1)
check('egg_collection_reload',invoke('LoadGameSave',0)==1)
check('egg_hatch_progress',invoke('GetBoxMonDataAt',59,29,39)==hatch_progress)
check('loaded_egg_flag',invoke('GetBoxMonDataAt',59,29,fields['MON_DATA_IS_EGG'])==1)
# Boxed fusion bodies cannot be erased while orphaning a stored partner.
for i in range(80):wr(A+i,rd(party+i,1),1)
fused=invoke('GetFormSpeciesId',646,1)
check('fusion_form_exists',fused!=646 and fused>0)
wr(V,fused);invoke('SetBoxMonData',A,18,V)
invoke('StorageWriteMon',0,0,A)
fusion_partner=rd(symbols['gPokemonStoragePtr'])+56404
wr(fusion_partner+84,1,1)
check('boxed_fusion_detected',invoke('StorageHasBoxedFusion')==1)
check('orphaning_fusion_conversion_rejected',invoke('StorageChangeMode',0,1)==0)
check('fusion_body_preserved',invoke('GetBoxMonDataAt',0,0,18)==fused)
open_options();tap(1);frames(20);capture('fusion_guard')
check('fusion_warning_does_not_switch',invoke('GetStorageBoxCount')==60)
tap(1);tap(2);frames(180)
fusion_partner=rd(symbols['gPokemonStoragePtr'])+56404
wr(fusion_partner+84,0,1)
check('unfused_mode_conversion_allowed',invoke('StorageChangeMode',0,1)==1)
open_options('CB2_ReinitMainMenu');tap(1);frames(20);capture('title_mode_change_blocked')
check('title_options_cannot_clear_storage',invoke('GetStorageBoxCount')==14)
warning_task=active('Task_StorageWarning')
check('title_warning_is_return_only',warning_task is not None and rd(symbols['gTasks']+warning_task*40+8+7*2,2)==4)

lib.shutdown()
result=dict(passed=True,rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),assertions=len(checks),full_pc_scan_frames=scan_frames,checks=checks)
(D/'validation.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS',len(checks),'production PC/menu/save integration assertions')
