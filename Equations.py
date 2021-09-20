from typing import Final
import Units
import math
from Spectrum import SpecColors

# value is performing distance
# time = distance/speed
class EquationUtil(Units.UnitUtil):
    def __init__(self, type_val=None, value=None, time=None, massa=None):
        super().__init__(type_val, value)
        self.__Time = time      #time in years
        self.__massa = massa
        self.LS: Final = 300000 #light speed 300,000km per sec
        self.AU: Final = 150000000
        self.G: Final = 6.67 * math.pow(10, -11)
        # self.__unit = Units.UnitUtil(type_val, value)      #composition

    def getTime(self):
        return self.__Time

    def getTimeOfLightSpeedInSecondsFromTheSun(self):
           return self.getKM() / (self.LS)

    def getTimeOfLightSpeedInMinutesFromTheSun(self):
           return self.getKM() / (self.LS * 60)

    def getTimeOfLightSpeedInHoursFromTheSun(self):
           return self.getKM() / (self.LS * 60 * 60)

    def getRsBlackHole(self):
        LS_meter = self.LS * 1000
        return (2*self.G*self.__massa) / math.pow(LS_meter, 2)
    def getRsDensityBlackHole(self):
        ###########
        # option1 #
        ###########
        # LS_meter = self.LS * 1000
        # a = 3 * math.pow(LS_meter, 6)
        # b = 32*math.pi*math.pow(self.G, 3)*math.pow(self.__massa, 2)
        # return a/b
        ###########
        # option2 #
        ###########
        return (self.__massa / ((4/3)*3.14*math.pow(self.getRsBlackHole(), 3))) / 1000

    def getKepler(self):
        if not(self.__Time and self.getType() == "KM"):
            print("ERROR - Time is None or type is not KM")
            exit(0)
        tSquere = self.__Time * self.__Time
        radiusAU = self.getVal() / self.AU
        radiusAuThird = radiusAU * radiusAU * radiusAU
        return tSquere/radiusAuThird

    def ThirdNewtonGravityBetweenTwoBodies(self, distanceBetweenBodiesInMeters, other):
        return (self.G*self.__massa*other.__massa) / math.pow(distanceBetweenBodiesInMeters, 2)

    def SpectrumTest(self):
        return SpecColors["purple"]

    def isKepler(self):
        k = self.getKepler()
        if k != 1:
            return False
        return True

    def setTime(self, time):
        self.__Time = time

    def setMassa(self, massa):
        self.__massa = massa
