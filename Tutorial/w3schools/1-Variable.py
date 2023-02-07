# multi assign
x, y , z = "orange", "Banana", "Cherry";
print(x)
print(y)
print(z)

#One Value to Multiple variables
a = b = c = "Orange"
print(a)
print(b)
print(c)

# Unpack a Collection
fruits = ["apple", "banana", "cherry", "kiwi"]
x1, y1, z1, i1 = fruits
print(x1)
print(y1)
print(z1)
print(i1)

# Output variable
x = "Python is awesome"
print(x)
x = "Python"
y = "is"
z = "awesome"
print(x, y, z, "kuda")
print(x+y+z)

x = 5
y = 10
print(x + y)

x = 5
y = "John"
print(str(x)+y)
print(x,y)

# global  variable
"""is variable outside of a function, and use it tinside the function"""

x = "awesome"
def myfunc():
    print("Python is "+x)

myfunc()

def myfunc():
    x = "fantastic"
    print("Python is "+x)

myfunc()

# global variable, is mean that variable who inside the function will access to outside
def myfun():
    global f
    f = "kuda"

myfun()

print(f)

