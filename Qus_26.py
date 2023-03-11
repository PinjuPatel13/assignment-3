'''
Write a Python program to replace last value of tuples in a list. 
'''

list1= [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
for tup1 in list1:
    print(tup1[:-1] + (1,))
