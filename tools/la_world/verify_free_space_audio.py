#!/usr/bin/env python3
"""Verify retained audio bytes and stable song IDs in the trimmed build."""
from pathlib import Path
import subprocess,re,json,struct,hashlib
R=Path(__file__).resolve().parents[2]
D=R/"docs/la_world/free_space/audio"
symbols={z[2]:int(z[0],16) for line in subprocess.check_output(["arm-none-eabi-nm","--defined-only",str(R/"pokeemerald-sinnoh-assets.elf")],text=True).splitlines() if len(z:=line.split())==3}
rom=(R/"pokeemerald-sinnoh-assets.gba").read_bytes()
def blob(address,size):
 assert 0x08000000<=address<=address+size<=0x08000000+len(rom)
 return rom[address-0x08000000:address-0x08000000+size]
source=(R/"sound/direct_sound_data.inc").read_text()
entries=re.findall(r"(\w+)::\s*\n(?:\.if TESTING == FALSE\n)?\s*\.incbin \"([^\"]+)\"",source)
variants={}
for label,path in entries:variants.setdefault(label,[]).append(path)
checked=[];omitted=[]
for label,paths in variants.items():
 if label not in symbols:omitted.append(label);continue
 assert any(blob(symbols[label],len(expected:=(R/path).read_bytes()))==expected for path in paths), label
 checked.append(label)
assert "Cry_Bulbasaur" in checked and "Cry_Pikachu" in checked
assert "Cry_SlowbroMega" not in symbols and "Cry_RayquazaMega" not in symbols
assert "Cry_Slowbro" in symbols and "Cry_Rayquaza" in symbols
table_source=(R/"sound/song_table.inc").read_text()
# Parse the original branch to keep the song ID inventory stable.
table_source=re.sub(r"\t\.if LA_AUDIO_GC\n\t\.rept \d+\n.*?\t\.endr\n\t\.else\n", "", table_source, flags=re.S)
rows=re.findall(r"^\s*song (\w+), (\w+), (\d+)",table_source,re.M)
players={"MUSIC_PLAYER_BGM":0,"MUSIC_PLAYER_SE1":1,"MUSIC_PLAYER_SE2":2,"MUSIC_PLAYER_SE3":3}
for i,(label,player,unknown) in enumerate(rows):
 ptr,mp,u=struct.unpack("<IHH",blob(symbols["gSongTable"]+8*i,8))
 expected_label = "dummy_song_header" if label.startswith("ph_") else label
 assert ptr==symbols[expected_label] and mp==players[player] and u==int(unknown), (i,label)
assert "gMultiBootProgram_PokemonColosseum_Start" not in symbols
report=dict(retained_sample_bytes_verified=len(checked),omitted_sample_labels=omitted,stable_song_table_entries=len(rows),rom_sha256=hashlib.sha256(rom).hexdigest(),runtime_audio_verified=False)
(D/"validation.json").write_text(json.dumps(report,indent=2)+"\n")
print(f"PASS: {len(checked)} retained samples byte-exact; {len(rows)} song IDs preserved; Bard phoneme slots silent")
