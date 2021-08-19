from Units import UnitUtil

if __name__ == "__main__":
    # types of the units
    types = ["SEC", "MINUTE", "METER", "KM", "AU", "LY", "PC"]
    distance = 150000000
    unit1 = UnitUtil(types[4], distance)
    print(unit1.getAU())