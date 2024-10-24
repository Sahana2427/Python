
#Factorial

"""def fact(n):
    if n==0:
        return 1
    else :
        return n*fact(n-1)
    
print(fact(4))"""

# Fib

"""def fib(m):
    if m<=1:
        return m
    else:
        return fib(m-2)+ fib(m-1)
    
print(fib(5))"""


# Sum of all digits using while loop

"""def sum_of_digits(n):
    sum =0
    while n!=0:
        d =n%10
        sum = sum+d
        n = n//10
    return sum

print(sum_of_digits(123))"""


# Sum of all digits using for loop

"""def get_sum(n):

    sum =0
    for digit in str(n):
        sum = sum + int(digit)
    return sum

print(get_sum(123))"""

# Sum of all digits Using recursion

"""def sum_digit(n):
    if n<=9:
        return n
    else:
        return n %10 + sum_digit(n//10)
    
print(sum_digit(345))"""

# Max element in given list

"""l =[1,2,3,4]
print(max(l))"""

# Max element in list using recursion

"""def max_find(l):
    if len(l)==1:
        return l[0]
    else:
        return max(l[0],max_find(l[1:]))
    
print(max_find([4,90,87,5,7]))"""

#Power of number by recursive method

"""print(pow(5,5))

def power(n,k):
    if k == 0:
        return 1
    else:
        return n * power(n,k-1)
    
print(power(2,4))"""

# Find length of entire string

"""def find_len(s):
    if s=='':
        return 0
    else:
        return 1 +find_len(s[1:])
    
print(find_len("jerry"))"""

# Reverse of a string

"""s1 = "sinchan"

print(s1[::-1])"""

"""def find_rev(s1):
    if s1 =="":
        return ""
    else:
        return find_rev(s1[1:])+s1[0]
    
print(find_rev("jerry"))"""

#Number of occurences of character

"""s ="jerry"
def find_char_count(s,c):
    if s =="":
        return 0
    elif s[0] == c:
        return 1 + find_char_count(s[1:],c)
    else:
        return find_char_count(s[1:],c)
        

print(find_char_count(s,"r"))"""

# Sorting the list and return true if its sorted

"""l =[1,2,3,4,5]
def chech_sort_list(l):
    if len(l)<=1:
        return True
    elif l[0]>=l[1]:
        return False
    else:
        return chech_sort_list(l[1:])
    
print(chech_sort_list(l))"""

#Perfect square or not

"""def check_sqaure(n,start=1):
    if n == start**2:
        return True
    elif n < start **2:
        return False
    else:
        return check_sqaure(n,start+1)

print(check_sqaure(4))"""

# Iterator And Next

"""Iterator is an object that contains a countable number of values meaning you can traverse all the values
"""

"""str = "jerry"
itr = iter(str)
print(next(itr))"""

"""str = iter("jerry")
print(next(str))
print(next(str))
print(next(str))
print(next(str))
print(next(str))

print(iter([1,2,3,4]))"""

"""l = iter(range(0,5))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))"""





    







