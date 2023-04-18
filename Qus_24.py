'''

Write a Python program to convert a list to a tuple. 
'''

def convert(list):
	return tuple(i for i in list)


list = [1, 2, 3, 4,"Hello"]
print(convert(list))



