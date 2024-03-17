#!/usr/bin/env python3
''' Script for converting rss file to binary '''

## Imports
import numpy as np
import rss
import babin as ba
import sys
import argparse
import com

def main() :
  ''' Scrip for converting rss file to bin file'''
  # Heading
  parser = argparse.ArgumentParser(description="Script for converting an rss file \
                                       to a bin file")
  # Get standard arguments
  parser = com.comargs(parser)
  # Get local arguments

  #Parse arguments
  args = parser.parse_args()

  #Create rss object
  rs = rss.RSSdata()
  rs.read(args.fin)

  data = np.reshape(rs.data,rs.data.size, order='F')

  fp = ba.bin(args.fout,"wb")
  fp.write(data)

  print("n1: ", rs.geomN[0]);
  print("n2: ", rs.geomN[1]);
  print("n3: ", rs.geomN[2]);
  print("d1: ", rs.geomD[0]);
  print("d2: ", rs.geomD[1]);
  print("d3: ", rs.geomD[2]);
  print("o1: ", rs.geomO[0]);
  print("o2: ", rs.geomO[1]);
  print("o3: ", rs.geomO[2]);

#--Usual python magic
if __name__ == "__main__":
    main()



