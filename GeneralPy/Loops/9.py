# Write a program to calculate the circumference and area of circles. Your output should be a table which lists the radius (r) of the circle, the circumference (c) and the area (a) for circles of radius 10 to 100 cm, in steps of 10 cm. The
# output should look like:
# radius       circumference       area
# 10           61.8                314
# 20           etc...
# 30
# (You can calculate circumference = 2 * 3.14 * radius, and area = 3.14 * radius ** 2)

import math

radius_values = list(range(10,  101,  10))

print("Radius (cm)\tCircumference (cm)\tArea (sq cm)")

for radius in radius_values:
    circumference = 2 * math.pi * radius
    area = math.pi * radius ** 2
    print("{}\t\t{:.1f}\t\t{:.1f}".format(radius, circumference, area))
