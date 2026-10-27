from pathlib import Path
import ctypes,subprocess,json,struct
from PIL import Image
R=Path(__file__).resolve().parents[5];HERE=R/'.la_work/amap/hns_runtime';HERE.mkdir(parents=True,exist_ok=True)
lib=ctypes.CDLL(str(HERE/'runner.so'));lib.boot.argtypes=[ctypes.c_char_p];lib.rd.restype=ctypes.c_uint;lib.wr.argtypes=[ctypes.c_uint,ctypes.c_uint,ctypes.c_int];lib.state.argtypes=[ctypes.c_char_p,ctypes.c_int];lib.shot.argtypes=[ctypes.c_char_p]
symbols={z[2]:int(z[0],16) for line in subprocess.check_output(['arm-none-eabi-nm','--defined-only',str(R/'pokeemerald.elf')],text=True).splitlines() if len(z:=line.split())==3}
def rd(a,n=4):return lib.rd(a,n)
def wr(a,v,n=4):lib.wr(a,v,n)
def frames(n,k=0):lib.frames(n,k)
def shot(name):
 p=HERE/(name+'.ppm');lib.shot(str(p).encode());im=Image.open(p);im.save(HERE/(name+'.png'));return str(HERE/(name+'.png'))
def state(name,load=False):assert lib.state(str(HERE/(name+'.state')).encode(),load)
def info():
 p=rd(symbols['gSaveBlock1Ptr']);print('callback',hex(rd(symbols['gMain']+4)),'saveptr',hex(p),'location',bytes(rd(p+4+i,1) for i in range(8)).hex(),'pos',rd(p,2),rd(p+2,2))
def warp(group,mid,x,y):
 a=symbols['sWarpDestination']
 for i,v in enumerate(struct.pack('<BBbxhh',group,mid,-1,x,y)):wr(a+i,v,1)
 wr(symbols['gMain']+4,symbols['WarpIntoMap']|1)
 frames(2)
 wr(symbols['gMain']+4,symbols['CB2_LoadMap']|1)
 frames(180)
def pos():
 p=rd(symbols['gSaveBlock1Ptr']);return rd(p,2),rd(p+2,2)
if __name__=='__main__':
 assert lib.boot(str(R/'pokeemerald.gba').encode());frames(600);info();shot('title')
 wr(symbols['gMain']+4,symbols['CB2_NewGame']|1);frames(300);info();shot('newbark');state('newbark')
