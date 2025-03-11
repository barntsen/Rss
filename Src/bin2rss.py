''' Module for converting bin files to rss '''

## Imports
import numpy as np
import rss as rs
import segy
import sys
import argparse
import babin as bin
import com
import sys

def main() :
  ''' Main script for converting bin files to rss files '''
  
  ## Get command line options

  # Hack for negative floats as option
  for i, arg in enumerate(sys.argv):
    if (arg[0] == '-') and arg[1].isdigit(): sys.argv[i] = ' ' + arg

  # Heading
  parser = argparse.ArgumentParser(description="Script for converting an su file \
                                       to an rss file")
  #Get arguments
  parser = com.comargs(parser)
  parser.add_argument("-type", default="generic", help="Input file name") 

  #Parse arguments
  args = parser.parse_args()

  if args.n1 == None :
    print("bin2rss: Missing first dimension")
    exit()
                        
  ## Reading bin file and writing rss file

  # Open the bin file
  fd = bin.bin(args.fin,"r")
  tmp = fd.read((args.n2,args.n1))
  data = np.transpose(tmp)

  # Get sizes and sampling intervals
  nx = args.n1
  ny = 1
  nz = args.n2
  dx = args.d1
  dy = args.d3
  dz = args.d2
  ox = args.o1
  oy = args.o3
  oz = args.o2

  #Note that for a binary file
  #there is no information on
  #source and receiver positions
  #so these will be ignored

  #Reshape into rss form
  data = np.reshape(data,[nx, ny, nz],'F')

  #Generic (model) file
  if args.type == 'generic' :
    # Creating a rockseis generic file header
    rssfile = rs.RSSdata(data);
  elif args.type  == '2d' :
    dim=2
    rssfile = rs.RSSdata(data,dim)
  elif args.type  == '3d' :
    dim=3
    rssfile = rs.RSSdata(data,dim)
  else : 
    print("bin2rss: Using generic format")

  # Setting origin
  print("ox,oy,oz:",ox,oy,oz)
  rssfile.geomO[0] = ox
  rssfile.geomO[1] = oy
  rssfile.geomO[2] = oz

  # Setting sampling
  rssfile.geomD[0] = dx;
  rssfile.geomD[1] = dy;
  rssfile.geomD[2] = dz;

  # Writting out the data to disk
  rssfile.data = data
  rssfile.write(args.fout);

#--Usual python magic
if __name__ == "__main__":
    main()
