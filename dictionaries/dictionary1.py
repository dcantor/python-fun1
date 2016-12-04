# Dictionary sample (key value pair)

food = {'chocolate' : 101, 'cheese' : 102, 'soup' : 103}

print "Food dictionary is: "
print food
print

# what is the value for key chocolate
print food['chocolate']
print

# for loop test
print "iterate over the food dictionary"
for x in food:
    print food[x]

# add new key/value pairs to the food dictionary
food['salad'] = 104
print food
print "There are ", len(food), " items in the food dictionary"
print

# delete a key from the dictionary
del food['chocolate']
print food
print