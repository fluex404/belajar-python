myset = {'apple','banana','cherry'}
myset.add('kuda')
# this is for add items, used add() function
myset.add('kuda')
print(myset)
myset = list(myset)
myset.append('kuda')
print(myset)

myfuckinglist = ['a','b','c','b']
print(myfuckinglist)
print(set(myfuckinglist))

print('this is the fucking set')
myfuckingset = {'a','b','c','d'}
print(myfuckingset)

# how to access items
for m in myfuckingset:
    print(m)

# check is present how to access items
print('a' in myfuckingset)
print(myfuckingset)
myupdate = ['a','c']
myfuckingset.update(myupdate)
print(myfuckingset)
# myfuckingset.remove('z')
print(myfuckingset)
myfuckingset.discard('a')
print(myfuckingset)

# to remove you can use
# remove() but if you remove something doesn't exist you will get error
# discard() not showing error if remove something doesn't exist
# pop()

thisset = {"apple", 'banana','cherry'}
print(thisset)
x = thisset.pop()
print(x)
print(thisset)

# for looping you only use for x in thisset it's gonna be easy

# if you wanna join two sets u can use union() function
set1 = {'a','b','c'}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
set1.update(set2)
print(set1)