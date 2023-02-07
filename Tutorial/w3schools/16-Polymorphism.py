class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        return 'animal\'s talk'

class Dog(Animal):
    def talk(self):
        return "Woooaaaaf!"
class Cat(Animal):
    def talk(self):
        return "Meawww!"

def animal_talk(animal):
    print(animal.talk())

dog = Dog("Buddy")
cat = Cat("Mimi")

animal_talk(dog)
animal_talk(cat)