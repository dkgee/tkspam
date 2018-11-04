

shoplist=['apple', 'mongo', 'carrot', 'banana']
print 'I have',len(shoplist),'items to purchase'

print 'These items are:'
for item in shoplist:
    print  item,

print '\nI also have to buy rice.'
shoplist.append('rice')
print 'list is now',shoplist

print 'sort list'
shoplist.sort()
print 'Sorted list:',shoplist

print 'First,',shoplist[0]
olditem=shoplist[0]
del shoplist[0]
print 'I bought item',olditem
print 'shopping list now',shoplist