'''
write a Python function that checks whether a passed string is 
palindrome or not
'''
def palindom(x):
    if x==x[::-1]:
        print("palindom")
    else:
        print("not a palindom")

palindom("Hello")