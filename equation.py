x1 = float(input("x1: "))
y1 = float(input("y1: "))

x2 = float(input("x2: "))
y2 = float(input("y2: "))

m = (y1 - y2) / (x1 - x2)

b = y1 - m * x1

print("Final equation: y = {}x + {}".format(round(m), round(b)))