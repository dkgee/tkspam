
import os
import time


source=['/Users/jht/mynginx/test01', '/Users/jht/mynginx/test02']

target_dir='/Users/jht/mynginx/backup/'

target=target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command="zip -qr '%s' %s"%(target, ' '.join(source))

if os.system(zip_command)==0:
    print 'Successful backup to', target
else:
    print 'Backup FAILED'