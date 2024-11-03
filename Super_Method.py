"""class pw:
    def __init__(self,mentor):
        self.mentor = mentor

    def mentor_name(self):
        print(self.mentor)


def datascience(pw):
    def __init__(self,mentor,mentor_mailid):
        self.mentor = mentor
        #super().__init__(mentor)  # If u have many variables u can use this , in this case we have only 1 variable, 
        # Asiigning previous class variables to this class(super method will call super class variable)

        self.mentor_mailid= mentor_mailid


    def show_info(self):
        print(self.mentor,self.mentor_mailid)


python_basic = datascience()

python_basic.show_info()"""


#############################-------------------------------------------------------------------------##############################


class human:
    def __init__(self):
        pass

    def eat(self):
        print( "The eat method from human")

class male(human):
    def __init__(self,name):
        self.name = name

    def eat(self):
        super().eat() #This
        print(self.name)


"""sudhanshu = human() # or thiss

sudhanshu.eat()"""

sudhanshu = male("sudhanshu")

sudhanshu.eat()
        