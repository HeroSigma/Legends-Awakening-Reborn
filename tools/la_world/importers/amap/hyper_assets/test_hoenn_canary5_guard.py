"""Host-test the actual scientist-driven connection guard, including removing blockers."""
import re,subprocess
import hoenn_canary5 as C

def verify():
 source=(C.ROOT/'src/fieldmap.c').read_text();fn=re.search(r'static bool32 HyperHoennConstructionConnectionBlocked.*?\n}\n',source,re.S)[0];assert 'if (HyperHoennConstructionConnectionBlocked(GetMapConnectionAtPos(x, y)))\n        return CONNECTION_INVALID;' in source
 prefix='''#include <assert.h>
#include <stddef.h>
#include <stdint.h>
typedef uint32_t u32;
typedef unsigned bool32;
#define TRUE 1
#define FALSE 0
#define OBJ_EVENT_GFX_SCIENTIST_1 123
#define MAP_DEWFORD_TOWN 11
#define MAP_ROUTE106 21
#define MAP_HYPERHOENN_34_68_ROUTE_106 44
#define MAP_GROUP(m) ((m)>>8)
#define MAP_NUM(m) ((m)&255)
struct ObjectEventTemplate {int graphicsId,x,y;};
struct MapEvents {u32 objectEventCount; const struct ObjectEventTemplate *objectEvents;};
struct MapHeader {struct MapEvents *events;};
struct MapConnection {int mapGroup,mapNum;};
struct SaveBlock {struct {int mapGroup,mapNum;} location;};
static struct SaveBlock save;
static struct SaveBlock *gSaveBlock1Ptr=&save;
static struct MapHeader gMapHeader;
'''
 tests='''int main(void) {
 struct ObjectEventTemplate objects[]={{OBJ_EVENT_GFX_SCIENTIST_1,0,7},{OBJ_EVENT_GFX_SCIENTIST_1,50,18}};
 struct MapEvents events={2,objects};
 struct MapConnection special={0,44},ordinary={0,11};
 gMapHeader.events=&events;
 save.location.mapNum=11;
 assert(HyperHoennConstructionConnectionBlocked(&special));
 assert(!HyperHoennConstructionConnectionBlocked(&ordinary));
 assert(!HyperHoennConstructionConnectionBlocked(NULL));
 events.objectEventCount=0;
 assert(!HyperHoennConstructionConnectionBlocked(&special));
 events.objectEventCount=2;save.location.mapNum=21;
 assert(HyperHoennConstructionConnectionBlocked(&special));
 assert(!HyperHoennConstructionConnectionBlocked(&ordinary));
 events.objectEventCount=0;
 assert(!HyperHoennConstructionConnectionBlocked(&special));
 events.objectEventCount=2;objects[1].graphicsId=0;
 assert(!HyperHoennConstructionConnectionBlocked(&special));
 save.location.mapNum=99;
 assert(!HyperHoennConstructionConnectionBlocked(&special));
 return 0;
}
'''
 p=C.OUT/'construction_guard_host_test.c';p.write_text(prefix+fn+tests);exe=p.with_suffix('');subprocess.run(['gcc','-std=c17','-O1','-g','-fsanitize=address,undefined',str(p),'-o',str(exe)],check=True,capture_output=True);subprocess.run([str(exe)],check=True,capture_output=True)
 result={'passed':True,'actual_runtime_function_tested':True,'cases':10,'scientist_removal_opens_connection':True,'ordinary_routes_unchanged':True,'sanitizers':'address,undefined'};C.dump(C.OUT/'construction_guard_validation.json',result);print(result);return result
if __name__=='__main__':verify()
