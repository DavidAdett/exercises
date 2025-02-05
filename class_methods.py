class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} says: Woof!")

    def birthday(self):
        self.age += 1
        print(f"{self.name} now has {self.age} years old.")

# Create an object of class Dog
my_dog = Dog("Kobe", 5)
my_dog.bark()            # Salida: Kobe says: Woof!
my_dog.birthday()        # Salida: Kobe now has 6 years old