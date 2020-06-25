# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 15:32:26 2020

@author: Dana
P3.1.1
"""
import math
import matplotlib.pyplot as plt
import numpy as np

f1 = []
f2 = []

x = np.linspace(-20,20,1000)
for i, j in enumerate(x):
    f1.append(math.log(1/(math.cos(x[i]))**2))
    f2.append(math.log(1/(math.sin(x[i]))**2))

fig = plt.figure(dpi=100)
plt.plot(x,f1)
plt.plot(x,f2)
plt.show()

'''
For f1/cos equation: when x is an even multiple of pi/2, the equation becomes ln(1/1) which is 0. 
                    when x is an odd multiple, the equation is undefined because there is a divide by 0 error.
For f2/sin equation: same idea but opposite because the graph is shifted by pi/2
If x = n*pi/2, the graph either reaches its minimim value of 0 (as described above; when n is even for cos and when
n is odd for sin) or comes to a sharp point to signify it is undefined/never reaches a specific value
'''