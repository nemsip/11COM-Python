import math

class Person:
    def __init__(self, first_name="", last_name=""):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return self.first_name + " " + self.last_name

    def say_hello(self):
        print(f"Hello, my name is {self.full_name()}")

nemit = Person("Nemith", "Wijesiri")

print(Person.full_name(nemit))

josh = Person("Josh", "Van Coller")

print(josh.full_name())

people = [nemit, josh]
for p in people:
    p.say_hello()

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

small = Circle(5)

large = Circle(40)

print(small.area())
print(large.area())

# pi_1 = 3.1415926535
# pi_2 = 897932384626 * 10 ** -10
# pi_3 = 433832795028
# pi_4 = 841971693993
