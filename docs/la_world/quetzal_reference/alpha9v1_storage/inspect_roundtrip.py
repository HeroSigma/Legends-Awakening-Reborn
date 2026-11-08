"""Compare known Gen-III field accessors across Quetzal's own box codec.
Only an isolated native core and synthetic RAM are touched.
"""
from pathlib import Path
import sys,json
R=Path('/home/allan/projects/Legends-Awakening-Reborn');sys.path.insert(0,str(R/'tools/la_world/importers/amap/hns_runtime'))
helper=R/'tools/la_world/importers/amap/hns_runtime/test_protagonist_assets.py'
exec(compile(helper.read_text().split("D=R/'docs/art/protagonists/trainer_draft'")[0].replace('BASE=0x0203f000','BASE=0x03007000'),'native_helpers','exec'))
symbols={'gMain':0x03002660,'CreateBoxMon':0x809c1f8,'GetBoxMonData':0x809ebd8,'SetBoxMonData':0x809f340,'Encode':0x8138394,'Decode':0x81381b8}
assert lib.boot(b'/mnt/c/Users/aadair/Downloads/Quetzal English Alpha 9v1.gba');frames(600)
SB2,SRC,DST,DATA,STRBUF,POOL=0x02030000,0x02010000,0x02010400,0x02010800,0x02010900,0x02018000
for start,size in [(SB2,0x400),(SRC,0x1000),(POOL,0x1000)]:
 for i in range(size):wr(start+i,0,1)
wr(0x030055c0,SB2);wr(0x030055bc,0x02000000)
for addr in [0x030055c4,0x030055c8,0x030055cc,0x030055d0]:wr(addr,POOL)
for i,c in enumerate([0xbb,0xcc,0xbf,0xc8,0xff]):wr(SB2+i,c,1)
wr(SB2+0xa,0x12345678)
invoke('CreateBoxMon',SRC,1,50,31,0,0)
fields={'personality':0,'ot_id':1,'language':3,'markings':8,'species':11,'held_item':12,'move1':13,'move2':14,'move3':15,'move4':16,'pp1':17,'pp2':18,'pp3':19,'pp4':20,'pp_bonuses':21,'cool':22,'beauty':23,'cute':24,'experience':25,'hp_ev':26,'attack_ev':27,'defense_ev':28,'speed_ev':29,'spattack_ev':30,'spdefense_ev':31,'friendship':32,'smart':33,'pokerus':34,'met_location':35,'met_level':36,'met_game':37,'pokeball':38,'hp_iv':39,'attack_iv':40,'defense_iv':41,'speed_iv':42,'spattack_iv':43,'spdefense_iv':44,'is_egg':45,'ability_num':46,'tough':47,'sheen':48,'ot_gender':49,'champion_ribbon':67,'effort_ribbon':71}
values={'held_item':1,'move1':33,'move2':45,'move3':73,'move4':22,'pp1':10,'pp2':11,'pp3':12,'pp4':13,'pp_bonuses':0x55,'hp_ev':252,'attack_ev':4,'defense_ev':0,'speed_ev':0,'spattack_ev':0,'spdefense_ev':252,'friendship':201,'cool':123,'beauty':124,'cute':125,'smart':126,'tough':127,'sheen':128,'pokerus':0x34,'met_location':11,'met_level':7,'pokeball':3,'hp_iv':1,'attack_iv':2,'defense_iv':3,'speed_iv':4,'spattack_iv':5,'spdefense_iv':6}
for name,value in values.items():wr(DATA,value);invoke('SetBoxMonData',SRC,fields[name],DATA)
def get(ptr):return {name:invoke('GetBoxMonData',ptr,field,STRBUF) for name,field in fields.items()}
before=get(SRC);original=bytes(rd(SRC+i,1) for i in range(88));results=[]
for mode in [0,1]:
 for meta in [0,1]:
  for i,c in enumerate(original):wr(SRC+i,c,1)
  wr(SB2+0x2bb,mode,1);wr(SB2+0x2c6,meta,1)
  invoke('Encode',SRC,0,0);invoke('Decode',DST,0,0);after=get(DST)
  results.append(dict(mode=mode,metadata_byte=meta,before=before,after=after,changed={k:dict(before=before[k],after=after[k]) for k in before if before[k]!=after[k]}))
lib.shutdown();out=R/'docs/la_world/quetzal_reference/alpha9v1_storage/roundtrip_results.json';out.write_text(json.dumps(dict(known_accessor_assumptions='Vanilla Gen III field IDs; results require value sanity checks before adoption.',user_save_loaded=False,results=results),indent=2)+'\n');print(json.dumps([dict(mode=x['mode'],metadata_byte=x['metadata_byte'],before_sanity={k:before[k] for k in ['species','hp_ev','spdefense_ev','hp_iv','move1']},changed=x['changed']) for x in results],indent=2))
