while (True):
    toRun = input("Property to find: ")

    if toRun == "distance":
        exec(open("./distance.py").read())
    elif toRun == "slope":
        exec(open("./slope.py").read())
    elif toRun == "midpoint":
        exec(open("./midpoint.py").read())
    elif toRun == "ratio":
        exec(open("./ratio.py").read())
    else:
        print("An error occurred. Please enter one of the following: distance, midpoint, slope.")
