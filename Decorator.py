"""A decorator is a design pattern that allows user to add new functionality to an existing object without altering its structure
The @ syntax is used to call the decorator on an ininput function
Multiple decorators can be applied to a single function
To craete decorator we need to accept functions as arguments"""


"""def test (func):
    def inner_test():
        print("This is start of my inner test")
        func()
        print("This is end of my inner test")

    return inner_test

@test    #Trying to decorate this function with above function(adding),When trying to decorate it will retain its original quality
def test1():
    print("This is my test1")
print(test1())"""

# Second example is to print start and end time of particular function
# We r trying to use repetitive task in both code

import time
"""def print_list(l):
    start_time = time.time()
    for i in l:
        print(i)
    end_time = time.time()
    total_time = end_time-start_time
    print(total_time)


def print_key(d):
    start_time = time.time()
    print(d.keys())
    end_time = time.time()
    total_time = end_time-start_time
    print(total_time)"""


# Decorator 
def fine_time(func): # external function which will take function as argument
    def cal_time(*args): # internal function which takes argument of a past function ,Pass here also the argumnet because it is a rapper function
        start_time = time.time()
        func(*args)  #If argument is not given it will show error, TypeError: fine_time.<locals>.cal_time() takes 0 positional arguments but 1 was given
        end_time = time.time()
        total_time = end_time-start_time
        print(total_time)

    return cal_time

# After decorating

"""@fine_time
def print_key(d):
    print(d.keys())

print_key({"key":"value","number":"one"})



@fine_time
def print_list(l):
    for i in l:
        print(i)

print(print_list([1,2,3,4]))"""


#Third Example

#Asked u to do logging each and every time so create a separate decorator for logging part

"""import logging

def  log_func(func):
    def log_inner(*args):
        logging.basicConfig(filename = "test.log",level = logging.INFO)
        logging.info("This is start of my function")
        func(*args)
        logging.info("This is end of my function")
    return log_inner

@fine_time
@log_func
def print_list(l):
    for i in l:
        print(i)

print(print_list([1,2,3,4]))"""

# TYPES OF VARIABLE
# Single underscore -- Protected variable , No underscore -- Public, Double underscore -- Private variable

# PROTECTED VARIABLE

"""class sudh:
    def __init__(self,subject):
        self._subject = subject

s1 = sudh("Data Engineering")

print(s1._subject)"""

# PRIVATE VARIABLE

"""class sudh:
    def __init__(self,subject):
        self.__subject = subject

s1 = sudh("Data Engineering")

s1._sudh__subject= "Big Data" # Until u append class name u won't get output in private variable

print(s1._sudh__subject)"""

#INBUILT DECORATOR

class sudh:
    def __init__(self,subject):
        self.__subject = subject

@property

def subject1(self):
    return self.__subject

@subject1.setter
def subject1(self,subject):
    self.__subject = subject

@subject1.getter
def subject1(self):
    return self.__subject

s2 = sudh("Data Analytics")

print(s2.subject1)





    

