import segy
import numpy as np

fp = open("vp.su","rb")
trhds,traces = segy.readtrs(fp,1,"su")
ntr = segy.getntr(fp,trhds[0].ns)
print("no of traces: ", ntr)
fp.close()

fp = open("vp.su","rb")
trhds,traces = segy.readtrs(fp,-1,"su")

fpo = open("vp-out.su", "wb")
segy.writetrs(fpo, trhds, traces,'su')
fpo.close()





