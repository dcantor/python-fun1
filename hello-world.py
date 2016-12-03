var1 = 'hello world'
var2 = "Python programming"

print "var1[0]:", var1[0]
print "var2[1:5]:", var2[1:5]

var3 = 'Hello World!'
print "Updated String :- ", var3[:6] + 'Python'

print len(var3)

#################################
print'Pyg Latin'

pyg = 'ay'
original= raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    print original
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    print new_word
else:
    print 'empty'

