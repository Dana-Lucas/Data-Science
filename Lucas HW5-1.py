# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 19:59:05 2020

@author: Dana

P2.6.3
"""
f = open('ex2-6-g-esi-data.txt','r')
x_ij = [[],[],[],[]]
x_ij[0] = radius = []
x_ij[1] = density = []
x_ij[2] = Vesc = []
x_ij[3] = Tsurf = []
x = [1.0,1.0,1.0,288]
w = [0.57,1.07,0.7,5.58]
ESIvalues = []
name = []
for i, line in enumerate(f):
    if i>3:
        line = line.lstrip() # remove leading whitespace
        index = line.find('  ') # find the location of the first two spaces
        name.append(line[:index]) # call out the object name
        line = line[index+2:] # then truncate the string to everything else
        line = line.split()
        radius.append(float(line[1]))
        density.append(float(line[2]))
        Vesc.append(float(line[4]))
        Tsurf.append(float(line[6]))
f.close()
for j, parts in enumerate(radius):
    ESI = 1
    for i, parts in enumerate(x_ij):
        ESI *= (1-(((((x_ij[i][j]-x[i])/(x_ij[i][j]+x[i])))**2)**0.5))**(w[i]/(4))
    ESIvalues.append(ESI)
maximum = max(ESIvalues)
for i, num in enumerate(ESIvalues):
    print('{:15} ESI value = {:.4f}'.format(name[i],ESIvalues[i]))
print()
print('{} has an ESI value of {:.4f} and has the closet properties to those of Earth'.format(name[ESIvalues.index(maximum)], ESIvalues[ESIvalues.index(maximum)]))
