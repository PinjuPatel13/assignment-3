'''
Write a Python program to convert a list of tuples into a dictionary. 
'''
list1=[(1,"23"),(2,"45"),(3,"36"),(4,"18")]
dict_1=dict()
for student,marks in list1:
	dict_1.setdefault(student, []).append(marks)
print(dict_1)
