class test:
    def __init__(self):
        self.__x = "sudh"  # Private variable
        self.y ="kumar" # Public variable
        self.z = "punya" # Public variable

    def __test_math (self):
        return "This is just a test"
    
    # To give access to private variable use below, User will not know there is x but they should be able to access it

    def access_var(self):
        return self.__x
    

    # To update value of x

    def update_var(self,data):
        self.__x = data



t1 = test()
#print(t1.__x) # Cannot access x variable
print(t1.access_var()) # User will not be able to see x but (access_var) they can access function name and value of variable

print(t1._test__x) #  Private variable can be accessed only using _class name
print(t1._test__test_math()) #  Private variable can be accessed only using _class name

print("---------------------------------------------------------------------------------------------------------------------------")

t1.update_var(10)
print(t1.access_var())

print("---------------------------------------------------------------------------------------------------------------------------")

print(t1.y) # When you type print(t1.) -- Only y and z will be shown in autofill because z and y are public variable while x is private variable



                                              # More Example

# Going to bank and deposit amount there is an update , delay or withdraw there is an update

class bank:

    def __init__(self,account_no,balance):
        self._account_no = account_no
        self.__balance = balance

    def check_balance(self,password):
        if password == "mysecurepass":
            return self.__balance
        else:
            return "Incorrect password"
        
sudh = bank(12, 500)
print(sudh.check_balance("mysec"))



# Another example

class queue:
    def __init__(self):
        self._queue = []

    def enqueue(self,data):
        self._queue.append(data)

    def dequeue(self):
        if self._queue :
            return self._queue.pop(0)
        else:
            print("It's empty")

    def showdata(self):
        return self._queue

q = queue()
print(q.dequeue())

q.enqueue(40)

print(q.showdata())





