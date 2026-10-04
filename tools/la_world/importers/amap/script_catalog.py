from __future__ import annotations

import json
import struct
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

ROM_BASE = 0x08000000
MOVEMENT_ACTION_STEP_END = 0xFE
MAX_SCRIPT_COMMANDS = 4096
MAX_SCRIPT_BYTES = 0x10000
MAX_TEXT_BYTES = 0x1000
MAX_MOVEMENT_BYTES = 0x400
MAX_MART_ITEMS = 0x200


def u16(data: bytes, off: int) -> int:
    return struct.unpack_from("<H", data, off)[0]


def u32(data: bytes, off: int) -> int:
    return struct.unpack_from("<I", data, off)[0]


def gba_to_offset(ptr: int, rom_size: int) -> Optional[int]:
    if ROM_BASE <= ptr < ROM_BASE + rom_size:
        return ptr - ROM_BASE
    return None


def offset_to_gba(off: int) -> int:
    return ROM_BASE + off


def ptr_hex(off: Optional[int]) -> Optional[str]:
    return None if off is None else f"0x{offset_to_gba(off):08X}"


# Emerald event command names and fixed command lengths. Lengths include the
# opcode byte. 0x5C (trainerbattle) is variable and handled separately.
# The command order follows pret/pokeemerald data/script_cmd_table.inc.
_OP_NAMES = [
    "nop", "nop1", "end", "return", "call", "goto", "goto_if", "call_if",
    "gotostd", "callstd", "gotostd_if", "callstd_if", "returnram", "endram",
    "setmysteryeventstatus", "loadword", "loadbyte", "setptr", "loadbytefromptr",
    "setptrbyte", "copylocal", "copybyte", "setvar", "addvar", "subvar", "copyvar",
    "setorcopyvar", "compare_local_to_local", "compare_local_to_value",
    "compare_local_to_ptr", "compare_ptr_to_local", "compare_ptr_to_value",
    "compare_ptr_to_ptr", "compare_var_to_value", "compare_var_to_var", "callnative",
    "gotonative", "special", "specialvar", "waitstate", "delay", "setflag",
    "clearflag", "checkflag", "initclock", "dotimebasedevents", "gettime", "playse",
    "waitse", "playfanfare", "waitfanfare", "playbgm", "savebgm", "fadedefaultbgm",
    "fadenewbgm", "fadeoutbgm", "fadeinbgm", "warp", "warpsilent", "warpdoor",
    "warphole", "warpteleport", "setwarp", "setdynamicwarp", "setdivewarp",
    "setholewarp", "getplayerxy", "getpartysize", "additem", "removeitem",
    "checkitemspace", "checkitem", "checkitemtype", "addpcitem", "checkpcitem",
    "adddecoration", "removedecoration", "checkdecor", "checkdecorspace", "applymovement",
    "applymovementat", "waitmovement", "waitmovementat", "removeobject", "removeobjectat",
    "addobject", "addobjectat", "setobjectxy", "showobjectat", "hideobjectat", "faceplayer",
    "turnobject", "trainerbattle", "dotrainerbattle", "gotopostbattlescript",
    "gotobeatenscript", "checktrainerflag", "settrainerflag", "cleartrainerflag",
    "setobjectxyperm", "copyobjectxytoperm", "setobjectmovementtype", "waitmessage", "message",
    "closemessage", "lockall", "lock", "releaseall", "release", "waitbuttonpress", "yesnobox",
    "multichoice", "multichoicedefault", "multichoicegrid", "drawbox", "erasebox",
    "drawboxtext", "showmonpic", "hidemonpic", "showcontestpainting", "braillemessage",
    "givemon", "giveegg", "setmonmove", "checkpartymove", "bufferspeciesname",
    "bufferleadmonspeciesname", "bufferpartymonnick", "bufferitemname", "bufferdecorationname",
    "buffermovename", "buffernumberstring", "bufferstdstring", "bufferstring", "pokemart",
    "pokemartdecoration", "pokemartdecoration2", "playslotmachine", "setberrytree",
    "choosecontestmon", "startcontest", "showcontestresults", "contestlinktransfer", "random",
    "addmoney", "removemoney", "checkmoney", "showmoneybox", "hidemoneybox", "updatemoneybox",
    "getpokenewsactive", "fadescreen", "fadescreenspeed", "setflashlevel", "animateflash",
    "messageautoscroll", "dofieldeffect", "setfieldeffectargument", "waitfieldeffect", "setrespawn",
    "checkplayergender", "playmoncry", "setmetatile", "resetweather", "setweather", "doweather",
    "setstepcallback", "setmaplayoutindex", "setobjectsubpriority", "resetobjectsubpriority",
    "createvobject", "turnvobject", "opendoor", "closedoor", "waitdooranim", "setdooropen",
    "setdoorclosed", "addelevmenuitem", "showelevmenu", "checkcoins", "addcoins", "removecoins",
    "setwildbattle", "dowildbattle", "setvaddress", "vgoto", "vcall", "vgoto_if", "vcall_if",
    "vmessage", "vbuffermessage", "vbufferstring", "showcoinsbox", "hidecoinsbox", "updatecoinsbox",
    "incrementgamestat", "setescapewarp", "waitmoncry", "bufferboxname", "textcolor", "loadhelp",
    "unloadhelp", "signmsg", "normalmsg", "comparehiddenvar", "setmodernfatefulencounter",
    "checkmodernfatefulencounter", "trywondercardscript", "setworldmapflag", "warpspinenter",
    "setmonmetlocation", "moverotatingtileobjects", "turnrotatingtileobjects", "initrotatingtilepuzzle",
    "freerotatingtilepuzzle", "warpmossdeepgym", "selectapproachingtrainer", "lockfortrainer",
    "closebraillemessage", "messageinstant", "fadescreenswapbuffers", "buffertrainerclassname",
    "buffertrainername", "pokenavcall", "warpwhitefade", "buffercontestname", "bufferitemnameplural",
]

