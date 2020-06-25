# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 19:36:08 2020

@author: Dana
"""

'''
The best-fit parameters are [-2.17081393e+01  1.71994539e-02  1.25960404e+00  5.62200813e+01].

Therefore, the period of oscillation is 365.313. This is reasonable because each year is 365 
days long and each cycle/period should last approximately 1 year.

'''


import matplotlib.pyplot as plt
from scipy import optimize, stats
import numpy as np

f = open("MDBALTIM.txt",'rt')
daycount = []
temp = []
years = []
templist = []

for count,line in enumerate(f):
    s = line.split()
    if float(s[-1]) == -99.0:
        continue
    daycount.append(float(count))
    temp.append(float(s[-1]))
    years.append(s[2])
    
yearlist = list(set(years))

for i in yearlist:
    tempbyyear = []
    for j,(a,b) in enumerate(zip(years,temp)):
        if a == i:
            tempbyyear.append(b)
    templist.append(tempbyyear)
dictionary = dict(zip(yearlist,templist))
#print(dictionary)
f.close()

def f(t,a,b,c,d):
    return a*np.sin(b*t+c)+d
        
popt,pcov = optimize.curve_fit(f,daycount,temp,[-35,0.0175,0,50])
y_fit = [f(day,*popt) for day in daycount]
print("The best-fit parameters are {}.".format(popt))
print("The period of oscillation is {:.3f}.".format(2*np.pi/popt[1]))

fig1 = plt.figure(dpi=100)

plt.subplot(211)
plt.plot(daycount,temp)
plt.ylabel('Temperature (F)')

plt.subplot(212)
plt.scatter(daycount,temp,color='r',marker='.',alpha=0.05)
plt.xlabel('Date (since 1/1/95)')
plt.ylabel('Temperature (F)')
plt.plot(daycount,y_fit,'b-',lw=1)

plt.show()