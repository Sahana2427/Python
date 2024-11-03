class fileopener:

    def __init__(self,filename):
        self.filename = filename

    
    def open_file(self):
        print("Thhis wll open the file",self.filename)


open = fileopener("Notes")

open.open_file()


import time

class timer:
    def __init__(self):
        self.start_time=time.time()

        def task (self):
            spent_time = time.time()- self.start_time
            print(spent_time)

        def __del__ (self):
            print("")

        def __str__(self):
            return "Thois is my class timer"
        

t1 = timer()

print(t1.task())

print(t1)