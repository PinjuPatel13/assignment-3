'''
How can you pick a random item from a list or tuple? 
'''

'''
Random.choice()
We can use the random.choice () function if we want to select a random item from a list, tuple, or string.
'''
import random
list1=[1,2,3,5,667,879,64,6,43,27,7]
x=random.choice(list1)
print(x)
tup1=("abc",23,45,67)
y=random.choice(tup1)
print(y)