'''
write a Python script to concatenate following dictionaries to create a new one.
'''

dic1={1:"C", 2:"JAVA"}
dic2={3:"PYTHON", 4:"HELLO"}
dic3={5:50,6:60}
dic4 = {}
for i in (dic1, dic2, dic3):
     dic4.update(i)
print(dic4)