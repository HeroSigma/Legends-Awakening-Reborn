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
moves={n:int(v) for n,v in re.findall(r'(MOVE_[A-Z_0-9]+)\s*=\s*(\d+)',(R/'include/constants/moves.h').read_text())}
for move,item,species in [('MOVE_THIEF','ITEM_FIRIUM_Z',4),('MOVE_COVET','ITEM_CHARIZARDITE_X',6)]:
 start(0)
 for flagnum in range(0x867,0x86f):setflag(flagnum)
 invoke('ScriptGiveMon',493,100,0);player=symbols['gParties'];warp(0,16,10,16);frames(60)
 invoke('SetMonMoveSlot',player,moves[move],0)
 for j in [1,2,3]:invoke('SetMonMoveSlot',player,0,j)
 monset(player,'HELD_ITEM',0);e=enemy(species,100);monset(e,'HELD_ITEM',items[item]);invoke('SetMonMoveSlot',e,moves['MOVE_GROWL'],0);print('BEFORE',monget(e,'HELD_ITEM'),monget(player,'MOVE1'),flush=True);invoke('BattleSetup_StartScriptedWildBattle')
 recovered=False
 for i in range(12000):
  if itemcount(items[item])==1 or rd(symbols['gBattleMons']+48,2)==items[item]:recovered=True;break
  frames(1,1 if i%20==0 else 0)
 capture('theft_end_'+move)
 print('DEBUG',hex(rd(symbols['gMain']+4)),hex(rd(symbols['gBattleMainFunc'])),rd(symbols['gBattleOutcome'],1),rd(player+86,2),rd(e+86,2),flush=True)
 print('POSTHELD',monget(player,'HELD_ITEM') if rd(symbols['gMain']+4)!=symbols['BattleMainCB2']|1 else rd(symbols['gBattleMons']+48,2),flush=True)
 check('actual_'+move+'_recovers_'+item,recovered)
 print(move,item,'recovered',recovered,flush=True)
 lib.shutdown()
print('Native Thief/Covet recovery passed',flush=True)
