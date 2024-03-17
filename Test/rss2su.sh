#!/bin/sh
#Test of conversion from rss format to su format

#Test generic file type
cp vp-orig.rss vp.rss
rss2su vp.rss vp.su

#Test 2D data typ
cp p-orig.rss p.rss
rss2su p.rss p.su


