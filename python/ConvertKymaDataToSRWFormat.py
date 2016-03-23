#!/usr/bin/env python

import sys
import os.path



def ConvertKymaDataToSRWFormat (InFileName, OutFileName):
  """Convert the kyma format to the SRW input format"""

  if os.path.exists(OutFileName):
    print 'ERROR: File already exists.  Move it first:', OutFileName
    return False

  fi = open(InFileName, 'r')
  fo = open(OutFileName, 'w')

  B = []

  for line in fi:
    B.append( map(float, line.split()) )

  fi.close()

  ZStart = B[0][0]
  ZStop  = B[-1][0]
  StepSizeZ = (ZStop - ZStart) / float(len(B) - 1)

  NewZStart = -(1.5687740096 - ZStart)

  print 'ZStart', ZStart, 'ZStop', ZStop, 'NewZStart', NewZStart, 'len(B)', len(B), 'StepSizeZ', StepSizeZ

  fo.write('#Bx [T], By [T], Bz [T] on 3D mesh: inmost loop vs X (horizontal transverse position), outmost loop vs Z (longitudinal position)\n')
  fo.write('#0.0 #initial X position [m]\n')
  fo.write('#0.0 #step of X [m]\n')
  fo.write('#1 #number of points vs X\n')
  fo.write('#0.0 #initial Y position [m]\n')
  fo.write('#0.0 #step of Y [m]\n')
  fo.write('#1 #number of points vs Y\n')
  fo.write('#' + str(NewZStart) + ' #initial Z position [m]\n')
  fo.write('#' + str(StepSizeZ) +' #step of Z [m]\n')
  fo.write('#' + str(len(B)) +' #number of points vs Z\n')

  for b in B:
    fo.write( '\t'.join(map(str, [b[1], b[3], 0.0])) + '\n' )

  fo.close()

  return True








if __name__ == "__main__":
  if len(sys.argv) != 3:
    print 'Usage:', sys.argv[0], '[InFile] [OutFile]'
    exit(1)

  if not ConvertKymaDataToSRWFormat(sys.argv[1], sys.argv[2]):
    exit(1)
  exit(0)
