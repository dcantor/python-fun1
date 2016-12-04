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

