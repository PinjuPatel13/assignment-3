'''
Write a Python program to find the highest 3 values in a dictionary 
'''
dict1 = {'A': 67, 'B': 23, 'C': 45,'D': 56, 'E': 12, 'F': 69}
print(dict1)
x=list(dict1.values())
d=dict()
x.sort(reverse=True)
x=x[:3]
for i in x:
	for j in dict1.keys():
		if(dict1[j]==i):
			print(str(j)+" : "+str(dict1[j]))
