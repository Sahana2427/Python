"""def add(a,b):
    a=20
    b=40
    print(a+b)"""

"""add(20,40)"""


"""
def fullname(a,b):
    c=a+b
    print(c)

fullname("pw","skills")"""
    
# If u want to store value in some variable use return . In this value will be stored in x

"""def fullname(a,b):
    c=a+b
    return c

x = fullname("pw","skills")
print(x)"""


#None If u don't specify what to return

"""def fullname(a,b):
    c=a+b
    return 

x = fullname("pw","skills")
print(x)
"""

# In this value won't be stored in x
#pwskills
#None
"""def fullname(a,b):
    c=a+b
    print (c)

x = fullname("pw","skills")
print(x)"""

#Simple calculator using function

"""def calc(a,b):
    sum = a+b
    sub=a-b
    mul = a*b
    div=a/b
    return sum,sub,mul,div

x = calc(2,4)
print(x)"""

"""def calc():
    a = int(input("enter a")) 
    b = int(input("enter b"))
    sum = a+b
    sub=a-b
    mul = a*b
    div=a//b
    return sum,sub,mul,div

x = calc()
print(x)"""

# Area of rectangle

"""def areaofrectangle(a,b):
    area = a*b
    print(area)

areaofrectangle(2,4)"""

"""def areaoftriangle(a,b):
     return 0.5*a*b

x=areaoftriangle(2,2)
print(x)"""
    



#Print the first 5 positive integers in ascending order with one number in each line

"""def numbers():
    for i in range(1,6):
        print(i)

numbers()"""

# Accept integer as an input and pritn sqaure as an output


"""def sqaure():
    integ = int(input("Enter an number"))
    print(integ*integ)

sqaure()
"""

# Accept two integers as input and print their sum as output

"""def sum():
    a = int(input("Enter first number"))
    b= int(input("Enter second number"))
    c = a+b
    print("The sum of two numbers : " ,c)

sum()"""


#Accept two words as input and print the two words after adding a space between them

"""def fullname(first,second):
    print(first + " " + second)

fullname("Tom","Jerry")"""

#To accept limit and print even numbers

"""def even_no():
    limit1 = int(input("Enter first limit"))
    limit2 = int(input("Enter second limit"))
    for i in range(limit1,limit2+1):
        if i%2 == 0:
            print(i)

even_no()"""


# global and local variable

"""y= 10""" # global variable
"""
def globalvar():
    x = 20 # local variable
    print(x)
    print(y)

globalvar()"""

#print(x)
# local var can't be used outside function -- print(x)



# Function Arguments

#Positional Argument
# A positional argument is a variable , value or object that is passed to a function in specific order based on function's argument

"""def add_numbers(a,b):
    sum = a+b
    print("sum",sum)

add_numbers(2,4)"""

# Default argument
# If user does not give value it will take default value

"""def add_numbers(a=4,b=5):
    sum = a+b
    print("sum",sum)

add_numbers(5,5)

def emp(name="sahana"):
    print(name)

emp("tom")"""


# Keyword Argument
# Uses parameter name to assign value to a function or method rather than arguments order
"""def display_info(first_name,last_name):
    print(first_name,last_name)

display_info(first_name="sahana",last_name="saraswathi")"""


# *args and **kargs

#*args Can pass variable length argument

"""def find_sum(*numbers):
    result = 0
    for num in numbers:
        result = result + num
    print(result)

find_sum(1,2,3,4,5)"""



#**args

"""def intro(**data):
    print("Data type of argument",data)

    for key,value in data.items():
        print(key,value)

intro(firstname="Tom",lastname="Jerry")"""


# Double star Another example can pass n number of keyword arguments (key,value)
"""
def simple(**x):
    print(x)

simple(name="imran",age=40,subject="kannada")"""

# Single * ouput is tupple (just arguments)
"""def simple(*y):
    print(y)

simple(1,2,3,4)"""

#observer here if u dont give keyword it will show error so always give in keywork argument for
"""def simple1(**y):
    print(y)

simple1(1,2,3,4)"""


"""dict = {"id":1, "name":"sahana", "grade": "a"}

print(dict.values())
print(dict.keys())"""


"""def showkeyvalue(**kwargs):
    print(kwargs)


showkeyvalue(x=2,u=5)"""

# LAMBDA FUNCTION -- Function without its name

# lambda arguments : function body
#print function call

"""x = lambda : print("hello world")

x()"""

"""add_number = lambda a,b : a+b

print(add_number(2,3))"""

"""mul_num = lambda a,b : a*b
print("Multiplication of two number is :", end =" ")
print(mul_num(2,2))"""

"""a = int(input("Enter first number"))
b = int(input("Enter second number"))

sqaure = lambda a,b:(a**2,b**2)
print(sqaure(a,b))"""

"""x = lambda n : "It is even" if n%2 ==0 else "It is odd"

print(x(3))"""

"""greatest= lambda a,b:a if a>b else b
print(greatest(2,3))"""


products = [
    {"name": "product1","price":50},
    {"name": "product2","price":40},
    {"name": "product3","price":30},
    {"name": "product4","price":80}
]

#sorted

"""sorted_products = sorted(products,key = lambda x:x["price"])

for i in sorted_products:
    print(i)"""


# Write a labda expression that accepts a character as argument and return true if its vowel or false

"""char = input("Enter a character:")

vowel = lambda char: "Vowel" if char in ("a" or "e" or "i" or "o" or "u") else "Not vowel"

print(vowel(char))"""

"""def test(*args):
    return(args)

print(test(1,2,3,4,"sudh"))"""


"""def test(**args):
    return args

print(test(a=4,b=5,name="sahana"))"""

"""def practice(a=10,b=15):
    c = a+b
    return c

print(practice(2,4))"""

# LAMBDA variable = lambda arguments : condition

"""m = lambda a,b : a+b

print(m(2,8))

print(m)"""

"""def even(m):
    if m%2 == 0:
        return("even")
    else:
        return("odd")

print(even(24))"""

"""y = lambda m :"even" if m%2==0 else "odd"

print(y(78))"""

"""upper_case=lambda s : s.upper()
print(upper_case("sahana"))"""

"""l = [1,2,3,4,5,6,7]

def sum_odd(l):
    l1 = []
    for i in l:
        if i%2!=0:
            l1.append(i)
    return sum(l1)
            
print(sum_odd(l))"""

# lambda function one line code to return odd numbers from list
"""l = [1,2,3,4,5,6,7]
print(sum([i for i in l if i%2!=0]))"""


# Program to find factorial of a number

"""def fact(n):
    if n == 0:
        return 1
    else :
        return n*fact(n-1)  #recursive function
    
print(fact(4))"""

# using for loop 
"""factorial = 1
num = 4
for i in range(1,num+1):
    factorial = factorial *i
print(factorial)

def fact(n):
    a = 1
    for i in range(1,n+1):
        a = a*i
    return a

print(fact(4))  """

"""fact = lambda n: 1 if n == 0 else n*fact(n-1)

    
print(fact(4))"""

