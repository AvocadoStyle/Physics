from Equations import EquationUtil
import math
if __name__ == "__main__":
    # types of the units
    types = ["SEC", "MINUTE", "METER", "KM", "AU", "LY", "PC"]

    valueType = 150000000
    TimeForSurrunding = 2
    DistanceToPlanet = 450*math.pow(10, 6)
    Type = types[3]

    eq1 = EquationUtil(types[4], valueType, TimeForSurrunding, DistanceToPlanet)
    K = eq1.getKepler()
    K = eq1.getKeplerBoolean()