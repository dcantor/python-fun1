# for loop test

for friend in ['dan', 'ryan', 'jen']:
    invitation = 'Hi ' + friend + '. Please come to my party on Saturday!'
    print(invitation)


for i in range(5):
    print 'i is now:', i


# while loop test

number = 0
while number != '42':
    number = raw_input('enter something')


for i in [12, 16, 17, 24, 29]:
    if i % 2 == 1:  # if the number is odd
        break        # immediately exit the loop
    print(i)
print("done")

for i in [12, 16, 17, 24, 29, 30]:
    if i % 2 == 1:      # if the number is odd
        continue        # don't process it
    print(i)
print("done")