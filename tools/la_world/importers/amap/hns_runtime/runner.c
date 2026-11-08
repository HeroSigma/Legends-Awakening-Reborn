#include <mgba/core/core.h>
#include <mgba/core/log.h>
#include <mgba-util/vfs.h>
#include <stdlib.h>
#include <stdio.h>
static void quiet(struct mLogger*l,int c,enum mLogLevel v,const char*f,va_list a){}
static struct mLogger logger={.log=quiet};
static struct mCore* c; static color_t pix[240*160];
int boot(const char* rom){mLogSetDefaultLogger(&logger);c=mCoreCreate(mPLATFORM_GBA);if(!c||!c->init(c))return 0;mCoreInitConfig(c,"mercury-runtime-test");c->opts.useBios=0;c->opts.skipBios=1;c->setVideoBuffer(c,pix,240);if(!mCoreLoadFile(c,rom))return 0;c->reset(c);return 1;}
void frames(int n,int keys){c->setKeys(c,keys);for(int i=0;i<n;i++)c->runFrame(c);c->setKeys(c,0);}
unsigned rd(unsigned a,int size){return size==1?c->busRead8(c,a):size==2?c->busRead16(c,a):c->busRead32(c,a);}
void wr(unsigned a,unsigned v,int size){if(size==1)c->busWrite8(c,a,v);else if(size==2)c->busWrite16(c,a,v);else c->busWrite32(c,a,v);}
int state(const char* path,int load){size_t n=c->stateSize(c);void* data=malloc(n);FILE* f=fopen(path,load?"rb":"wb");if(!f){free(data);return 0;}int ok;if(load){ok=fread(data,1,n,f)==n&&c->loadState(c,data);}else{ok=c->saveState(c,data)&&fwrite(data,1,n,f)==n;}fclose(f);free(data);return ok;}
void shot(const char* path){FILE*f=fopen(path,"wb");fprintf(f,"P6\n240 160\n255\n");for(int i=0;i<240*160;i++){unsigned x=pix[i];fputc(x&255,f);fputc((x>>8)&255,f);fputc((x>>16)&255,f);}fclose(f);}
void shutdown(void){c->deinit(c);}
