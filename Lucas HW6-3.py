# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 23:44:58 2020

@author: Dana

"""

def index(file,column,row):
    f = open(file,'r')
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
    
    # Clean up the lists; removing empty leading/trailing spaces, making all the same case
#    for i, a in enumerate(matrix):
#        matrix.remove(matrix[1])
    for i, c in enumerate(columns):
        columns[i] = columns[i].lower()
    for j, r in enumerate(rows):
        rows[j] = rows[j].strip()
        rows[j] = rows[j].lower()
    
    # Make inputs not case sensitive
    column = column.lower()
    row = row.lower()
    
    # Provides the full property name if not already provided
    for i in columns:
        if column in i:
            column = i
    print(matrix)
    # If an invalid input is typed into the definition, the program will not crash
    if column not in columns or row not in rows:
        return 'Your input is invalid! Try providing more information/letters and check your spelling.'
   
    # Finds which row/column the input is in so the matrix can be navigated
    columnindex = columns.index(column)
    rowindex = rows.index(row)
    
    return 'The {} of {} is {}.'.format(columns[columnindex],rows[rowindex].title(),matrix[columnindex][rowindex + 1])
    
    
    
print(index('planetary-fact-sheet.txt','Orbital velocity','Mars'))
print(index('planetary-fact-sheet.txt','Mean TEMPerature (C)','NePTunE'))
print(index('planetary-fact-sheet.txt','num','jupiter'))
    