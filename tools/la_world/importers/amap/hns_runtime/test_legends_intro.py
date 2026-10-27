from probe import *
D=R/'docs/story/intro_draft1';HERE=R/'.la_work/amap/hns_runtime'
def tasks():
 out=[]
 for i in range(16):
  a=symbols['gTasks']+i*40
  if rd(a+4,1):out.append((i,rd(a),[rd(a+8+j*2,2) for j in range(16)]))
 return out
def current():
 for i,f,d in tasks():
  for name,address in symbols.items():
   if name.startswith(('Task_NewGameBirchSpeech_','Task_LegendsCreator_')) and f==address|1:return name,i,d
 return '',0,[]
assert lib.boot(str(R/'pokeemerald.gba').encode())
frames(600);shot('intro_boot');frames(1,8);frames(180);frames(1,8);frames(180);shot('intro_menu');frames(1,1);frames(180);frames(1,1);frames(180);shot('intro_creator')
print(current(),flush=True);state('intro_creator');lib.shutdown()
