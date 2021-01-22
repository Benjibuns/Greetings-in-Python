# Classes Challenge 1
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return f"This wonderful friends name is {self.name}"

    def get_age(self):
        return f"{self.name}'s age is {self.age}."


class Cat(Pet):
    def speak(self):
        return "meow"


class Dog(Pet):
    def speak(self):
        return "woof"


dog_one = Dog("Joe", 3)
dog_two = Dog("Ialou", 7)
cat_one = Cat("Apollo", 9)
cat_two = Cat("Anteninha", 8)

print(dog_two.get_age())

# Classes Challenge 2
class Parent:
    def __init__(self, arg_one, arg_two):
        pass

    def some_func(self):
        pass

    def some_other_func(self):
        pass


class Child_one(Parent):
    def __str__(self):
        pass

    def __repr__(self):
        pass


class Child_two(Parent):
    def __str__(self):
        pass

    def __repr__(self):
        pass
