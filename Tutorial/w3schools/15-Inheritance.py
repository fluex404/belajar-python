class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person('John','Doe')
x.printname()

# child
class Student(Person):
    def __init__(self, fname, lname, age=22):
        super().__init__(fname, lname)
        #ading properties
        self.age = age
    def setAge(self, age):
        self.age = age
    def __str__(self):
        return f'{self.firstname} {self.lastname} {self.age}'


s = Student(fname='Isa',lname='Subani', age=27)
print(s)

