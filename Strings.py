#String Function

s1 = "myskills"
s2= "myskills"
s3 = "My name is sahana"
s4 = "my name is sahana. i am learning python"

print(len(s1))

print(s1.count("l")) # Number of occurences of char

print(s1.find("k")) #Finds index of k

print(s1.index("k")) # Finds index of k

print(s1.find("z")) # -1 if particular char is not present

#print(s1.index("z")) # error if particular char is not present

print(s1.upper()) # capitalizes all char

print(s2.lower())

print(s3.title()) #camel case

print(s3.split()) # Splits string into a list also u can specify separator


print(s4.split('s')) # Incase of this separator is s

print(s4.replace('s','n'))  # original string is as it is since strings are immutable
print(s4)

print(s1.center(19, 'z'))  # centers string inbetween given char total characters including given string will be 19


s5 = "    myskills"
print(s5.lstrip())

s6 = 'myskills   '
print(s6.rstrip())

#Is Function

print(s1.isalpha())
print(s1.isalnum())
print(s1.isnumeric())



