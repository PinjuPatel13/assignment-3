'''
Write a Python program to check whether a list contains a sub list 
'''
list1=[2,3,4,5,6,7]
list2=[2,3,4]


result=False
for i in range(len(list1)-len(list2) + 1):
        if list1[i:i+len(list2)]==list2:
            result=True        
print(result)

