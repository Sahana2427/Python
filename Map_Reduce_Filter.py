#Take input as list and add 2 to each element in list

"""l = [5,6,7,89]
l1 =[]
for i in l:
    l1.append(i+2)
print(l1)"""

"""def add_list(l):
    l1 =[]
    for i in l:
        l1.append(i+2)
    print(l1)

add_list({4,5,6,7})"""

#Map using lambda
"""l = [5,6,8]
print(list(map(lambda a : a+2,l)))"""

# Map using function
"""l =[5,6,7,8]
def test(c):
    return c+2

print(list(map(test,l)))

print(test(5))

print(list(map(test,[1,2,3])))"""

# Length of string 

"""l = ["sudh ","sahana"]
l1 =[]
for i in l:
    l1.append(len(i))
print(l1)"""

"""l =["sahanasahana"]"""
"""def len_ofstring(l):
    l1 =[]
    for i in l:
        l1.append(len(i))
    print(l1)

len_ofstring(['sahanasahana'])"""

#Map using lambda

"""l1 = ["sudh","sahana","tom"]

print(list(map(lambda n : len(n), l1)))"""

#Map using Function
"""l1 = ["jerry","shinchan"]
def length(d):
    return len(d)

print(list(map(length,l1)))

print(length("bheem"))"""

#------------------------------------------------------------------------------------------------------------------------------------#

#REDUCE


from functools import reduce
"""l = [5,3,2,1,4]
print(reduce(lambda a,b:a+b,l))
print(reduce(lambda a,b:a if a>b else b,l))
print(reduce(lambda a,b:min(l),l))
print(reduce(lambda a,b:max(l),l))"""

"""n = 4
fact = reduce(lambda a,b:a*b,range(n,n+1))"""

"""n=4
def test (a,b):
    return a*b

fact = reduce(test,range(1,n+1))
print(fact)"""


"""l = [1,2,3,4,5,6]

print(reduce( lambda a,b:a*b,[i for i in l if i%2==0]))"""


#------------------------------------------------------------------------------------------------------------------------------------#

#FILTER

"""l = [1,2,3,4,5,6,7]

print(list(filter(lambda a:a%2==0,l)))
print(list(filter(lambda a:a%2!=0,l)))"""

"""s = "PW console"
print(list(filter(lambda a:a.lower(),s)))"""

l = ["pw","console", "java","jupiter"]
print(list(filter(lambda a:len(a)>4,l)))
print(list(filter(lambda a:a[0]=="p",l)))

#Fibonicii

def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
   

print(fib(7))


# Addition of number from 1 to 100

def sum_till(n):
    if n == 1:
        return 1
    else:
        return n +sum_till(n-1)
    
print(sum_till(5))




