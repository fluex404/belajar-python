class MyClass:
    # name = 'Isa'
    # age = 22

    # def __init__(self, name, age):
    def __init__(self, name='Isa', age=22):
        self.name = name
        self.age = age
    def __str__(this): # as default the this is self, but i try to custome it
        return f'{this.name}, {this.age}'

    def hi(self):
        print('Haaaii, '+self.name)

# m1 = MyClass('Isa Subani','isasubani@gmail.com')
m1 = MyClass(age=25)
print(m1.name, m1.age)
print(m1)

m1.hi()

# update
m1.name = 'Test'
m1.hi()

# delete propertie of name
# del m1.name
# m1.hi()

# delete objects
del m1