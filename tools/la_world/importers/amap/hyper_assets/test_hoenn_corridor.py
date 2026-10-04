#!/usr/bin/env python3
"""Exercise camera transition assets and current corridor geometry/ownership."""
import collections,re,subprocess,unittest
from pathlib import Path
import hoenn_corridor_correction as C
class CorridorTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.ledger=C.load(C.OUT/'coordinate_remap_ledger.json');cls.layouts={z['id']:z for z in C.load(C.ROOT/'data/layouts/layouts.json')['layouts']};cls.maps={n:C.load(C.ROOT/f'data/maps/{n}/map.json') for n in [*C.TARGETS,'DewfordTown','Route106']}
 def test_protected_maps_assets_gameplay_map_ids_and_save(self):C.validate()
 def test_current_ocean_seams_and_native_destinations(self):
  for seam in self.ledger['connection_checks']:
   n=seam['map'];dest=seam['destination'];a=C.grid_for(self.layouts[self.maps[n]['layout']]);dm=C.load(C.ROOT/f'data/maps/{dest}/map.json');b=C.grid_for(self.layouts[dm['layout']]);self.assertIn(seam['connection'],self.maps[n]['connections'])
   for q in seam['crossing_cells']:
    x=a.cell(*q['from']);y=b.cell(*q['to']);self.assertEqual(0,x['collision']);self.assertEqual(0,y['collision']);self.assertTrue(x['elevation']==y['elevation'] or x['elevation'] in [0,15] or y['elevation'] in [0,15])
  self.assertEqual('MAP_ISLAND_CAVE',self.maps['Route105']['warp_events'][0]['dest_map']);self.assertEqual((9,21),tuple(self.maps['Route105']['warp_events'][0][v] for v in ['x','y']));self.assertEqual('MAP_ABANDONED_SHIP_DECK',self.maps['Route108']['warp_events'][0]['dest_map'])
 def test_scientists_are_reachable_and_no_extra_gameplay_registered(self):
  ls=self.layouts;maps=self.maps
  for gate in self.ledger['construction_gates']:
   n=gate['map'];e=gate['scientist'];g=C.grid_for(ls[maps[n]['layout']]);self.assertTrue(g.walk(e['x'],e['y']));self.assertEqual('0',e['flag']);self.assertEqual('TRAINER_TYPE_NONE',e['trainer_type']);self.assertEqual((0,0),(e['movement_range_x'],e['movement_range_y']))
   block={(z['x'],z['y']) for z in maps[n]['object_events'] if z['script'].startswith(n+'_EventScript_HyperConstruction')};start=(2,11) if n=='DewfordTown' else(48,17) if n=='Route106' else(33,33)
   # Land+Surf traversal; climb/warp-only behaviors are excluded. Same-elevation water required.
   todo=collections.deque([start]);seen={start}
   while todo:
    x,y=todo.popleft();v=g.cell(x,y)
    for a,b in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
     if not(0<=a<g.w and 0<=b<g.h) or(a,b) in block or(a,b) in seen:continue
     w=g.cell(a,b)
     if w['collision'] or w['elevation'] not in [0,15,v['elevation']] and v['elevation'] not in [0,15]:continue
     if w['translated_behavior'] in [0x60,0x64]:continue
     seen.add((a,b));todo.append((a,b))
   self.assertTrue(any(q in seen for q in [(e['x']-1,e['y']),(e['x']+1,e['y']),(e['x'],e['y']-1),(e['x'],e['y']+1)]),(n,e,'scientist unreachable'))
   text=(C.ROOT/f'data/maps/{n}/scripts.inc').read_text();body=re.search('^'+e['script']+r'::\n(.*?)(?=^\w+:)',text,re.M|re.S)[1];self.assertNotRegex(body,r'warp|setflag|clearflag|setvar|trainerbattle|giveitem|callnative')
  for n in ['DewfordTown','Route106']:self.assertEqual(C.load(C.OUT/'original'/f'data/maps/{n}/map.json')['connections'],maps[n]['connections'])
 def test_native_weather_dive_and_regi_gate_compatibility(self):
  g=C.grid_for(self.layouts[self.maps['Route105']['layout']]);native=C.words(C.ROOT/'data/tilesets/primary/general/metatile_attributes.bin')
  for i in [0x14E,0x14F]:self.assertEqual(native[i]&255,g.attrs[0][i]&255)
  self.assertEqual(0x60,g.cell(9,21)['translated_behavior']);s=(C.ROOT/'data/maps/Route105/scripts.inc').read_text();self.assertIn('call_if_unset FLAG_REGI_DOORS_OPENED, Route105_CloseRegiEntrance',s);self.assertIn('setmetatile 9, 21, 0x09F, TRUE',s)
  for xy in [(10,29),(11,29),(20,54),(21,54)]:self.assertEqual(0,g.cell(*xy)['collision']);self.assertIn(g.cell(*xy)['translated_behavior'],range(0x10,0x16))
 def test_transition_executes_native_gameplay_sequence_and_reloads_changed_primary(self):
  def extract(t):a=t.index('void LoadMapFromCameraTransition(');b=t.index('static void LoadMapFromWarp(',a);return t[a:b]
  old=extract((C.OUT/'original/src/overworld.c').read_text()).replace('LoadMapFromCameraTransition(','OriginalTransition(',1);new=extract((C.ROOT/'src/overworld.c').read_text());calls=set(re.findall(r'\b(\w+)\s*\(',new+old))-{'if','void','LoadMapFromCameraTransition','OriginalTransition'}
  special={'LoadCurrentMapData','GetNumPalsInPrimary','ApplyWeatherColorMapToPals'}
  pre='''#include <assert.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>
typedef uint8_t u8;
struct Tileset { int tag; };
struct MapLayout { const struct Tileset *primaryTileset; };
struct MapHeader { struct MapLayout *mapLayout; int regionMapSectionId; } gMapHeader;
static struct Tileset primaryA, primaryB;
static struct MapLayout source, destination;
static int sLastMapSectionId;
#define FALSE 0
#define TRUE 1
#define FREE_MATCH_CALL 0
#define I_VS_SEEKER_CHARGING 0
#define WARP_ID_NONE -1
#define MAPSEC_BATTLE_FRONTIER 77
#define OW_HIDE_REPEAT_MAP_POPUP 1
#define NUM_PALS_TOTAL 13
static char trace[8192];
static int weatherStart,weatherCount;
static void record(const char *s){strcat(trace,s);strcat(trace,";");}
static void LoadCurrentMapData(void){record("LoadCurrentMapData");gMapHeader.mapLayout=&destination;}
static int GetNumPalsInPrimary(struct MapLayout *p){assert(p==&destination);return 7;}
static void ApplyWeatherColorMapToPals(int first,int count){assert(gMapHeader.mapLayout==&destination);weatherStart=first;weatherCount=count;record("ApplyWeatherColorMapToPals");}
'''
  for call in sorted(calls-special):pre+=f'static void {call}(){{record("{call}");}}\n'
  main='''
static void setup(int different){source.primaryTileset=&primaryA;destination.primaryTileset=different?&primaryB:&primaryA;gMapHeader.mapLayout=&source;gMapHeader.regionMapSectionId=1;trace[0]=0;}
int main(void){char original[8192];setup(0);OriginalTransition(0,20);strcpy(original,trace);setup(0);LoadMapFromCameraTransition(0,20);assert(strcmp(original,trace)==0);assert(weatherStart==7&&weatherCount==6);setup(1);LoadMapFromCameraTransition(0,20);assert(strstr(trace,"InitMap;CopyMapTilesetsToVram;LoadMapTilesetPalettes;ApplyWeatherColorMapToPals;InitTilesetAnimations;UpdateLocationHistoryForRoamer"));assert(!strstr(trace,"CopySecondaryTilesetToVramUsingHeap;"));assert(weatherStart==0&&weatherCount==13);assert(strstr(trace,"RunOnTransitionMapScript;InitMap;"));assert(strstr(trace,"RunOnResumeMapScript;"));puts("Same-primary native sequence exact; changed-primary graphics/palettes/both animations reloaded after destination load.");return 0;}
'''
  p=C.OUT/'camera_transition_host_test.c';p.write_text(pre+old+new+main);exe=C.OUT/'camera_transition_host_test';subprocess.run(['gcc','-std=c17','-O1','-g','-fsanitize=address,undefined',str(p),'-o',str(exe)],check=True,capture_output=True,text=True);q=subprocess.run([str(exe)],check=True,capture_output=True,text=True);C.dump(C.OUT/'camera_transition_host_result.json',{'passed':True,'result':q.stdout.strip(),'sanitizers':'address,undefined','actual_source_functions_exercised':True})
if __name__=='__main__':unittest.main()
