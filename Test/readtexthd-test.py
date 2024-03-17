import segy
import numpy

fp = open("vp.sgy","rb")

texthd = segy.readtexthd(fp)
print(texthd)

bhd = segy.segybhd()

bhd = segy.readbhd(fp,bhd)

print("ns: ", bhd.ns)
print("dt: ", bhd.dt)
print("fmt: ", bhd.fmt)

trhd = segy.segyhd("segy")
trhd,trace = segy.readtr(fp,trhd)
print("ns: ", trhd.ns)
print("dt: ", trhd.dt)
print(trace)
