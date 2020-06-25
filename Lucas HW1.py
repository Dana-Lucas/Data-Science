"""
Dana Lucas 1/22/2020

Q2.2.1. a.) 2.7/2 = 1.35    (This is just regular division)
        b.) 2/4-1 = -0.5    (Perfrom division before subtraction)
        c.) 2//4-1 = -1     (Integer division before subtraction)
        d.) (2+5)%3 = 1     (Do addition in parenthesis before remainder division)
        e.) 2+5%3 = 4       (Do remainder division before addition)
        f.) 3*4//6 = 2      (Complete in order shown)
        g.) 3*(4//6) = 0    (Integer division equals 0 and multiplied by anything still 0)
        h.) 3*2**2 = 12     (Exponential first then multiplication))
        i.) 3**2*2 = 18     (Complete in order shown)

Q2.2.5. By using the variable e and importing the math package, the system thinks the number e is being used 
        rather than the assigned value of 2. Therefore, it is computing sqrt(8^e) where e is 2.71...
        
Q2.2.9. a.) not 1<2 or 4>2                   true
        b.) not (1<2 or 4>2)                 false
        c.) 1<2 or 4>2                       true
        d.) 4>2 or 10/0==0                   true
        e.) not 0<1                          false
        f.) 1 and 2                          2
        g.) 0 and 1                          0
        h.) 1 or 0                           1
        i.) type(complex(2,3).real) is int   false

P2.2.4. The surface area of the geoid is 510065621724078.94 km^2 and the surface area of a perfect sphere is 
        510064471909788.25 km^2. Therefore, the surface area of the geoid is larger.

"""

import math
a = 6378137.0
c = 6356752.314245
x = math.sqrt(1-((c**2)/(a**2)))
S1 = 2*math.pi*(a**2)*(1+((1-x**2)/x)*math.atanh(x))
print(S1)
b = 6371*(10**3)
S2 = 4*math.pi*(b**2)
print(S2)
print(S1>S2)