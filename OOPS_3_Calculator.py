from functools import reduce 

class calculator:

    def add(self,*args):
        return sum(args)
    
    def subtraction(self,*args):
        return reduce(lambda a,b : a-b,args)
    
himanshu = calculator()

"""print(himanshu.add(1,2,3,4))"""
    

print(himanshu.add(1,2,3,4))