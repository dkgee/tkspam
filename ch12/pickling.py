

import cPickle as p
#import pickle as p


shoplistfile='shoplist.data'

shoplist=['apple', 'mongo', 'carrot']

f=file(shoplistfile, 'w')
p.dump(shoplist, f)
f.close()

del shoplist

f=file(shoplistfile)
storedlist = p.load(f)
print storedlist


