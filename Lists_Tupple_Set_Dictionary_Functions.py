l1 = [1, 2, 3, 4, "sudha", "suhana", 345.345, [2, 3, 4, 8]]

l1.append("sfhj")  # as it is it will appends at last
print(l1)

l1.insert(3, 45)  # as it is inserts at particular index
print(l1)

l1.extend([6, 7, 8])  # inserts as individual element at last
print(l1)

l3 = [1, 2, 3, 5, 6]  # pops element at given index or else deleted at last index
l3.pop(3)
print(l3)

l4 = [5,6,8] # deleted entire lis
print(l4)
del l4

l5 = ['s', 'p' , 's']  # removes first occurence of s
(l5.remove('s'))
print(l5)

print(l5.count('s'))  # counts number of occurences of element

l6 = ['s', 'p' , 's', 'o']  # index of given element

print(l6.index('s'))

l6.reverse()  # reverses list
print(l6)

l6.sort()  # sorts in ascending (does not sort heterogenous data)
print(l6)

l6.sort(reverse=True)
print(l6)

l8 = [3, 6, 7, 7, 3, 2, 1, 8, 879, 456, 34]  # remove duplicates and print in sorted order
l9 = set(l8)
print(l9)
l10 = list(l9)
l10.sort()
print(l10)



list0 = [1, 2, 3, 4]
list1 = [5, 6, 7, 8]
list0 = list1

print(list0)

list0[0] = 200
print(list1)

list2 = list0.copy()
print(list2)

print(list1)

list0[1] = 300

print(list0)  # --- same
print(list1)  # --- same
print(list2)  # --- different

# Tupples

tup = (1, 2, 3, 4, 5, 6)
print(tup.count(4))

print(tup.index(1))

# Set

s = {3, 4, 5, 6, 234, 5674}

s.add(456)
print(s)

s.pop()  # removes from begining
print(s)

s.discard(6)
print(s)


print("--------------------------------------------------------------------------------------------")

# Dictionary

dict = {"name" : "sahana", "subject" : ["data science", "big data"], "number" : 45367}
print(dict)

print(dict.keys())
print(dict.values())
print(dict["name"])
print(list(dict.items()))
dict.pop("name")
print(dict)


dict["name"] = "sahana"
print(dict)