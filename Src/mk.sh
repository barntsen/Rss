#!/bin/sh

EXE=\#\!/usr/bin/python3
echo $EXE > xaa.txt
inst=../Bin

cat xaa.txt bin2rss.py > $inst/bin2rss
chmod +x $inst/bin2rss

cat xaa.txt su2rss.py > $inst/su2rss
chmod +x $inst/su2rss

cp rss.py $inst
cp segy.py $inst
cp ibm_float.py $inst

