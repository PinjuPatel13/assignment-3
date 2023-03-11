'''
 Differentiate between append () and extend () methods? 
'''
list1=[2,4,5,6,8,12,333]
list1.append(67)
print(list1)

list1=[2,4,5,6,8,12,333]
list1.extend(range(1,11,3))
print(list1)
