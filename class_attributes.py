class Dog:
    # Class attribute
    species = "Canis lupus familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

# Access class attribute
print(Dog.species) # Print: Canis Lupus Familiaris

# Create an object
my_dog = Dog("Kobe", 5)
print(my_dog.species) # Print: Canis Lupus Familiaris