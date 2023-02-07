# Local Scope
def myfunc():
  x = 300
  print(x)

myfunc()

# Function Inside Function
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

# Global Scope
x = 300

def myfunc():
  print(x)

myfunc()

print(x)

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)

# Global Keyword
def myfunc():
  global x
  x = 700

myfunc()

print(x)


result = 0

def calR():
    global result
    result= 30

print(result)
calR()
print(result)