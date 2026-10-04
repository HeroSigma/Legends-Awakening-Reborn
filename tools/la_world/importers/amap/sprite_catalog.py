from __future__ import annotations

import json
import math
import struct
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

ROM_BASE = 0x08000000
PROJECT_OAM_DIMS = {(8, 8), (16, 8), (16, 16), (32, 8), (32, 16), (16, 32), (32, 32), (64, 32), (64, 64)}
PROJECT_SUBSPRITE_DIMS = {(16, 16), (16, 32), (32, 32), (64, 32), (64, 64)}


def u16(data: bytes, off: int) -> int:
    return struct.unpack_from('<H', data, off)[0]


def u32(data: bytes, off: int) -> int:
    return struct.unpack_from('<I', data, off)[0]


def gba_to_offset(ptr: int, rom_size: int) -> Optional[int]:
    if ROM_BASE <= ptr < ROM_BASE + rom_size:
        return ptr - ROM_BASE
    return None


def ptr_hex(off: Optional[int]) -> Optional[str]:
    return None if off is None else f'0x{ROM_BASE + off:08X}'


@dataclass
class ObjectGraphicsInfo:
    graphics_id: int
    table_entry_offset: int
    info_offset: int
    tile_tag: int
    palette_tag: int
    reflection_palette_tag: int
    frame_size: int
    width: int
    height: int
    packed_flags: int
    tracks: int
    oam_offset: Optional[int]
    subsprite_tables_offset: Optional[int]
    anims_offset: Optional[int]
    images_offset: Optional[int]
    affine_anims_offset: Optional[int]

    @property
    def extractable(self) -> bool:
        return self.images_offset is not None and self.frame_size > 0 and self.width > 0 and self.height > 0


