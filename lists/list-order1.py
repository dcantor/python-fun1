animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]

print animals.index("badger")

animals.insert(1, "dog")

print animals

for x in animals:
    print x


#count how many times something shows up in the list
animals.append("badger")
animals.append("badger")
animals.append("badger")
print animals

print animals.count("badger")

# Remove objects from the list
animals.remove("emu")
print animals

# Reverse the list
animals.reverse()
print animals


list1=["dog", "cat", "mouse"]
list2=["doge", "cat", "mouse"]
print list1
print list2

print cmp(list1, list2)

# list operations
newlist1 = list1 * 4
print newlist1

# for fun
for x in newlist1: print x