# Fixed byte lengths from the Emerald event macro definitions. Values corrected
# for nested `map`/`formatwarp` macros and commands that have separate AT forms.
_OP_LENGTHS = [
    1,1,1,1,5,5,6,6,2,2,3,3,1,1,2,6,3,6,6,6,3,9,5,5,5,5,5,3,3,6,6,6,9,5,5,5,5,3,5,1,3,3,3,3,5,1,1,3,1,3,1,4,3,1,3,2,2,8,8,8,3,8,8,8,8,8,5,1,5,5,5,5,3,5,5,3,3,3,3,7,9,3,5,3,5,3,5,7,5,5,1,4,0,1,1,1,3,3,3,7,3,4,1,5,1,1,1,1,1,1,3,5,6,6,1,5,5,5,1,2,5,15,3,5,3,4,2,4,4,4,4,4,4,6,5,5,5,3,4,1,1,1,1,3,6,6,6,4,3,4,3,2,3,3,2,5,3,4,3,3,1,5,9,1,3,1,2,3,6,5,9,3,5,5,1,5,5,8,1,3,3,3,6,1,5,5,5,6,6,5,5,6,3,3,3,2,8,1,4,2,5,1,1,1,6,3,3,1,3,8,4,3,1,3,1,8,1,1,1,5,2,4,4,5,8,4,6,
]

if len(_OP_NAMES) != 0xE3 or len(_OP_LENGTHS) != 0xE3:
    raise RuntimeError("internal Emerald script opcode table length mismatch")

OP_SPECS: Dict[int, Tuple[str, int]] = {
    i: (_OP_NAMES[i], _OP_LENGTHS[i]) for i in range(0xE3)
}

# Map-header script constants from include/constants/map_scripts.h.
MAP_SCRIPT_TYPES = {
    1: "on_load",
    2: "on_frame_table",
    3: "on_transition",
    4: "on_warp_into_map_table",
    5: "on_resume",
    6: "on_dive_warp",
    7: "on_return_to_field",
}

