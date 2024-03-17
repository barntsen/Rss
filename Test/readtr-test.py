import segy
import numpy as np
import babin

fp = open("vp.su","rb")

trhds,traces = segy.readtrs(fp,-1,"su")

print("d1: ",trhds[0].d1)

fpo = open("vp.bin", "wb")
tmp = traces.astype(np.float32)
tmp.tofile(fpo)

fp.close()
fpo.close()





