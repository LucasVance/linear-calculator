import math

# Get two sets of coordinates from user
x1 = int(input("x1: "))
y1 = int(input("y1: "))

x2 = int(input("x2: "))
y2 = int(input("y2: "))

# Find distance using the distance formula
distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Print distance and round with two digits
print("Distance: " + str(round(distance, 2)))
