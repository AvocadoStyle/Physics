from Equations import EquationUtil
import math
import matplotlib.pyplot as plt
import astropy
import numpy as np
if __name__ == "__main__":
    a = EquationUtil("KM", 450000000, 2)
    # print(a.getTimeOfLightSpeedInMinutesFromTheSun())
    print(a.getKepler())