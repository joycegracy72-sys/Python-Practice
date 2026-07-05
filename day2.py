# Parent class
class Animal:
    def sound(self):
        print("Animal makes a sound")

# Child class
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Object
dog = Dog()

dog.sound()   # Inherited from Animal
dog.bark()    # Dog's own method