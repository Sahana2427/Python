# Plus operator will perform differently when u pass int and string

"""def test(a,b):
    return a+b

print(test(3,9))

print(test("tom","jerry"))

class datascience:
    def student(self):
        pass

class dataeng(datascience):
    def student(self):
        print("This will give me detail about data eng student")

class bigdata(datascience):
    def student(self):
        print("This will give me detail about big data student")

yash = dataeng()
farhana = bigdata()

yash.student()
farhana.student()

pw = datascience()
pw.student()"""

#Method Overloading

"""class bigdata:
    def __init__(self,number_of_class,number_of_student):
        self.number_of_class = number_of_class
        self.number_of_student = number_of_student

    def __add__(self,other): #other is not keyword
        return bigdata(self.number_of_class+other.number_of_class,self.number_of_student+other.number_of_student)
    

c1 = bigdata(1,10)
c2 = bigdata(2,10)
#bigdata(3,20)
c3 = bigdata(2,10)
result = c1+c2+c3
print(result.number_of_class,result.number_of_student)


# ...................../....

class dataeng():
    def student(self):
        print("This will give me detail about data eng student")

d1 = dataeng()
d2 = dataeng()
d3 = dataeng()
r = d1+d2+d3"""

# Another example

"""class datascience():
    def student(self):
        print("This will give me detail about data eng student")

class bigdata():
    def student(self):
        print("This will give me detail about big data student")

def output_class(class_obj):
    return class_obj.student()

SESHA = datascience()
sashi = bigdata()
print(output_class(SESHA))
print(output_class(sashi))"""

#Exampple

class skills:
    def student(self):
        return "This is skills student"

class datascience (skills):
    def student(self):
        print ("This will give me detail about data science student")

ujwal = datascience()
ujwal.student()



