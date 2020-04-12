# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 10:19:52 2019

@author: giles
"""

# File handling in Python
# Python can open, close, read to and write to files

#f = open('kipling.txt','w')
#
#print(type(f))
#
#f.write('If you can keep your head while all about you \nare losing theirs\
#and blaming it on you,\n')
#
#f.write('If you can trust yourself when all men doubt you,\n\
#But make allowance for their doubting too;\n')
#
#f.write('If you can wait and not be tired by waiting,\n\
#Or being lied about, don\'t deal in lies,\n')
#
#f.write('Or being hated, don\'t give way to hating,\n\
#And yet don\'t look too good, nor talk too wise:\n')
#
#f.close()
#
#f = open('kipling.txt','r')
#
#print(type(f))
#
#print(f.read())
#f.close()
#
#f = open('kipling.txt','r')
#
#print(f.readline())
#f.close()
#print()
#
#f = open('kipling.txt','r')
#
#print(type(f))
#
#print(f.readlines())
#f.close()

#f = open('kipling.txt','r')
#
#print(type(f))
#
#content = f.readlines()
#f.close()


#
#f = open('kipling.txt','a')
#f.write('If you can dream - and not make dreams your master;\n\
#If you can think - and not make thoughts your aim;\n')
#f.close()
#print()
#f = open('kipling.txt','r')
#print(f.read())
#f.close()
#print()
#with open('kipling.txt','r') as f:
#    for line in f.readlines():
#        print(line,end='')


# Functions

#print('Hello, world!')

#def hello():
#    print('Hello, world!')
#
#hello()
##
#for i in range(5):
#    hello()


#def hi(name):
#    print(f'Hello, {name}!')
##    
#hi('Giles')    
#hi('Anthony')


#hi()

#def hi_2(name='Giles'):
#    print(f'Hello, {name}!')
##
#hi_2()

#n=20
#a = 0
#b = 1
#for i in range(n):
#    a,b = b,a+b
#print(a)    
#    
#    
#    
def fib(n):
    ''' Calculates and returns the nth fibonacci number'''
    a = 0
    b = 1
    for i in range(n):
        a,b = b,a+b
    return a
#    
##    
#fib_num = fib(20)
#print(fib_num)
##    
#for i in range(20):
#    print(fib(i))
    
    
# Docstring
    
#def calc_mean(first,*remainder):
#    '''
#    This calculates the mean of numbers.
#    '''
#    mean = (first + sum(remainder))/ (1 + len(remainder))
#    print(type(remainder))
#    return mean
#    
#print(calc_mean(23,43,56,76,45,34,65,78,975,3456,54))
#    
#
#   
    
# Recursion

def fib_2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_2(n-1) + fib_2(n-2)
#    
    
#x = fib_2(20)
#print(x) 
#y = fib(1000)
#print(y)
##    
#x = fib_2(37)    
#print(x)


    
import timeit


t1 = timeit.Timer("fib(36)","from greetings import fib")
print(t1.timeit(5))
    
t2 = timeit.Timer("fib_2(36)","from greetings import fib_2")
print(t2.timeit(5))


