import segy
import numpy as np
import babin

fp = open("vp.su","rb")

trhd = segy.segyhd("su")
trhd,trace = segy.readtr(fp,trhd)
print(trhd.ns)
print("trace: ",trace)

fpo = open("vpo.su", "wb")
segy.writetr(fpo,trhd,trace)

fp.close()
fpo.close()





