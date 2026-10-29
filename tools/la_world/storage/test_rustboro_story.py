"""Rustboro office and Tera onboarding, isolated native emulator saves."""
from pathlib import Path
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
import tempfile,struct
names=['MAP_GROUP(MAP_RUSTBORO_CITY_DEVON_CORP_3F)','MAP_NUM(MAP_RUSTBORO_CITY_DEVON_CORP_3F)','VAR_DEVON_CORP_3F_STATE','VAR_RUSTBORO_CITY_STATE','FLAG_LA_INTRO_ACTIVE','VAR_LITTLEROOT_INTRO_STATE','FLAG_RETURNED_DEVON_GOODS','FLAG_RECEIVED_POKENAV','FLAG_SYS_POKENAV_GET','FLAG_LA_TERA_RESEARCH_INTRO','ITEM_FIRE_TERA_SHARD','SPECIES_CHARMANDER','ITEM_LETTER']
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "constants/maps.h"\n#include "constants/items.h"\nconst unsigned v[]={'+','.join(names)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 c=dict(zip(names,struct.unpack('<'+str(len(names))+'I',(td/'c.bin').read_bytes())))
def unlocked():
 invoke('LegendsPrepareTeraChange')
 return rd(symbols['gSpecialVar_Result'],2)!=4
def flag(n):return invoke('FlagGet',c[n])
def var(n):return invoke('VarGet',c[n])
def until(pred,limit=24000):
 for i in range(limit):
  if pred():return
  frames(1,1 if i%31<4 else 0)
 raise AssertionError(('timeout',pos(),location()))
def script(n):invoke('ScriptContext_SetupScript',symbols[n]);frames(5)
for gender in [0,1]:
 start(gender);invoke('FlagClear',c['FLAG_LA_INTRO_ACTIVE']);invoke('VarSet',c['VAR_LITTLEROOT_INTRO_STATE'],7)
 invoke('StorageChangeMode',gender,1);invoke('ScriptGiveMon',4,16,0)
 invoke('FlagSet',c['FLAG_RETURNED_DEVON_GOODS'])
 check('no_shards_before_pokenav_'+str(gender),unlocked()==0)
 warp(c[names[0]],c[names[1]],2,2)
 until(lambda:any(all(rd(symbols['gStringVar4']+offset+i,1)==rd(symbols['LegendsRustboro_Text_BirchReport']+i,1) for i in range(12)) for offset in range(4)))
 frames(600)
 out=R/'docs/story/rustboro';out.mkdir(parents=True,exist_ok=True)
 shutil.copy2(shot('rustboro_birch'),out/('birch_'+str(gender)+'.png'))
 until(lambda:var('VAR_DEVON_CORP_3F_STATE')==1)
 until(lambda:rd(symbols['sGlobalScriptContextStatus'],1)==2)
 check('office_grants_pokenav_'+str(gender),flag('FLAG_RECEIVED_POKENAV') and flag('FLAG_SYS_POKENAV_GET'))
 check('office_sets_call_scene_'+str(gender),var('VAR_RUSTBORO_CITY_STATE')==6)
 check('letter_obtained_'+str(gender),invoke('CheckBagHasItem',c['ITEM_LETTER'],1)==1)
 check('office_releases_controls_'+str(gender),invoke('ArePlayerFieldControlsLocked')==0)
 check('milestones_alone_do_not_unlock_shards_'+str(gender),unlocked()==0)
 before=invoke('CountTotalItemQuantityInBag',c['ITEM_FIRE_TERA_SHARD'])
 invoke('LegendsAwardCaughtShard',c['SPECIES_CHARMANDER'],0)
 check('no_reward_before_explanation_'+str(gender),invoke('CountTotalItemQuantityInBag',c['ITEM_FIRE_TERA_SHARD'])==before)
 script('LegendsTera_Scientist')
 until(lambda:active('Task_HandleMultichoiceInput') is not None)
 check('first_conversation_sets_flag_'+str(gender),flag('FLAG_LA_TERA_RESEARCH_INTRO')==1)
 check('first_conversation_unlocks_collection_'+str(gender),unlocked()==1)
 frames(30);frames(4,2);frames(60)
 check('scientist_cancel_releases_controls_'+str(gender),invoke('ArePlayerFieldControlsLocked')==0)
 wr(symbols['gBattleTypeFlags'],0)
 invoke('LegendsAwardCaughtShard',c['SPECIES_CHARMANDER'],0)
 check('primary_type_shard_after_intro_'+str(gender),invoke('CountTotalItemQuantityInBag',c['ITEM_FIRE_TERA_SHARD'])==before+1)
 script('LegendsTera_Scientist')
 until(lambda:active('Task_HandleMultichoiceInput') is not None)
 check('repeat_visit_opens_service_'+str(gender),flag('FLAG_LA_TERA_RESEARCH_INTRO')==1)
 frames(30);frames(4,2);frames(60)
for name in ['LegendsRustboro_Text_BirchReport','LegendsTera_Text_Introduction','RustboroCity_DevonCorp_3F_Text_MrStoneIHaveFavor','RustboroCity_DevonCorp_3F_Text_MrStoneGoWithCautionAndCare','RustboroCity_Text_HelpMeIWasRobbed','RustboroCity_Text_IdBetterGetBackToWork']:
 invoke('StringExpandPlaceholders',symbols['gStringVar4'],symbols[name])
 lines=[[]]
 for i in range(1200):
  v=rd(symbols['gStringVar4']+i,1)
  if v==255:break
  if v in (250,251,254):lines.append([])
  else:lines[-1].append(v)
 for j,line in enumerate(lines):
  for k,v in enumerate(line+[255]):wr(0x0203fc00+k,v,1)
  width=invoke('GetStringWidth',1,0x0203fc00,0)
  check('dialogue_width_'+name+'_'+str(j),width<=208)
lib.shutdown()
out=R/'docs/story/rustboro';out.mkdir(parents=True,exist_ok=True)
(out/'validation.json').write_text(json.dumps(dict(passed=True,assertions=len(checks),rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=checks),indent=2)+'\n')
print('PASS',len(checks),'Rustboro checks',flush=True)