class ObjectSpriteCatalog:
    """Discover and export Gen III ObjectEvent overworld graphics directly from a ROM.

    This intentionally does not execute event scripts. Dynamic graphics IDs therefore
    remain unresolved and are reported as such.
    """

    def __init__(self, rom: bytes, out_dir: Path):
        self.data = rom
        self.size = len(rom)
        self.out = Path(out_dir)
        self.pointer_table_offset: Optional[int] = None
        self.static_count: int = 0
        self.palette_table_offset: Optional[int] = None
        self.infos: Dict[int, ObjectGraphicsInfo] = {}
        self.palette_by_tag: Dict[int, int] = {}
        self.assets: Dict[str, dict] = {}
        self.warnings: List[str] = []

    @staticmethod
    def bgr555_to_rgb(word: int) -> Tuple[int, int, int]:
        r5 = word & 0x1F
        g5 = (word >> 5) & 0x1F
        b5 = (word >> 10) & 0x1F
        return ((r5 << 3) | (r5 >> 2), (g5 << 3) | (g5 >> 2), (b5 << 3) | (b5 >> 2))

    def _read_palette(self, off: int) -> List[Tuple[int, int, int]]:
        if off < 0 or off + 32 > self.size:
            raise ValueError('palette outside ROM')
        return [self.bgr555_to_rgb(u16(self.data, off + i * 2)) for i in range(16)]

    def _write_jasc(self, path: Path, colors: Sequence[Tuple[int, int, int]]) -> None:
        lines = ['JASC-PAL', '0100', str(len(colors))]
        lines.extend(f'{r} {g} {b}' for r, g, b in colors)
        path.write_text('\n'.join(lines) + '\n', encoding='ascii')

    def _parse_info_at(self, off: int, graphics_id: int = -1, table_entry_offset: int = -1) -> Optional[ObjectGraphicsInfo]:
        if off < 0 or off + 0x24 > self.size:
            return None
        tile_tag = u16(self.data, off)
        palette_tag = u16(self.data, off + 2)
        reflection_palette_tag = u16(self.data, off + 4)
        frame_size = u16(self.data, off + 6)
        width, height = struct.unpack_from('<hh', self.data, off + 8)
        packed_flags = self.data[off + 12]
        tracks = self.data[off + 13]
        if frame_size <= 0 or frame_size > 0x4000:
            return None
        if width <= 0 or height <= 0 or width > 128 or height > 128 or width % 8 or height % 8:
            return None
        # For normal 4bpp object sprites each frame is width*height/2 bytes.
        # Permit deviations for special objects but reject obviously unrelated data.
        expected = width * height // 2
        if not (frame_size == expected or (32 <= frame_size <= expected * 4)):
            return None

        ptr_fields = [u32(self.data, off + p) for p in (0x10, 0x14, 0x18, 0x1C, 0x20)]
        ptr_offsets = [gba_to_offset(p, self.size) for p in ptr_fields]
        images_off = ptr_offsets[3]
        if images_off is None or images_off + 8 > self.size:
            return None
        first_frame_ptr = u32(self.data, images_off)
        first_frame_off = gba_to_offset(first_frame_ptr, self.size)
        first_frame_size = u16(self.data, images_off + 4)
        if first_frame_off is None or first_frame_size <= 0 or first_frame_size > 0x4000:
            return None

        return ObjectGraphicsInfo(
            graphics_id=graphics_id,
            table_entry_offset=table_entry_offset,
            info_offset=off,
            tile_tag=tile_tag,
            palette_tag=palette_tag,
            reflection_palette_tag=reflection_palette_tag,
            frame_size=frame_size,
            width=width,
            height=height,
            packed_flags=packed_flags,
            tracks=tracks,
            oam_offset=ptr_offsets[0],
            subsprite_tables_offset=ptr_offsets[1],
            anims_offset=ptr_offsets[2],
            images_offset=images_off,
            affine_anims_offset=ptr_offsets[4],
        )

    def _discover_pointer_table(self) -> None:
        # Find every aligned pointer whose target looks like ObjectEventGraphicsInfo,
        # then choose the densest 0x800-byte cluster. This is resilient to relocated
        # and extended tables while avoiding a vanilla hardcoded address.
        sources: List[int] = []
        for src in range(0, self.size - 3, 4):
            target = gba_to_offset(u32(self.data, src), self.size)
            if target is not None and self._parse_info_at(target) is not None:
                sources.append(src)
        if not sources:
            raise RuntimeError('Could not discover ObjectEventGraphicsInfo pointer table')

        sources.sort()
        best_lo = best_hi = 0
        left = 0
        window = 0x800
        for right, value in enumerate(sources):
            while value - sources[left] > window:
                left += 1
            if right - left > best_hi - best_lo:
                best_lo, best_hi = left, right
        cluster = sources[best_lo:best_hi + 1]
        if len(cluster) < 32:
            raise RuntimeError('Object graphics pointer candidates were too sparse')
        base = min(cluster)
        self.pointer_table_offset = base

        # Continue through occasional special/nonstandard entries. Once we hit a
        # solid run of unrelated words, the static table has ended and dynamic IDs
        # begin (or another data object follows it).
        last_good = -1
        bad_run = 0
        for gid in range(0, 1024):
            pos = base + gid * 4
            if pos + 4 > self.size:
                break
            target = gba_to_offset(u32(self.data, pos), self.size)
            info = self._parse_info_at(target, gid, pos) if target is not None else None
            if info is not None:
                self.infos[gid] = info
                last_good = gid
                bad_run = 0
            else:
                bad_run += 1
                if gid >= 64 and bad_run >= 8:
                    break
        if last_good < 31:
            raise RuntimeError('Discovered object graphics table was implausibly small')
        self.static_count = last_good + 1

    def _discover_palette_table(self) -> None:
        tags = {info.palette_tag for info in self.infos.values()}
        if not tags:
            return
        best_start = None
        best_entries: Dict[int, int] = {}
        best_score = -1

        # SpritePalette is { pointer, u16 tag, padding }. Search for a table that
        # covers the largest number of palette tags referenced by graphics infos.
        for start in range(0, self.size - 8, 4):
            tag0 = u16(self.data, start + 4)
            pad0 = u16(self.data, start + 6)
            if pad0 != 0 or tag0 not in tags:
                continue
            entries: Dict[int, int] = {}
            for i in range(96):
                off = start + i * 8
                if off + 8 > self.size:
                    break
                ptr = u32(self.data, off)
                tag = u16(self.data, off + 4)
                pad = u16(self.data, off + 6)
                if pad != 0 or not (0x1000 <= tag <= 0x2FFF):
                    break
                pal_off = gba_to_offset(ptr, self.size)
                if pal_off is not None and pal_off + 32 <= self.size:
                    entries[tag] = pal_off
                elif ptr not in (0, 0x08FFFFFF, 0xFFFFFFFF):
                    # Still permit placeholder records, but stop on random data.
                    break
            score = len(tags.intersection(entries.keys()))
            if score > best_score:
                best_score = score
                best_start = start
                best_entries = entries

        if best_start is not None and best_score >= max(4, min(8, len(tags) // 2)):
            self.palette_table_offset = best_start
            self.palette_by_tag = best_entries
        else:
            self.warnings.append('Could not confidently discover object-event palette table; sprite PNGs will use a diagnostic grayscale palette.')

    def discover(self) -> None:
        self._discover_pointer_table()
        self._discover_palette_table()

    def _image_table_counts(self) -> Dict[int, int]:
        image_offsets = sorted({i.images_offset for i in self.infos.values() if i.images_offset is not None})
        counts: Dict[int, int] = {}
        for idx, off in enumerate(image_offsets):
            nxt = image_offsets[idx + 1] if idx + 1 < len(image_offsets) else None
            if nxt is not None and nxt > off and (nxt - off) % 8 == 0:
                count = (nxt - off) // 8
                if 1 <= count <= 64:
                    counts[off] = count
                    continue
            counts[off] = 1
        return counts

    def _decode_frame(self, raw: bytes, width: int, height: int, colors: Sequence[Tuple[int, int, int]]):
        from PIL import Image
        needed = width * height // 2
        raw = raw[:needed].ljust(needed, b'\0')
        img = Image.new('P', (width, height), 0)
        palette = []
        for r, g, b in colors[:16]:
            palette.extend((r, g, b))
        palette.extend([0, 0, 0] * (256 - len(colors[:16])))
        img.putpalette(palette)
        img.info['transparency'] = 0
        px = img.load()
        tiles_x = width // 8
        tiles_y = height // 8
        pos = 0
        for ty in range(tiles_y):
            for tx in range(tiles_x):
                tile = raw[pos:pos + 32]
                pos += 32
                for y in range(8):
                    for pair in range(4):
                        byte = tile[y * 4 + pair]
                        px[tx * 8 + pair * 2, ty * 8 + y] = byte & 0xF
                        px[tx * 8 + pair * 2 + 1, ty * 8 + y] = (byte >> 4) & 0xF
        return img

    def _fallback_palette(self) -> List[Tuple[int, int, int]]:
        return [(0, 0, 0)] + [(i * 17, i * 17, i * 17) for i in range(1, 16)]

    def _extract_one(self, gid: int, frame_counts: Dict[int, int]) -> dict:
        key = f'gfx_{gid:03d}'
        if gid >= self.static_count:
            meta = {
                'id': gid,
                'key': key,
                'status': 'dynamic_unresolved',
                'reason': 'graphics id is outside the discovered static object graphics table; resolving it requires runtime VAR_OBJ_GFX_ID_* state/scripts',
            }
            self.assets[key] = meta
            return meta

        info = self.infos.get(gid)
        if info is None or not info.extractable:
            meta = {'id': gid, 'key': key, 'status': 'special_unresolved', 'reason': 'graphics info uses a special/nonstandard image path'}
            self.assets[key] = meta
            return meta

        folder = self.out / 'sprites' / key
        frames_dir = folder / 'frames'
        frames_dir.mkdir(parents=True, exist_ok=True)

        palette_off = self.palette_by_tag.get(info.palette_tag)
        if palette_off is not None:
            colors = self._read_palette(palette_off)
            self._write_jasc(folder / 'palette.pal', colors)
            (folder / 'palette.gbapal').write_bytes(self.data[palette_off:palette_off + 32])
            palette_status = 'rom'
        else:
            colors = self._fallback_palette()
            self._write_jasc(folder / 'palette.pal', colors)
            palette_status = 'fallback_grayscale'

        count = frame_counts.get(int(info.images_offset), 1)
        frame_paths: List[str] = []
        frame_images = []
        raw_frames = bytearray()
        frame_sizes: List[int] = []
        frame_offsets: List[int] = []
        for index in range(count):
            entry = int(info.images_offset) + index * 8
            if entry + 8 > self.size:
                break
            data_ptr = u32(self.data, entry)
            data_off = gba_to_offset(data_ptr, self.size)
            data_size = u16(self.data, entry + 4)
            if data_off is None or data_size <= 0 or data_size > 0x4000 or data_off + data_size > self.size:
                break
            # FrameImage size is authoritative. Decode only enough pixels for the
            # declared width/height while preserving the original raw bytes.
            raw = self.data[data_off:data_off + data_size]
            frame_offsets.append(len(raw_frames))
            frame_sizes.append(data_size)
            raw_frames.extend(raw)
            img = self._decode_frame(raw, info.width, info.height, colors)
            rel = Path('sprites') / key / 'frames' / f'frame_{index:02d}.png'
            img.save(self.out / rel, transparency=0)
            frame_paths.append(str(rel).replace('\\', '/'))
            frame_images.append(img.convert('RGBA'))

        (folder / 'frames.4bpp').write_bytes(bytes(raw_frames))

        if frame_images:
            from PIL import Image
            cols = min(6, len(frame_images))
            rows = math.ceil(len(frame_images) / cols)
            sheet = Image.new('RGBA', (cols * info.width, rows * info.height), (0, 0, 0, 0))
            for idx, frame in enumerate(frame_images):
                sheet.alpha_composite(frame, ((idx % cols) * info.width, (idx // cols) * info.height))
            sheet.save(folder / 'sheet.png')
            frame_images[0].save(folder / 'preview.png')

        expected_frame_size = info.width * info.height // 2
        palette_slot = info.packed_flags & 0x0F
        shadow_size = (info.packed_flags >> 4) & 0x03
        inanimate = bool(info.packed_flags & 0x40)
        source_flag7 = bool(info.packed_flags & 0x80)
        standard_frames = bool(frame_paths) and all(size == expected_frame_size for size in frame_sizes)
        project_import_safe = (
            palette_off is not None
            and len(frame_paths) >= (1 if inanimate else 9)
            and standard_frames
            and (info.width, info.height) in PROJECT_OAM_DIMS
        )
        oam_symbol = f'gObjectEventBaseOam_{info.width}x{info.height}' if (info.width, info.height) in PROJECT_OAM_DIMS else None
        subsprite_symbol = f'sOamTables_{info.width}x{info.height}' if (info.width, info.height) in PROJECT_SUBSPRITE_DIMS else None

        meta = {
            'id': gid,
            'key': key,
            'status': 'extracted' if frame_paths else 'unresolved',
            'graphics_pointer_table_entry': ptr_hex(info.table_entry_offset),
            'graphics_info_pointer': ptr_hex(info.info_offset),
            'tile_tag': info.tile_tag,
            'palette_tag': info.palette_tag,
            'reflection_palette_tag': info.reflection_palette_tag,
            'palette_pointer': ptr_hex(palette_off),
            'palette_status': palette_status,
            'palette_raw': f'sprites/{key}/palette.gbapal' if palette_off is not None else None,
            'width': info.width,
            'height': info.height,
            'frame_size': info.frame_size,
            'frame_count': len(frame_paths),
            'frame_sizes': frame_sizes,
            'frame_offsets': frame_offsets,
            'expected_frame_size': expected_frame_size,
            'standard_frame_stride': standard_frames,
            'project_import_safe': project_import_safe,
            'project_oam_symbol': oam_symbol,
            'project_subsprite_symbol': subsprite_symbol,
            'palette_slot': palette_slot,
            'shadow_size': shadow_size,
            'inanimate': inanimate,
            'source_flag7': source_flag7,
            'frames': frame_paths,
            'preview': f'sprites/{key}/preview.png' if frame_paths else None,
            'sheet': f'sprites/{key}/sheet.png' if frame_paths else None,
            'images_table_pointer': ptr_hex(info.images_offset),
            'oam_pointer': ptr_hex(info.oam_offset),
            'subsprite_tables_pointer': ptr_hex(info.subsprite_tables_offset),
            'anims_pointer': ptr_hex(info.anims_offset),
            'affine_anims_pointer': ptr_hex(info.affine_anims_offset),
            'packed_flags': info.packed_flags,
            'tracks': info.tracks,
        }
        (folder / 'sprite.json').write_text(json.dumps(meta, indent=2), encoding='utf-8')
        self.assets[key] = meta
        return meta

    def extract(self, graphics_ids: Iterable[int]) -> Dict[str, dict]:
        self.out.mkdir(parents=True, exist_ok=True)
        self.discover()
        frame_counts = self._image_table_counts()
        ids = sorted({int(i) for i in graphics_ids if 0 <= int(i) <= 0xFFFF})
        for gid in ids:
            self._extract_one(gid, frame_counts)

        dynamic = [m['id'] for m in self.assets.values() if m.get('status') == 'dynamic_unresolved']
        if dynamic:
            self.warnings.append(
                'Dynamic object graphics IDs could not be resolved without executing scripts/runtime variables: '
                + ', '.join(str(i) for i in dynamic)
            )
        manifest = {
            'format': 'A-Map Object Sprite Catalog v0.1',
            'graphics_pointer_table': ptr_hex(self.pointer_table_offset),
            'static_graphics_count': self.static_count,
            'palette_table': ptr_hex(self.palette_table_offset),
            'requested_graphics_ids': ids,
            'extracted_count': sum(1 for x in self.assets.values() if x.get('status') == 'extracted'),
            'unresolved_count': sum(1 for x in self.assets.values() if x.get('status') != 'extracted'),
            'assets': self.assets,
            'warnings': self.warnings,
        }
        sprites_dir = self.out / 'sprites'
        sprites_dir.mkdir(exist_ok=True)
        (sprites_dir / 'manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
        return self.assets
