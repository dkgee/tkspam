#
#
# class ShortInputException(Exception):
#     def __init__(self, length, atleast):
#         Exception.__init__(self)
#         self.length = length
#         self.atleast = atleast
#
#
# try:
#     s = raw_input("Enter ->")
#
# except EOFError:
#     print 'xxxx'
#
# except ShortInputException,x:
#     print 'ssss, the input was of length %d, was expecting at leas, %d'%(x.length, x.atleast)
#
# else:
#     print 'uuuuuu'



import time

try:
    f = file('../ch12/poem.txt')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        time.sleep(2)
        print line
finally:
    f.close()
    print 'Cleaning up...closed the file'
