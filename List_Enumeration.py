#List comprehension (output,collection,condtion) prints in one line
"""lst = [1,2,3,4,5,6,7,8,9]

a = [x for x in lst]
print(a)"""

"""lst = [1,2,3,4,5,6,7,8,9]
a = [x+1 for x in lst]
print(a)"""

"""lst = [1,2,3,4,5,6,7,8,9]
c=[x for x in lst if x>4]
print(c)"""


"""lst = [1,2,3,4,5,6,7,8,9]
c=[x for x in lst if x%2 == 0]
print(c)"""

"""lst = [1,2,3,4,5,6,7,8,9]
c=[x for x in lst if x>4 if x%2 == 0]
print(c)"""

#if else is different syntax
lst = [1,2,3,4,5,6,7,8,9]
c=[x if x>4 else "less than 4" for x in lst]
print(c)


