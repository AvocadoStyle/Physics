class UnitUtil:
    def __init__(self, type=None, value=None):
        self._type = type
        self._value = value

    def getVal(self):
        return self._value

    def getAU(self):
        if self._type == "AU":
            return self._value
        elif self._type == "KM":
            return self._value / 150000000
        else:
            return "not such type - ERROR"

    def setValue(self, type, value):
        self._value = value
        self._type = type
