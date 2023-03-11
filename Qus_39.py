'''
Write a Python script to merge two Python dictionaries .
'''
def Merge(dict1, dict2):
	return(dict1.update(dict2))

dict1 = {'a': 1, 'b': 2}
dict2 = {'d': 4, 'c': 3}
print(Merge(dict1, dict2))


print(dict1)
