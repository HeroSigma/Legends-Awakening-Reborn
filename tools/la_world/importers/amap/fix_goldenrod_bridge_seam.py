"""Open the two Goldenrod road lanes at the existing reciprocal connection."""
import json, struct
from pathlib import Path
R = Path(__file__).resolve().parents[4]
def main():
 layouts = json.loads((R / 'data/layouts/layouts.json').read_text())['layouts']
 ledger = []
 for name, edge in [('GSJohto_3_5_Goldenrod_City', 'left'), ('GSJohto_3_66_Goldenrod_City', 'right')]:
  m = json.loads((R / 'data/maps' / name / 'map.json').read_text())
  l = next(x for x in layouts if x['id'] == m['layout'])
  assert any(c['direction'] == edge and c['offset'] == 0 for c in m['connections'])
  p = R / l['blockdata_filepath']; b = bytearray(p.read_bytes())
  x = 0 if edge == 'left' else l['width'] - 1
  for y in (17, 18):
   offset = (y * l['width'] + x) * 2
   old = struct.unpack_from('<H', b, offset)[0]
   new = (old & 0x3ff) | 0x3000
   struct.pack_into('<H', b, offset, new)
   ledger.append(dict(map=name, x=x, y=y, before=hex(old), after=hex(new)))
  p.write_bytes(b)
 (R / 'docs/la_world/gs_johto/goldenrod_seam_fix.json').write_text(json.dumps(ledger, indent=2) + '\n')
 print('Opened four road boundary cells; curbs, warps and connections preserved')
if __name__ == '__main__': main()
