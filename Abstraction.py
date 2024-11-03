# Creation of outline/interfaces or skeleton is called abstraction


"""class cartoon:
    def cartoon_details(self):
        return "This will give list of cartoon details"
    
t1 = cartoon()
print(t1.cartoon_details())"""

# To create abstract class inside python we have another class/package by which we can create abstract class
#Creating class label diagram

"""from abc import ABC,abstractmethod #To achieve abstraction 
class skills(ABC): #If u remove ABC  and abstract method decorator u won't get error 

    #To keep that as abstract method(who can call it)

    #@abstractmethod
    def databaseconnect(self):
        pass

    #@abstractmethod
    def checkuserenrollment(self,user_mail_id):
        pass
    
    #@abstractmethod
    def check_completed_lecture(self,user_id,class_id): # You should implement all one by one or else u will get error, 
        #You ca comment @abstract in all methods u won't get error
        pass
    
    #@abstractmethod
    def check_lab_uses(self,user_id):
        pass
    
    #@abstractmethod
    def check_internship(self,user_id):
        pass


class databaseconnect(skills): #Someone who is writing databaseconnect should inherit skills 
    def databaseconnect(self):
        print('This is first method')


db1 = databaseconnect()
db1.databaseconnect()
db1.databaseconnect()"""


# ANOTHER EXAMPLE 

class calculation:

    @staticmethod
    def add(x,y):
        return x+y
    
    @staticmethod # Notification to say that method directly belongs to class (we r not using object/self to call method)
    def sub(x,y):
        return x-y
    
    def div(self,x,y):
        return x/y
    
    


"""a = calculation()
print(a.add(3,4))"""

#or 

print(calculation.add(3,4))

"""b = calculation()
print(b.div(4,2))"""

print(calculation.div(4,4,2)) #when ur not using object to call u should give slef value also


# Without calling or creating object u should be able to create method

#In simple u need to create class based method


class cal(calculation):
    pass

c1 = cal()
print(c1.add(3,4))


print(cal.add(32,2))


#   ANOTHER EXAMPLE

class file_ops:
    def __init__(self,filename):
        self.filename = filename
    
    def read_file(self):
        with open(self.filename,'r') as file:
            return file.read()
    

    def write_file(self,data):
        with open(self.filename,'w') as file:
            file.write(data)


sudh_op_file = file_ops('sudhfile.txt')
sudh_op_file.write_file("fsfdhasghjghgjhjhjh")