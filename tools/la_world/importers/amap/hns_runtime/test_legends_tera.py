"""Native mGBA chapter tests. All saves are disposable; no player battery is opened."""
from pathlib import Path
import hashlib,json,subprocess,shutil
exec(compile(Path(__file__).with_name('test_legends_bedroom.py').read_text().split('for gender in [0,1]:')[0],'bedroom_helpers','exec'))
# Saving relocates EWRAM save blocks; keep the isolated call helper in unused IWRAM.
exec(compile(Path(__file__).with_name('test_protagonist_assets.py').read_text().split("D=R/'docs/art/protagonists/trainer_draft'")[0].replace('BASE=0x0203f000','BASE=0x03007000'),'arm_helpers','exec'))
D=R/'docs/la_world/tera_economy';(D/'screenshots').mkdir(parents=True,exist_ok=True)
checks=[]
def check(n,v):
 checks.append(dict(test=n,passed=bool(v)))
 assert v,(n,location(),pos(),var(0x4083),var(0x4084))
def capture(n):shutil.copy2(shot('littleroot_arc_'+n),D/'screenshots'/(n+'.png'))
def var(n,value=None):
 a=rd(symbols['gSaveBlock1Ptr'])+0x139c+(n-0x4000)*2
 if value is not None:wr(a,value,2)
 return rd(a,2)
def setflag(n,on=True):
 a=rd(symbols['gSaveBlock1Ptr'])+0x1270+n//8
 wr(a,rd(a,1)|(1<<(n%8)) if on else rd(a,1)&~(1<<(n%8)),1)
def actors():
 return {rd(symbols['gObjectEvents']+i*36+8,1):rd(symbols['gObjectEvents']+i*36+4,2) for i in range(16) if rd(symbols['gObjectEvents']+i*36,1)&1}
def itemcount(item):
 key=rd(rd(symbols['gSaveBlock2Ptr'])+0xac,2);total=0
 for pocket in range(5):
  a=symbols['gBagPockets']+pocket*8;ptr=rd(a);cap=rd(a+4,1)
  total+=sum(rd(ptr+i*4+2,2)^key for i in range(cap) if rd(ptr+i*4,2)==item)
 return total
def money():return rd(rd(symbols['gSaveBlock1Ptr'])+0x490)^rd(rd(symbols['gSaveBlock2Ptr'])+0xac)
def advance_arc(target,suffix,limit=22000):
 loss=False;lab_battle=False;multi=False;names=set();snap=set()
 for i in range(limit):
  phase=var(0x4083)
  if rd(symbols['gMain']+4)==symbols['BattleMainCB2']|1:
   if flag(0x37):
    lab_battle=True
    if 'lab' not in snap:
     frames(220);capture('lab_battle_'+suffix);snap.add('lab')
     check('lab_normal_trainer_not_birch_tutorial_'+suffix,not (rd(symbols['gBattleTypeFlags'])&16))
     check('red_uses_riolu_level_10_'+suffix,rd(symbols['gBattleMons']+140,2)==447 and rd(symbols['gParties']+600+84,1)==10)
   if flag(0x38):
    multi=True
    if 'multi' not in snap:
     frames(220);capture('double_battle_'+suffix);snap.add('multi')
     required=(1<<0)|(1<<6)|(1<<15)|(1<<22)
     check('true_four_trainer_battle_'+suffix,(rd(symbols['gBattleTypeFlags'])&required)==required and rd(symbols['gBattlersCount'],1)==4)
     check('red_is_battle_partner_'+suffix,rd(symbols['gPartnerTrainerId'],2)==866)
     check('red_battles_with_riolu_not_pikachu_'+suffix,rd(symbols['gBattleMons']+280,2)==447)
  if flag(0x37) and rd(symbols['gBattleOutcome'],1)==2:loss=True
  for key in ['BirchRecognizes','PortalArrival','PlayerIntroduction','KeepStarter','RioluGift','RedCongratulates','BrendanRecognizes','NationalDexGift','DexNavGift','ElaraThought']:
   label=symbols['LegendsArc_Text_'+key]
   if key not in names and all(rd(symbols['gStringVar4']+k,1)==rd(label+k,1) for k in range(10)):
    names.add(key);frames(120);capture(key+'_'+suffix)
    def actor(local):
     return next(symbols['gObjectEvents']+j*36 for j in range(16) if rd(symbols['gObjectEvents']+j*36,1)&1 and rd(symbols['gObjectEvents']+j*36+8,1)==local)
    if key in ['BirchRecognizes','PortalArrival','RioluGift','KeepStarter','NationalDexGift','DexNavGift']:
     facing=3 if key in ['BirchRecognizes','PortalArrival','RioluGift'] else 1
     check('birch_faces_speaker_'+key+'_'+suffix,rd(actor(2)+24,1)&15==facing)
    if key=='BirchRecognizes':
     check('red_faces_birch_at_opening_'+suffix,rd(actor(7)+24,1)&15==4)
    if key=='PortalArrival':
     red=actor(7)
     check('red_stays_with_pikachu_for_birch_'+suffix,(rd(red+16,2)-7,rd(red+18,2)-7)==(5,4) and rd(red+24,1)&15==4)
    if key=='PlayerIntroduction':
     red=actor(7);pika=actor(8)
     check('lab_red_approached_'+key+'_'+suffix,(rd(red+16,2)-7,rd(red+18,2)-7)==(5,5))
     check('lab_red_faces_player_'+key+'_'+suffix,rd(red+24,1)&15==4)
     check('lab_pikachu_faces_conversation_'+key+'_'+suffix,rd(pika+24,1)&15==4)
    if key=='BrendanRecognizes':
     check('route_player_walks_to_brendan_'+suffix,pos()==(10,4))
     red=actor(22);pika=actor(23)
     check('route_red_in_front_of_may_'+suffix,(rd(red+16,2)-7,rd(red+18,2)-7)==(11,4) and rd(red+24,1)&15==2)
     check('route_pikachu_at_right_facing_group_'+suffix,(rd(pika+16,2)-7,rd(pika+18,2)-7)==(12,4) and rd(pika+24,1)&15==3)
  if phase==target and rd(symbols['sGlobalScriptContextStatus'],1)==2:
   frames(60);return dict(lost=loss,lab=lab_battle,multi=multi,text=sorted(names))
  active=[rd(symbols['gTasks']+j*40) for j in range(16) if rd(symbols['gTasks']+j*40+4,1)]
  key=2 if symbols['Task_HandleYesNoInput']|1 in active else 1
  frames(1,key if i%15==0 else 0)
 raise AssertionError(('arc timeout',target,suffix,var(0x4083),var(0x4084),location(),pos(),hex(rd(symbols['gMain']+4)),actors()))
