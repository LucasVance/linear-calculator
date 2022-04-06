toRun = input("Property to find: ")

if toRun == "distance":
    exec(open("./distance.py").read())
elif toRun == "slope":
    exec(open("./slope.py").read())
elif toRun == "midpoint":
    exec(open("./midpoint.py").read())
else:
    print("An error occurred.")