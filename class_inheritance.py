class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("This animal make a sound.")

class Dog(Animal): # Dog Inheritate from Animal
    def make_sound(self):
        print(f"{self.name} says: Woof!")

# Create an object of Dog class
my_dog = Dog("kobe")
my_dog.make_sound()