#!/usr/bin/env python3
# create a DP-GMM and draw samples from it
from numpy.random import multivariate_normal
from random import uniform
import sys

if len(sys.argv) != 2:
  print("Usage: {} <n>".format(sys.argv[0]))
  exit(1)

def rand_cov():
  """Generate a random 2x2 covariance matrix"""
  c = uniform(-1, 1)
  return [[uniform(0, 1), c], [c, uniform(0, 1)]]

def find_index(draw, urn):
  """Find index in urn of given draw"""
  i = 0
  while draw >= 0:
    draw -= urn[i]
    i+=1
  return i-1

alpha = 1

colors = []
urn = [alpha]
n = alpha

for _ in range(int(sys.argv[1])):
  draw = uniform(0, n)
  i = find_index(draw, urn)
  if i==len(urn)-1:
    colors.append(((uniform(-5, 5), uniform(-5, 5)), rand_cov()))
    urn.append(alpha)
    urn[i] = 0
  urn[i] += 1
  n += 1
  print(multivariate_normal(colors[i][0], colors[i][1]))

print(colors)
print(urn)
