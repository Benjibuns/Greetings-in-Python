class Cat:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "meow"

    def cats_name(self):
        return f"This cats name is {self.name}"

cat_one = Cat("Apollo")
cat_two = Cat("Anteninha")

print(cat_two.cats_name())