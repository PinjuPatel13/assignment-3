'''
Write a Python program to check multiple keys exists in a dictionary 
'''

dict1={'a':"HELLO",'b':"PYTHON",'c':23,'r':45,'p':48}
s1 = set(['a', 'c'])
s2 = set(['b', 'q'])

print(s1.issubset(dict1.keys()))
print(s2.issubset(dict1.keys()))
