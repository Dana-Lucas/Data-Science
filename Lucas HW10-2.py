# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 17:05:28 2020

@author: Dana
"""
import matplotlib.pyplot as plt
import numpy as np

f = np.loadtxt('dow.txt',float)

fig = plt.figure(dpi=100,figsize=(8,6))
plt.subplots_adjust(hspace=.320,wspace=.475,left=0.085,right=0.960,top=0.895,bottom=0.145)


# Data for #1
plt.subplot(241)
plt.plot(f,c='m',lw=0.5)
plt.title('Original Data')
plt.xlabel('time')
plt.xticks(size='small')
plt.yticks(size='small')

# Coefficients for #1
plt.subplot(245)
c1=np.fft.rfft(f)
plt.semilogy(abs(c1),c='r',lw=0.5)
plt.xlabel('Fourier Coefficients')
plt.ylabel('Magnitude')
plt.xticks(size='small')
plt.yticks(size='small')

# Coefficients for #2
plt.subplot(246)
c2=np.fft.rfft(f)
for i2 in range(len(c2)):
    if abs(i2)<100:
        c2[i2] = 0
plt.semilogy(abs(c2),c='r',lw=0.5)
plt.xlabel('Fourier Coefficients')
plt.ylabel('Magnitude')
plt.xticks(size='small')
plt.yticks(size='small')

# Data for #2
plt.subplot(242)
c2=np.fft.irfft(c2)
plt.plot(abs(c2),c='m',lw=0.5)
plt.title('High Pass Filter Data')
plt.xlabel('time')
plt.xticks(size='small')
plt.yticks(size='small')

# Coefficients for #3
plt.subplot(247)
c3=np.fft.rfft(f)
for i3 in range(len(c3)):
    if abs(i3)>100:
        c3[i3] = 0
plt.semilogy(abs(c3),c='r',lw=0.5)
plt.xlabel('Fourier Coefficients')
plt.ylabel('Magnitude')
plt.xticks(size='small')
plt.yticks(size='small')

# Data for #3
plt.subplot(243)
c3=np.fft.irfft(c3)
plt.plot(abs(c3),c='m',lw=0.5)
plt.title('Low Pass Filter Data')
plt.xlabel('time')
plt.xticks(size='small')
plt.yticks(size='small')

# Coefficients for #4
plt.subplot(248)
c4=np.fft.rfft(f)
for i4 in range(len(c4)):
    if abs(c4[i4])<0.005*max(c4):
        c4[i4]=0
plt.semilogy(abs(c4),c='r',lw=0.5)
plt.xlabel('Fourier Coefficients')
plt.ylabel('Magnitude')
plt.xticks(size='small')
plt.yticks(size='small')
        
# Data for #4
plt.subplot(244)
c4=np.fft.irfft(c4)
plt.plot(abs(c4),c='m',lw=0.5)
plt.title('Magnitude Filter Data')
plt.xlabel('time')
plt.xticks(size='small')
plt.yticks(size='small')

plt.show()

'''
 #1:
 The first 100 coefficients are removed. Because the first couple coefficients
 are the most important ones that define the general shape of the curve, most 
 of the curve's distinguishing features are lost.
 
 #2:
 Only the first 100 coefficients are shown. Because these are the most important
 coefficients in defining the shape of the curve, not a whole lot is lost. The 
 coefficients that make small corrections to the curve are missing, but this does 
 not affect the shape and it is still possible to make out the important features.
 
 #3:
 This removes a lot of the "static" in the data. A smoother curve is produced and 
 the tiny details and jiggity-jags are lost.

'''