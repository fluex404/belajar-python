l = ["apple", "banana", "orange"]
print(l)
print(len(l))

l = list(("apple", "banana", "orange"))
print(l)
l.append('cerry')
print(l)

l = ("apple", "banana")
print(l)

# Negative Indexing
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])

# Check if Item Exists
if "apple" in thislist:
    print("ada")
else:
    print("tidak ada")

# Change Item Value
thislist = ["a", 'b', 'c', 'd']
thislist[1] = "z"
print(thislist)

# Change a Range of Item Values
thislist = ["a", 'b', 'c', 'd']
thislist[1:3] = ['x', 'x']
print(thislist)

# Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, 'x')
print(thislist)

#Append Items
#To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Extend List
thislist = ["apple", 'banana', 'cherry']
tropical = ['mongo', 'pineapple','papaya']
thislist.extend(tropical)
print(thislist)

# Add Any Iterable
thislist     = ['apple', 'banana','cherry']
thistupple = ('kiwi','orange')
thislist.extend(thistupple)
print(thislist)

# Remove Specified Item
thislist = ['apple','banana','cherry']
thislist.remove('banana')
print(thislist)

# Remove Specified Index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# delete index
thislist = ['a','b','c','d']
del thislist[1]
thislist[2] = None
print(thislist)

# clear the list
thislist = ['a','c','b','d','e']
thislist.clear()
print(thislist)

# Loop Through a List
thislist = ['apple','banana','cherry']
for x in thislist:
    print(x)

for i in range(len(thislist)):
    print(i, thislist[i])

# Looping Using List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "i" in x]
print(newlist)

# Condition
print([ab for ab in fruits if ab not in ['apple', 'kiwi']])

# Iterable
print([x for x in range(10)])
print([x for x in range(10) if x > 0])

# Expression
print([x.upper() for x in fruits])
print(['hello' for x in fruits])
print([x if x=='apple' else 'tidak ada apple' for x in fruits])
print([x+1 for x in range(10)])