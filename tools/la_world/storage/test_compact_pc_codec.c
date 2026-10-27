#include "compact_pc_codec.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static uint32_t seed=0x1a602801;
static unsigned checks;
static uint8_t records[LA_PC_SLOTS][LA_PC_RECORD_BYTES];
static uint32_t Next(void){seed^=seed<<13;seed^=seed>>17;seed^=seed<<5;return seed;}
#define CHECK(x) do {checks++;if(!(x)){fprintf(stderr,"line %d: %s\n",__LINE__,#x);exit(1);}}while(0)
static void Roundtrip(struct LaPcTraits *v,uint8_t *out)
{
 struct LaPcTraits decoded;uint8_t twice[LA_PC_RECORD_BYTES];uint64_t rank;uint8_t evs[6];
 CHECK(LaPcEncode(v,out));CHECK(LaPcDecode(out,&decoded));
 CHECK(LaPcPeekSpecies(out)==decoded.species);CHECK(LaPcPeekEgg(out)==decoded.egg);CHECK(LaPcPeekItem(out)==decoded.item);
 for(unsigned slot=0;slot<4;slot++) { CHECK(LaPcPeekMove(out,slot)==decoded.moves[slot]); }
 CHECK(memcmp(v,&decoded,sizeof(*v))==0);CHECK(LaPcEncode(&decoded,twice));CHECK(memcmp(out,twice,sizeof(twice))==0);CHECK(LaPcRankEvs(v->evs,&rank));CHECK(LaPcUnrankEvs(rank,evs));CHECK(memcmp(evs,v->evs,6)==0);
}
int main(int argc,char **argv)
{
 unsigned trial,i,j;struct LaPcTraits v;uint8_t out[LA_PC_RECORD_BYTES],evs[6];uint64_t rank;
 CHECK(sizeof(records)==55800);CHECK(!LaPcUnrankEvs(LA_PC_EV_COMBINATIONS,evs));CHECK(!LaPcUnrankEvs(UINT64_MAX,evs));
 for(i=0;i<6;i++)for(j=0;j<6;j++)if(i!=j){memset(&v,0,sizeof(v));v.species=1;v.evs[i]=255;v.evs[j]=255;Roundtrip(&v,out);}
 memset(&v,0,sizeof(v));v.species=1;v.evs[0]=255;v.evs[1]=255;v.evs[2]=1;CHECK(!LaPcEncode(&v,out));CHECK(!LaPcRankEvs(v.evs,&rank));
 memset(&v,0,sizeof(v));v.species=2048;CHECK(!LaPcEncode(&v,out));v.species=1;v.original_nature=25;CHECK(!LaPcEncode(&v,out));
 memset(&v,0,sizeof(v));CHECK(LaPcEncode(&v,out));for(i=0;i<LA_PC_RECORD_BYTES;i++)CHECK(out[i]==0);CHECK(LaPcDecode(out,&v));CHECK(v.species==0);
 for(trial=0;trial<30000;trial++) {
  unsigned budget=510;memset(&v,0,sizeof(v));v.species=1+Next()%1572;v.tera_type=Next()%32;v.item=Next()%1024;v.experience=Next()%2097152;v.pp_bonuses=Next();v.evolution_tracker=Next()%1024;
  for(i=0;i<4;i++)v.moves[i]=Next()%1024;
  for(i=0;i<6;i++){unsigned maximum=budget<255?budget:255;v.evs[i]=Next()%(maximum+1);budget-=v.evs[i];v.ivs[i]=Next()%32;}
  for(i=5;i;i--){j=Next()%(i+1);unsigned swap=v.evs[i];v.evs[i]=v.evs[j];v.evs[j]=swap;}
  v.ability=Next()%4;v.mint_nature=Next()%32;v.original_nature=Next()%25;v.female=Next()%2;v.shiny=Next()%2;v.friendship=Next();v.hyper_trained=Next()%64;v.egg=Next()%2;v.ball=Next()%64;v.foreign_ot=Next()%2;v.wurmple_branch=Next()%2;v.shadow=Next()%2;v.fateful=Next()%2;v.champion_ribbon=Next()%2;v.pokerus=Next();v.beauty=Next();v.personality_mod100_quotient=Next()%4;v.dynamax_level=Next()%16;v.gigantamax_factor=Next()%2;v.foreign_language=Next()%2;v.markings=Next()%16;
  Roundtrip(&v,out);if(trial<LA_PC_SLOTS)memcpy(records[trial],out,LA_PC_RECORD_BYTES);
 }
 for(i=0;i<LA_PC_SLOTS;i++){uint8_t again[LA_PC_RECORD_BYTES];CHECK(LaPcDecode(records[i],&v));CHECK(LaPcEncode(&v,again));CHECK(memcmp(again,records[i],LA_PC_RECORD_BYTES)==0);}
 if(argc==2){FILE *f=fopen(argv[1],"wb");CHECK(f!=NULL);CHECK(fwrite(records,1,sizeof(records),f)==sizeof(records));CHECK(fclose(f)==0);}
 printf("{\"passed\":true,\"assertions\":%u,\"random_roundtrips\":30000,\"populated_slots\":1800,\"record_bytes\":31,\"payload_bytes\":55800}\n",checks);return 0;
}
