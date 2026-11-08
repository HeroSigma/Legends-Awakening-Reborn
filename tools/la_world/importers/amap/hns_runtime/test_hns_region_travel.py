from probe import *
import hashlib
D=R/'docs/la_world/hns_regions';m=json.loads((D/'manifest.json').read_text());results=[]
assert lib.boot(str(R/'pokeemerald.gba').encode());frames(600);wr(symbols['gMain']+4,symbols['CB2_NewGame']|1);frames(300)
def loc():
 p=rd(symbols['gSaveBlock1Ptr']);return [rd(p+4,1),rd(p+5,1)]
for label,name in [('LA_TeleportScientist_WarpKantoAR','HnS_PalletTown')]:
 row=next(x for x in m['maps'] if x['name']==name)
 # Invoke the compiled project-owned branch through the native bytecode interpreter.
 a=symbols['sGlobalScriptContext']
 for i in range(116):wr(a+i,0,1)
 wr(a+1,1,1);wr(a+8,symbols[label]);wr(a+92,symbols['gScriptCmdTable']);wr(a+96,symbols['gScriptCmdTableEnd'])
 wr(symbols['sGlobalScriptContextStatus'],0,1);wr(symbols['sLockFieldControls'],1,1)
 frames(240)
 results.append(dict(test=label,actual=loc(),expected=[row['group'],row['map']],position=list(pos()),passed=loc()==[row['group'],row['map']]))
 shot('hns_full_kanto_arrival')
(D/'runtime_final_travel.json').write_text(json.dumps(dict(rom_sha256=hashlib.sha256((R/'pokeemerald.gba').read_bytes()).hexdigest(),checks=results),indent=2)+'\n')
print(results);lib.shutdown()
