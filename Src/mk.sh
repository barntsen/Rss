#!/bin/sh

EXE=\#\!/usr/bin/python3
echo $EXE > xaa.txt
inst=../Bin

cat xaa.txt bin2rss.py > $inst/bin2rss
chmod +x $inst/bin2rss

cp rss.py $inst

