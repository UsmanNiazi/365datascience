# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 13:21:29 2019

@author: giles
"""

def add(L):
    ''' Adds the integer items of a list'''
    size = len(L)
    total = 0
    iterator = 0
#    pdb.set_trace()
#     print('Reached the while loop')
    while iterator < size:
        total = total + L[iterator]
        iterator +=1
#         print(f'Iterator is {iterator} total is {total}')
    return total 

my_list = [1,2,3,4,5,6,7,'eight']
add(my_list)
