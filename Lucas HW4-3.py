# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 16:29:16 2020

@author: Dana

P2.5.10

"""
import random as r
import math as m
import matplotlib.pyplot as plt
import numpy
num = 0
n = 1000 # This can be anything, but the higher it is the more accurate value of pi you will get
xvals = []
yvals = []
colors = []
pi_xvals = numpy.linspace(0,1,n)
pi_yvals = []
for i in range(n):
    x = r.random()
    xvals.append(x)
    y = r.random()
    yvals.append(y)
    if y < m.sqrt(1-x**2):
        num += 1
    pi_yvals.append((1-(pi_xvals[i]**2))**(1/2))
    if yvals[i] < m.sqrt(1-xvals[i]**2):
        colors.append('b')
    else:
        colors.append('r')
p = num/n # proportion of points under the curve to total points
print('pi is approximately equal to:',p*4)

fig = plt.figure(dpi=100)
plt.scatter(xvals,yvals,c=colors,s = 8,alpha = 0.4)

plt.plot(pi_xvals,pi_yvals)
plt.show()