#!/usr/bin/env python3
from __future__ import annotations

import struct
import tempfile
from pathlib import Path
from types import SimpleNamespace

from amap_batch_bridge import LayoutInfo, RomScanner
from script_catalog import ROM_BASE, ScriptCatalog


def test_script_catalog() -> None:
    buf = bytearray(0x1000)
    root = 0x100
    child = 0x200
    text = 0x300
    movement = 0x400

    # lock; faceplayer; message; call; release; end
    stream = bytearray([0x6A, 0x5A, 0x67])
    stream += struct.pack("<I", ROM_BASE + text)
    stream += bytearray([0x04]) + struct.pack("<I", ROM_BASE + child)
    stream += bytearray([0x6C, 0x02])
    buf[root:root + len(stream)] = stream

    # setvar; applymovement; waitmovement; return
    child_stream = bytearray([0x16]) + struct.pack("<HH", 0x4000, 1)
    child_stream += bytearray([0x4F]) + struct.pack("<H", 1) + struct.pack("<I", ROM_BASE + movement)
    child_stream += bytearray([0x51]) + struct.pack("<H", 1) + bytearray([0x03])
    buf[child:child + len(child_stream)] = child_stream
    buf[text:text + 6] = bytes([0xC2, 0xD9, 0xE0, 0xE0, 0xE3, 0xFF])
    buf[movement:movement + 4] = bytes([0x01, 0x02, 0x03, 0xFE])

    class DummyScanner:
        data = bytes(buf)
        size = len(buf)

        def parse_map_scripts(self, _header):
            return {"entries": [{"index": 0, "type_name": "on_load", "script_pointer_raw": ROM_BASE + root}]}

        def parse_npcs(self, _header):
            return [], {"object": 0, "warp": 0, "coord": 0, "bg": 0}

        def parse_coord_events(self, _header):
            return [], {"object": 0, "warp": 0, "coord": 0, "bg": 0}

        def parse_bg_events(self, _header):
            return [], {"object": 0, "warp": 0, "coord": 0, "bg": 0}

    catalog = ScriptCatalog(DummyScanner(), Path(tempfile.mkdtemp()))
    diag = catalog.extract([SimpleNamespace(id="0.0", header_offset=0)])
    assert diag["script_count"] == 2
    assert root in catalog.scripts and child in catalog.scripts
    assert text in catalog.texts and movement in catalog.movements
    assert catalog.scripts[root]["status"] == "decoded"
    assert catalog.scripts[child]["status"] == "decoded"


def test_event_tables() -> None:
    buf = bytearray(0x1000)
    buf[0x100:0x104] = bytes([0, 0, 1, 2])
    struct.pack_into("<4I", buf, 0x104, 0, 0, ROM_BASE + 0x200, ROM_BASE + 0x220)

    struct.pack_into("<HH", buf, 0x200, 3, 4)
    buf[0x204] = 2
    struct.pack_into("<H", buf, 0x206, 0x4000)
    struct.pack_into("<H", buf, 0x208, 7)
    struct.pack_into("<I", buf, 0x20C, ROM_BASE + 0x500)

    struct.pack_into("<HH", buf, 0x220, 5, 6)
    buf[0x224] = 1
    buf[0x225] = 0
    struct.pack_into("<I", buf, 0x228, ROM_BASE + 0x510)

    struct.pack_into("<HH", buf, 0x22C, 7, 8)
    buf[0x230] = 0
    buf[0x231] = 7
    struct.pack_into("<HH", buf, 0x234, 25, 3)

    buf[0x300] = 1
    struct.pack_into("<I", buf, 0x301, ROM_BASE + 0x500)
    buf[0x305] = 2
    struct.pack_into("<I", buf, 0x306, ROM_BASE + 0x340)
    buf[0x30A] = 0
    struct.pack_into("<HHI", buf, 0x340, 0x4001, 2, ROM_BASE + 0x520)
    struct.pack_into("<H", buf, 0x348, 0)

    scanner = object.__new__(RomScanner)
    scanner.data = bytes(buf)
    scanner.size = len(buf)
    scanner._header_cache = {
        0: {
            "events_offset": 0x100,
            "scripts_offset": 0x300,
            "connections_offset": None,
            "layout": LayoutInfo(0, 20, 20, 0, 0, 0, 0),
        }
    }

    coords, _ = scanner.parse_coord_events(0)
    bgs, _ = scanner.parse_bg_events(0)
    scripts = scanner.parse_map_scripts(0)
    assert coords[0]["script_pointer_raw"] == ROM_BASE + 0x500
    assert bgs[0]["type"] == "sign"
    assert bgs[1]["type"] == "hidden_item"
    assert scripts["entries"][1]["conditions"][0]["script_pointer_raw"] == ROM_BASE + 0x520


def main() -> int:
    test_script_catalog()
    test_event_tables()
    print("A-Map Batch Bridge v1.0 self-test: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
