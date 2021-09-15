from Equations import EquationUtil
import math
import matplotlib.pyplot as plt
import astropy
import numpy as np
if __name__ == "__main__":
    a = EquationUtil("AU", 5.2, 1, 1)
    # print(a.getVal())
    # a.setValueToAUfromKM()
    # print(a.getVal())
    print(a.getTimeOfLightSpeedInMinutesFromTheSun())
    print(a.getTimeOfLightSpeedInSecondsFromTheSun())









    # types of the units
    # types = ["SEC", "MINUTE", "METER", "KM", "AU", "LY", "PC"]
    #
    # valueType = 150000000
    # TimeForSurrunding = 2
    # DistanceToPlanet = 450*math.pow(10, 6)
    # Type = types[3]
    #
    # eq1 = EquationUtil(types[4], valueType, TimeForSurrunding, DistanceToPlanet)
    # K = eq1.getKepler()
    # print(K)
    # K = eq1.getKeplerBoolean()
    # if K:
    #     print("Kepler formula is: {}\n".format(K))
    # else:
    #     print("Kepler K is diffrent than 1 {}".format(K))
    #
    #
    #
    #
    # ##################################################
    #
    # loga, logl, logte = np.loadtxt('isoc_z008.dat', usecols=(0, 3, 4), unpack=True)
    # w7 = np.where(loga == 7.0)  # 10**7
    # w7_5 = np.where(loga == 7.5)
    # w8 = np.where(loga == 8.0)
    # w8_5 = np.where(loga == 8.5)
    # w9 = np.where(loga == 9.0)
    # plt.figure(figsize=[8, 5])
    #
    # plt.plot(logte[w7], logl[w7], label='10 Myr')
    # plt.plot(logte[w8], logl[w8], label='100 Myr')
    # plt.plot(logte[w7_5], logl[w7_5], label='31.6 Myr')
    # plt.plot(logte[w8_5], logl[w8_5], label='316.2Myr')
    # plt.plot(logte[w9], logl[w9], label='1 Byr')
    #
    # plt.xlabel('Log(Teff)')
    # plt.ylabel('Log L')
    # plt.axis([5.0, 3.5, 0, 6])
    # plt.title("Isochrones for star cluster with metallicity z =0.008")
    # plt.legend()
    # plt.grid()
    # plt.show()