"""Native mGBA integration checks; isolated battery, never the player's save."""
from pathlib import Path
R=Path.cwd()
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
import tempfile,struct
names=['FLAG_LA_RECEIVED_RED_MEGA_RING','FLAG_BADGE01_GET','FLAG_BADGE02_GET','FLAG_SYS_GAME_CLEAR','VAR_LA_RIFT_TRACKER','FLAG_LA_QUEST_BASE','ITEM_ROCKIUM_Z','ITEM_FIGHTINIUM_Z','ITEM_SUPER_POTION','ITEM_FOCUS_SASH','SPECIES_RALTS','MON_DATA_IS_SHINY','MON_DATA_HELD_ITEM','MON_DATA_SPECIES','sizeof(struct Pokemon)','MAP_RUSTBORO_CITY_GYM','MAP_DEWFORD_TOWN_GYM','MAP_RUSTBORO_CITY','MAP_OLDALE_TOWN','MAP_LITTLEROOT_TOWN_PROFESSOR_BIRCHS_LAB','VAR_LA_LITTLEROOT_ARC','VAR_BIRCH_LAB_STATE','ITEM_TERA_ORB','FLAG_LA_TERA_ORB_ACTIVATED','ITEM_RIFT_TRACKER','MAP_HYPERHOENN_34_67_TIMELESS_WOODS','FLAG_LA_TIMELESS_WOODS_ENTERED','FLAG_LA_TIMELESS_WOODS_CONSPIRACY_SEEN','FLAG_LA_TIMELESS_WOODS_ORB_TAKEN','FONT_SMALL']
with tempfile.TemporaryDirectory() as td:
 td=Path(td)
 (td/'c.c').write_text('#include "global.h"\n#include "pokemon.h"\n#include "text.h"\n#include "constants/maps.h"\n#include "constants/flags.h"\n#include "constants/vars.h"\n#include "constants/items.h"\nconst unsigned v[]={'+','.join(names)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 c=dict(zip(names,struct.unpack('<'+str(len(names))+'I',(td/'c.bin').read_bytes())))
def state(i):return invoke('LegendsQuest_State',i)
def claim(i):
 wr(symbols['gSpecialVar_0x8004'],i,2);invoke('LegendsQuest_Claim')
 return rd(symbols['gSpecialVar_Result'],2)
def at(n,x=5,y=6):
 m=c[n];warp(m>>8,m&255,x,y);frames(40)
def finish():
 for i in range(12000):
  if rd(symbols['sGlobalScriptContextStatus'],1)==2 and not rd(symbols['sLockFieldControls'],1):return
  frames(1,1 if i%24<3 else 0)
 raise AssertionError('script did not finish')
start(0)
invoke('ScriptGiveMon',c['SPECIES_RALTS'],5,0)
check('initial_main_active',state(0)==1)
check('next_chapter_locked',state(1)==0)
invoke('FlagSet',c['FLAG_LA_RECEIVED_RED_MEGA_RING'])
check('old_receipt_claimed',state(1)==3)
check('no_duplicate_main_gift',claim(1)==0)
invoke('VarSet',c['VAR_LA_LITTLEROOT_ARC'],5)
invoke('VarSet',c['VAR_BIRCH_LAB_STATE'],5)
at('MAP_RUSTBORO_CITY_GYM')
invoke('FlagSet',c['FLAG_BADGE01_GET'])
check('gym_ready',state(10)==2)
invoke('AddBagItem',c['ITEM_ROCKIUM_Z'],999)
check('full_stack_defers_reward',claim(10)==2 and state(10)==2)
invoke('RemoveBagItem',c['ITEM_ROCKIUM_Z'],999)
wr(symbols['gSpecialVar_0x8004'],10,2)
invoke('ScriptContext_SetupScript',symbols['LegendsQuest_ClaimFromMenu'])
frames(20)
check('quest_has_no_hoopa_delivery','Task_QuestRing' not in symbols)
print(shot('quest_reward_ring'),flush=True)
finish()
check('gym_claim',state(10)==3)
check('direct_delivery_complete',state(10)==3)
check('gym_received',invoke('CheckBagHasItem',c['ITEM_ROCKIUM_Z'],1))
check('gym_once',claim(10)==0)
invoke('FlagSet',c['FLAG_BADGE02_GET'])
check('wrong_gym_blocks',claim(11)==4)
at('MAP_DEWFORD_TOWN_GYM')
invoke('FlagClear',c['FLAG_LA_QUEST_BASE']+21)
check('previous_reward_required',claim(11)==3)
invoke('FlagSet',c['FLAG_LA_QUEST_BASE']+21)
display_windows_before=rd(0x04000000,2)&0xe000
invoke('LegendsQuests_Open');frames(10)
check('dark_room_preview_not_masked',(rd(0x04000000,2)&0xe000)==0)
for i in range(11):tap(128)
tap(1);frames(10)
check('quest_details_open',rd(symbols['gTasks']+active('Task_Quests')*40+8+3*2,2)==1)
print(shot('quest_unbound_details'),flush=True)
tap(1);finish()
check('next_gym_claim',state(11)==3)
check('field_display_windows_restored',(rd(0x04000000,2)&0xe000)==display_windows_before)
check('menu_claim_returns_to_field',active('Task_Quests') is None and not rd(symbols['sLockFieldControls'],1))
for i in range(24):check('rift_locked_'+str(i),not invoke('LegendsQuest_RiftAllowed',i))
invoke('VarSet',c['VAR_LA_RIFT_TRACKER'],2)
invoke('LegendsQuest_SurveyRift',0)
check('preleague_survey_rejected',state(20)==0)
invoke('FlagSet',c['FLAG_SYS_GAME_CLEAR'])
check('postleague_active',state(20)==1)
invoke('LegendsQuest_SurveyRift',0)
check('survey_reward_ready',state(20)==2)
check('wrong_giver_blocks',claim(20)==4)
at('MAP_LITTLEROOT_TOWN_PROFESSOR_BIRCHS_LAB',6,5)
check('individual_permit_claim',claim(20)==1)
check('only_that_rift_opens',invoke('LegendsQuest_RiftAllowed',0) and not invoke('LegendsQuest_RiftAllowed',1))
check('permit_no_duplicate',claim(20)==0)
invoke('FlagClear',c['FLAG_SYS_GAME_CLEAR'])
check('permission_still_requires_league',not invoke('LegendsQuest_RiftAllowed',0))
# Real quest overlay, NPC preview, pagination, close/reopen stability.
palette_before=bytes(rd(symbols['gPlttBufferUnfaded']+480+u,1) for u in range(32))
invoke('LegendsQuests_Open');frames(30)
print(shot('quest_main'),flush=True)
tap(1);frames(10);tap(2);frames(10)
check('details_back_returns_to_list',active('Task_Quests') is not None and rd(symbols['gTasks']+active('Task_Quests')*40+8+3*2,2)==0)
tap(256);tap(4);frames(10)
check('empty_active_filter_safe',rd(symbols['gTasks']+active('Task_Quests')*40+8+2,2)==65535)
print(shot('quest_unbound_empty_filter'),flush=True)
for i in range(3):tap(4)
tap(256)
for i in range(25):tap(128);frames(2)
tap(256);frames(20);print(shot('quest_side'),flush=True)
tap(2);frames(30)
check('quest_overlay_closes',active('Task_Quests') is None and not rd(symbols['sLockFieldControls'],1))
check('quest_palette_restored',bytes(rd(symbols['gPlttBufferUnfaded']+480+u,1) for u in range(32))==palette_before)
for i in range(12):
 invoke('LegendsQuests_Open');frames(5);tap(256);tap(128);tap(2);frames(5)
check('repeated_open_close_safe',rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1)
# The item sidequest never consumes supplies on invalid/double claims.
at('MAP_RUSTBORO_CITY',29,22)
wr(symbols['gSpecialVar_0x8004'],18,2);invoke('LegendsQuest_Accept')
check('side_accept',state(18)==1)
check('missing_supplies_no_reward',claim(18)==0)
invoke('AddBagItem',c['ITEM_SUPER_POTION'],3)
check('supplies_ready',state(18)==2)
check('item_exchange_success',claim(18)==1)
check('medicine_consumed',not invoke('CheckBagHasItem',c['ITEM_SUPER_POTION'],1))
check('sash_received',invoke('CheckBagHasItem',c['ITEM_FOCUS_SASH'],1))
check('exchange_once',claim(18)==0)
at('MAP_OLDALE_TOWN',17,12)
wr(symbols['gSpecialVar_0x8004'],19,2);invoke('LegendsQuest_Accept')
check('ralts_ready',state(19)==2)
wr(symbols['gSpecialVar_0x8004'],6,2);invoke('LegendsQuest_TradeRalts')
check('trade_cancel_no_reward',state(19)==2)
wr(symbols['gSpecialVar_0x8004'],0,2);invoke('LegendsQuest_TradeRalts')
check('trade_shiny',invoke('GetMonData2',symbols['gParties'],c['MON_DATA_IS_SHINY']))
check('trade_once',state(19)==3)

# A deferred native story gift remains claimable at its original location.
at('MAP_RUSTBORO_CITY',29,22)
invoke('FlagSet',c['FLAG_LA_QUEST_BASE']+12) # Rowan's pending gift
check('pending_main_reward_ready',state(6)==2)
check('pending_main_wrong_location',claim(6)==4)
# Measure the real font, not a character-count approximation.
for i in range(20):
 base=symbols['sQuests']+28*i
 for offset,x in [(0,4),(4,36),(8,36),(12,4),(16,26)]:
  ptr=rd(base+offset)
  width=invoke('GetStringWidth',c['FONT_SMALL'],ptr,0)
  check('quest_text_fit_'+str(i)+'_'+str(offset),width+x<=224)
# Save/load preserves the reward ledger.
check('quest_save',invoke('TrySavingData',0)==1)
invoke('FlagClear',c['FLAG_LA_QUEST_BASE']+37)
check('quest_load',invoke('LoadGameSave',0)==1)
check('reward_ledger_persists',state(18)==3 and state(19)==3)
# Both sidequest NPCs stand on walkable ground, adjacent to a walkable approach.
for name,x,y in [('MAP_RUSTBORO_CITY',29,21),('MAP_OLDALE_TOWN',17,11)]:
 at(name,x,y+1)
 check('walkable_giver_'+name,invoke('MapGridGetCollisionAt',x+7,y+7)==0)
 check('walkable_approach_'+name,invoke('MapGridGetCollisionAt',x+7,y+8)==0)
# Exercise the actual paged Start menu and its return path.
invoke('FlagSet',c['FLAG_SYS_GAME_CLEAR'])
tap(8);frames(30);tap(256);frames(30)
print(shot('quest_start_tools'),flush=True)
tap(2);frames(30)
check('start_returns_to_field',rd(symbols['gMain']+4)==symbols['CB2_Overworld']|1)


# Check every new field-dialogue line with the game's normal font.
for name in sorted(symbols):
 if not name.startswith('LegendsQuest_Text_'):continue
 ptr=symbols[name]; data=bytearray()
 for j in range(1500):
  b=rd(ptr+j,1)
  if b==255:break
  data.append(b)
 for k,line in enumerate(re.split(b'[\xfe\xfb\xfa]',bytes(data))):
  if 0xfd in line:continue # Expanded names are checked through their surrounding native scripts.
  for j,b in enumerate(line+b'\xff'):wr(0x03007500+j,b,1)
  check('dialogue_fit_'+name+'_'+str(k),invoke('GetStringWidth',1,0x03007500,0)<=208)
# Opening one permit must let the native source warp proceed to Ultra Space.
tap(2);frames(10)
for n in ['FLAG_LA_TIMELESS_WOODS_ENTERED','FLAG_LA_TIMELESS_WOODS_CONSPIRACY_SEEN','FLAG_LA_TIMELESS_WOODS_ORB_TAKEN']:
 invoke('FlagSet',c[n])
invoke('FlagSet',c['FLAG_SYS_GAME_CLEAR'])
invoke('FlagSet',c['FLAG_LA_QUEST_BASE']+(20+11)*2+1)
at('MAP_HYPERHOENN_34_67_TIMELESS_WOODS',24,9)
frames(32,64);frames(160)
m=c['MAP_HYPERHOENN_34_67_TIMELESS_WOODS']
sb=rd(symbols['gSaveBlock1Ptr'])
check('permitted_native_warp_travels',(rd(sb+4,1),rd(sb+5,1))!=(m>>8,m&255))
print(shot('quest_permitted_ultra_space'),flush=True)
print('QUEST CHECKS',len(checks),flush=True)
