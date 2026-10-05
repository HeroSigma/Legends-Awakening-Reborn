#!/usr/bin/env python3
"""Keep additive Sinnoh map identities within Emerald's signed WarpData range."""
import copy
import hoenn_finalization as F
R=F.R;O=R/'.la_work/amap/hyper_sinnoh_id_correction'
FAMILIES={
 'Solaceon_Town':'Solaceon_Ruins','Veilstone_City':'Lost_Tower','Celestic_Town':'Route_210','Snowpoint_City':'Crown_Shrine','Sunyshore_City':'Sinnoh_League','Pastoria_City':'Desert_Ruins',
 'Route_201':'Twinleaf_Town','Verity_Lakefront':'Twinleaf_Town','Lake_Verity':'Twinleaf_Town',
 'Route_202':'Sandgem_Town','Route_219':'Sandgem_Town','Route_220':'Sandgem_Town','Route_221':'Sandgem_Town','Pal_Park':'Sandgem_Town',
 'Route_203':'Oreburgh_City','Route_207':'Oreburgh_City','Oreburgh_Gate':'Oreburgh_City','Oreburgh_Mine':'Oreburgh_City',
 'Route_204':'Jubilife_City','Ravaged_Path':'Jubilife_City','Route_218':'Canalave_City','Iron_Island':'Canalave_City',
 'Route_205':'Floaroma_Town','Valley_Windworks':'Floaroma_Town','Fuego_Ironworks':'Floaroma_Town',
 'Route_206':'Eterna_City','Eterna_Forest':'Eterna_City','Old_Chateau':'Eterna_City',
 'Route_208':'Hearthome_City','Route_209':'Lost_Tower','Route_211':'Route_210','Route_212':'Hearthome_City','Route_213':'Desert_Ruins','Route_214':'Lost_Tower','Route_215':'Lost_Tower',
 'Route_216':'Crown_Shrine','Route_217':'Crown_Shrine','Lake_Acuity':'Crown_Shrine','Acuity_Lakefront':'Crown_Shrine','Regigigas_Temple':'Crown_Shrine',
 'Route_222':'Sinnoh_League','Route_223':'Sinnoh_League','Victory_Road':'Sinnoh_League',
 'Lake_Valor':'Desert_Ruins','Valor_Lakefront':'Desert_Ruins','Great_Marsh':'Desert_Ruins',
 'Sendoff_Spring':'Spear_Pillar','Spring_Path':'Spear_Pillar','Mt_Coronet':'Spear_Pillar','Amity_Square':'Hearthome_City','Sinnoh_Region':'Jubilife_City'
}
def regroup(groups):
 result=copy.deepcopy(groups);order=groups['group_order'];assert len(order)>=127
 kept=order[:127];assert all(g.startswith('gMapGroup_HyperSinnoh_') for g in order[112:])
 for g in order[127:]:
  family=g.removeprefix('gMapGroup_HyperSinnoh_');assert family in FAMILIES,family
  target='gMapGroup_HyperSinnoh_'+FAMILIES[family];assert target in kept
  result[target]+=result.pop(g)
 result['group_order']=kept
 assert all(len(result[g])<=127 for g in kept),'Signed map-number range'
 return result

def apply():
 assert not (O/'receipt.json').exists(),'Already applied'
 rec=F.load(R/'.la_work/amap/hyper_sinnoh_asset_travel/receipt.json');expected={f:rec['changed_baseline_files'].get(f,{}).get('after',h) for f,h in rec['baseline'].items()};user={}
 for f,h in expected.items():
  actual=F.digest(R/f) if (R/f).exists() else None
  if actual!=h:user[f]={'before':h,'after':actual,'ownership':'Pre-existing user edit; not modified by correction'}
 assert set(user)<={'data/layouts/SootopolisCity_MysteryEventsHouse_1F/map.bin','data/maps/SootopolisCity_MysteryEventsHouse_1F/map.json','src/zz_slot_size_probe.c','src/data/region_map/region_map_sections.json'},user
 f='data/maps/map_groups.json';old=F.load(R/f);new=regroup(old);O.mkdir(parents=True);F.dump(O/'original_map_groups.json',old)
 # Existing 0..126 group and map identities remain exact, including the Oreburgh save.
 for g in old['group_order'][:127]:assert new[g][:len(old[g])]==old[g]
 F.dump(R/f,new)
 beforeids={n:[gi,mi] for gi,g in enumerate(old['group_order']) for mi,n in enumerate(old[g])};afterids={n:[gi,mi] for gi,g in enumerate(new['group_order']) for mi,n in enumerate(new[g])}
 F.dump(O/'receipt.json',{'schema':'hyper-sinnoh-signed-id-correction-v1','user_edits':user,'changed_files':{f:{'before':expected[f],'after':F.digest(R/f)}},'before_ids':beforeids,'after_ids':afterids,'renumbered_new_maps':{n:{'before':v,'after':afterids[n]} for n,v in beforeids.items() if v!=afterids[n]},'save_abi_changed':False,'runtime_verified':False})
 print('Consolidated178groups to127; preserved all pre-existing maps and Oreburgh IDs.')
if __name__=='__main__':apply()
