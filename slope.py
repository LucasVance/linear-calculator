import math

# Get two sets of (x, y) coordinates
x1 = input("x1: ")
y1 = input("y1: ")

x2 = input("x2: ")
y2 = input("y2: ")

# Find change in both variables
deltaY = int(y1)-int(y2)
deltaX = int(x1)-int(x2)

# Find greatest common divisor to simplify fraction
gcd = math.gcd(deltaY, deltaX)
deltaY = deltaY/gcd
deltaX = deltaX/gcd
print("GCD = " + str(gcd))

# If x = 0, slope is undefined. If y = 0, slope = 0. If none of these, print deltaY over deltaX as fraction.
if deltaX == 0:
    print("Slope = undefined")
elif deltaY == 0:
    print("Slope = 0")
else:
    print("Slope:")
    print(deltaY)
    print("--")
    print(deltaX)
