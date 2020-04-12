# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 15:17:56 2019

@author: giles
"""

'''
Question 1

Create a class to represent a bank account. It will need to have a balance,
a method of withdrawing money, depositing money and displaying the balance to
the screen. Create an instance of the bank account and check that the methods 
work as expected.
'''

#class BankAccount(object):
#    ''' Docstring to go here'''
#    
#    def __init__(self,balance=0.0):
#        self.balance = balance
#        
#    def display_balance(self):
#        print(f'Your balance is {self.balance}')
#        
#    def make_deposit(self):
#        amount = float(input('How much would you like to deposit?:> '))
#        self.balance += amount
#        print(f'Balance is now {self.balance}.')
#        
#    def make_withdrawal(self):
#        amount = float(input('How much would you like to withdraw?:> '))
#        if amount > self.balance:
#            print(f'You do not have sufficient funds, your balance is {self.balance}')
#        else:
#            self.balance -= amount
#            print(f'Withdrawal successful: balance is now {self.balance}.')
            
   

'''
Question 2
 Create a circle class that will take the value of a radius and 
 return the area of the circle
'''
import math

class Circle(object):
    ''' Represents a circle with radius. Calculates area.'''
    
    def __init__(self,radius):
        self.radius = radius
        
    def calc_area(self):
        area = math.pi * (self.radius)**2
        return area
        
    


         