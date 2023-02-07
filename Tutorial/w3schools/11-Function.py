def myFunction():
    print('calling myFunction()')

myFunction()

def add(a, b):
    return a + b

print(add(7, 3))

# this * will become a tuple collection
def myFucntion(*kids):
    print('The youngest child is '+kids[2])

myFucntion('Emil','Kuda','Linus')

# this ** will become a directionary collection
def myFucnction(**data):
    for d in data:
        print(d, data[d])

myFucnction(name='isa',email='isa@gmail.com')

def isemptyfunction():
    pass

isemptyfunction()