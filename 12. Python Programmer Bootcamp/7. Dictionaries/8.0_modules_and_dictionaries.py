# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

#import math
#
##https://docs.python.org/3/library/math.html#module-math
#
#
#print(math.pi)
##
#print(math.cos(0))
##
#import random
#
#print(randint(1,100))
#

#print(random.randint(1,100))

# https://docs.python.org/3/library/random.html

#for i in range(100):
#    print(random.randint(1,100),end=' ')
#    
#import webbrowser
##
#webbrowser.open('https://docs.python.org/3/library/webbrowser.html') 



## Dictionaries

capitals = {'France':'Paris','Spain':'Madrid','United Kingdom':'London',
            'India':'New Delhi','United States':'Washington DC','Italy':'Rome',
            'Denmark':'Copenhagen','Germany':'Berlin','Greece':'Athens',
            'Bulgaria':'Sofia','Ireland':'Dublin','Mexico':'Mexico City'
            }

#capitals['Germany']
#capitals.get('Germany')
#
#capitals['South Korea'] = 'Seoul'
#
#print(capitals)
#
#capitals.items()
#print()
#
#print(capitals.items())
#
##for country in capitals:
##    print(country)
###    
#for country, city in capitals.items():
#    print(f'The capital of {country}, is {city}')    
#    
#print()    
##
#print(capitals.keys())
##
#print()
#print(capitals.values())
#
#
#if 'France' in capitals:
#    print('It contains France')
#        
#L = [1,2,3,4,5]
#
#print(7 in L)

sherlock = '''
Mr. Sherlock Holmes, who was usually very late in the mornings, save upon those not infrequent occasions when he was up all night, was seated at the breakfast table. I stood upon the hearth-rug and picked up the stick which our visitor had left behind him the night before. It was a fine, thick piece of wood, bulbous-headed, of the sort which is known as a “Penang lawyer.” Just under the head was a broad silver band nearly an inch across. “To James Mortimer, M.R.C.S., from his friends of the C.C.H.,” was engraved upon it, with the date “1884.” It was just such a stick as the old-fashioned family practitioner used to carry—dignified, solid, and reassuring.

“Well, Watson, what do you make of it?”

Holmes was sitting with his back to me, and I had given him no sign of my occupation.

“How did you know what I was doing? I believe you have eyes in the back of your head.”

“I have, at least, a well-polished, silver-plated coffee-pot in front of me,” said he. “But, tell me, Watson, what do you make of our visitor’s stick? Since we have been so unfortunate as to miss him and have no notion of his errand, this accidental souvenir becomes of importance. Let me hear you reconstruct the man by an examination of it.”

“I think,” said I, following as far as I could the methods of my companion, “that Dr. Mortimer is a successful, elderly medical man, well-esteemed since those who know him give him this mark of their appreciation.”

“Good!” said Holmes. “Excellent!”

“I think also that the probability is in favour of his being a country practitioner who does a great deal of his visiting on foot.”

“Why so?”

“Because this stick, though originally a very handsome one has been so knocked about that I can hardly imagine a town practitioner carrying it. The thick-iron ferrule is worn down, so it is evident that he has done a great amount of walking with it.”

“Perfectly sound!” said Holmes.

“And then again, there is the ‘friends of the C.C.H.’ I should guess that to be the Something Hunt, the local hunt to whose members he has possibly given some surgical assistance, and which has made him a small presentation in return.”

“Really, Watson, you excel yourself,” said Holmes, pushing back his chair and lighting a cigarette. “I am bound to say that in all the accounts which you have been so good as to give of my own small achievements you have habitually underrated your own abilities. It may be that you are not yourself luminous, but you are a conductor of light. Some people without possessing genius have a remarkable power of stimulating it. I confess, my dear fellow, that I am very much in your debt.”

He had never said as much before, and I must admit that his words gave me keen pleasure, for I had often been piqued by his indifference to my admiration and to the attempts which I had made to give publicity to his methods. I was proud, too, to think that I had so far mastered his system as to apply it in a way which earned his approval. He now took the stick from my hands and examined it for a few minutes with his naked eyes. Then with an expression of interest he laid down his cigarette, and carrying the cane to the window, he looked over it again with a convex lens.
'''

#letter_count = {}
#for letter in sherlock:
#    letter_count[letter.lower()] = letter_count.get(letter,0) + 1
#
#
##    
#print(letter_count)    
##    
#import matplotlib.pyplot as plt
##
#
#
#x,y = zip(*letter_count.items())
##
#plt.bar(x,y)
#plt.show()
##
#letter_count_clean = {}
#
#for k,v in letter_count.items():
#    if k.isalpha():
#        letter_count_clean[k] = v
#        
#print(letter_count_clean)     
#
#x,y = zip(*letter_count_clean.items())
#
#plt.bar(x,y) 
#plt.show()   
#
#
#
#my_list_1 = [1,2,3,4]
#my_list_2 = ['a','b','c','d']
#
#joined = list(zip(my_list_1,my_list_2))
#print(f'The result of the zip function is {joined} it is of type {type(joined)}')
#
#i,j = zip(*joined)

#print(capitals.items())
#print()
#x,y = zip(*capitals.items())


#new_words = sherlock.split(' ')
#
#print(new_words)
#
#'Sherlock' in new_words

#for i in range(len(new_words)):
#    new_words[i] = new_words[i].strip('\n')
##    
#print(new_words)

### Tuples

#my_tuple = (1,2,3,4)
#my_list = [5,6,7,8]
#my_string = 'Australia'
#
#my_tuple[0]
#my_tuple[:3]
#
#my_list[0] = 1000
#my_tuple[0] = 2000
#my_string[4] = 'q'
#
### Summary
#
## Lists are mutable
## Dictionaries are mutable
## Tuples are immutable
## Strings are immutable


### Another Dimension

#my_list = [[1,2,3],[4,5,6],[7,8,9]]

#my_list[0]
#my_list[1]
#my_list[2]
#
#my_list[1][1]


#countries = {'France':{'Capital':'Paris','Language':'French'},'Spain':{'Capital':'Madrid','Language':'Spanish'},
#             'United Kingdom':{'Capital':'London','Language':'English'},
#            'United States':{'Capital':'Washington DC','Language':'English'},
#            'Italy':{'Capital':'Rome','Language':'Italian'}
#            }
##
##
##countries['France']
##
#for key, value in countries.items():
#    print(key,value) 
#
#print()
#for key, value in countries.items():
#    print(f'{value["Capital"]} is the capital of {key}, they speak {value["Language"]}.')


from collections import Counter

print(Counter(sherlock.lower()))

new_dict = dict(Counter(sherlock.lower()))
#
new_dict = {k:v for k,v in new_dict.items() if k.isalpha()}
#
print(new_dict)

L = [x**2 for x in range(1,11)]

M = []
for x in range(1,11):
    M.append(x**2)
    
    