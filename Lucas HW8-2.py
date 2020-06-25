# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 19:05:07 2020

@author: Dana
"""

def provide_P(n):
    P = [1,1,1]
    for i in list(range(n)):
        P.append(P[-2]+P[-3])
    return P
    
def provide_Q(n):
    Q = [3,0,2]
    for i in list(range(n)):
        Q.append(Q[-2]+Q[-3])
    return Q

print(provide_P(10000))
print(provide_Q(10000))


# Sieve of Eratosthenes
def primes(n):
    primeslist = []
    prime = [] 
    for j in range(n+1):
        prime.append(True)
    p = 2
    while (p*p <= n): 
        if (prime[p] == True): 
            for k in range(p*2,n+1,p): 
                prime[k] = False
        p += 1
    prime[0] = False
    prime[1] = False
    for s in range(n+1): 
        if prime[s]: 
            primeslist.append(s)
    return primeslist

print()
print('There are {} unique integers in P and {} unique integers in Q.'.format(len(set(provide_P(10000))),len(set(provide_P(10000)))))
print('{} integers occur in both P and Q.'.format(len(set(provide_P(10000)) & set(provide_Q(10000)))))
print('{} prime integers occur in both P and Q.'.format(len( (set(provide_P(10000)) | set(provide_Q(10000))) & set(primes(10000))) ))
print('{} is the only non-prime number that occurs in both P and Q.'.format( (set(provide_P(10000)) & set(provide_Q(10000))) - set(primes(10000))) )

