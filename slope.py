import math

x1 = input("x1: ")
y1 = input("y1: ")

x2 = input("x2: ")
y2 = input("y2: ")

deltaY = int(y1)-int(y2)
deltaX = int(x1)-int(x2)

gcd = math.gcd(deltaY, deltaX)
deltaY = deltaY/gcd
deltaX = deltaX/gcd

print("GCD = " + str(gcd))
print("Dividing now...")
print("Answer: ")
print(deltaY)
print(deltaX)
