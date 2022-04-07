while (True):
    to_run = input("Property to find: ")

    if to_run == "distance":
        exec(open("./distance.py").read())
    elif to_run == "slope":
        exec(open("./slope.py").read())
    elif to_run == "midpoint":
        exec(open("./midpoint.py").read())
    elif to_run == "ratio":
        exec(open("./ratio.py").read())
    elif to_run == "equation":
        exec(open("./equation.py").read())
    else:
        print("An error occurred. Please enter one of the following: distance, midpoint, slope.")
