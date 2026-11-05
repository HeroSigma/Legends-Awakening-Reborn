"""Read-only donor trainer-portrait archive and local searchable gallery."""
from pathlib import Path
from PIL import Image
import struct,re,json,hashlib,shutil,html
R=Path(__file__).resolve().parents[4];D=R/'docs/art/donor-portraits';D.mkdir(parents=True,exist_ok=True)
rows=[];coverage=[]
def lz(b,o):
 if o<0 or o+4>len(b) or b[o]!=16:raise ValueError('header')
 n=int.from_bytes(b[o+1:o+4],'little')
 if n not in [32,2048,4096,8192]:raise ValueError('size')
 z=bytearray();o+=4
 while len(z)<n:
  f=b[o];o+=1
  for bit in range(7,-1,-1):
   if len(z)>=n:break
   if f>>bit&1:
    a,c=b[o:o+2];o+=2;distance=((a&15)<<8|c)+1
    if distance>len(z):raise ValueError('distance')
    for _ in range((a>>4)+3):z.append(z[-distance])
   else:z.append(b[o]);o+=1
 return bytes(z[:n])
def ptr(b,o):return struct.unpack_from('<I',b,o)[0]-0x8000000
def sequence(b,o,palette=False):
 n=0
 for i in range(600):
  try:
   p=ptr(b,o+i*8);size,tag=struct.unpack_from('<HH',b,o+i*8+4)
   if not 0<=p<len(b)-4 or (size!=i if palette else tag!=i or size not in [2048,4096,8192]):break
   if b[p]!=16 or int.from_bytes(b[p+1:p+4],'little') not in ([32] if palette else [2048,4096,8192]):break
   n+=1
  except:break
 return n
def discover(b):
 pics=[];pals=[]
 for m in re.finditer(b'\x00\x08\x00\x00',b):
  o=m.start()-4
  if o<0 or o%4:continue
  n=sequence(b,o)
  if 50<=n<=350:pics.append((o,n))
 for m in re.finditer(b'[\x08\x09]\x00\x00\x00\x00',b):
  o=m.start()-3
  if o<0 or o%4:continue
  n=sequence(b,o,True)
  if 50<=n<=350:pals.append((o,n))
 pairs=[]
 for o,n in pics:
  matches=sorted([(abs(p-o),p,m) for p,m in pals if m==n])
  if matches and matches[0][0]<0x200000:pairs.append((o,matches[0][1],n))
 return pairs
sources=[]
for donor in ['bwa','swsh','aestheticred']:
 p=R/f'.la_work/amap/{donor}_full_v11/manifest.json';m=json.loads(p.read_text());source=Path(m['rom']['path']);source=source if source.exists() else R/f'.la_work/amap/donor_preservation/{donor}/reference/donor.gba';sources.append((donor,source,None))
