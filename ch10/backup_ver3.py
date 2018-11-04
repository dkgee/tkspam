
import os
import time


source=['/Users/jht/mynginx/test01', '/Users/jht/mynginx/test02']

target_dir='/Users/jht/mynginx/backup/'

today=target_dir + time.strftime('%Y%m%d')
now=time.strftime('%H%M%S')

comment=raw_input('Enter a comment--->')
if len(comment)==0:
    target=today + os.sep + now + '.zip'
else:
    target=today + os.sep + now + "_" + comment.replace(" ","_") + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print "Successfully created directory",today

zip_command="zip -qr '%s' %s"%(target, ' '.join(source))

if os.system(zip_command)==0:
    print 'Successful backup to', target
else:
    print 'Backup FAILED'

### the softeware develop process
# What (analyze)
# How (design)
# Code (action)
# Test (test and debug)
# Use (action or develop)
# maintenance (optimize)