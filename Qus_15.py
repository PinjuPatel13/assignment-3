'''
Write a Python program to get unique values from a list 

'''
list=[]
list1=[23,34,23,1,45,56,67,67,54,34,23,67,2,3,4,4,3,2,1]
for i in list1:
    if i not in list: 
        list.append(i)
print(list)



