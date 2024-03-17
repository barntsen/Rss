import sys
import argparse

def comargs(parser) :
  """Get common command line arguments """

  # Hack for negative floats as option
  for i, arg in enumerate(sys.argv):
    if (arg[0] == '-') and arg[1].isdigit(): sys.argv[i] = ' ' + arg

  parser.add_argument("-n1",dest="n1",type=int,
                        help="First dimension of data")
  parser.add_argument("-n2",dest="n2",type=int,default=1,
                        help="Second dimension of data")
  parser.add_argument("-n3",dest="n3",type=int,default=1,
                        help="Third dimension of data")
  parser.add_argument("-d1",dest="d1",type=float,default=1.0,
                        help="First dimension sampling interval")
  parser.add_argument("-d2",dest="d2",type=float,default=1.0,
                        help="Second dimension sampling interval")
  parser.add_argument("-d3",dest="d3",type=float,default=1.0,
                        help="Third dimension sampling interval")
  parser.add_argument("-o1",dest="o1",type=float,default=0.0,
                        help="First dimension origo")
  parser.add_argument("-o2",dest="o2",type=float,default=0.0,
                        help="Second dimension origo")
  parser.add_argument("-o3",dest="o3",type=float,default=0.0,
                        help="Third dimension origo")
  parser.add_argument("fin", help="Input file name")
  parser.add_argument("fout",help="Output file name")
                        
  return parser


