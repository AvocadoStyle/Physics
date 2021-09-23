from typing import Final
import Units
import math
from Spectrum import SpecColors


class EquationUtil(Units.UnitUtil):
    def __init__(self, type_val=None, value=None, time=None, massa=None, temperture=None, radius=None, luminusity=None):
        super().__init__(type_val, value)
        self.__Time = time      #time in years
        self.__massa = massa
        self.__temperature = temperture
        self.__radius = radius
        self.__luminusity = luminusity
        self.LS: Final = 300000
        self.AU: Final = 150000000
        self.G: Final = 6.67 * math.pow(10, -11)
        self.SUN_MASS: Final = 2 * math.pow(10, 30)
        self.PARSEC_LIGHT_YEAR: Final = 3.26
        self.PARSEC_AU: Final = 206700
        self.PARSEC_KM: Final = 3.1 * math.pow(10, 13)

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
        return (self.__massa / ((4/3)*3.14*math.pow(self.getRsBlackHole(), 3))) / 1000

    def getHowMuchSunMass(self):
        return self.__massa / self.SUN_MASS

    def getKepler(self):
        if not(self.__Time and self.getType() == "KM"):
            print("ERROR - Time is None or type is not KM")
            exit(0)
        tSquere = self.__Time * self.__Time
        radiusAU = self.getVal() / self.AU
        radiusAuThird = radiusAU * radiusAU * radiusAU
        return tSquere/radiusAuThird

    def getParallaxLY(self, angle):
        parsec =  1 / (angle)   # 1sec parsec is 3.26LY
        return parsec * self.PARSEC_LIGHT_YEAR

    def getParallaxAU(self, angle):
        parsec =  1 / (angle)   # 1sec parsec is 3.26LY
        return parsec * self.PARSEC_AU

    def getParallaxKM(self, angle):
        parsec = 1 / (angle)  # 1sec parsec is 3.26LY
        return parsec * self.PARSEC_KM

    def getHipparcosLight(self):
        pass

    def getLumminusBySunMass(self):
        return math.pow(self.getHowMuchSunMass(), 4)

    def ThirdNewtonGravityBetweenTwoBodies(self, distanceBetweenBodiesInMeters, other):
        return (self.G*self.__massa*other.__massa) / math.pow(distanceBetweenBodiesInMeters, 2)

    def getLumminusityStephanBoltzman(self):
        if (self.__radius and self.__temperature) != None:
            return 4 * math.pi * self.__radius * math.pow(self.__temperature, 4)
        print("ERROR - radius or temperature is None, cannot calculate")


    def SpectrumTest(self):
        return SpecColors["purple"]

    def isKepler(self):
        k = self.getKepler()
        if k != 1:
            return False
        return True

    def setTime(self, time):
        self.__Time = time

    # def setMassa(self, massa):
    #     self.__massa = massa
    #
    def setLuminosityStephanBoltzman(self):
        self.__luminusity = self.getLumminusityStephanBoltzman()
