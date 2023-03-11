'''
How will you create a dictionary using tuples in python? 
'''
tup1= ((24, "bobby"), (21, "ojsawi"))
final = dict((key,value) for key, value in tup1)
print(final)


