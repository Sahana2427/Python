"""l =[1,2,3,4,7,0]
l1=[]
def even_parse(l):
    try:
        for i in l:
            if i%2==0:
                l1.append(i)
        return l1
    except Exception as e:
        print(e)
        pass
    print("Print something")
print(even_parse(5))"""

    
    
#print(even_parse("sudhl")) -- Throws error

#print(even_parse(l)) -- prints even number

"""try :
    a = int(input("Enter a value for a :"))
    b = int(input("Enter a value for b :"))
    c = a/b
    print(c)
except:
    pass
print("Print something")"""

# Shows output as division by zero 
"""try:
    c = 6/0
except Exception as e:
    print(e)"""

# Shows error as division by zero
"""a = 10
b = 0
print(a/b)"""

# Subclasses of Exception 
"""try:
    a = int(input("Enter a"))
    b= int(input("Enter b"))
    c=a/b
except TypeError as t:
    print(t)
except ZeroDivisionError as z:
    print(z)
except ValueError as v:
    print(v)"""

# Nested try

"""try:
    x=5/0
except ZeroDivisionError as z:
    print(z)
    try:
        y = int("sudh")
    except ValueError as v:
        print(v)"""

# On successs of try else will execute and finally will be executed always

"""try:
    x = 5/0
except ZeroDivisionError as z:
    print(z)
else :
    print('This will execute itself once try will execute without any error')
finally:
    print('This will execute always')

try:
    x = 5/2
except ZeroDivisionError as z:
    print(z)
else :
    print('This will execute itself once try will execute without any error')
finally:
    print('This will execute always')"""

# Dictionary example
"""try:
    d = {"name":"sahana","mobile_no":23454,"email_id":"sudh"}
    print(d["course"])
except Exception as e:
    print (e)
    print("This is a keyword")"""


"""try:
    d = {"name":"sahana","mobile_no":23454,"email_id":"sudh"}
    print(d["course"])
except :
    pass
    print("This is a keyword")"""

# List in exception handling
"""try:
    l =[1,2,3,4,5]
    print(l[10])
except Exception as e:
    print(e)"""


#Scripting



#Python scripting commands
import os
"""pwd = os.getcwd()
print("Cureent working directory",pwd)"""


"""ls = os.listdir()
print("List of files and folders",ls)"""

#Remove spaces in file or folder name ,use double forward slash or single backward slash
import os
"""path ="C:\\"
ls = os.listdir(path)
print("List of files and folders",ls)"""

#Exception in no such file or directory

#without exception throws error

"""file ="C:\\"
f = open(file)
f.read()"""

#With exception
"""try:
    file ="C:\\"
    f = open(file)
    f.read()
except Exception as e:
    print(e)"""


#Change directory
"""os.chdir("C:\\GIt_practice")

pwd = os.getcwd()
print("Current working directory",pwd)"""

"""open("C:\GIt_practice\test1.txt")"""

#Types of using exception
#Multiple classes of error in same line

#1
"""try:
    n = int(input("enter n:"))
    div = 342/n
    print(div)
except (ValueError, ZeroDivisionError):
    print("User has entered invalid input or may ne zero")"""

#2
"""try:
    n = int(input("enter n:"))
    div = 342/n
    print(div)
except Exception :
    print("User has entered invalid input or may ne zero")
"""
#3
"""try:
    try:
        n = int(input("enter n:"))
        div = 342/n
        print(div)
    except Exception :
        print("User has entered invalid input or may be zero")
except Exception:
    print("User has entered invalid input or may be zero")"""


# Open & Close the file

f = open("C://GIT_practice//test1.txt")
f.read()
f.close()


# To raise exception

try:
    age = int(input("Enter age:"))
    if age<20:
        raise ValueError("Entered age is not applicable")
except ValueError as v:
    print(v)












    










