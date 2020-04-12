#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 13:04:18 2019

@author: Giles
"""

'''
Question 1
Write code that asks the user to input a number between 1 and 5 inclusive.
The code will take the integer value and print out the string value. So for
example if the user inputs 2 the code will print two. Reject any input that
is not a number in that range
'''

#user_input = int(input('Please enter an integer between 1-5:> '))
#if user_input == 1:
#    print('one')
#elif user_input == 2:
#    print('two')
#elif user_input == 3:
#    print('three')
#elif user_input == 4:
#    print('four')
#elif user_input == 5:
#    print('five')
#else:
#    print('Out of range')

'''
Question 2
Repeat the previous task but this time the user will input a string and the
code will ouput the integer value. Convert the string to lowercase first.
'''
#user_input = input('Please enter an string between One and five:> ')
#user_input = user_input.lower()
#if user_input == 'one':
#    print(1)
#elif user_input == 'two':
#    print(2)
#elif user_input == 'three':
#    print(3)
#elif user_input == 'four':
#    print(4)
#elif user_input == 'five':
#    print(5)
#else:
#    print('Out of range')
'''
Question 3
Create a variable containing an integer between 1 and 10 inclusive. Ask the
user to guess the number. If they guess too high or too low, tell them they
have not won. Tell them they win if they guess the correct number.
'''
#secret_number = 3
#guess = input('Guess the number between 1-10:> ')
#if guess.isdigit():
#    guess = int(guess)
#    if guess == secret_number:
#        print('You guessed the correct number! You win!')
#    elif guess > secret_number and guess <= 10:
#        print('You guessed too high. Sorry you lose!')
#    elif guess < secret_number and guess >= 1:
#        print('You guessed too low. Sorry you lose!')
#    else:
#        print('Out of range')
#else:
#    print('That\'s not even an integer! What are you playing at?!')

'''
Question 4
Ask the user to input their name. Check the length of the name. If it is
greater than 5 characters long, write a message telling them how many characters
otherwise write a message saying the length of their name is a secret
'''
#name = input('Please enter your name:>')
#name_len = len(name)
#if name_len > 5:
#    print('Your name contains',name_len,'characters.')
#else:
#    print('I\'m not telling you the length of your name.')

'''
Question 5
Ask the user for two integers between 1 and 20. If they are both greater than
15 return their product. If only one is greater than 15 return their sum, if
neither are greater than 15 return zero
'''
#int_1 = int(input('Please enter an integer between 1-20:> '))
#int_2 = int(input('Please enter another integer between 1-20:> '))
#
#if int_1 > 15 and int_2 > 15:
#    print(int_1 * int_2)
#elif int_1 > 15 or int_2 > 15:
#    print(int_1 + int_2)
#else:
#    print(0)

'''
Question 6
Ask the user for two integers, then swap the contents of the variables. So if
var_1 = 1 and var_2 = 2 initially, once the code has run var_1 should equal 2
and var_2 should equal 1.
'''
#int_1 = int(input('Please enter first integer:> '))
#int_2 = int(input('Please enter second integer:> '))
#print('Before swapping int_1 =',int_1,'and int_2 =',int_2)
#int_1,int_2 = int_2,int_1
#print('After swapping int_1 =', int_1,'and int_2 = ',int_2)
