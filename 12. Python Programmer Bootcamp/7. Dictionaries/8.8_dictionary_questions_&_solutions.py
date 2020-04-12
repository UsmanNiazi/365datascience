# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 17:32:12 2019

@author: giles
"""

'''
Question 1
Can you remember how to check if a key exists in a dictionary?
Using the capitals dictionary below write some code to ask the user to input
a country, then check to see if that country is in the dictionary and if it is
print the capital. If not tell the user it's not there.
'''

#capitals = {'France':'Paris','Spain':'Madrid','United Kingdom':'London',
#            'India':'New Delhi','United States':'Washington DC','Italy':'Rome',
#            'Denmark':'Copenhagen','Germany':'Berlin','Greece':'Athens',
#            'Bulgaria':'Sofia','Ireland':'Dublin','Mexico':'Mexico City'
#            }
#
#user_input = input('Which country would you like to check?:> ')
#
#user_input = user_input.lower()
#
#
#
#while ('united kingdom' not in user_input and not user_input.isalpha()):
#    if user_input == 'united states':
#        break
#    print('You must input a string')
#    user_input = input('Which country would you like to check?:> ')
#
#user_input = user_input.title()
##print(user_input)
#if user_input in capitals:
#    print(f'The capital of {user_input} is {capitals[user_input]}')
#else:
#    print('No data available') 
    
'''
Question 2
Write python code that will create a dictionary containing key, value pairs
that represent the first 12 values of the Fibonacci sequence 
i.e {1:0,2:1,3:1,4:2,5:3,6:5,7:8 etc}    
'''
#n = 12
#a = 0 
#b = 1
#d = dict()
#for i in range(1,n+1):
#    d[i] = a
#    a,b = b,a+b
#print(d)  

'''
Question 3
Create a dictionary to represent the open, high, low, close share price data 
for 4 imaginary companies. 'Python DS', 'PythonSoft', 'Pythazon' and 'Pybook'
the 4 sets of data are [12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
[98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]
'''

#companies = ['Python DS', 'PythonSoft', 'Pythazon', 'Pybook']
#key_names = ['Open','High','Low','Close']
#prices = [[12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
#[98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]]
#
#d_1 = {}
#
#for i in range(len(key_names)):
#    d_1[companies[i]] = dict(zip(key_names,prices[i]))
#        
#print(d_1)    

'''
Question 4
Go to the python module web page and find a module that you like. Play with it, 
read the documentation and try to implement it.
'''
## Days until holiday!
#import datetime
#
#today = datetime.date.today()
#
#print(f"Today's date is {today}")
#holiday = datetime.date(2019,12,25)
#delta = holiday - today
#
#print(f"Just {delta.days} days until the holidays!")

'''
Question 5
Create a dictoinary containing as keys the letters from A-Z, the values should 
be random numbers created from the random module. Can you draw a bar graph of 
the results?
'''

#import random
#
#keys = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#
#d = dict()
#
#for letter in keys:
#    d[letter] = random.randint(1,100)
#    
#print(d)    
#
#import matplotlib.pyplot as plt
#
#x,y = zip(*d.items()) 
#
#plt.bar(x,y)
    
'''
Question 6
Create a dictionary containing 4 suits of 13 cards 
['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
'''

suits = ['Spades','Clubs','Hearts','Diamonds']
rank = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']

deck = dict()

for i in suits:
    deck[i] = rank
    
print(deck)    

