#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 11:19:29 2019

@author: Giles
"""

# BOOLEAN EXPRESSIONS

#3 == 3
#3 == 2

#x = 5
#y = 6
##
#print('x =',x,'y =',y)
#print('Checking less than with \'<\':',x < y)
#print('Checking greater than with \'>\':',x > y)

#var_1 = 7
#var_2 = 7
#
#print('var_1 =',var_1,'var_2 = ',var_2)
#print('Checking equality with \'==\':',var_1 == var_2)
#print('Checking not equal with \'!=\':',var_1 != var_2)
#print('Checking less than or equal with \'<=\':',var_1 <= var_2)
#print('Checking greater than or equal with \'>=\':',var_1 >= var_2)
#
#print('Demonstrate that \'True\' is Boolean in python with \
#\'type(True)\':',type(True))

#var_3 = 20
#var_4 = 25

# LOGICAL OPERATORS

#and or not

var_3,var_4,var_5 = 15, 20, 25
##
print('var_3 =',var_3,'var_4 =',var_4,'var_5 =',var_5, end = '\n\n')
###
print('var_4 and var_5 < 100?',var_4 < 100 and var_5 < 100 )
print('var_4 and var_5 < 22?',var_4 < 22 and var_5 < 22)
print('var_4 or var_5 < 22?',var_4 < 22 or var_5 < 22, end = '\n\n')
##
print('not True is:',not True)
print('not False is:',not False, end = '\n\n')
##
print('not(var_4 and var_5 < 100?)',not(var_4  < 100 and var_5 < 100))
print('not(var_4 and var_5 < 22?)',not(var_4 < 22 and var_5 < 22))
print('not(var_4 or var_5 < 22?)',not(var_4 < 22 or var_5 < 22))

# if statement

#some_condition = True
#
#if some_condition:
#    print('The variable \'some_condition\' is True')
#else:
#    print('The variable \'some_condition\' is False')

# What should I wear?

#temp = int(input('Please enter the temperature in Celsius. \
#An integer between 0-40:>>> '))
#
#if temp > 30:
#    print('Wear shorts and sun cream!')
#elif temp <= 30 and temp > 20:
#    print('It\'s warm, but not shorts weather!')
#elif temp <= 20 and temp > 10:
#    print('You\'ll probably need a vest today!')
#else:
#    print('Too cold! Don\'t go out!')

# A little more on strings

#my_string = 'Python'

#len(my_string)
#my_string[0]
#my_string[1]
#my_string[0:4]
#my_string[:4]
#my_string[-1]
#letter = my_string[4]

#my_string.upper()
#my_string.lower()

# Guess the word

#word = 'summer'
#
#guess = input('I\'m thinking of a word, can you guess what it is? Hint \
#it\'s a season.>>> ')
#
#guess = guess.lower()
#
#if guess == 'summer':
#    print('Yes, it\'s Summer: well done!')
#elif guess == 'winter':
#    print('No, it\'s not Winter. Sorry!')
#elif guess == 'autumn':
#    print('No, it\'s not Autumn. Sorry!')
#elif guess == 'spring':
#    print('No, it\'s not Spring. Sorry!')
#else:
#    print(guess.capitalize(),'is not a season!')
