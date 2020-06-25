# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 09:24:41 2020

@author: Dana
"""

""" HW: Q2.3.4, P2.3.3
Q2.3.4.) The output is: 
            1st
            3rd
            5th
        The number n is first printed by the first part of the format method and then then the suffix is added.
        The suffix of each is computed based on the number n. For example, n=1 computes to suff[2:4]. So...the
        part of the string 'suff' from 2 inclusive to 4 exclusive is printed. '{:d}{:s}' formats the string
        appropriately. {:d} is the format code that allows the first part (n) to be printed as a number and 
        {:s} is the code that allows the suffix to be printed as a string. There is no space or other characters
        in between the number and suffix because the two format codes are right next to each other.
        
P2.3.3.) See code below
    
"""


suff = 'thstndrdththththththth'
n=1
print('{:d}{:s}'.format(n, suff[n*2:n*2+2]))
n=3
print('{:d}{:s}'.format(n, suff[n*2:n*2+2]))
n=5
print('{:d}{:s}'.format(n, suff[n*2:n*2+2]))

# =============================================================================
# string2 = [1,0,0,0,1,0,0,0,1]
# print('[{} {} {}]'.format(string2[0],string2[1],string2[2]))
# print('[{} {} {}]'.format(string2[3],string2[4],string2[5]))
# print('[{} {} {}]'.format(string2[6],string2[7],string2[8]))
# =============================================================================

print()

a11 = 1
a12 = 0
a13 = 0
a21 = 0
a22 = 1
a23 = 0
a31 = 0
a32 = 0
a33 = 1
print('[{} {} {}]\n[{} {} {}]\n[{} {} {}]'.format(a11,a12,a13,a21,a22,a23,a31,a32,a33))

print()

b11 = 0.0
b12 = 3.4
b13 = -1.2
b21 = -1.1
b22 = 0.5
b23 = -0.2
b31 = 2.3
b32 = -1.4
b33 = -0.7
print('[{: 1.1f} {: 1.1f} {: 1.1f}]\n[{: 1.1f} {: 1.1f} {: 1.1f}]\n[{: 1.1f} {: 1.1f} {: 1.1f}]'.format(b11,b12,b13,b21,b22,b23,b31,b32,b33))

