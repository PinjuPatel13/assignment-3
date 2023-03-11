'''
Write a Python program to count the number of strings where the string 
length is 2 or more and the first and last character are same from a given 
list of strings.
'''

list1=["hello",23,45.6,"PYTHON",23,2,3,2,4,3,45.6,2,2,"hello"]
print(list1.count("hello"))
a=(len(list1))
print(a)
if  a>=2:
     b= list1[0]==list1[-1]
print(b)
