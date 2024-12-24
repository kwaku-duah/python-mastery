# represent anything using class
# pieces of information(attributes) and behaviour

class Dog:
    """ a simple attempt to model(REPRESENT A DOG)"""
    def __init__(self, name, age):
        """ initialise name and age attributes"""
        self.name = name
        self.age = age


    def sit(self):
        """ simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting")


    def roll_over(self):
        """Simulate a rolling over in response to a command """
        print(f"{self.name} is rolled over!")

# Going to make an instance from a class
# calling an attribute, name of instance dot name of attribute
# my_dog.name, my_dog.age
my_dog = Dog("Soldier",3)
print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")


# calling a method
# instance name dot method name - 
my_dog.roll_over()

#another instance of a class
your_dog = Dog('Tiger',5)
print(f"Your dog is called {your_dog.name} and it is {your_dog.age} years old!")

your_dog.sit()