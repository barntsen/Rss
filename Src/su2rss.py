''' Module for converting su files to rss '''

## Imports
import numpy as np
import rss as rs
import segy
import sys
import argparse

def setrssgeom(rssfile, trhds,dim) :
  """ Set geometry of sources and receivers 
    
    Parameters
      rssfile : rss data object
      trhds   : Array of trace headers
      dim     : 2: 2D data 3: 3D data

    Return 
      True
  """
  
  i=0
  # 2D data
  if dim == 2 :
    for trhd in trhds :
      if scalco < 0 :
        scalar = -1/scalco
      elif scalco > 0 :
        scalar = scalco
      else:
        scalar = 1
      rssfile.srcX[i] = trhd.sx*scalar
      rssfile.srcZ[i] = trhd.gwdepth
      rssfile.GroupX[i] = trhd.gx * scalar
      rssfile.GroupZ[i] = trhd.gwdepth
  # 3D data
  elif dim == 3 :
    for trhd in trhds :
      if scalco < 0 :
        scalar = -1/scalco
      elif scalco > 0 :
        scalar = scalco
      else :
        scalar = 1
      rssfile.srcX[i] = trhd.sx * scalar
      rssfile.srcY[i] = trhd.sy * scalar
      rssfile.srcZ[i] = trhd.gwdepth
      rssfile.GroupX[i] = trhd.gx * scalar
      rssfile.GroupY[i] = trhd.gy * scalar
      rssfile.GroupZ[i] = trhd.gwdepth

  return True

def main() :
  ''' Main script for converting su files to rss files '''
  ## Get command line options

  # Hack for negative floats as option
  for i, arg in enumerate(sys.argv):
    if (arg[0] == '-') and arg[1].isdigit(): sys.argv[i] = ' ' + arg

  # Heading
  parser = argparse.ArgumentParser(description="Script for converting an su file \
                                       to an rss file")
  # Get arguments
  parser.add_argument("fin", help="Input file")                
  parser.add_argument("fout", help="Output file")                
  parser.add_argument("-type", default="generic", 
                    help="Data type: generic, 2d or 3d")                
  #Parse arguments
  args = parser.parse_args()
                        
  ## Reading su file and writing rss file

  # Open the su file
  fd = open(args.fin,"rb")
  #Read the file
  trhds,data = segy.readtrs(fd,-1,"su")

  #Generic (model) file
  if args.type == 'generic' :
    # Creating a rockseis generic file header
    # Get sizes and sampling intervals
    nz = trhds[0].ns
    nx = len(trhds)
    ny = 1
    dx = trhds[0].d1
    dy = trhds[0].d1
    dz = trhds[0].d2
    #Reshape into rss form
    data = np.reshape(data,[nx, ny, nz],'F')
    mod = rs.RSSdata(data);
    # Setting origin
    mod.geomO[0] = 0.0;
    mod.geomO[1] = 0.0;
    mod.geomO[2] = 0.0;
    # Setting sampling
    mod.geomD[0] = dx;
    mod.geomD[1] = dy;
    mod.geomD[2] = dz;
  elif args.type  == '2d' :
    dim=2
    rssfile = rs.RSSdata(data,dim)
    setrssgeom(rssfile,trhds,dim)
  elif args.type  == '3d' :
    dim=3
    rssfile = rs.RSSdata(data,dim)
    setrssgeom(rssfile,trhds,dim)
    setrssgeom(trhds,mod,dim)
  else : 
    print("Using generic format")

  # Writting out the data to disk
  mod.write(args.fout);

#--Usual python magic
if __name__ == "__main__":
    main()
