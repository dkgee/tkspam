
number=23
running=True

while running:
    guess=int(raw_input('Enter an integer:'))

    if guess==number:
        print 'you got it' #new block start here
        running=False
    elif guess<number:
        print("no, it is a little higher than that")
    else:
        print "no, it is a little lower than that"
else:
    print 'The while loop is over.'

print 'Down'
