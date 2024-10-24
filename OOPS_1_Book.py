class book:

    def __init__(self,name,title,page_no):
        self.name_of_the_book = name
        self.title_of_the_book = title
        self.page_no = page_no

    def extract_details(self):
        print(self.name_of_the_book,self.title_of_the_book)

    def print_page_no(self):
        print(self.page_no)

sudhanshu = book("DSA","Practical DSA", 435)

sudhanshu.extract_details() # To see that particular function


print(sudhanshu.name_of_the_book) #To see particular things (variable)


#####################################################################################################################################

# Difference is u will get same output for all the class variable

class book:

    def __init__(self):
        self.name_of_the_book = "Tom"
        self.title_of_the_book = "DSA"
        self.page_no = "345"

    def extract_details(self):
        print(self.name_of_the_book,self.title_of_the_book)

    def print_page_no(self):
        print(self.page_no)

student_1 = book()
print(student_1.name_of_the_book)

student_2 = book()
print(student_2.name_of_the_book)