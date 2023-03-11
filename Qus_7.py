'''
 Write a Python program to remove duplicates from a list. 
'''

set1=set()
list1=[1,2,3,2,1,3,4,5,4,5,6,7,8,5,6,7,87,87,9,10,3,8,10]
for i in list1:
    if list1.count(i)>1:
        set1.add(i)
print(set1)

        