sources.insert(0,('hyper',Path('/mnt/c/Users/aadair/Downloads/tools/Donor Roms/HypEm v5.7 EN+QoL.gba'),[(0x101be90,0x101c660,93),(0x101c178,0x101c948,60),(0x101c358,0x101cb28,97)]))
sources.append(('mercury',Path('/home/allan/mercury-map-inspection/mercury_beta2.gba'),[(0x23957c,0x239a1c,148)]))
sources.append(('stone_dragon_3',Path('/mnt/c/Users/aadair/Downloads/tools/Donor Roms/Stone Dragon 3.gba'),None))
for donor,source,tables in sources:
 if not source.exists():coverage.append(dict(donor=donor,status='SOURCE_MISSING'));continue
 b=source.read_bytes();tables=tables or discover(b);good=0;errors=[]
 print(donor,[(hex(a),hex(p),n) for a,p,n in tables],flush=True)
 for ti,(table,pals,count) in enumerate(tables):
  for index in range(count):
   try:
    raw=lz(b,ptr(b,table+index*8));colors=lz(b,ptr(b,pals+index*8));assert len(colors)==32
    rgb=[tuple((v>>s&31)*255//31 for s in [0,5,10]) for v in struct.unpack('<16H',colors)]
    im=Image.new('P',(64,len(raw)//32));im.putpalette(sum((list(c) for c in rgb),[])+[0]*720)
    for y in range(im.height):
     for x in range(64):im.putpixel((x,y),raw[((y//8)*8+x//8)*32+(y%8)*4+x%8//2]>>(4*(x%2))&15)
    key=f'set{ti+1}_{index:03}';out=D/'images'/donor/(key+'.png');out.parent.mkdir(parents=True,exist_ok=True);im.save(out,bits=4,transparency=0)
    name=''
    if donor=='hyper' and ti==0:name={71:'Brendan',72:'May'}.get(index,'')
    if donor=='bwa' and index==99:name='Shadow Triad'
    rows.append(dict(donor=donor,key=key,name=name,image=out.relative_to(D).as_posix(),width=im.width,height=im.height,table=hex(table),palette_table=hex(pals),index=index,raw_sha256=hashlib.sha256(raw).hexdigest()))
    good+=1
   except Exception as e:errors.append(dict(table=hex(table),index=index,error=str(e)))
 coverage.append(dict(donor=donor,status='EXTRACTED' if good else 'TABLE_NOT_CONFIRMED',count=good,tables=[dict(front=hex(a),palette=hex(p),entries=n) for a,p,n in tables],sha256=hashlib.sha256(b).hexdigest(),errors=errors))
hns=Path('/home/allan/la-scratch/pokehns-canary-source/graphics/trainers/front_pics');good=0
for p in sorted(hns.glob('*.png')):
 out=D/'images/hns'/p.name;out.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,out)
 with Image.open(out) as im:
  rows.append(dict(donor='hns',key=p.stem,name=p.stem.replace('_',' ').title(),image=out.relative_to(D).as_posix(),width=im.width,height=im.height,source_sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
 good+=1
coverage.append(dict(donor='hns',status='SOURCE_ART',count=good))
coverage.append(dict(donor='gs_chronicles',status='SOURCE_MISSING',reason='Exported maps remain, but original ROM is unavailable; portraits cannot be recovered from those map exports.'))
(D/'manifest.json').write_text(json.dumps(dict(portraits=rows,coverage=coverage,graphics_only=True,linked_into_rom=False),indent=2)+'\n')
page='''<!doctype html><meta charset="utf-8"><title>Legends Awakening — Donor Portraits</title><style>
*{box-sizing:border-box}body{margin:0;background:#171d28;color:#eef4fa;font:16px system-ui}header{position:sticky;top:0;background:#202a39;padding:18px 28px;z-index:2;border-bottom:2px solid #58c4bc}h1{font-size:24px;margin:0 0 8px}p{margin:5px 0;color:#b9c8d7}input,select,button{font:inherit;background:#111925;color:#eef4fa;border:1px solid #637487;border-radius:6px;padding:9px;margin:8px 8px 0 0}#grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:14px;padding:25px}.card{background:#283245;border-radius:9px;padding:12px;text-align:center;cursor:pointer}.card:hover{outline:2px solid #58c4bc}.art{height:140px;display:flex;align-items:center;justify-content:center;background:repeating-conic-gradient(#303a49 0% 25%,#27303e 0% 50%) 50%/16px 16px;border-radius:5px}.art img{image-rendering:pixelated;width:128px;height:128px;object-fit:cover;object-position:top}small{display:block;color:#a8bed0;overflow-wrap:anywhere}strong{display:block;margin:8px 0}dialog{max-width:90vw;background:#202a39;color:white;border:1px solid #58c4bc;border-radius:10px}dialog::backdrop{background:#000b}dialog img{image-rendering:pixelated;max-height:65vh;width:256px;object-fit:contain;background:#303a49}#foot{padding:20px;text-align:center}a{color:#6edbd0}.notice{padding:0 25px}
</style><header><h1>Legends Awakening · Donor portraits</h1><p>Browse front/battle portraits. Click an image for its full sheet and source ID. Unnamed entries keep donor IDs; duplicates are retained.</p><select id="donor"><option value="">All donors</option></select><input id="search" placeholder="Character or source ID"><span id="count"></span></header><p class="notice" id="coverage"></p><main id="grid"></main><div id="foot"><button id="more">Show more</button></div><dialog id="modal"><button onclick="document.querySelector('dialog').close()">Close</button><h2 id="title"></h2><img id="large"><p id="details"></p><a id="file" target="_blank">Open full image</a></dialog><script>
const DATA=__DATA__, COVERAGE=__COVERAGE__;let shown=0,filtered=[];const $=s=>document.querySelector(s);
[...new Set(DATA.map(x=>x.donor))].forEach(d=>$('#donor').add(new Option(d,d)));
$('#coverage').textContent=COVERAGE.map(x=>x.donor+': '+(x.count??x.status)).join(' · ');
function reset(){const q=$('#search').value.toLowerCase(),d=$('#donor').value;filtered=DATA.filter(x=>(!d||x.donor===d)&&[x.donor,x.key,x.name].join(' ').toLowerCase().includes(q));shown=0;$('#grid').replaceChildren();$('#count').textContent=filtered.length+' portraits';more()}
function more(){for(const x of filtered.slice(shown,shown+80)){const c=document.createElement('article');c.className='card';const art=document.createElement('div');art.className='art';const im=document.createElement('img');im.loading='lazy';im.src=x.image;im.alt=x.name||x.key;art.append(im);const title=document.createElement('strong');title.textContent=x.name||x.key;const sub=document.createElement('small');sub.textContent=x.donor+' / '+x.key;c.append(art,title,sub);c.onclick=()=>{$('#title').textContent=x.name||x.key;$('#large').src=x.image;$('#details').textContent=x.donor+' / '+x.key+' · '+x.width+'×'+x.height+(x.table?' · table '+x.table+' · entry '+x.index:'');$('#file').href=x.image;$('#modal').showModal()};$('#grid').append(c)}shown+=80;$('#more').hidden=shown>=filtered.length}
$('#more').onclick=more;$('#search').oninput=reset;$('#donor').onchange=reset;reset();</script>'''
(D/'gallery.html').write_text(page.replace('__DATA__',json.dumps(rows)).replace('__COVERAGE__',json.dumps(coverage)))
print('TOTAL',len(rows),'portraits',flush=True)
