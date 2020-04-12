# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 09:35:23 2019

@author: giles
"""

#Everything in python is an object!

#x = 1
#
##help(x)
##dir(x)
##
#y = [1,2,3]
##help(y)
##dir(y)
##
#z = {'a':1}
#help(z)
#dir(z)


# Objects combine functions with data. Think of a list

# Class is the blue print of an object 

# Inside the class there are attributes, which are the variables for that class

#class Patient(object):
#     ''' Medical centre patient'''
#     pass
     

#class variables and instance variables:
   
#class Patient(object):
#     ''' Medical centre patient'''
#     
#     def __init__(self,name,age):
#         
#         self.name = name
#         self.age = age
#     
#steve = Patient('Steven Hughes',48)
#abigail = Patient('Abigail Sandwick',32)

#class Patient(object):
#     ''' Medical centre patient'''
#     
#     status = 'patient'
#     
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
##     
##
#steve = Patient('Steven Hughes',48)
#abigail = Patient('Abigail Sandwick',32)
#
#   
#
#class Patient(object):
#     ''' Medical centre patient'''
#     
#     status = 'patient'
#     
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         
#         
#     def get_details(self):
#         print(f'Patient record: {self.name}, {self.age} years.')
#
#steve = Patient('Steven Hughes',48)
#abigail = Patient('Abigail Sandwick',32)


class Patient(object):
     ''' Medical centre patient'''
     
     status = 'patient'
     
     def __init__(self,name,age):
         self.name = name
         self.age = age
         self.conditions = []
         
     def get_details(self):
         print(f'Patient record: {self.name}, {self.age} years.' \
               f' Current information: {self.conditions}.')
         
     def add_info(self,information):
         self.conditions.append(information)
#     
#
#steve = Patient('Steven Hughes',48)
#abigail = Patient('Abigail Sandwick',32)

class Infant(Patient):
    ''' Patient under 2 years'''
    
    def __init__(self,name,age):
        self.vaccinations = []
        super().__init__(name,age)
        
    def add_vac(self,vaccine):
        self.vaccinations.append(vaccine)
        
    def get_details(self):
         print(f'Patient record: {self.name}, {self.age} years.' \
               f' Patient has had {self.vaccinations} vaccines.' \
               f' Current information: {self.conditions}.' \
               f'\n{self.name} IS AN INFANT, HAS HE HAD ALL HIS CHECKS?')
        
#archie = Infant('Archie Fittleworth',0)        
#archie.add_vac('MMR') 
         
class Patient(object):
     ''' 
         Attributes
         ----------
         name: Patient name
         age: Patient age
         conditions: Existing medical conditions
     '''
     
     status = 'patient'
     
     def __init__(self,name,age):
         self.name = name
         self.age = age
         self.conditions = []
         
     def get_details(self):
         print(f'Patient record: {self.name}, {self.age} years.' \
               f' Current information: {self.conditions}.')
         
     def add_info(self,information):
         self.conditions.append(information)
         
         
         
         
         
         