# Trainer battle command lengths by TRAINER_BATTLE_* mode. The six-byte base is
# opcode + type + trainer id + local id, followed by N pointers.
_TRAINER_BATTLE_POINTER_COUNTS = {
    0: 2,  # SINGLE
    1: 3,  # CONTINUE_SCRIPT_NO_MUSIC
    2: 3,  # CONTINUE_SCRIPT
    3: 1,  # SINGLE_NO_INTRO_TEXT
    4: 3,  # DOUBLE
    5: 2,  # REMATCH
    6: 4,  # CONTINUE_SCRIPT_DOUBLE
    7: 3,  # REMATCH_DOUBLE
    8: 4,  # CONTINUE_SCRIPT_DOUBLE_NO_MUSIC
    9: 2,  # PYRAMID
    10: 2, # SET_TRAINER_A
    11: 2, # SET_TRAINER_B
    12: 2, # HILL
}
_TRAINER_BATTLE_SCRIPT_ARG = {1: 2, 2: 2, 6: 3, 8: 3}

# Minimal readable Gen III text map. Raw bytes remain authoritative, so unknown
# control codes are rendered as escapes rather than guessed.
_GEN3_TEXT: Dict[int, str] = {0x00: " "}
for _i, _c in enumerate("0123456789"):
    _GEN3_TEXT[0xA1 + _i] = _c
_GEN3_TEXT.update({
    0xAB: "!", 0xAC: "?", 0xAD: ".", 0xAE: "-", 0xAF: "·", 0xB0: "…",
    0xB1: "“", 0xB2: "”", 0xB3: "‘", 0xB4: "’", 0xB5: "♂", 0xB6: "♀",
    0xB7: "¥", 0xB8: ",", 0xB9: "×", 0xBA: "/", 0xF0: ":",
})
for _i, _c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    _GEN3_TEXT[0xBB + _i] = _c
for _i, _c in enumerate("abcdefghijklmnopqrstuvwxyz"):
    _GEN3_TEXT[0xD5 + _i] = _c


@dataclass
class ScriptRoot:
    pointer: int
    source: str
    map_id: str
    source_index: Optional[int] = None
    source_detail: Optional[str] = None


