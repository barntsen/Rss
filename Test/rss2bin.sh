#!/bin/sh
# Test of conversion from rss file to bin file

#Get original rss file
cp vp-orig.rss vp.rss

#Convert to bin file
rss2bin vp.rss vp.bin
