"""Native Store tier progression and Mr. Stone reward persistence."""
from pathlib import Path
import tempfile,subprocess,struct,json,hashlib,shutil
R=Path(__file__).resolve().parents[3]
exec(compile((R/'tools/la_world/storage/test_pc_integration.py').read_text().split('start(0)')[0],'helpers','exec'))
D=R/'docs/features/badge-store-stone';D.mkdir(parents=True,exist_ok=True)
checks=[]
def check(n,v):
 checks.append(dict(test=n,passed=bool(v)));assert v,n
items={'EXP_CANDY_XS':0,'HEALTH_FEATHER':0,'EXP_CANDY_S':1,'HP_UP':1,'PROTEIN':1,'HEALTH_MOCHI':1,'MACHO_BRACE':1,'EXP_CANDY_M':2,'ABILITY_CAPSULE':2,'FRESH_START_MOCHI':2,'TIMID_MINT':2,'ADAMANT_MINT':2,'POWER_WEIGHT':2,'POWER_ANKLET':2,'RARE_CANDY':4,'EXP_CANDY_L':4,'DYNAMAX_CANDY':4,'ABILITY_PATCH':4,'EXP_CANDY_XL':6,'BOTTLE_CAP':2,'GOLD_BOTTLE_CAP':4}
names=['SCR_OP_CALL','SCR_OP_END','FLAG_BADGE01_GET','FLAG_SYS_GAME_CLEAR','FLAG_LA_STONE_SHINY_CHARM','FLAG_DELIVERED_STEVEN_LETTER','FLAG_RECEIVED_EXP_SHARE','ITEM_SHINY_CHARM','ITEM_EXP_SHARE','ITEM_STRANGE_BALL','ITEM_MASTER_BALL','VAR_DEVON_CORP_3F_STATE','VAR_0x8004','offsetof(struct SaveBlock1,money)']+['ITEM_'+x for x in items]
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'c.c').write_text('#include "global.h"\n#include "item.h"\n#include "constants/flags.h"\n#include "constants/vars.h"\n#include "constants/script_commands.h"\n#include <stddef.h>\nconst unsigned v[]={'+','.join(names)+'};')
 subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(td/'c.c'),'-o',str(td/'c.o')],cwd=R,check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(td/'c.o'),str(td/'c.bin')],check=True)
 c=dict(zip(names,struct.unpack('<'+str(len(names))+'I',(td/'c.bin').read_bytes())))
start(0)
wallet=rd(symbols['gSaveBlock1Ptr'])+c['offsetof(struct SaveBlock1,money)'];invoke('SetMoney',wallet,999999)
for badges in range(9):
 for i in range(8):invoke('FlagSet' if i<badges else 'FlagClear',c['FLAG_BADGE01_GET']+i)
 for name,minimum in items.items():
  item=c['ITEM_'+name];tag=f'{badges}_{name}'
  check(tag+'_availability',bool(invoke('LegendsStore_ItemAllowed',item))==(badges>=minimum))
  if badges<minimum:
   before=invoke('CountTotalItemQuantityInBag',item)
   check(tag+'_locked_purchase',invoke('LegendsStore_Buy',item,1,99)==1)
   check(tag+'_no_charge',invoke('GetMoney',wallet)==999999 and invoke('CountTotalItemQuantityInBag',item)==before)
 check(f'{badges}_Strange_excluded',invoke('LegendsStore_ItemAllowed',c['ITEM_STRANGE_BALL'])==0)
 check(f'{badges}_Master_still_League_locked',invoke('LegendsStore_ItemAllowed',c['ITEM_MASTER_BALL'])==0)
for i in range(8):invoke('FlagClear',c['FLAG_BADGE01_GET']+i)
invoke('FlagSet',c['FLAG_BADGE01_GET']+3)
check('Flannery_named_milestone',invoke('LegendsStore_ItemAllowed',c['ITEM_ABILITY_PATCH'])==1 and invoke('LegendsStore_ItemAllowed',c['ITEM_EXP_CANDY_XL'])==0)
invoke('FlagSet',c['FLAG_SYS_GAME_CLEAR'])
check('Champion_Master' ,invoke('LegendsStore_ItemAllowed',c['ITEM_MASTER_BALL'])==1)
check('Champion_all_training',all(invoke('LegendsStore_ItemAllowed',c['ITEM_'+name])==1 for name in items))
lib.shutdown()
# Test the genuine letter-delivery NPC script on its own map with a real actor.
mg=json.loads((R/'data/maps/map_groups.json').read_text())
for group,gname in enumerate(mg['group_order']):
 if 'RustboroCity_DevonCorp_3F' in mg[gname]:mapnum=mg[gname].index('RustboroCity_DevonCorp_3F');break
