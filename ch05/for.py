

# for i in range(1, 5):
#     print i
# else:
#     print 'The for loop is over'

# break sentence
# while True:
#     s = raw_input('Enter something:')
#     if s=='quit':
#         break
#     print "Length of the string is ",len(s)
# print 'Done'


### continue sentence
# while True:
#     s = raw_input('Enter something:')
#     if s=='quit':
#         break
#     if len(s)<3:
#         continue
#     print "Input is of sufficient lenght"
#
# print 'Done'
#
# def func(x):
#     #global x
#     print 'x is ',x
#     x=2
#     print 'Changed local x to ', x
#
# x=50
# func(x)
# print 'Value of x is',x


# def say(message, times=1):
#     print message*times
#
# say('hello')
# say('World', 5)

# def func(a, b=5, c=10):
#     print 'a is',a, 'and b is',b, 'and c is',c
#
# func(3, 7)
# func(25, c=24)
# func(c=50,a=100)


# def maximum(x, y):
#     if x>y:
#         return x
#     else:
#         return y
#
# print maximum(13,9)

## document strings
# def printMax(x, y):
#     ''' Prints the maximum of two numbers.
#
#     The two values must be integers.'''
#     x=int(x)
#     y=int(y)
#
#     if x>y:
#         print x,'is maximum'
#     else:
#         print y,'is maximum'
#
# printMax(3, 5)
# print printMax.__doc__
# help(printMax)
