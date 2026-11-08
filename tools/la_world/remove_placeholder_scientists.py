"""Remove message-only construction NPCs and the explicit Littleroot debug warp NPC.
Default is an inventory. --apply edits only object lists, with local backups.
--stage stages only these deletions against HEAD, preserving unrelated user map edits.
"""
from pathlib import Path
import json,re,subprocess,sys,datetime,hashlib
R=Path(__file__).resolve().parents[2]
def labels():
 result={}
 for p in (R/'data/maps').glob('*/scripts.inc'):
  for m in re.finditer(r'^(\w+)::?\n(.*?)(?=^\w+::?\n|\Z)',p.read_text(),re.M|re.S):result[m[1]]=m[2]
 return result
def removable(o,blocks):
 if 'SCIENTIST' not in o.get('graphics_id',''):return False
 script=o.get('script','')
 if script=='LA_TeleportScientist':return True
 if 'Construction' not in script or script not in blocks:return False
 commands=[line.strip().split()[0] for line in blocks[script].splitlines() if line.strip() and not line.lstrip().startswith('@')]
 return bool(commands) and set(commands)<={'lock','faceplayer','msgbox','release','end'}
def cleaned(m,blocks):
 keep=[o for o in m.get('object_events',[]) if not removable(o,blocks)]
 removed=[o for o in m.get('object_events',[]) if removable(o,blocks)]
 return dict(m,object_events=keep),removed
def main():
 blocks=labels();apply='--apply' in sys.argv;stage='--stage' in sys.argv
 assert not stage or apply
 report=[];backup=R/'.la_work/scientist-cleanup'/datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
 if apply:backup.mkdir(parents=True,exist_ok=True)
 for p in sorted((R/'data/maps').glob('*/map.json')):
  raw=p.read_bytes();m=json.loads(raw);new,removed=cleaned(m,blocks)
  relative=str(p.relative_to(R))
  head_raw=subprocess.check_output(['git','show','HEAD:'+relative],cwd=R) if stage else raw
  head=json.loads(head_raw);staged,committed=cleaned(head,blocks)
  if not removed and not committed:continue
  row=dict(map=p.parent.name,removed_live=removed,removed_commit=committed,unrelated_fields_preserved=True)
  report.append(row)
  if apply and removed:
   target=backup/relative;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(raw)
   p.write_text(json.dumps(new,indent=2)+'\n')
   actual=json.loads(p.read_text())
   assert {k:v for k,v in actual.items() if k!='object_events'}=={k:v for k,v in m.items() if k!='object_events'}
   assert actual['object_events']==[o for o in m['object_events'] if not removable(o,blocks)]
  if stage and committed:
   # Stage a HEAD-derived object deletion only; user layout/warp/NPC edits stay unstaged.
   content=(json.dumps(staged,indent=2)+'\n').encode()
   blob=subprocess.check_output(['git','hash-object','-w','--stdin'],input=content,cwd=R,text=False).decode().strip()
   subprocess.run(['git','update-index','--cacheinfo','100644',blob,relative],cwd=R,check=True)
 result=dict(maps=len(report),removed_live=sum(len(x['removed_live']) for x in report),removed_commit=sum(len(x['removed_commit']) for x in report),applied=apply,staged=stage,entries=report)
 if apply:
  out=R/'docs/la_world/scientist_cleanup';out.mkdir(parents=True,exist_ok=True)
  (out/'removals.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({k:v for k,v in result.items() if k!='entries'},indent=2))
if __name__=='__main__':main()
