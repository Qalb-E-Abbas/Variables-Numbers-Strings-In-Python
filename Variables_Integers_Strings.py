# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 13:44:43 2021

@author: Qalbe
"""

# Variables in python

rent = 100
gass = 200

total = rent + gass

print(total)

item1 = "apple"
item2 = "banana"

print("Items are:", item1, "and", item2)



#Numbers in python

print(3+3)
print(3-2)
print(3**3)

Islamabad = 100
Pindi = 200

total_distance = Islamabad + Pindi
print(total_distance)

mph = 65
time = total_distance/mph

print(time) #output 4.615384615384615

round(time, 2) #outpt 4.62


10+2*3 #output 16
(10+2)*3 #output  36



6-5.3 #output  0.7000000000000002

round(6-5.3, 2)  #output 0.7



# Strings in python
text = 'hello world'
text #output 'hello'
text[0] #output 'h'

#indexing
text[0:5] #output 'hello'
text[6:11] #output 'world'
text[6:] #output 'world'
text[:5] #output 'hello'


text = "Let's Learn Python"

text #Output "Let's Learn Python"



text = 'hello'
text2 = 'world'

text + text2 #Outoput 'helloworld'
text + ' ' +text2 #Outoput 'hello world'




num = 12
text + num # output TypeError: can only concatenate str (not "int") to str

text+str(num) #output 'hello12'
