#!/usr/bin/env python3
"""Verify map-ID preservation and linked four-region payloads after pruning."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
REPORT = ROOT / "docs/features/four-region-maps"

def symbols(elf):
    result = {}
    for line in subprocess.check_output(["arm-none-eabi-nm", "-S", str(elf)], text=True).splitlines():
        parts = line.split()
        if len(parts) == 4:
            address, size, kind, name = parts
            result[name] = (int(address, 16), int(size, 16))
        elif len(parts) == 3:
            address, kind, name = parts
            result[name] = (int(address, 16), 0)
    return result

def validate(before_elf, before_rom):
    manifest = json.loads((REPORT / "removal-manifest.json").read_text())
    groups = json.loads((ROOT / "data/maps/map_groups.json").read_text())
    slots = {name: [group, index] for group, key in enumerate(groups["group_order"])
             for index, name in enumerate(groups[key])}
    assert slots == manifest["original_map_slots"], "Map IDs shifted"
    for name, digest in manifest["retained_map_sha256"].items():
        assert hashlib.sha256((ROOT / "data/maps" / name / "map.json").read_bytes()).hexdigest() == digest, name
    layouts = json.loads((ROOT / "data/layouts/layouts.json").read_text())["layouts"]
    assert [row["id"] for row in layouts] == manifest["original_layout_ids"], "Layout IDs shifted"
    for row in layouts:
        if row["id"] in manifest["retained_layout_sha256"]:
            assert hashlib.sha256(json.dumps(row, sort_keys=True).encode()).hexdigest() == manifest["retained_layout_sha256"][row["id"]], row["id"]
        else:
            assert row.get("alias_of") == "LittlerootTown_Layout", row["id"]
    retired_ids = set(manifest["removed_map_ids"])
    for name in manifest["retained_map_sha256"]:
        row = json.loads((ROOT / "data/maps" / name / "map.json").read_text())
        for field in ("connections", "warp_events"):
            assert not any((event.get("map") in retired_ids or event.get("dest_map") in retired_ids) for event in row.get(field) or []), (name, field)
    encounters = json.loads((ROOT / "src/data/wild_encounters.json").read_text())
    assert not any(row.get("map") in retired_ids for group in encounters["wild_encounter_groups"]
                   for row in group.get("encounters", [])), "Retired encounters remain"

    old = symbols(before_elf)
    new = symbols(ROOT / "pokeemerald.elf")
    oldrom = Path(before_rom).read_bytes()
    newrom = (ROOT / "pokeemerald.gba").read_bytes()
    def payload(rom, symbol):
        address, size = symbol
        return rom[address - 0x08000000:address - 0x08000000 + size]
    removed_symbols = manifest["removed_tilesets"] + manifest["removed_graphics_symbols"]
    assert not any(name in new for name in removed_symbols), "Retired tileset graphics still linked"
    assert not any(name in new for name in ("sAccumulaGraphics", "sNuvemaGraphics", "sStreams")), "Test-map stream still linked"
    # Plain graphics and palette declarations contain no relocated pointers.
    graphics = set()
    declaration = re.compile(r"^const\s+u(?:8|16|32)\s+(?:ALIGNED\(\d+\)\s+)?(\w+)", re.M)
    for filename in ("graphics.h", "metatiles.h", "hyper_graphics.h", "hyper_metatiles.h",
                     "gs_johto_graphics.h", "gs_johto_metatiles.h", "mercury_johto_graphics.h", "mercury_johto_metatiles.h"):
        graphics.update(declaration.findall((ROOT / "src/data/tilesets" / filename).read_text()))
    checked_graphics = 0
    for name in graphics:
        if name not in old or not old[name][1]:
            continue
        assert name in new, "Retained asset missing: " + name
        assert payload(oldrom, old[name]) == payload(newrom, new[name]), "Retained asset changed: " + name
        checked_graphics += 1
    checked_layouts = 0
    for row in (row for row in layouts if row["id"] in manifest["retained_layout_sha256"]):
        for suffix, field in (("_Border", "border_filepath"), ("_Blockdata", "blockdata_filepath")):
            name = row["name"] + suffix
            if name not in old:
                continue
            assert name in new, name
            size = (ROOT / row[field]).stat().st_size
            assert payload(oldrom, (old[name][0], size)) == payload(newrom, (new[name][0], size)), name
        checked_layouts += 1
    for row in layouts:
        if row.get("alias_of"):
            assert new[row["name"]][0] == new["LittlerootTown_Layout"][0], row["name"]
            assert row["name"] + "_Blockdata" not in new, row["name"]
    used = new["__rom_end"][0] - 0x08000000
    result = {"retired_maps": len(retired_ids), "retained_maps_unchanged": len(manifest["retained_map_sha256"]),
              "retained_layouts_checked": checked_layouts, "retained_graphics_byte_exact": checked_graphics,
              "all_map_and_layout_ids_stable": True, "retired_graphics_absent": True,
              "used_rom_bytes": used, "free_rom_bytes": 32 * 1024 * 1024 - used,
              "recovered_rom_bytes": old["__rom_end"][0] - new["__rom_end"][0]}
    (REPORT / "validation.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--before-elf", required=True)
    parser.add_argument("--before-rom", required=True)
    args = parser.parse_args()
    validate(args.before_elf, args.before_rom)
