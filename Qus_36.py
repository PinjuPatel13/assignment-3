'''
How Do You Check The Presence Of A Key In A Dictionary? 
'''
dict={'a':"HELLO",'b':"PYTHON",'c':23,'r':45,'p':48}
key='i'
x = list(dict.keys())
result = "Not Present"
if(x.count(key) == 1):
	result = "Present"
print(result)
