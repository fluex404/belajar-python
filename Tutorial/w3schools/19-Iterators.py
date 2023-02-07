mytupple = ('apple','banana','cherry')
myit = iter(mytupple)

print(next(myit))
print(next(myit))
print(next(myit))

mystr = 'banana'
strit = iter(mystr)
print(next(strit))
print(next(strit))
print(next(strit))
print(next(strit))
print(next(strit))
print(next(strit))

#create iterator
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)