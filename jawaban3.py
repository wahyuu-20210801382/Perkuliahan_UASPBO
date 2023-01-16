# polymorshm
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("MeONG, Meong")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("GUKK GUKK")


cat1 = Cat("LUKI", 3)
dog1 = Dog("BOMER", 2.5)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()
