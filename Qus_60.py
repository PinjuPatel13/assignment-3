'''
Write a Python program to calculate the area of a trapezoid .
'''


def Area(b1, b2, h):
	return ((b1 + b2) / 2) * h


base1 = 10; base2 = 15; height = 8
area = Area(base1, base2, height)
print("Area is:", area)
