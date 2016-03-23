#!/usr/bin/env python

import sys
import math
import matplotlib.pyplot as plt


def FindUndulatorCenter(ZBy):
  "find the max and mins in the By distribution"

  AllMaximum  = []
  AllMaximumX = []

  # Loop over data and find min/max for every point
  IsAbove = False
  IsBelow = False
  MaxBy = 0
  MinBy = 0
  ZMax  = 0
  ZMin  = 0
  ZMaxI = 0
  ZMinI = 0
  MaxListInd  = []

  BThreshold = 0.004
  for i in range( len(ZBy) ):

    if ZBy[i][1] < -BThreshold:
      if IsAbove:
        MaxListInd.append(ZMaxI)
        MaxBy = 0
      IsBelow = True
      IsAbove = False

    if ZBy[i][1] > BThreshold:
      if IsBelow:
        MaxListInd.append(ZMinI)
        MinBy = 0
      IsBelow = False
      IsAbove = True

    if IsAbove and ZBy[i][1] > MaxBy:
      MaxBy = ZBy[i][1]
      ZMax  = ZBy[i][0]
      ZMaxI = i
    if IsBelow and ZBy[i][1] < MinBy:
      MinBy = ZBy[i][1]
      ZMin  = ZBy[i][0]
      ZMinI = i

  if IsAbove:
    MaxListInd.append(ZMaxI)

  if IsBelow:
    MaxListInd.append(ZMinI)

  print 'Number of max/min seen I: ', len(MaxListInd)


  for i in MaxListInd:
    x = []
    y = []

    for j in range(-1, 2):
      x.append(ZBy[i+j][0])
      if ZBy[i][1] >= 0:
        y.append(ZBy[i+j][1])
      else:
        y.append(-ZBy[i+j][1])

    denom = (x[0] - x[1]) * (x[0] - x[2]) * (x[1] - x[2])
    A = (x[2] * (y[1] - y[0]) + x[1] * (y[0] - y[2]) + x[0] * (y[2] - y[1])) / denom
    B = (math.pow(x[2], 2) * (y[0] - y[1]) + math.pow(x[1], 2) * (y[2] - y[0]) + math.pow(x[0], 2) * (y[1] - y[2])) / denom
    C = (x[1] * x[2] * (x[1] - x[2]) * y[0] + x[2] * x[0] * (x[2] - x[0]) * y[1] + x[0] * x[1] * (x[0] - x[1]) * y[2]) / denom

    ParabolaMaxX = -B / (2.0 * A)
    ParabolaMaxY = A * ParabolaMaxX * ParabolaMaxX + B * ParabolaMaxX + C

    AllMaximum.append([ParabolaMaxX, ParabolaMaxY])
    AllMaximumX.append(ParabolaMaxX)


  Center = sum(AllMaximumX) / float(len(AllMaximumX))

  for m in AllMaximum:
    print m

  Z  = []
  By = []
  for vals in ZBy:
    Z.append(vals[0])
    By.append(vals[1])

  plt.xlabel('Z Position [m]')
  plt.ylabel('Magnetic Field [T]')
  p2 = plt.plot(Z, By)
  plt.legend(['By'])

  for val in AllMaximumX:
    plt.axvline(val)


  plt.show()


  return Center




def ReadKymaFileFormat (InFileName):
  """Get field from Kyma data format"""

  fi = open(InFileName, 'r')

  ZBy = []
  for line in fi:
    B = map(float, line.split())
    ZBy.append( [B[0], B[3]] )


  Z  = []
  By = []

  for vals in ZBy:
    Z.append(vals[0])
    By.append(vals[1])



  return ZBy
  




if __name__ == "__main__":
  if len(sys.argv) != 2:
    print 'Usage:', sys.argv[0], '[InFile]'
    exit(1)

  ZBy = ReadKymaFileFormat(sys.argv[1])

  Center = FindUndulatorCenter(ZBy)
  print 'Center:', Center
