# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 11:38:27 2020

@author: Dana

P8.2.7
"""
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

def f(r,phi):
    e_val = 0.1
    ratio = 0.265
    theta,omega=r[0],r[1]
    dtheta = omega*((1-e_val**2)**2/(1+e_val*math.cos(phi)))**2 #dtheta/dphi
    domega = -1*ratio*(3/2)*math.sin(2*(theta-phi))*(1+e_val*math.cos(phi))/((1-e_val**2)**2) #domega/dphi
    return dtheta,domega
    
p_points = np.linspace(0,200,10000000)

plt.figure(dpi=100)
plt.subplot(211)
out = odeint(f,[0,0],p_points)
theta_points1=out[:,0]
omega_points1=out[:,1]
plt.plot(p_points,omega_points1,'m-')
plt.xlabel('Orbital Angle (phi)')
plt.ylabel('Spin Rate (omega)')

plt.subplot(212)
out2 = odeint(f,[0,2],p_points)
theta_points2=out2[:,0]
omega_points2=out2[:,1]
plt.plot(p_points,omega_points2,'b--')
plt.xlabel('Orbital Angle (phi)')
plt.ylabel('Spin Rate (omega)')

plt.subplots_adjust(top=0.935,bottom=0.110,left=0.110,right=0.935,hspace=0.350)
plt.show()





