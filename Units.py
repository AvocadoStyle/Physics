class UnitUtil:
    def __init__(self, type_val, value):
        self._type = type_val
        self._value = value

    def getVal(self):
        return self._value

    def getType(self):
        return self._type

    def getAU(self):
        if self._type == "AU":
            return self._value
        elif self._type == "KM":
            return self._value / 150000000
        else:
            return "not such type - ERROR"

    def getKM(self):
        if self._type == "AU":
            return self._value * 150000000
        elif self._type == "KM":
            return self._value
        else:
            return "not such type - ERROR"
    def setValueToAUfromKM(self):
        if self._type == "KM":
            self._value = self._value / 150000000
            self._type = "AU"
        else:
            print("ERROR")
            exit(EnvironmentError)

    def setValueToKMfromAU(self):
        if self._type == "AU":
            self._value = self._value * 150000000
            self._type = "KM"
        else:
            print("ERROR")
            exit(EnvironmentError)
