import Spectrum
from Equations import EquationUtil
import math
import matplotlib.pyplot as plt
import astropy
import numpy as np
if __name__ == "__main__":




    #################
    # Spectrum Test #
    #################
    # a = EquationUtil()
    # test = a.SpectrumTest()
    # print(test)


    ##########################
    # BlackHole RS check sun #
    ##########################
    sun = EquationUtil("AU", 0, None, (2 * math.pow(10, 30)))
    print(sun.getRsDensityBlackHole())









    ###########################################
    # ThirdNewtonGravityBetweenTwoBodies test #
    ###########################################

    # earth = EquationUtil("AU", 1, None, (6.14 * math.pow(10, 24)))
    # sun = EquationUtil("AU", 0, None, (2 * math.pow(10, 30)))
    #
    # a = earth.ThirdNewtonGravityBetweenTwoBodies(150000000000, sun)
    # print(a)