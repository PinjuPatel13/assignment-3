'''
Write a Python function that takes two lists and returns true if they have 
at least one common member
'''
list1=[1,2,3,4]
list2=[11,21,23,24]

result=False
for i in list1:
    for n in list2:
        if i==n:
            result=True
        
print(result)

