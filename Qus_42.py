'''
Write a Python program to print all unique values in a dictionary. 
'''
dict1=[{1:"HELLO"},{2:"PYTHON"},{3:56}]
print(dict1)

result=[]
for i in dict1:
	result.extend(list(i.values()))
result=list(set(result))
print(result)
