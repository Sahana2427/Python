# Method 1

"""class a :
    def test(self):
        print("This test method is part of class a")

    def test1(self):
        print("This test1 method is part of class a")


obj_a = a()

obj_a.test()

obj_a = a()

obj_a.test1()"""

"""class b :
    def test(self):
        print("This test method is part of class a")

obj_b = b()

obj_b.test()"""

# Second Method

"""class b(a):
    pass

obj_b = b()

obj_b.test()
obj_b.test1()"""

"""class b(a):

    def test1b(self):
        print("This test1b method is part of class a")


obj_b = b()
obj_b.test1b()"""



######################################################################################################################################

