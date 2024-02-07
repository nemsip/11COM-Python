import random

planets = [
    "Mercury",
    "Venus",
    "Mars",
    "Uranus",
    "Earth",
    "Jupiter",
    "Satern",
    "Neptune"
]

ranInt = random.randint(0, 8)

print("There are  " + str(len(planets)) + " planets.")
print(planets[ranInt])


for planet in planets:
    print(planet+" is a planet!")

for n in range(100):
    print("This will aparently print 100 times.")

input("Press enter 2 close")