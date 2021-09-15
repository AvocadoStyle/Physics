from typing import Final
import Units


class EquationUtil(Units.UnitUtil):
    def __init__(self, type_val, value, time, distance):
        super().__init__(type_val, value)
        self.__Time = time
        self.__Distance = distance
        self.LS: Final = 300000
        # self.__unit = Units.UnitUtil(type_val, value)      #composition

    def getTime(self):
        return self.__Time

    def getDistance(self):
        return self.__Distance

    def getTimeOfLightSpeedInSecondsFromTheSun(self):
           return self.getKM() / (self.LS)

    def getTimeOfLightSpeedInMinutesFromTheSun(self):
           return self.getKM() / (self.LS * 60)

    def getTimeOfLightSpeedInHoursFromTheSun(self):
           return self.getKM() / (self.LS * 60 * 60)

    def getKepler(self):
        TimeSquar = self.__Time*self.__Time
        DistanceThird = self.__Distance/self.getVal()
        # DistanceThird = DistanceThird*DistanceThird*DistanceThird ####@@@@@@@@@todo@@@@@@@@@@@#####
        K = TimeSquar/DistanceThird
        return K

    def getKeplerBoolean(self):
        k = self.getKepler()
        if k != 1:
            return False
        return True