

ab={ "ss":"ss@yahoo.info", 'uu':'uu@sina.com', 'pp':'pp@123.org'}

print 'ss address is %s'%ab['ss']

ab['yy']='yy@182.org'

del ab['uu']

print 'remainder length is %d.'%len(ab)
for name,address in ab.items():
    print 'Contact %s at %s'%(name,address)

if 'pp' in ab:
    print "\npp's address is %s"%ab['pp']