import re
mon_fields=re.findall(r'MON_DATA_[A-Z_0-9]+',(R/'include/pokemon.h').read_text().split('enum MonData {')[1].split('};')[0])
def field(k):return mon_fields.index('MON_DATA_'+k)
def monget(ptr,k):return invoke('GetMonData2',ptr,field(k))
def monset(ptr,k,v):
 wr(BASE+0x240,v);invoke('SetMonData',ptr,field(k),BASE+0x240)
def clean_enemy():
 for n in range(600):wr(symbols['gParties']+600+n,0,1)
def enemy(species,level=5):
 clean_enemy();invoke('CreateMon',symbols['gParties']+600,species,level,123456,0);invoke('CalculateMonStats',symbols['gParties']+600)
 return symbols['gParties']+600
items={name:int(value) for name,value in re.findall(r'(ITEM_[A-Z_0-9]+)\s*=\s*(\d+)',(R/'include/constants/items.h').read_text())}
start(0);invoke('ScriptGiveMon',4,10,0);player=symbols['gParties']
setflag(0x90,False);setflag(0x10,False)
e=enemy(4);monset(e,'HP',0);wr(symbols['gBattleTypeFlags'],0);wr(symbols['gBattleOutcome'],1,1)
fire=items['ITEM_FIRE_TERA_SHARD'];stellar=items['ITEM_STELLAR_TERA_SHARD']
invoke('LegendsAwardWildShards');check('no_shards_before_devon',itemcount(fire)==0)
# Lookup native Pokenav milestone by parsing its numeric flag.
flags=(R/'include/constants/flags.h').read_text()
pokenav=int(re.search(r'#define FLAG_RECEIVED_POKENAV\s+(0x[0-9A-Fa-f]+)',flags)[1],16)
setflag(0x90);setflag(pokenav)
invoke('LegendsAwardWildShards');check('primary_fire_shard_on_defeat',itemcount(fire)==1)
e=enemy(1);monset(e,'HP',0);invoke('LegendsAwardWildShards');check('primary_not_secondary',itemcount(items['ITEM_GRASS_TERA_SHARD'])==1 and itemcount(items['ITEM_POISON_TERA_SHARD'])==0)
e=enemy(7);wr(symbols['gBattleOutcome'],7,1);wr(symbols['gBattlerTarget'],1,1);wr(symbols['gBattlerPartyIndexes']+2,0,2)
# Battler party indices are u8 in this checkout; index zero is zero either way.
invoke('LegendsAwardCaughtShard',7,0);invoke('LegendsAwardWildShards');check('shard_on_capture',itemcount(items['ITEM_WATER_TERA_SHARD'])==1)
for outcome in [2,4,5,6]:
 wr(symbols['gBattleOutcome'],outcome,1);n=itemcount(items['ITEM_WATER_TERA_SHARD']);invoke('LegendsAwardWildShards');check('no_reward_for_live_escape_'+str(outcome),itemcount(items['ITEM_WATER_TERA_SHARD'])==n)