class ScriptCatalog:
    """Lossless-first Emerald event-script catalog/decompiler.

    The decoder follows known Emerald script pointers, texts, movement streams and
    marts. If a hack introduces an unsupported opcode or malformed command, the
    record is stopped at that exact byte and a raw diagnostic window is preserved.
    It never guesses a command length after an unknown opcode.
    """

    def __init__(self, scanner, out: Path):
        self.s = scanner
        self.data: bytes = scanner.data
        self.size: int = scanner.size
        self.out = Path(out)
        self.scripts: Dict[int, dict] = {}
        self.texts: Dict[int, dict] = {}
        self.movements: Dict[int, dict] = {}
        self.marts: Dict[int, dict] = {}
        self.roots_by_map: Dict[str, List[dict]] = {}
        self.reachable_by_map: Dict[str, set[int]] = {}
        self.warnings: List[str] = []
        self._queue: List[Tuple[int, str]] = []
        self._queued: set[int] = set()
        self._active_map: Optional[str] = None

    def _valid_off(self, off: Optional[int], size: int = 1) -> bool:
        return off is not None and 0 <= int(off) <= self.size - size

    def _ptr_off(self, raw: int) -> Optional[int]:
        return gba_to_offset(raw, self.size)

    def _queue_script(self, raw_ptr: int, reason: str, map_id: Optional[str] = None) -> Optional[int]:
        off = self._ptr_off(raw_ptr)
        if off is None:
            return None
        if map_id:
            self.reachable_by_map.setdefault(map_id, set()).add(off)
        if off not in self._queued and off not in self.scripts:
            self._queued.add(off)
            self._queue.append((off, reason))
        return off

    def add_root(self, root: ScriptRoot) -> None:
        off = self._ptr_off(root.pointer)
        rec = {
            "pointer": f"0x{root.pointer:08X}",
            "offset": off,
            "source": root.source,
            "source_index": root.source_index,
            "source_detail": root.source_detail,
        }
        self.roots_by_map.setdefault(root.map_id, []).append(rec)
        if off is not None:
            self.reachable_by_map.setdefault(root.map_id, set()).add(off)
            self._queue_script(root.pointer, f"root:{root.source}", root.map_id)
        else:
            rec["status"] = "invalid_pointer"

    def _decode_text_preview(self, raw: bytes) -> str:
        out: List[str] = []
        for b in raw:
            if b == 0xFF:
                break
            if b in (0xFA, 0xFB, 0xFC, 0xFD, 0xFE):
                out.append(f"<{b:02X}>")
            else:
                out.append(_GEN3_TEXT.get(b, f"<{b:02X}>"))
        return "".join(out)

    def _extract_text(self, ptr: int, source: str) -> Optional[dict]:
        off = self._ptr_off(ptr)
        if off is None:
            return None
        if off in self.texts:
            self.texts[off].setdefault("sources", []).append(source)
            return self.texts[off]
        end = off
        while end < self.size and end - off < MAX_TEXT_BYTES:
            if self.data[end] == 0xFF:
                end += 1
                break
            end += 1
        raw = self.data[off:end]
        terminated = bool(raw and raw[-1] == 0xFF)
        rec = {
            "pointer": ptr_hex(off),
            "offset": off,
            "length": len(raw),
            "terminated": terminated,
            "preview": self._decode_text_preview(raw),
            "raw_hex": raw.hex(),
            "sources": [source],
        }
        if not terminated:
            rec["status"] = "unterminated_or_too_long"
            self.warnings.append(f"Text {ptr_hex(off)} did not terminate within {MAX_TEXT_BYTES} bytes")
        else:
            rec["status"] = "extracted"
        self.texts[off] = rec
        return rec

    def _extract_movement(self, ptr: int, source: str) -> Optional[dict]:
        off = self._ptr_off(ptr)
        if off is None:
            return None
        if off in self.movements:
            self.movements[off].setdefault("sources", []).append(source)
            return self.movements[off]
        end = off
        while end < self.size and end - off < MAX_MOVEMENT_BYTES:
            b = self.data[end]
            end += 1
            if b == MOVEMENT_ACTION_STEP_END:
                break
        raw = self.data[off:end]
        terminated = bool(raw and raw[-1] == MOVEMENT_ACTION_STEP_END)
        rec = {
            "pointer": ptr_hex(off),
            "offset": off,
            "length": len(raw),
            "terminated": terminated,
            "actions": list(raw),
            "raw_hex": raw.hex(),
            "sources": [source],
            "status": "extracted" if terminated else "unterminated_or_too_long",
        }
        self.movements[off] = rec
        if not terminated:
            self.warnings.append(f"Movement {ptr_hex(off)} did not terminate with 0xFE within {MAX_MOVEMENT_BYTES} bytes")
        return rec

    def _extract_mart(self, ptr: int, source: str) -> Optional[dict]:
        off = self._ptr_off(ptr)
        if off is None:
            return None
        if off in self.marts:
            self.marts[off].setdefault("sources", []).append(source)
            return self.marts[off]
        items: List[int] = []
        pos = off
        terminated = False
        for _ in range(MAX_MART_ITEMS):
            if pos + 2 > self.size:
                break
            item = u16(self.data, pos)
            pos += 2
            if item == 0:
                terminated = True
                break
            items.append(item)
        raw = self.data[off:pos]
        rec = {
            "pointer": ptr_hex(off),
            "offset": off,
            "length": len(raw),
            "terminated": terminated,
            "items": items,
            "raw_hex": raw.hex(),
            "sources": [source],
            "status": "extracted" if terminated else "unterminated_or_too_long",
        }
        self.marts[off] = rec
        if not terminated:
            self.warnings.append(f"Mart list {ptr_hex(off)} did not terminate within {MAX_MART_ITEMS} items")
        return rec

    @staticmethod
    def _command_u8(raw: bytes, rel: int) -> int:
        return raw[rel]

    @staticmethod
    def _command_u16(raw: bytes, rel: int) -> int:
        return struct.unpack_from("<H", raw, rel)[0]

    @staticmethod
    def _command_u32(raw: bytes, rel: int) -> int:
        return struct.unpack_from("<I", raw, rel)[0]

    def _trainerbattle_length(self, pos: int) -> Optional[int]:
        if pos + 2 > self.size:
            return None
        mode = self.data[pos + 1]
        count = _TRAINER_BATTLE_POINTER_COUNTS.get(mode)
        if count is None:
            return None
        return 6 + count * 4

    def _classify_command_refs(self, pos: int, opcode: int, raw: bytes, map_id: Optional[str]) -> List[dict]:
        refs: List[dict] = []
        src = ptr_hex(pos) or f"offset:{pos}"

        def add_ref(kind: str, ptr: int, follow_script: bool = False, asset: Optional[str] = None):
            off = self._ptr_off(ptr)
            rec = {"kind": kind, "pointer": f"0x{ptr:08X}", "offset": off}
            refs.append(rec)
            if follow_script and off is not None:
                self._queue_script(ptr, f"{src}:{OP_SPECS[opcode][0]}", map_id)
            elif asset == "text" and off is not None:
                self._extract_text(ptr, src)
            elif asset == "movement" and off is not None:
                self._extract_movement(ptr, src)
            elif asset == "mart" and off is not None:
                self._extract_mart(ptr, src)

        # Branch/call script pointers.
        if opcode in (0x04, 0x05):
            add_ref("script", self._command_u32(raw, 1), follow_script=True)
        elif opcode in (0x06, 0x07):
            add_ref("script", self._command_u32(raw, 2), follow_script=True)

        # Movement streams.
        elif opcode in (0x4F, 0x50):
            add_ref("movement", self._command_u32(raw, 3), asset="movement")

        # Message/text pointers.
        elif opcode in (0x67, 0x78, 0x85, 0x9B, 0xDB, 0xDF):
            add_ref("text", self._command_u32(raw, 1), asset="text")

        # Mart lists.
        elif opcode in (0x86, 0x87, 0x88):
            add_ref("mart", self._command_u32(raw, 1), asset="mart")

        # Trainer battle has mode-dependent text/event-script pointer fields.
        elif opcode == 0x5C and len(raw) >= 6:
            mode = raw[1]
            count = _TRAINER_BATTLE_POINTER_COUNTS.get(mode, 0)
            script_arg = _TRAINER_BATTLE_SCRIPT_ARG.get(mode)
            for i in range(count):
                p = self._command_u32(raw, 6 + i * 4)
                if script_arg == i:
                    add_ref("trainer_event_script", p, follow_script=True)
                else:
                    add_ref("trainer_text_or_data", p, asset="text")
        return refs

    def _decode_script(self, off: int, reason: str, map_id: Optional[str]) -> dict:
        if off in self.scripts:
            return self.scripts[off]
        pos = off
        commands: List[dict] = []
        status = "decoded"
        stop_reason = "terminator"
        command_count = 0

        while pos < self.size and pos - off < MAX_SCRIPT_BYTES and command_count < MAX_SCRIPT_COMMANDS:
            opcode = self.data[pos]
            spec = OP_SPECS.get(opcode)
            if spec is None:
                status = "unsupported_opcode"
                stop_reason = f"opcode_0x{opcode:02X}_outside_emerald_table"
                break
            name, length = spec
            if opcode == 0x5C:
                dyn_len = self._trainerbattle_length(pos)
                if dyn_len is None:
                    status = "unsupported_trainerbattle_mode"
                    stop_reason = "unknown_trainerbattle_mode"
                    break
                length = dyn_len
            if length <= 0 or pos + length > self.size:
                status = "truncated_command"
                stop_reason = f"truncated_{name}"
                break
            raw = self.data[pos:pos + length]
            cmd = {
                "offset": pos,
                "pointer": ptr_hex(pos),
                "opcode": opcode,
                "opcode_hex": f"0x{opcode:02X}",
                "name": name,
                "length": length,
                "raw_hex": raw.hex(),
            }
            refs = self._classify_command_refs(pos, opcode, raw, map_id)
            if refs:
                cmd["references"] = refs
            # Helpful structured fields for common commands.
            if opcode in (0x16, 0x17, 0x18, 0x19, 0x1A, 0x21, 0x22) and length >= 5:
                cmd["arg0_u16"] = self._command_u16(raw, 1)
                cmd["arg1_u16"] = self._command_u16(raw, 3)
            elif opcode in (0x29, 0x2A, 0x2B, 0x60, 0x61, 0x62) and length >= 3:
                cmd["arg_u16"] = self._command_u16(raw, 1)
            elif opcode in (0x39,0x3A,0x3B,0x3D,0x3E,0x3F,0x40,0x41,0xC4,0xD1,0xD7,0xE0) and length == 8:
                cmd["warp"] = {
                    "map_group": raw[1], "map_num": raw[2], "warp_id": raw[3],
                    "x": struct.unpack_from("<h", raw, 4)[0],
                    "y": struct.unpack_from("<h", raw, 6)[0],
                }
            elif opcode == 0x3C and length == 3:
                cmd["warp"] = {"map_group": raw[1], "map_num": raw[2]}
            elif opcode == 0x5C and length >= 6:
                cmd["trainerbattle"] = {
                    "mode": raw[1],
                    "trainer": self._command_u16(raw, 2),
                    "local_id": self._command_u16(raw, 4),
                }
            commands.append(cmd)
            command_count += 1
            pos += length

            # Hard linear-flow terminators. Calls and conditional branches keep
            # decoding the fall-through path while their targets are queued.
            if opcode in (0x02, 0x03, 0x05, 0x08, 0x0C, 0x0D, 0x5E, 0x5F, 0xB9):
                stop_reason = name
                break
        else:
            if command_count >= MAX_SCRIPT_COMMANDS:
                status = "limit_reached"
                stop_reason = "command_limit"
            elif pos - off >= MAX_SCRIPT_BYTES:
                status = "limit_reached"
                stop_reason = "byte_limit"
            elif pos >= self.size:
                status = "rom_end"
                stop_reason = "rom_end"

        decoded_end = pos
        # On a failure, include a short raw diagnostic tail beginning at the byte
        # that could not safely be decoded. This is deliberately not interpreted.
        diagnostic_tail = b""
        if status != "decoded":
            diagnostic_tail = self.data[pos:min(self.size, pos + 64)]

        rec = {
            "pointer": ptr_hex(off),
            "offset": off,
            "source_reason": reason,
            "status": status,
            "stop_reason": stop_reason,
            "decoded_length": max(0, decoded_end - off),
            "commands": commands,
            "diagnostic_tail_hex": diagnostic_tail.hex(),
        }
        self.scripts[off] = rec
        return rec

    def _propagate_reachability(self, map_id: str) -> None:
        # Scripts are globally deduplicated, but per-map reachability should include
        # dependencies discovered from any script already known for this map.
        known = self.reachable_by_map.setdefault(map_id, set())
        changed = True
        while changed:
            changed = False
            for off in list(known):
                rec = self.scripts.get(off)
                if not rec:
                    continue
                for cmd in rec.get("commands", []):
                    for ref in cmd.get("references", []):
                        if ref.get("kind") not in ("script", "trainer_event_script"):
                            continue
                        target = ref.get("offset")
                        if isinstance(target, int) and target not in known:
                            known.add(target)
                            changed = True

    def scan_maps(self, maps: Iterable) -> None:
        maps = list(maps)
        for m in maps:
            map_id = m.id
            # Map-header scripts and conditional map-script tables.
            map_scripts = self.s.parse_map_scripts(m.header_offset)
            for entry in map_scripts.get("entries", []):
                p = entry.get("script_pointer_raw")
                if isinstance(p, int) and not entry.get("script_pointer_is_condition_table"):
                    self.add_root(ScriptRoot(p, "map_script", map_id, entry.get("index"), entry.get("type_name")))
                for cond in entry.get("conditions", []):
                    cp = cond.get("script_pointer_raw")
                    if isinstance(cp, int):
                        self.add_root(ScriptRoot(cp, "map_script_condition", map_id, cond.get("index"), entry.get("type_name")))

            # Object-event scripts.
            npcs, _ = self.s.parse_npcs(m.header_offset)
            for npc in npcs:
                p = npc.get("script_pointer_raw")
                if isinstance(p, int) and p:
                    self.add_root(ScriptRoot(p, "object_event", map_id, npc.get("index"), f"local_id={npc.get('local_id')}"))

            # Coordinate scripts. NULL scripts are weather coord events.
            coords, _ = self.s.parse_coord_events(m.header_offset)
            for ev in coords:
                p = ev.get("script_pointer_raw")
                if isinstance(p, int) and p:
                    self.add_root(ScriptRoot(p, "coord_event", map_id, ev.get("index"), f"x={ev.get('x')},y={ev.get('y')}"))

            # Sign/background scripts only. Hidden items and secret bases carry data.
            bgs, _ = self.s.parse_bg_events(m.header_offset)
            for ev in bgs:
                p = ev.get("script_pointer_raw")
                if isinstance(p, int) and p:
                    self.add_root(ScriptRoot(p, "bg_event", map_id, ev.get("index"), f"kind={ev.get('kind')}"))

        # Decode roots and recursively queued dependencies. Keep the originating
        # map when possible so dependencies become reachable from that map.
        while self._queue:
            off, reason = self._queue.pop(0)
            self._queued.discard(off)
            owner_maps = [mid for mid, offsets in self.reachable_by_map.items() if off in offsets]
            map_id = owner_maps[0] if owner_maps else None
            self._decode_script(off, reason, map_id)
            # A newly decoded script may have queued children; mark those children
            # reachable from every map that can reach the parent.
            rec = self.scripts[off]
            child_offsets = []
            for cmd in rec.get("commands", []):
                for ref in cmd.get("references", []):
                    if ref.get("kind") in ("script", "trainer_event_script") and isinstance(ref.get("offset"), int):
                        child_offsets.append(int(ref["offset"]))
            for mid in owner_maps:
                self.reachable_by_map.setdefault(mid, set()).update(child_offsets)

        for m in maps:
            self._propagate_reachability(m.id)

    def map_payload(self, map_id: str) -> dict:
        reachable = sorted(self.reachable_by_map.get(map_id, set()))
        return {
            "roots": self.roots_by_map.get(map_id, []),
            "reachable_script_pointers": [ptr_hex(x) for x in reachable],
            "scripts": [self.scripts[x] for x in reachable if x in self.scripts],
        }

    def _write_global_assets(self) -> None:
        root = self.out / "scripts"
        root.mkdir(parents=True, exist_ok=True)
        (root / "script_catalog.json").write_text(json.dumps({
            "format": "A-Map Batch Bridge script catalog v1.0",
            "decoder": "Emerald event bytecode, lossless-first conservative mode",
            "scripts": [self.scripts[k] for k in sorted(self.scripts)],
            "texts": [self.texts[k] for k in sorted(self.texts)],
            "movements": [self.movements[k] for k in sorted(self.movements)],
            "marts": [self.marts[k] for k in sorted(self.marts)],
            "warnings": self.warnings,
        }, indent=2, ensure_ascii=False), encoding="utf-8")

        # Human-readable disassembly. It is intentionally diagnostic output, not a
        # claim that original source labels or expansion-ready symbolic constants
        # can be recovered from a compiled ROM.
        lines: List[str] = [
            "# A-Map Batch Bridge v1.0 script disassembly",
            "# Diagnostic reconstruction from ROM bytecode; labels are generated.",
            "",
        ]
        for off in sorted(self.scripts):
            rec = self.scripts[off]
            lines.append(f"Script_{offset_to_gba(off):08X}:")
            for cmd in rec.get("commands", []):
                refs = cmd.get("references", [])
                suffix = ""
                if refs:
                    suffix = "  ; " + ", ".join(f"{r['kind']}={r['pointer']}" for r in refs)
                lines.append(f"  {cmd['pointer']}: {cmd['raw_hex']:<48} {cmd['name']}{suffix}")
            if rec.get("status") != "decoded":
                lines.append(f"  ; STOP {rec.get('status')}: {rec.get('stop_reason')}")
                if rec.get("diagnostic_tail_hex"):
                    lines.append(f"  ; raw tail {rec['diagnostic_tail_hex']}")
            lines.append("")
        (root / "scripts_disassembly.txt").write_text("\n".join(lines), encoding="utf-8")

    def extract(self, maps: Iterable) -> dict:
        maps = list(maps)
        self.scan_maps(maps)
        self._write_global_assets()
        return {
            "script_count": len(self.scripts),
            "text_count": len(self.texts),
            "movement_count": len(self.movements),
            "mart_count": len(self.marts),
            "root_count": sum(len(v) for v in self.roots_by_map.values()),
            "decoded_script_count": sum(1 for r in self.scripts.values() if r.get("status") == "decoded"),
            "partial_script_count": sum(1 for r in self.scripts.values() if r.get("status") != "decoded"),
            "warnings": self.warnings,
        }
