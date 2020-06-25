# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 21:37:27 2020

@author: Dana
"""

def index(file):
    f = open(file,'r')
    D = {}

    columns = []
    matrix = []
    
    for line in f:
        
        # This skips the beginning comments of the file
        if line[0] == '#': continue
        
        # This splits each line up into a separated list
        s = line.split('\t')

        ''' 
        This below creates an index map for finding the value; 
        it is a group of lists (one list for each property; contents 
        of each of these lists are the values of that property 
        for each planet) inside a list
        '''
        matrix.append(s)
#        print(s)
        
        # These create lists to signify all the properties that can be chosen
        # and all the planets that can be chosen
        if line[1] == line[1].upper():
            rows = s # The first line is already a list, so just call it rows
        if s[1] == s[1].lower():
            columns.append(s[0].strip())
    
    # This takes the first line out of the 'matrix' because it lists the planets and is not needed
    # Need to find out how to remove the first item of each list because the properties aren't needed in it either --
    # It works because you can just add 1 to the row index at the end, but I don't like it
    matrix.remove(matrix[0])

    for m in matrix:
        m.remove(m[0])
    # Clean up the lists; removing empty leading/trailing spaces, making all the same case
#    for i, a in enumerate(matrix):
#        matrix.remove(matrix[1])
#    for i, c in enumerate(columns):
#        columns[i] = columns[i].lower()
    for j, r in enumerate(rows):
        rows[j] = rows[j].strip()
        rows[j] = rows[j].lower()
    
    # Create a dictionary inside a dictionary
    for r in rows:
        D[r] = {}
        for c in columns:
            D[r][c] = matrix[columns.index(c)][rows.index(r)]
    print(D['mars'])
    print()
    return matrix
 
print(index('planetary-fact-sheet.txt'))

    
#print(index('planetary-fact-sheet.txt','Orbital velocity','Mars'))
#print(index('planetary-fact-sheet.txt','Mean TEMPerature (C)','NePTunE'))
#print(index('planetary-fact-sheet.txt','num','jupiter'))
    