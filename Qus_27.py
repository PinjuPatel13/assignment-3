'''
Write a Python program to find the repeated items of a tuple. 
'''
result=False
#tup1=(12,23,23,12,34,34,54,45,54,6,7,8,9)
tup1=(1,2,3,4)
for i in tup1:
    if  tup1.count(i)>1:
        result=True
        
print(result)
