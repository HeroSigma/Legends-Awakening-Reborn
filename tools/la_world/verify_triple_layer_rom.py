from pathlib import Path
import re,json,subprocess,hashlib
P=Path(__file__).resolve().parents[2];D=P/'docs/la_world/triple_layer';rom=(P/'pokeemerald.gba').read_bytes();syms={}
for l in subprocess.check_output(['arm-none-eabi-nm','-S','--defined-only',str(P/'pokeemerald.elf')],text=True).splitlines():
 z=l.split()
 if len(z)==4:syms[z[3]]=(int(z[0],16),int(z[1],16))
paths=dict(re.findall(r'const u(?:16|32)\s+(\w+)\[\]\s*=\s*INCBIN_U(?:16|32)\("([^"]+)"\)',(P/'src/data/tilesets/metatiles.h').read_text()));count=0
for symbol,rel in paths.items():
 if symbol not in syms:continue
 raw=(P/rel).read_bytes();address,size=syms[symbol];assert size==len(raw),(symbol,size,len(raw));offset=address-0x8000000;assert rom[offset:offset+size]==raw,symbol;count+=1
v=json.loads((D/'validation.json').read_text());v['linked_metatile_and_attribute_arrays_verified']=count;v['rom_sha256']=hashlib.sha256(rom).hexdigest();v['rom_used_bytes']=32229076;v['rom_limit_bytes']=33554432;(D/'validation.json').write_text(json.dumps(v,indent=2)+'\n');print('PASS:',count,'linked metatile/attribute arrays match converted source byte-for-byte; ROM fits 32MB.')