seen=set()
def stone():
 wr(symbols['gSpecialVar_LastTalked'],1,2)
 invoke('ScriptContext_SetupScript',symbols['RustboroCity_DevonCorp_3F_EventScript_MrStone'])
 for i in range(16000):
  if i>60 and rd(symbols['sGlobalScriptContextStatus'],1)==2:
   frames(45);return
  for label in ['ThankYouForDeliveringLetter','ExplainShinyCharm','PlayerCharmPromise']:
   symbol='RustboroCity_DevonCorp_3F_Text_'+label
   if label not in seen and bytes(rd(symbols[symbol]+j,1) for j in range(12)) in bytes(rd(symbols['gStringVar4']+j,1) for j in range(100)):
    frames(800);shutil.copy2(shot('Stone_'+label),D/(label+'.png'));seen.add(label)
  frames(1,1 if i%17==0 else 0)
 raise AssertionError('Stone dialogue did not finish')
start(0);invoke('VarSet',c['VAR_DEVON_CORP_3F_STATE'],1);warp(group,mapnum,16,5)
check('starts_with_EXPShare_flag',invoke('FlagGet',c['FLAG_RECEIVED_EXP_SHARE'])==1)
stone()
check('no_charm_before_letter',invoke('CheckBagHasItem',c['ITEM_SHINY_CHARM'],1)==0 and invoke('FlagGet',c['FLAG_LA_STONE_SHINY_CHARM'])==0)
invoke('FlagSet',c['FLAG_DELIVERED_STEVEN_LETTER']);stone()
check('letter_rewards_ShinyCharm',invoke('CountTotalItemQuantityInBag',c['ITEM_SHINY_CHARM'])==1)
check('independent_claim_flag',invoke('FlagGet',c['FLAG_LA_STONE_SHINY_CHARM'])==1)
check('EXPShare_unchanged',invoke('CountTotalItemQuantityInBag',c['ITEM_EXP_SHARE'])==1)
stone();check('repeat_no_duplicate',invoke('CountTotalItemQuantityInBag',c['ITEM_SHINY_CHARM'])==1)
# Older/debug saves already owning a Charm acknowledge it without duplication.
invoke('FlagClear',c['FLAG_LA_STONE_SHINY_CHARM']);stone()
check('already_owned_no_duplicate',invoke('CountTotalItemQuantityInBag',c['ITEM_SHINY_CHARM'])==1 and invoke('FlagGet',c['FLAG_LA_STONE_SHINY_CHARM'])==1)
check('save',invoke('TrySavingData',0)==1)
invoke('FlagClear',c['FLAG_LA_STONE_SHINY_CHARM']);invoke('RemoveBagItem',c['ITEM_SHINY_CHARM'],1)
check('load',invoke('LoadGameSave',0)==1)
check('reward_persists',invoke('CountTotalItemQuantityInBag',c['ITEM_SHINY_CHARM'])==1 and invoke('FlagGet',c['FLAG_LA_STONE_SHINY_CHARM'])==1)
for label in ['Stone','Knuckle','Heat','Feather','Rain']:
 script=bytes([c['SCR_OP_CALL']])+struct.pack('<I',symbols['ProgressionUnlocks_'+label])+bytes([c['SCR_OP_END']])
 for i,v in enumerate(script):wr(0x03007500+i,v,1)
 invoke('ScriptContext_SetupScript',0x03007500);frames(800)
 check(label+'_actual_notice',bytes(rd(symbols['gStringVar4']+i,1) for i in range(12))==bytes(rd(symbols['ProgressionUnlocks_Text_'+label]+i,1) for i in range(12)))
 shutil.copy2(shot('badge_notice_'+label),D/(label+'-unlock.png'))
 for i in range(4000):
  if rd(symbols['sGlobalScriptContextStatus'],1)==2:break
  frames(1,1 if i%17==0 else 0)
 else:raise AssertionError('notice script did not finish')
lib.shutdown()
# Badge messages are wired only into the first-victory paths and describe the
# same unlock tiers exercised above, not repeated reward-claim interactions.
for name,label,n in [('RustboroCity_Gym','Stone',1),('DewfordTown_Gym','Knuckle',2),('LavaridgeTown_Gym_1F','Heat',4),('FortreeCity_Gym','Feather',6),('SootopolisCity_Gym_1F','Rain',8)]:
 script=(R/f'data/maps/{name}/scripts.inc').read_text()
 check(f'badge_{n}_notice_hook',f'setflag FLAG_BADGE{n:02d}_GET\n\tcall ProgressionUnlocks_{label}' in script and script.count('call ProgressionUnlocks_'+label)==1)
(D/'validation.json').write_text(json.dumps(dict(checks=checks,user_save_loaded=False,rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest()),indent=2)+'\n')
print('PASS',len(checks),'badge Store and Stone reward checks',flush=True)