monset(e,'HP',0);wr(symbols['gBattleOutcome'],1,1)
for mask in [8,2,16,512,1<<24,1<<20]:
 wr(symbols['gBattleTypeFlags'],mask);n=itemcount(items['ITEM_WATER_TERA_SHARD']);invoke('LegendsAwardWildShards');check('excluded_battle_'+str(mask),itemcount(items['ITEM_WATER_TERA_SHARD'])==n)
wr(symbols['gBattleTypeFlags'],0)
# A defeated opponent in a double battle awards once per actual mon.
e=enemy(4);monset(e,'HP',0);invoke('CreateMon',e+100,7,5,98765,0);monset(e+100,'HP',0)
f=itemcount(fire);w=itemcount(items['ITEM_WATER_TERA_SHARD']);invoke('LegendsAwardWildShards');check('double_two_primary_shards',itemcount(fire)==f+1 and itemcount(items['ITEM_WATER_TERA_SHARD'])==w+1)
# Deterministic rare bonus sample (independent of regular drop).
e=enemy(4);monset(e,'HP',0);invoke('SeedRng',12345)
for i in range(400):invoke('LegendsAwardWildShards')
check('stellar_bonus_is_rare',0<itemcount(stellar)<20)
# Preserve assigned items and measure the actual 5% held-item entry point.
e=enemy(4);wr(symbols['gBattleTypeFlags'],0);invoke('SeedRng',9876);held=0;seen=set()
for i in range(2000):
 monset(e,'HELD_ITEM',0);invoke('SetWildMonHeldItem');item=monget(e,'HELD_ITEM');held+=bool(item);seen.add(item)
check('five_percent_held_item_roll',65<=held<=135)
check('charmander_both_charizardites',items['ITEM_CHARIZARDITE_X'] in seen and items['ITEM_CHARIZARDITE_Y'] in seen)
check('matching_z_crystal',items['ITEM_FIRIUM_Z'] in seen)
monset(e,'HELD_ITEM',items['ITEM_LEFTOVERS']);invoke('SetWildMonHeldItem');check('explicit_item_preserved',monget(e,'HELD_ITEM')==items['ITEM_LEFTOVERS'])
# Cost checks, revalidation and unchanged-type rejection.
wr(symbols['gSpecialVar_0x8004'],0,2);wr(symbols['gSpecialVar_0x8005'],0,2);monset(player,'TERA_TYPE',11)
normal=items['ITEM_NORMAL_TERA_SHARD'];invoke('LegendsCommitTeraChange');check('short_shards_no_change',rd(symbols['gSpecialVar_Result'],2)==1 and monget(player,'TERA_TYPE')==11)
invoke('AddBagItem',normal,50);invoke('LegendsPrepareTeraChange');check('prepare_cost_50',rd(symbols['gSpecialVar_0x8007'],2)==50 and itemcount(normal)==50)
invoke('LegendsCommitTeraChange');check('change_cost_exactly_50',monget(player,'TERA_TYPE')==1 and itemcount(normal)==0)
invoke('AddBagItem',normal,50);invoke('LegendsCommitTeraChange');check('same_type_no_charge',rd(symbols['gSpecialVar_Result'],2)==3 and itemcount(normal)==50)
wr(symbols['gSpecialVar_0x8005'],18,2);amount=itemcount(stellar);invoke('AddBagItem',stellar,150-amount);invoke('LegendsPrepareTeraChange');check('stellar_quote_150',rd(symbols['gSpecialVar_0x8007'],2)==150)
invoke('LegendsCommitTeraChange');check('stellar_cost_exactly_150',monget(player,'TERA_TYPE')==20 and itemcount(stellar)==0)
monset(player,'IS_EGG',1);wr(symbols['gSpecialVar_0x8005'],0,2);invoke('LegendsCommitTeraChange');check('egg_no_charge',rd(symbols['gSpecialVar_Result'],2)==2 and itemcount(normal)==50);monset(player,'IS_EGG',0)
# Lab cells and entrance stay traversable after the native Devon milestones.
mapids=(R/'include/constants/map_groups.h').read_text()
m=re.search(r'MAP_HYPERHOENN_34_10_BASEMENT\s*= \((\d+) \| \((\d+) << 8\)\)',mapids)
assert m
warp(int(m[2]),int(m[1]),4,3);frames(90)
check('scientist_cell_walkable',invoke('MapGridGetCollisionAt',11,9)==0)
check('service_interaction_cell_walkable',invoke('MapGridGetCollisionAt',11,10)==0)
capture('basement_scientist');tap(64);tap(1)
for i in range(300):frames(1,1 if i%30==0 else 0)
capture('tera_type_menu')
lib.shutdown()
(D/'runtime_validation.json').write_text(json.dumps({'checks':checks,'held_samples':2000,'held_count':held,'all_passed':all(c['passed'] for c in checks),'user_save_loaded':False},indent=2)+'\n')
print('Tera economy checks:',len(checks),'held:',held,flush=True)
