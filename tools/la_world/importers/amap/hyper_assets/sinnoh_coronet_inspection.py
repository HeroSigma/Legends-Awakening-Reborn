#!/usr/bin/env python3
"""Project-owned inspection offers at Coronet construction gates; no donor story state."""
import hoenn_finalization as F
R=F.R;O=R/'.la_work/amap/hyper_sinnoh_id_correction'
def enable(maps,scripts):
 changes=[]
 for n,m in maps.items():
  if not n.startswith('HyperSinnoh_') or not n.endswith('_Mt_Coronet'):continue
  for e in m['object_events']:
   label=e['script']
   if not label.endswith('_EventScript_Construction'):continue
   nearby=[(abs(w['x']-e['x'])+abs(w['y']-e['y']),i,w) for i,w in enumerate(m['warp_events']) if abs(w['x']-e['x'])+abs(w['y']-e['y'])<=3]
   if not nearby:continue
   distance,i,w=min(nearby,key=lambda z:(z[0],z[1]));text=scripts[n];old='\tmsgbox '+label+'_Text, MSGBOX_DEFAULT\n';assert old in text,(n,'Already enabled')
   new='\tmsgbox '+label+'_Text, MSGBOX_YESNO\n\tgoto_if_eq VAR_RESULT, NO, '+label+'_Cancel\n\twarp '+w['dest_map']+', '+str(w['dest_warp_id'])+'\n\twaitstate\n'
   text=text.replace(old,new,1).replace(label+'_Text:\n',label+'_Cancel:\n\trelease\n\tend\n'+label+'_Text:\n',1).replace('This area is under construction.\\pPlease check back later!','This passage is under construction.\\pWould you like to inspect beyond it?');scripts[n]=text
   changes.append({'map':n,'scientist_cell':[e['x'],e['y']],'source_warp':i,'destination':w['dest_map'],'destination_warp':w['dest_warp_id'],'reason':'Offer project inspection travel through the nearest actual source door; cancel preserves position and no progression state is changed.'})
 return changes

def apply():
 fix=F.load(O/'receipt.json');assert not fix.get('inspection_gate_changes'),'Already applied'
 maps={p.parent.name:F.load(p) for p in (R/'data/maps').glob('HyperSinnoh_*/map.json')};scripts={n:(R/f'data/maps/{n}/scripts.inc').read_text() for n in maps};changes=enable(maps,scripts)
 for row in changes:
  n=row['map'];f=f'data/maps/{n}/scripts.inc';p=O/'gate_original'/f;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes((R/f).read_bytes());before=F.digest(R/f);(R/f).write_text(scripts[n]);fix['changed_files'][f]={'before':before,'after':F.digest(R/f)}
 fix['inspection_gate_changes']=changes;F.dump(O/'receipt.json',fix);print('Enabled',len(changes),'Coronet inspection offers')
if __name__=='__main__':apply()
