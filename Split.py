#Split function splits strings into function

"""txt = "welcome to jungle"
x = txt.split()
print("Split =",x)

txt1 = "welcome to jungle"
print("Split =",txt1.split())

#setting maxsplit parameter to 1 will return list with 2 elements

fruits = "apple#banana#cherry"
print(fruits.split("#",1))

a,b = input("Enter two number").split()
c = int(a)+int(b)
print(c)"""

"""x = input("enter two numbers")
sum = int(x.split()[0]) + int(x.split()[1])
print(sum)"""

"""word1,word2 = input("Enter two words").split()
c = word1+word2
print(c)"""


s = input("enter roll no, name and percentage")
roll,name,percentage =s.split()
print("roll",roll)
print("name",name)
print("percentage",percentage)