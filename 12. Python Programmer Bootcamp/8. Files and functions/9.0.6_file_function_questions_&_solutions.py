# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 15:15:24 2019

@author: giles
"""

# Exercises

'''
#Question 1
#Create a function that will calculate the sum of two numbers. Call it sum_two.
#'''
#
#def sum_two(a,b):
#    ''' This function returns the sum of two numbers. '''
#    
#    return a + b
##
#print(f'The sum of 3 and 4 is {sum_two(3,4)}' )
#
'''
Question 2
Write a function that performs multiplication of two arguments. By default the 
function should multiply the first argument by 2. Call it multiply.
'''

#def multiply(a,b=2):
#    
#    '''
#    Returns the product of a and b; if b not given 
#    returns 2 * a.
#    '''
#    
#    return a * b
##
#print(f'Inputting 3 gives {multiply(3)}')
#print(f'Inputting 3 and 5 gives {multiply(3,5)}')
#
#
#
'''
#Question 3
#Write a function to calculate a to the power of b. If b is not given
#its default value should be 2. Call it power.
#'''
#
#def power(a,b=2):
#    '''
#    Returns a**b; if b not given,
#    it will return a**2
#    '''
#    return a ** b
#
#print(f'Inputting 8 gives {power(8)}')
#print(f'Inputting 2 and 8 gives {power(2,8)}')

'''
##Question 4
##Create a new file called capitals.txt , store the names of five capital cities
##in the file on the same line.
##'''
#file = open('capitals.txt','w')
#file.write('London, ')
#file.write('Paris, ')
#file.write('Madrid, ')
#file.write('Lisbon, ')
#file.write('Rome,')
#file.close()


'''
#Question 5 
#Write some code that requests the user to input another capital city.
#Add that city to the list of cities in capitals. Then print the file to
#the screen.
#'''
#user_input = input('Plese enter a capital city:> ')
#
#file = open('capitals.txt','a')
#file.write('\n' + user_input)
#file.close
#
#file = open('capitals.txt','r')
#print(file.read())
#file.close

'''
Question 6
Write a function that will copy the contents of one file to a new file.
'''
def copy_file(infile,outfile):
    ''' Copies the contents of infile to a new file, outfile.'''

    with open(infile) as file_1:
        with open(outfile, "w") as file_2:
            file_2.write(file_1.read()) 



copy_file('capitals.txt','new_capitals.txt')













