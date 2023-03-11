'''
write a Python function that takes a list and returns a new list with unique 
elements of the first list.
'''
list=[]
list1=[1,2,3,4,5,6,5,4,3]
for i in list1:
    if i not in list:
            list.append(i)
for i in list:
       print (i)
print(list1)

