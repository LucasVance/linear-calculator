import math

# Get two sets of (x, y) coordinates
x1 = input("x1: ")
y1 = input("y1: ")

x2 = input("x2: ")
y2 = input("y2: ")

# Find change in both variables
delta_y = int(y1)-int(y2)
delta_x = int(x1)-int(x2)

# Find greatest common divisor to simplify fraction
gcd = math.gcd(delta_y, delta_x)
delta_y = delta_y/gcd
delta_x = delta_x/gcd
print("GCD = " + str(gcd))

# If x = 0, slope is undefined. If y = 0, slope = 0. If none of these, print deltaY over deltaX as fraction.
if delta_x == 0:
    print("Slope = undefined")
elif delta_y == 0:
    print("Slope = 0")
else:
    print("Slope:")
    print(delta_y)
    print("--")
    print(delta_x)

