thistuples = ('apple','banana','cherry')
print(thistuples)
print(thistuples[1])

# update
# thistuples[1] = 'orange'
# print(thistuples)

# unpacking
# extract into variables
fruits = ('apple','banan','cherry')
(fruit1, fruit2, fruit3) = fruits

print(fruit1)
print(fruit2)
print(fruit3)

# Using Asterisk*
fruits = ('cherry','strawberry','rasberry', 'apple','banana')
(fruit1, fruit2, *fruit3) = fruits

print(fruit1)
print(fruit2)
print(fruit3)

# looping
print('loop')
for f in fruits:
    print(f)

print(fruit3*2)