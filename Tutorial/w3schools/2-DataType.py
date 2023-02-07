x = 5
y = "kuda"
z = 2.1

print(x, type(x))
print(y, type(y))
print(z, type(z))

x = 1j
print(x * 2)

#list
x = ["honda", "yamaha", "suzuki"]
print(x)
#tuple
x = ("a", "b", "c")
print(x)
#range
x = range(6)
print(x)
print(list(x))

#dict
x = {'name': 'John', 'email': 'john@gmail.com'}
print(x.get('name'))
print(x.get('email'))

#set
x = {'a', 'b', 'c', 'c'}
print(x)
print(frozenset(x))

#bytes
x = b"Hello"
print(x)

#memory view
print(memoryview(x))

x = None
print(x)