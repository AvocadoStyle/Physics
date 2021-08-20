from Units import UnitUtil

class EquationUtil:
    def __init__(self, type, value, Time=None, Distance=None):
        self._unit = UnitUtil(type, value)
        self.__hey = 1
        self.__Time = Time
        self.__Distance = Distance

    def getTime(self):
        return self.__Time

    def getDistance(self):
        return self.__Distance

    def getKepler(self):
        TimeSquar = self.__Time*self.__Time
        DistanceThird = self.__Distance/self._unit.getVal()
        # DistanceThird = DistanceThird*DistanceThird*DistanceThird ####@@@@@@@@@todo@@@@@@@@@@@#####
        K = TimeSquar/DistanceThird
        return K

    def getKeplerBoolean(self):
        k = self.getKepler()
        if k != 1:
            return False
        return True