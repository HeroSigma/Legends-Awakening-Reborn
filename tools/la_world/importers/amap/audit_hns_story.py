"""Read-only donor story dependency audit; never enables donor scripts."""
from pathlib import Path
import re,json,collections
R=Path(__file__).resolve().parents[4];S=Path('/home/allan/la-scratch/pokehns-canary-source');D=R/'docs/la_world/hns_story'
def main():
 mf=json.loads((R/'docs/la_world/hns_regions/manifest.json').read_text())
 scripts={};duplicates=[]
 for folder in [S/'data/maps',S/'data/scripts']:
  for p in sorted(folder.rglob('*.inc')):
   text=p.read_text(errors='replace');matches=list(re.finditer(r'(?m)^([A-Za-z_]\w*)::?\s*(?:@.*)?$',text))
   for i,m in enumerate(matches):
    body=text[m.end():matches[i+1].start() if i+1<len(matches) else len(text)]
    if m[1] in scripts and scripts[m[1]][1]!=body:duplicates.append(m[1])
    scripts[m[1]]=(str(p.relative_to(S)),body)
 roots=set();missing_map_scripts=[]
 for row in mf['maps']:
  if row['reference_only']:continue
  p=S/'data/maps'/row['source']/'scripts.inc'
  if p.exists():roots.update(re.findall(r'(?m)^(\w+)::?',p.read_text()))
  else:missing_map_scripts.append(row['source'])
 seen=set();queue=list(roots);commands=collections.Counter();specials=set();native=set();flags=set();variables=set();trainers=set();mapids=set();items=set()
 while queue:
  label=queue.pop()
  if label in seen:continue
  seen.add(label)
  if label not in scripts:continue
  path,body=scripts[label]
  for line in body.splitlines():
   line=line.strip().split('@',1)[0].strip()
   if not line or line[0] in '.#':continue
   op=line.split()[0];commands[op]+=1
   if op in ['special','specialvar']:
    rest=line.split(maxsplit=1)[1]
    specials.add(rest.split(',')[-1].strip().split()[0])
   if op=='callnative':native.add(line.split()[1].rstrip(','))
  for token in re.findall(r'\b[A-Za-z_]\w*\b',body):
   if token in scripts and token not in seen:queue.append(token)
   for prefix,dest in [('FLAG_',flags),('VAR_',variables),('TRAINER_',trainers),('MAP_',mapids),('ITEM_',items)]:
    if token.startswith(prefix):dest.add(token)
 native_src=''.join(p.read_text(errors='replace') for p in (R/'src').glob('*.c'))
 nflags=(R/'include/constants/flags.h').read_text();nvars=(R/'include/constants/vars.h').read_text()
 sf=(S/'include/constants/flags.h').read_text();sv=(S/'include/constants/vars.h').read_text()
 def defs(t):return {m[1]:m[2].split('//')[0].strip() for m in re.finditer(r'(?m)^#define\s+(\w+)\s+([^\n]+)',t)}
 nf,nv,df,dv=map(defs,[nflags,nvars,sf,sv])
 conflicts=[]
 for kind,used,donor,native_defs in [('flag',flags,df,nf),('variable',variables,dv,nv)]:
  for name in sorted(used):
   if name in donor and name in native_defs and donor[name]!=native_defs[name]:conflicts.append(dict(kind=kind,name=name,donor=donor[name],native=native_defs[name]))
 unknownspecials=[x for x in specials if not re.search(r'\b'+re.escape(x)+r'\s*\(',native_src)]
 unknownnative=[x for x in native if not re.search(r'\b'+re.escape(x)+r'\s*\(',native_src)]
 report=dict(source_commit=mf['source_commit'],active_maps=495,root_labels=len(roots),reachable_labels=len(seen),missing_map_scripts=missing_map_scripts,duplicate_labels=sorted(set(duplicates)),flags=sorted(flags),variables=sorted(variables),trainers=sorted(trainers),map_references=sorted(mapids),items=sorted(items),script_commands=dict(commands),special_functions=sorted(specials),native_callbacks=sorted(native),missing_special_implementations=sorted(unknownspecials),missing_native_implementations=sorted(unknownnative),differently_defined_shared_constants=conflicts,donor_only_flags=sorted(flags-nf.keys()),donor_only_variables=sorted(variables-nv.keys()),reachable_script_files=sorted({scripts[x][0] for x in seen if x in scripts}))
 D.mkdir(exist_ok=True);(D/'dependency_audit.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({k:len(v) if isinstance(v,(list,dict)) else v for k,v in report.items()},indent=2))
 print('MISSING_SPECIALS',unknownspecials[:50]);print('MISSING_NATIVE',unknownnative[:40])
if __name__=='__main__':main()
