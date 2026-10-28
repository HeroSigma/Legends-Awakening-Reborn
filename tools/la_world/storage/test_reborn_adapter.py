"""Execute staged codec against Reborn's real ARM Pokemon functions.
Uses a disposable ROM copy, never a player's battery or permanent release.
"""
from pathlib import Path
import sys, re, json, hashlib, subprocess
R=Path('/home/allan/projects/Legends-Awakening-Reborn')
sys.path.insert(0,str(R/'tools/la_world/importers/amap/hns_runtime'))
helper=R/'tools/la_world/importers/amap/hns_runtime/test_protagonist_assets.py'
exec(compile(helper.read_text().split("D=R/'docs/art/protagonists/trainer_draft'")[0].replace('BASE=0x0203f000','BASE=0x03007000').replace('frames(1)\n assert rd(RESULT)', 'frames(1)\n for retry in range(3600):\n  if rd(RESULT)!=0xdeadbeef:break\n  frames(1)\n invoke.last_frames=retry+1\n assert rd(RESULT)'),'arm_helpers','exec'))
D=R/'docs/la_world/compact_pc';D.mkdir(parents=True,exist_ok=True)
work=R/'.la_work/compact_pc'
patch=(work/'adapter.bin').read_bytes()
assert len(patch)<0x10000
rom=bytearray((R/'pokeemerald.gba').read_bytes());rom[0x1ff0000:0x1ff0000+len(patch)]=patch
path=work/'adapter_test.gba';path.write_bytes(rom)
for line in subprocess.check_output(['arm-none-eabi-nm',str(work/'adapter.elf')],text=True).splitlines():
 z=line.split()
 if len(z)==3:symbols[z[2]]=int(z[0],16)
enum=(R/'include/pokemon.h').read_text().split('enum MonData {')[1].split('};')[0]
fields={name:i for i,name in enumerate(re.findall(r'\bMON_DATA_[A-Z0-9_]+\b',enum))}
A,B,C,V=0x0203fc00,0x0203f100,0x0203f200,0x0203f300
checks=0
decode_frames=[]
def check(value,message):
 global checks
 checks+=1
 assert value,message
def get(ptr,name):return invoke('GetBoxMonData3',ptr,fields['MON_DATA_'+name],0)
def put(ptr,name,value):
 wr(V,value);invoke('SetBoxMonData',ptr,fields['MON_DATA_'+name],V)
