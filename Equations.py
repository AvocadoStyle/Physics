from typing import Final
import Units

# value is performing distance
# time = distance/speed
class EquationUtil(Units.UnitUtil):
    def __init__(self, type_val, value, time=None):
        super().__init__(type_val, value)
        self.__Time = time      #time in years
        self.LS: Final = 300000 #light speed 300,000km per sec
        self.AU: Final = 150000000
        # self.__unit = Units.UnitUtil(type_val, value)      #composition

    def getTime(self):
        return self.__Time

    def getTimeOfLightSpeedInSecondsFromTheSun(self):
           return self.getKM() / (self.LS)

    def getTimeOfLightSpeedInMinutesFromTheSun(self):
           return self.getKM() / (self.LS * 60)

    def getTimeOfLightSpeedInHoursFromTheSun(self):
           return self.getKM() / (self.LS * 60 * 60)

    def getKepler(self):
        if not(self.__Time and self.getType() == "KM"):
            print("ERROR - Time is None or type is not KM")
            exit(0)
        tSquere = self.__Time * self.__Time
        radiusAU = self.getVal() / self.AU
        radiusAuThird = radiusAU * radiusAU * radiusAU
        return tSquere/radiusAuThird

    def getKeplerBoolean(self):
        k = self.getKepler()
        if k != 1:
            return False
        return True

    def setTime(self, time):
        self.__Time = time

    def setVal(self, time):
        self.__Time = time