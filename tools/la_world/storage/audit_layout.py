"""Compile the actual Reborn ABI and inventory expanded-profile omissions.
Does not change game structs, ROMs, or player saves.
"""
from pathlib import Path
import json, struct, subprocess, hashlib
R=Path(__file__).resolve().parents[3]
D=R/'docs/la_world/compact_pc'
W=R/'.la_work/compact_pc'
OMIT=['pokeblocks','filler1','berryBlenderRecords','unused_9C2','tvShows','pokeNews','contestWinners','linkBattleRecords','enigmaBerry','mysteryGift','trainerHillTimes','ramScript','recordMixingGift','trainerNameRecords','registeredTexts','trainerHill','secretBases']
DECOR=['playerRoomDecorations','playerRoomDecorationPositions','decorationDesks','decorationChairs','decorationPlants','decorationOrnaments','decorationMats','decorationPosters','decorationDolls','decorationCushions']

def audit():
    W.mkdir(parents=True,exist_ok=True);D.mkdir(parents=True,exist_ok=True)
    fields=[('SaveBlock1',f) for f in OMIT+DECOR]+[('SaveBlock2','playerApprentice')]
    source='#include "global.h"\n#include "pokemon_storage_system.h"\n#include <stddef.h>\nconst unsigned layout[] = {\n'
    source+='sizeof(struct SaveBlock1), sizeof(struct SaveBlock2), sizeof(struct SaveBlock3), sizeof(struct PokemonStorage),\n'
    source+='\n'.join('offsetof(struct %s,%s), sizeof(((struct %s *)0)->%s),'%(s,f,s,f) for s,f in fields)+'\n};\n'
    c=W/'layout_audit.c';o=W/'layout_audit.o';b=W/'layout_audit.bin';c.write_text(source)
    subprocess.run(['arm-none-eabi-gcc','-iquote','include','-mabi=apcs-gnu','-mthumb','-march=armv4t','-DMODERN=1','-DEMERALD','-std=gnu17','-c',str(c),'-o',str(o)],cwd=R,check=True)
    subprocess.run(['arm-none-eabi-objcopy','-O','binary','--only-section=.rodata',str(o),str(b)],check=True)
    values=struct.unpack('<'+'I'*(b.stat().st_size//4),b.read_bytes())
    sizes=dict(zip(['SaveBlock1','SaveBlock2','SaveBlock3','PokemonStorage'],values[:4]))
    spans=[dict(block=s,field=f,offset=values[4+2*i],size=values[5+2*i]) for i,(s,f) in enumerate(fields)]
    # SaveBlock2's core ends immediately before apprentice/Frontier/minigame records.
    spans[-1]['size']=sizes['SaveBlock2']-spans[-1]['offset']
    kept=sizes['SaveBlock1']+sizes['SaveBlock2']-sum(v['size'] for v in spans)
    pc=60*30*31+4+60*9+60+4*100
    result=dict(version=2,sizes=sizes,expanded_omissions=spans,story_bytes=kept,pc_bytes=pc,header_bytes=64,sector_payload_bytes=4072,slot_sectors=16,slot_capacity=16*4072,slot_used=64+kept+pc+sizes['SaveBlock3'])
    result['slot_spare']=result['slot_capacity']-result['slot_used']
    assert result['slot_spare']>=0,result
    result['abi_sha256']=hashlib.sha256(json.dumps(result,sort_keys=True).encode()).hexdigest()
    (D/'layout_audit.json').write_text(json.dumps(result,indent=2)+'\n')
    return result
if __name__=='__main__':print(json.dumps(audit(),indent=2))
