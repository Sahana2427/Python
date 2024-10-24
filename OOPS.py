# Self is not a keyword it can be anything. It is instance of a class. Created as reference to that class


class bankaccount:

    def openaccount(self,name,email_id):
        print("open an account by taking name and email_id ")
        return name+email_id
    
    def deposit(self,deposit_amount):
        print("I am trying to deposit amount")
    

    def withdraw(self,withdraw_amount):
        print("I am trying to withdraw amount")

    def update_details(self,name_update,email_update):
        print("I am trying to update my mail id and name")


def openaccount(self,name,email_id):
        print("open an account by taking name and email_id ")
        return name+email_id


print((openaccount(1,"Sahana","sahanasahana24@gmail.com")))

# Assign class to a variable(class variable or object of classes or instance of classes)


sudh = bankaccount()

print(sudh.openaccount("tom","tom@1234"))

#Init Function is an Inbuilt function is used to initialise my class variable(object) with some data


####################################################################################################################################


class list_ops:
     
     a = 10

     def __init__(self,a):
          self.a1 = a    # if u change a1 to a2 or any other thing it will show error ALSO CALLED CONSTRUCTOR
          self.a2 = "sudh"
          self.a3 = a
         
     def extractfromindex(self,l,index):
          return l[index]
     
     def extractrangedata(self,l,start,end):
          return l[start:end]
     

     def extracteven(self,l):
          l1=[]
          for i in l:
               if i%2 ==0:
                    l1.append(i)
          return l1
     


first_obj =list_ops # Class variable
print(first_obj.extractfromindex(1,[1,2,3,4,5,6],4))
print(first_obj.extracteven(1,[1,2,3,4,5,6]))
print(first_obj.extractrangedata(1,[1,2,3,4,5,6,7],0,3))
print(first_obj.a) # Accessing variable inside class
     
# You can create any number of objects for a class but u will get same a value

third_object = list_ops
print(third_object.a)


# Init

#second_obj = list_ops #Execute only this it will show error

second_obj = list_ops([1,2,3,4,5])
print(second_obj.a1) 
print(second_obj.a2) #To access a2(hardcode)
second_obj = list_ops([1,2,3,4,5,6]) #a3
print(second_obj.a3)


# Kind of method by which we will be able to provide data to your classs for different objects init is basically a constructor method
     

