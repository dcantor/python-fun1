# function to count how many small numbers (< 10) are in a list
def count_small(numbers):
    total = 0
    for n in numbers:
            if n < 10:
                total = total +1
    return total


my_dict = [4,5,6,7,11,12,100,200]

print "There are ", count_small(my_dict), "numbers less than 10 in my dictionary"



def printme( str ):
   "This prints a passed string into this function"
   print str
   return

printme("Ain't this a grand function?")
printme("Yep")



def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print "Values inside the function: ", mylist
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print "Values outside the function: ", mylist



def printme2( str ):
   "This prints a passed string into this function"
   print str
   return;

# Now you can call printme function
printme2( str = "My string")




def printinfo( name, age = 35 ):
   "This prints a passed info into this function"
   print "Name: ", name
   print "Age ", age
   return;

# Now you can call printinfo function
printinfo( age=50, name="miki" )
printinfo( name="miki" )



def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print "Output is: "
   print arg1
   for var in vartuple:
      print var
   return;

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )

# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2;

# Now you can call sum as a function
print "Value of total : ", sum(10, 20)
print "Value of total : ", sum(20, 20)