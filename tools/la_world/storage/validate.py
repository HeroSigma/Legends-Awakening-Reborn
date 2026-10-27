"""Validate staged collection storage without editing the playable ROM/save."""
from pathlib import Path
import hashlib, json, subprocess, sys
from audit_layout import R, D, W
from generate_ev_prefix import render
P=Path(__file__).resolve().parent
RELEASE=Path('/mnt/c/Users/aadair/Downloads/Legends-Awakening-Reborn/Legends-Awakening-Reborn.gba')

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None

def run(args):return subprocess.check_output([str(a) for a in args],cwd=R,text=True)

def main():
    W.mkdir(parents=True,exist_ok=True);D.mkdir(parents=True,exist_ok=True)
    guarded=[R/'pokeemerald.gba',RELEASE,RELEASE.with_suffix('.sav')]
    before={str(p):digest(p) for p in guarded}
    assert (P/'compact_pc_ev_prefix.inc').read_text()==render(),'regenerate EV table'
    host=['gcc','-std=c11','-O1','-g','-Wall','-Wextra','-Werror','-fsanitize=address,undefined']
    run(host+[P/'compact_pc_codec.c',P/'test_compact_pc_codec.c','-o',W/'test_codec'])
    codec=json.loads(run([W/'test_codec',W/'1800_records.bin']))
    (D/'codec_validation.json').write_text(json.dumps(codec,indent=2)+'\n')
    arm=['arm-none-eabi-gcc','-mthumb','-march=armv4t','-mabi=apcs-gnu','-std=gnu17','-O2','-Wall','-Wextra','-Werror']
    run(arm+['-c',P/'compact_pc_codec.c','-o',W/'codec_arm.o'])
    run(arm+['-iquote','include','-iquote',P,'-DMODERN=1','-DEMERALD','-Wno-ignored-qualifiers','-Wno-sign-compare','-c',P/'reborn_pc_adapter.c','-o',W/'adapter_arm.o'])
    for stem in ['reborn_pc_bank','test_reborn_pc_bank']:
        run(arm+['-iquote','include','-iquote',P,'-DMODERN=1','-DEMERALD','-Wno-ignored-qualifiers','-Wno-sign-compare','-c',P/(stem+'.c'),'-o',W/(stem+'.o')])

    (W/'adapter.ld').write_text('SECTIONS { . = 0x09FF0000; .text : { *(.text*) } .rodata : { *(.rodata*) } .data : { *(.data*) } /DISCARD/ : { *(.ARM.attributes) *(.comment) } }')
    run(['arm-none-eabi-gcc','-mthumb','-march=armv4t','-mabi=apcs-gnu','-nostdlib','-Wl,-T,'+str(W/'adapter.ld'),'-Wl,--just-symbols,pokeemerald.elf',W/'adapter_arm.o',W/'codec_arm.o',W/'reborn_pc_bank.o',W/'test_reborn_pc_bank.o','-lgcc','-o',W/'adapter.elf'])
    run(['arm-none-eabi-objcopy','-O','binary',W/'adapter.elf',W/'adapter.bin'])
    print(run([sys.executable,P/'test_reborn_adapter.py']).strip())
    print(run([sys.executable,P/'test_collection_format.py']).strip())
    after={str(p):digest(p) for p in guarded}
    assert before==after,'guarded ROM/save changed during validation'
    report=dict(passed=True,scope='Isolated component tests; production integration is validated separately',codec=codec,adapter=json.loads((D/'adapter_validation.json').read_text()),save_format=json.loads((D/'save_format_validation.json').read_text()),guarded_files_unchanged=True,guarded_file_hashes=after)
    (D/'validation.json').write_text(json.dumps(report,indent=2)+'\n')
    print('PASS: codec, native adapter, synthetic save recovery; release and battery unchanged')
if __name__=='__main__':main()
