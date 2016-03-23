#!/usr/bin/env python

import sys

import matplotlib.pyplot as plt



fi = open(sys.argv[1], 'r')

Z  = []
Bx = []
By = []

for line in fi:
  B = map(float, line.split())
  Z.append(B[0])
  Bx.append(B[1])
  By.append(B[3])

plt.xlabel('Z Position [m]')
plt.ylabel('Magnetic Field [T]')
p1 = plt.plot(Z, Bx)
p2 = plt.plot(Z, By)
plt.legend(['Bx', 'By'])
plt.show()


