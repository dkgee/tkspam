
number=23
guess=int(raw_input('Enter an integer:'))

if guess==number:
    print 'you got it' #new block start here
elif guess<number:
    print("no, it is a little higher than that")
else:
    print "no, it is a little lower than that"

print 'Down'
