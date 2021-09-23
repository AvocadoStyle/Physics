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
    # sunMass = (2 * math.pow(10, 30))
    # sunMassOneHundredFiftyMillion = sunMass * 150 * math.pow(10, 6)

    ### sun = EquationUtil("AU", 0, None, (2 * math.pow(10, 30)))
    # sunOneHundrerFiftyMill = EquationUtil("AU", 0, None, sunMassOneHundredFiftyMillion)
    # print(sunOneHundrerFiftyMill.getHowMuchSunMass())





    ################
    # check parsec #
    ################
    # parsec = 1/40
    # checkStar = EquationUtil(None, None, None, None)
    # print(checkStar.getParallaxAU(parsec))



    ##########################
    # BlackHole RS check sun #
    ##########################
    sunMass = (2 * math.pow(10, 30))
    # twoTimeSunMass = sunMass*2
    sunTwoMASS = EquationUtil(None, None, None, sunMass, None, None, None)
    print(sunTwoMASS.getRsDensityBlackHole())






    ###########################################
    # ThirdNewtonGravityBetweenTwoBodies test #
    ###########################################

    # earth = EquationUtil("AU", 1, None, (6.14 * math.pow(10, 24)))
    # sun = EquationUtil("AU", 0, None, (2 * math.pow(10, 30)))
    #
    # a = earth.ThirdNewtonGravityBetweenTwoBodies(150000000000, sun)
    # print(a)