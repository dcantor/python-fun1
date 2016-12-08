class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = "good"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        print self.name
        print self.age


hippo = Animal("Hippy", 10)
sloth = Animal("steve", 11)
ocelot = Animal("dan", 12)

hippo.description()

print hippo.health
print sloth.health
print ocelot.health

