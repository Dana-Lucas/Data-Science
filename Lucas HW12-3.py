# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 09:26:48 2020

@author: Dana
"""

from scipy.integrate import tplquad
import numpy as np

def f(theta,z,r):
    return z**2*r**3

H = 2
R = 2.5

val, error = tplquad(f,0,R,\
                     lambda r: r*H/R,lambda r: H, \
                     lambda r,z: 0, lambda r,z: 2*np.pi)

print("The moment of inertia is {:.2e} with error of {:.2e}".format(val,error))