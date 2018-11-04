
# import sys
#
# print 'The command line arguments are:'
# for i in sys.argv:
#     print i
#
# print '\n\nThe PYTHON PATH is',sys.path,'\n'

# import using_name
#
# using_name.sayhi()
# print 'Version',using_name.version


from using_name import sayhi,version

sayhi()
print 'Version',version