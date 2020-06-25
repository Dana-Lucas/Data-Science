# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 09:49:54 2020

@author: Dana
"""
import math
import matplotlib.pyplot as plt
import numpy as np

def fourier(n):
    xvals = np.linspace(-2,2,1000)
    yvals = []
    for j in xvals:
        f=0
        for i in range(1,n+1):
            k = (2*math.pi*i)
            A = (2/(math.pi*i))*math.sin(math.pi*0.75*i)
            f += (A*math.cos(k*j))
        yvals.append(f)
    return xvals,yvals

xvals1,yvals1 = fourier(2)
xvals2,yvals2 = fourier(10)
xvals3,yvals3 = fourier(100)
fig = plt.figure(dpi=100)
plt.plot(xvals1,yvals1,'b',lw=3,label='N=2')
plt.plot(xvals2,yvals2,'g',lw=3,label='N=10')
plt.plot(xvals3,yvals3,'r',lw=2,label='N=100')
plt.legend(loc='lower left')
plt.title('Truncated Fourier Series')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()
            
            
    