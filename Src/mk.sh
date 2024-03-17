#!/bin/sh

EXE=\#\!/usr/bin/python3
echo $EXE > xaa.txt
inst=../Bin

cat xaa.txt su2rss.py > $inst/su2rss
chmod +x $inst/su2rss
cat xaa.txt bin2rss.py > $inst/bin2rss
chmod +x $inst/bin2rss
cat xaa.txt rss2bin.py > $inst/rss2bin
chmod +x $inst/rss2bin
cat xaa.txt rss2su.py > $inst/rss2su
chmod +x $inst/rss2su

cp $HOME/Dropbox/Src/Babin/babin.py $inst 
cp segy.py $inst 
cp rss.py $inst 
cp com.py $inst
