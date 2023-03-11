'''
Write a Python program to remove an empty tuple(s) from a list of tuples. 
'''
list1=[(1,2),(3,4),(),(4,5,6),(),(87,90,78)]
for i in list1:
    print(i)
    if(len(i)==0):
        list1.remove(i)
print(list1)
