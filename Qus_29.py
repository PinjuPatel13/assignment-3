'''
Write a Python program to unzip a list of tuples into individual lists. 
'''


list = [('Bhautik', 1), ('Bro', 2), ('is', 3), ('Placed', 4)]
print(list)
a= [[i for i,j in list],
     [j for i,j in list]]
print(a)

