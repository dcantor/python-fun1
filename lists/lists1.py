zoo_animals = ["pangolin", "cassowary", "sloth", "cat" ];
# One animal is missing!

if len(zoo_animals) > 3:
	print "The first animal at the zoo is the " + zoo_animals[0]
	print "The second animal at the zoo is the " + zoo_animals[1]
	print "The third animal at the zoo is the " + zoo_animals[2]
	print "The fourth animal at the zoo is the " + zoo_animals[3]

zoo_animals[2] = 'hyena'
print zoo_animals[2]

zoo_animals.append("kitty")
zoo_animals.append("kat")
zoo_animals.append("dog")

print len(zoo_animals)
print zoo_animals
print

# list slicing
slice = zoo_animals[1:3]
print(slice)

slice = zoo_animals[:2]
print(slice)

slice = zoo_animals[1:]
print(slice)