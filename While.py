"""a = 100

while a>=1:
    print(a)
    a = a-1"""


"""a = 1
while a<=100:
    print(a,end=" ")
    a = a+1"""

"""sum = 0
n = 1
t = 5
while n <=t:
    sum = sum + n
    n = n-1
print(sum)"""

#Multiplication

"""print("hello world")"""

"""n = int(input("Enter number"))
i = 1

while i<=10:
    print(n,"*",i,"=",n*i)
    i=i+1"""

# Time sleep for 1 second


"""import time
s = 50
while s>0:
    print(s)
    time.sleep(1)
    s=s-1
print("Break time is over")"""

# Vendor Machine

"""money_in_hand = 20

while money_in_hand>=5:
    print(money_in_hand)
    choice = int(input("Enter your choice(1.biscuit,2.chips,3,redbull,4.coke)"))
    if choice == 1:
        print("take your biscuit")
        money_in_hand = money_in_hand-4
    elif choice==2:
        print("take your chips")
        money_in_hand = money_in_hand-5
    elif choice==3:
        print("take your redbull")
        money_in_hand = money_in_hand-20
    elif choice==3:
        print("take your coke")
        money_in_hand = money_in_hand-10
    else:
        print("entered incorrrect choice")
print("You don't have enough balance")
"""



"""import time 
s= 5s
while s>0:
    print(s)
    time.sleep(1)
    s=s-1
print("break time is over")"""

"""import time
stop = False
while not stop:
    print("enter s to stop it")
    time.sleep(1)
    press_stop=input("enter s for stop")

    if press_stop.lower() == "s":
        stop = True
print("Start the class break is over")"""

# Take 2 inputs from user i.e. username and password if its matching show message, if not matching and is 
# incorrect more than 5 times lock it

"""username = "sahana"
password = "sahanasahana@12"


if username == input("Enter username") and password == input("Enter password"):
    print('Logged in')
else:
    print("Incorrect username or password")"""


"""username = "sahana"
password = "sahanasahana@12"
counter = 1


while counter<=3:
    if username == input("Enter username") and password == input("Enter password"):
        print('Logged in')
    else:
        print("Incorrect username or password")
        counter = counter +1

else:
    print("account locked")"""

# To add item to list and end when not needed
todo_list=[]
end_of_todo = 'n'
while end_of_todo != 'y':
    todo_item=input("enter  your todo task")
    add_todo = todo_list.append(todo_item)
    end_of_todo = input("Enter n to add and y to end")
print("My todo list is ", todo_list)



