# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:21:51 2020

@author: Dana
"""

"""
part a: In a uniform random distribution, each value of x and theta is equally likely to occur.
        It is expected that the needle will cross through more lines because most of the angles
        cause the needle to pass through a lot of lines, and if each angle is equally likely then
        a lot of lines will be passed through.
        The average number of lines crossed through is displayed in the console.
part b: The number of crossings is more likely to be 0 because the angle is more likely to be 0, or
        completely vertical.
        The average number of lines crossed through is displayed in the console.
"""
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

def uniformVals(method):
    uniform_x = method.rvs(size=10000,loc = 0, scale = 2)
    uniform_theta = method.rvs(size=10000,loc = 0, scale = 2*np.pi)
    return uniform_x,uniform_theta

def normVals(method, loc = 0, scale = 0.3):
    x = np.linspace(method.ppf(-1*np.pi,loc = loc, scale = scale),\
                    method.ppf(np.pi,loc = loc, scale = scale))
    y = method.pdf(x,loc = loc, scale = scale)
    r = method.rvs(size=10000,loc = loc, scale = scale)
    return x,y,r


uniform_x,uniform_theta = uniformVals(stats.uniform)
x,y,norm_theta = normVals(stats.norm)


#uniform_x = np.random.uniform(0,2,size=10000)
#uniform_theta = np.random.uniform(0,2*np.pi,size=10000)
#norm_theta = np.random.normal(loc=0,scale=0.3,size=10000)


l = 100
d = 2

def calculateLines(x_vals,theta_vals):
    lines = []    
    for i,j in enumerate(x_vals):
    
        # Absolute value to remove the negative sign; the needle crosses 
        # through the same amount of lines no matter which sign
        angle = abs(np.sin(theta_vals[i])) 
        
        # Append number of lines each trial passes through
        # (The absolute value in this ensures that if the needle is almost perfectly vertical on the page
        # and therefore does not cross through any lines, that the count is still 0 when divided by the 
        # distance d rather than being a negative number like -1 (b/c -1//2 is -1, not 0) )
        lines.append(((abs((l/2)-(j/angle))*angle)//d)+((abs((l/2)-((d-j)/angle))*angle)//d))
    return lines
    
uniformlines = calculateLines(uniform_x,uniform_theta)
normlines = calculateLines(uniform_x,norm_theta)

plt.figure(dpi=100)
plt.subplot(121)
plt.hist(uniformlines, density = True)
plt.xlabel('Number of Lines Crossed Through')
plt.title('Random Uniform Distribution')

plt.subplot(122)
plt.hist(normlines,density = True)
plt.xlabel('Number of Lines Crossed Through')
plt.title('Normal Distribution')

plt.tight_layout()
plt.show()

print('The average number of crossings in the uniform distribution is {:.2f} lines.'.format(np.mean(uniformlines)))
print('The average number of crossings in the normal angle distribution is {:.2f} lines.'.format(np.mean(normlines)))
