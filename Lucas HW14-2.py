# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 20:50:31 2020

@author: Dana
"""
import sympy as sp
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

# Graph the data to see where the max is at
k1 = 2.8
k2 = 5.0
d = 0.5
n_vals = np.linspace(0,5,20)
P_vals = [(n_val-1)*k1+(n_val-1)*k2-(n_val-1)**2*k1*k2*d for n_val in n_vals]
plt.figure(dpi=100)
plt.plot(n_vals,P_vals)


# Determine the point where the slope is 0 by taking the derivative and setting to 0
n=sp.symbols('n')

def P_1(n):
    k1 = 2.8
    k2 = 5.0
    d = 0.5
    P = (n-1)*k1+(n-1)*k2-(n-1)**2*k1*k2*d
    return sp.diff(P,n)

print("By finding the derivative and setting it to 0, n is {}".format(sp.solveset(P_1(n),n)))


# Minimize the function
def P_analytical(nval):
    k1 = 2.8
    k2 = 5.0
    d = 0.5
    return -((nval-1)*k1+(nval-1)*k2-(nval-1)**2*k1*k2*d)

con = {'type':'ineq','fun':lambda nval: nval}

data = optimize.minimize(P_analytical,(1),constraints = con,method='slsqp')

print("By 'minimizing' the function, n is {}".format(data['x']))






