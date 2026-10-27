"""Exercise the actual linked ARM resolver in an isolated native mGBA instance."""
from probe import *
import hashlib, tempfile
D=R/'docs/la_world/pool_framework';D.mkdir(parents=True,exist_ok=True)
# Scratch lies beyond the linked EWRAM footprint; no user battery save is loaded.
BASE=0x0203f000
RULES=BASE+0x100
RESULT=BASE+0x180
assembly=r"""
.syntax unified
.thumb
.global start
start:
 push {r4,lr}
 ldr r0,arg0
 ldr r1,arg1
 ldr r2,arg2
 ldr r3,target
 bl call_r3
 ldr r1,result
 str r0,[r1]
 ldr r1,callback
 ldr r0,previous
 str r0,[r1]
 pop {r4}
 pop {r0}
 bx r0
call_r3:
 bx r3
.balign 4
arg0: .word 0
arg1: .word 0
arg2: .word 0
target: .word 0
result: .word 0
callback: .word 0
previous: .word 0
"""
with tempfile.TemporaryDirectory() as td:
 td=Path(td);(td/'invoke.s').write_text(assembly)
 subprocess.run(['arm-none-eabi-as','-mcpu=arm7tdmi','-o',str(td/'invoke.o'),str(td/'invoke.s')],check=True)
 subprocess.run(['arm-none-eabi-ld','-Ttext='+hex(BASE),'-e','start','-o',str(td/'invoke.elf'),str(td/'invoke.o')],check=True)
 subprocess.run(['arm-none-eabi-objcopy','-O','binary',str(td/'invoke.elf'),str(td/'invoke.bin')],check=True)
 code=(td/'invoke.bin').read_bytes()
 labels={z[2]:int(z[0],16) for line in subprocess.check_output(['arm-none-eabi-nm',str(td/'invoke.elf')],text=True).splitlines() if len(z:=line.split())==3}
def invoke(name,a=0,b=0,c=0):
 for i,v in enumerate(code):wr(BASE+i,v,1)
 for k,v in dict(arg0=a,arg1=b,arg2=c,target=symbols[name]|1,result=RESULT,callback=symbols['gMain']+4,previous=rd(symbols['gMain']+4)).items():wr(labels[k],v)
 wr(RESULT,0xdeadbeef)
 wr(symbols['gMain']+4,BASE|1)
 frames(1)
 assert rd(RESULT)!=0xdeadbeef,('native call did not return',name)
 return rd(RESULT)
checks=[]
def check(name,ok):
 assert ok,name
 checks.append(dict(test=name,passed=True))
def rules(entries,count=None,profiles=3):
 for i,row in enumerate(entries):
  for j,v in enumerate(row):wr(RULES+i*12+j*2,v,2)
 return invoke('ResolveDynamicEncounterRules',RULES,len(entries) if count is None else count,profiles)
def flag(n,on):
 a=rd(symbols['gSaveBlock1Ptr'])+0x1270+n//8
 wr(a,(rd(a,1)|(1<<(n%8))) if on else (rd(a,1)&~(1<<(n%8))),1)
assert lib.boot(str(R/'pokeemerald.gba').encode())
frames(600)
p=rd(symbols['gSaveBlock2Ptr'])
for i,v in enumerate([0xbb,0xcc,0xbf,0xc8,0xff,0,0,0]):wr(p+i,v,1)
wr(symbols['gMain']+4,symbols['CB2_NewGame']|1);frames(240)
count=rd(symbols['gWildMonHeaderCount'])
# The provider now returns badge-aware cached views; pointer identity with ROM data
# is intentionally no longer part of the contract.
for index in range(count):
 for tod in range(4):
  actual=invoke('GetEffectiveWildEncounterTypes',index,tod)
  assert actual!=0,(index,tod)
check('native_header_time_views_available',True)
empty=invoke('GetEffectiveWildEncounterTypes',0xffff,0)
check('invalid_header_has_empty_view',all(rd(empty+j*4)==0 for j in range(5)))
check('invalid_time_has_empty_view',invoke('GetEffectiveWildEncounterTypes',0,4)==empty)
check('oversized_header_has_empty_view',invoke('GetEffectiveWildEncounterTypes',0xffffffff,0)==empty)
check('no_active_map_profiles',invoke('GetDynamicEncounterProfileForMap',0,16)==0)
check('invalid_map_has_default_profile',invoke('GetDynamicEncounterProfileForMap',0xffff,0xffff)==0)
check('null_rules_fall_back',invoke('ResolveDynamicEncounterRules',0,1,3)==0)
check('empty_rules_fall_back',rules([],0)==0)
check('unconditional_rule_selects_profile',rules([(0,0,0,0,0,1)])==1)
flag(0x27,False);flag(0x28,False)
check('required_flag_blocks_profile',rules([(0x27,0,0,0,0,1)])==0)
flag(0x27,True)
check('required_flag_selects_profile',rules([(0x27,0,0,0,0,1)])==1)
flag(0x28,True)
check('forbidden_flag_blocks_profile',rules([(0x27,0x28,0,0,0,1)])==0)
flag(0x28,False)
check('first_matching_rule_wins',rules([(0x27,0,0,0,0,2),(0,0,0,0,0,1)])==2)
flag(0x27,False)
check('unmatched_rule_uses_next',rules([(0x27,0,0,0,0,2),(0,0,0,0,0,1)])==1)
variable=rd(symbols['gSaveBlock1Ptr'])+0x139c+(0x40f7-0x4000)*2
for value,expected in [(4,0),(5,1),(8,1),(9,0)]:
 wr(variable,value,2)
 check('variable_range_'+str(value),rules([(0,0,0x40f7,5,8,1)])==expected)
check('reversed_range_falls_back',rules([(0,0,0x40f7,8,5,1)])==0)
check('special_variable_rejected',rules([(0,0,0x800d,0,10,1)])==0)
check('invalid_flag_rejected',rules([(0xffff,0,0,0,0,1)])==0)
check('invalid_profile_rejected',rules([(0,0,0,0,0,3)])==0)
check('empty_profile_registry_rejected',rules([(0,0,0,0,0,1)],profiles=0)==0)
check('default_rule_overrides_later_match',rules([(0,0,0,0,0,0),(0,0,0,0,0,1)])==0)
lib.shutdown()
report=dict(rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),header_count=count,header_time_comparisons=count*4,checks=checks)
(D/'runtime_validation.json').write_text(json.dumps(report,indent=2)+'\n')
print('Native resolver checks:',len(checks),'header/time pointer comparisons:',count*4)
