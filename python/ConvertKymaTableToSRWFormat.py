#!/usr/bin/env python

import sys
import os.path
from ConvertKymaDataToSRWFormat import *



def ConvertKymaTableToSRWFormat (InFileName, OutFileName, InDataDir = '.', OutDataDir = '.'):
  """Convert the file table from kyma format to srw format"""

  if os.path.exists(OutFileName):
    print 'ERROR: File already exists.  Move it first:', OutFileName
    return False

  fi = open(InFileName, 'r')
  fo = open(OutFileName, 'w')


  FirstLine = fi.readline().split()
  i = 0
  d = dict()
  for w in FirstLine:
    d[w] = i
    i += 1


  Lines = []
  for line in fi:
    Lines.append( line.split() )
    t = line.split()

    NewName = 'epu57_esm_ph' +  t[d['ClbWavePhase']] + '_g' + t[d['ClbWaveGap']] + '.dat'
    print NewName

    PhaseMode = str(t[d['ClbPhaseMode']])
    MyPhaseMode = 'p1'
    if PhaseMode != '0':
      print 'ERROR: I do not know this phase mode:', PhaseMode
      raise
      



    print '\t'.join([t[d['ClbWaveGap']], t[d['ClbWavePhase']]]), 'PhaseMode', MyPhaseMode
    fo.write('\t'.join([t[d['ClbWaveGap']], MyPhaseMode, t[d['ClbWavePhase']], NewName, '1', '1\n']))

    ConvertKymaDataToSRWFormat(InDataDir + '/' + t[d['ClbOutFileFld']], OutDataDir + '/' + NewName)


  fi.close()








if __name__ == "__main__":
  if len(sys.argv) != 5:
    print 'Usage:', sys.argv[0], '[InFile] [OutFile] [InDataDir] [OutDataDir]'
    exit(1)

  if not ConvertKymaTableToSRWFormat(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]):
    exit(1)
  exit(0)
