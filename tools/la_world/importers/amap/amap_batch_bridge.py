#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Optional, Tuple

import legacy_emerald_bridge as legacy
from frlg_bridge import PROFILES, FireRedScanner, FireRedNormalizedExtractor, profile_for_sha

# Compatibility re-exports used by the v1.0 ROM-free self-test.
LayoutInfo = legacy.LayoutInfo
RomScanner = legacy.RomScanner



def parse_map_selector(text: str) -> Tuple[int,int]:
    m=re.fullmatch(r"\s*(\d+)\.(\d+)\s*",text)
    if not m:
        raise argparse.ArgumentTypeError("Map IDs must look like 3.0")
    return int(m.group(1)),int(m.group(2))


def select_profile(path: Path, requested: str) -> Tuple[str, Optional[dict]]:
    data=path.read_bytes(); sha=hashlib.sha256(data).hexdigest()
    if requested != "auto":
        if requested == "hyper_emerald": return requested,None
        p=PROFILES.get(requested)
        if not p: raise SystemExit(f"Unknown profile: {requested}")
        if p["sha256"] != sha:
            raise SystemExit(f"ROM SHA does not match requested profile {requested}\nexpected {p['sha256']}\nactual   {sha}")
        return requested,p
    hit=profile_for_sha(sha)
    if hit: return hit
    code=data[0xAC:0xB0].decode("ascii","replace") if len(data)>=0xB0 else ""
    if code == "BPEE": return "hyper_emerald",None
    raise SystemExit("Unknown ROM build. Use --profile with a supported exact-build profile.")


def main() -> int:
    ap=argparse.ArgumentParser(description="A-Map Batch Bridge v1.1 - Hyper Emerald + exact-build FireRed donor profiles")
    ap.add_argument("rom",nargs="?",type=Path)
    ap.add_argument("--profile",default="auto",choices=["auto","hyper_emerald",*PROFILES.keys()])
    ap.add_argument("--scan",action="store_true")
    ap.add_argument("--extract",action="append",type=parse_map_selector,default=[])
    ap.add_argument("--extract-all",action="store_true")
    ap.add_argument("--out",type=Path,default=Path("AmapBridgeExport"))
    ap.add_argument("--names",type=Path)
    ap.add_argument("--list-profiles",action="store_true")
    args=ap.parse_args()
    if args.list_profiles:
        print("hyper_emerald: legacy Emerald-derived autodiscovery (v1.0 path)")
        for key,p in PROFILES.items():
            print(f"{key}: {p['label']} | {p['sha256']}")
        return 0
    if not args.rom:
        ap.error("ROM path is required unless --list-profiles is used")
    profile_key,profile=select_profile(args.rom,args.profile)
    if profile_key == "hyper_emerald":
        scanner=legacy.RomScanner(args.rom,args.names); scanner.discover()
        print(json.dumps(scanner.diagnostics(),indent=2))
        if args.scan and not args.extract and not args.extract_all: return 0
        chosen=scanner.maps if args.extract_all else [scanner.get_map(*x) for x in args.extract]
        if not chosen: return 0
        manifest=legacy.Extractor(scanner,args.out).extract(chosen)
        print(f"Exported {len(manifest['maps'])} map(s) to {args.out}")
        return 0
    scanner=FireRedScanner(args.rom,profile_key,args.names); scanner.discover()
    diag=scanner.diagnostics(); print(json.dumps(diag,indent=2))
    if args.scan and not args.extract and not args.extract_all: return 0
    chosen=scanner.maps if args.extract_all else [scanner.get_map(*x) for x in args.extract]
    if not chosen: return 0
    manifest=FireRedNormalizedExtractor(scanner,args.out).extract(chosen)
    print(f"Exported {len(manifest['maps'])} map(s) to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