def blob(addr,count):return bytes(rd(addr+i,1) for i in range(count))
check(lib.boot(str(path).encode()),'boot');frames(600)
# New-game initialization supplies save pointers, trainer data, and map metadata.
wr(symbols['gMain']+4,symbols['CB2_NewGame']|1);frames(240)
check(rd(symbols['gSaveBlock2Ptr'])>=0x02000000,'save pointers')
# Real specimens cover genderless, single-gender, variable-gender and form species.
for n,species in enumerate([1,25,29,32,81,113,128,132,133,201,206,265,290,349,386,447,550,570,677,718,744,848,869,924,925,982,1000]):
 invoke('ScriptGiveMon',species,35,0)
 source=symbols['gPlayerParty'] if 'gPlayerParty' in symbols else symbols['gParties']
 # ScriptGiveMon appends to party; always copy the freshly created last member.
 count=rd(symbols['gPlayerPartyCount'],1) if 'gPlayerPartyCount' in symbols else rd(symbols['gPartiesCount'],1)
 if count>6:count=6
 for i in range(80):wr(A+i,rd(source+100*(count-1)+i,1),1)
 check(get(A,'SPECIES')==species,('create species',species,count,get(A,'SPECIES')))
 put(A,'LANGUAGE',1 if n%2 else 2)
 for field,value in [('MARKINGS',n%16),('HELD_ITEM',13),('PP_BONUSES',255),('FRIENDSHIP',201),('HIDDEN_NATURE',17),('POKERUS',0x24),('BEAUTY',201),('EVOLUTION_TRACKER',451),('DYNAMAX_LEVEL',10),('GIGANTAMAX_FACTOR',1),('CHAMPION_RIBBON',1),('MODERN_FATEFUL_ENCOUNTER',1),('IS_SHINY',n%2)]:put(A,field,value)
 for i,name in enumerate(['HP','ATK','DEF','SPEED','SPATK','SPDEF']):
  put(A,name+'_IV',(i*5+n)%32);put(A,name+'_EV',85);put(A,'HYPER_TRAINED_'+name,i%2)
 for i in range(4):put(A,'MOVE'+str(i+1),[33,45,85,98][i])
 expected={name:get(A,name) for name in ['MARKINGS','SPECIES','HELD_ITEM','EXP','PP_BONUSES','FRIENDSHIP','HIDDEN_NATURE','POKERUS','BEAUTY','EVOLUTION_TRACKER','DYNAMAX_LEVEL','GIGANTAMAX_FACTOR','CHAMPION_RIBBON','MODERN_FATEFUL_ENCOUNTER','IS_SHINY','TERA_TYPE','ABILITY_NUM','IS_EGG','POKEBALL']+[name+suffix for suffix in ['_IV','_EV'] for name in ['HP','ATK','DEF','SPEED','SPATK','SPDEF']]+['HYPER_TRAINED_'+name for name in ['HP','ATK','DEF','SPEED','SPATK','SPDEF']]+['MOVE'+str(i+1) for i in range(4)]}
 pid=get(A,'PERSONALITY');gender=invoke('GetGenderFromSpeciesAndPersonality',species,pid)
 check(invoke('LaPcEncodeBoxMon',A,C)==1,('encode',species))
 saved=blob(C,31)
 check(invoke('LaPcDecodeBoxMon',C,B)==1,('decode',species))
 decode_frames.append(invoke.last_frames)
 for field,value in expected.items():check(get(B,field)==value,('trait',species,field,value,get(B,field)))
 check((get(B,'LANGUAGE')!=2)==bool(n%2),('foreign-language marker',species))
 nameptr=invoke('GetSpeciesName',species)
 invoke('GetBoxMonData3',B,fields['MON_DATA_NICKNAME'],V+16)
 expected_name=bytearray()
 for j in range(13):
  char=rd(nameptr+j,1);expected_name.append(char)
  if char==255:break
 check(blob(V+16,len(expected_name))==bytes(expected_name),('regenerated species name',species))
 newpid=get(B,'PERSONALITY')
 check(newpid%100==pid%100,('rare evolution',species))
 check((newpid>>16)%10>=5 if (pid>>16)%10>=5 else (newpid>>16)%10<5,('Wurmple branch',species))
 check(invoke('GetGenderFromSpeciesAndPersonality',species,newpid)==gender,('gender',species))
 check(invoke('LaPcEncodeBoxMon',B,C)==1 and blob(C,31)==saved,('stable record',species))
 # Free party space for the next specimen. Disposable instance only.
 invoke('ZeroPlayerPartyMons')
invoke('InitHeap',symbols['gHeap'],0x1c500)
bank=invoke('AllocZeroed_',56804+128)
ctx=invoke('AllocZeroed_',2408)
check(0x02000000<=bank<0x02040000 and 0x02000000<=ctx<0x02040000,'allocate isolated bank/context')
report=V+32
check(invoke('LaPcBankNativeTest',ctx,bank,A,report)==1,('bank native test failed',rd(report+4),rd(report+8),hex(bank),hex(ctx),blob(bank,8).hex(),blob(ctx,8).hex()))
bank_checks=rd(report)
invoke('Free',ctx);invoke('Free',bank)
lib.shutdown()
result=dict(passed=True,assertions=checks,specimens=27,bank_assertions=bank_checks,bank_populated_slots=1800,record_bytes=31,base_rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),adapter_sha256=hashlib.sha256(patch).hexdigest(),decode_frames=decode_frames,scope='Isolated adapter/bank validation; no player battery opened')
(D/'adapter_validation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
