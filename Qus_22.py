'''
Write a Python program to check whether an element exists within a 
tuple.
'''
tup1=(1,2,3,4,5)
N=5
result = False
for ele in tup1:
    if N == ele:
        result = True
print(result)