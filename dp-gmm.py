#!/usr/bin/env python3
# create a DP-GMM and draw samples from it
from numpy.random import multivariate_normal
from random import uniform
import sys
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np

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


def plot_cov_ellipse(mean, cov):
  vals, vecs = np.linalg.eigh(cov)
  order = vals.argsort()[::-1]
  vals = vals[order]
  vecs = vecs[:,order]

  theta = np.degrees(np.arctan2(*vecs[:,0][::-1]))

  # Width and height are "full" widths, not radius
  width, height = 2 * np.sqrt(np.abs(vals))
  ellip = Ellipse(xy=mean, width=width, height=height, angle=theta, alpha=0.2)

  ax = plt.gca()
  ax.add_artist(ellip)


alpha = 1

x = []
y = []

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
  p = multivariate_normal(colors[i][0], colors[i][1])
  x.append(p[0])
  y.append(p[1])
  print(p)

for color in colors:
  plt.scatter([color[0][0]], [color[0][1]], marker="*")
  plot_cov_ellipse(*color)

print(colors)
print(urn)

plt.scatter(x, y)
plt.show()
