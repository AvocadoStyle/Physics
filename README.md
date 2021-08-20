# Physics equations for the curse Exploring The Universe.
## features
###Class UnitUtil:
gets the units from a value need to complete all the types of units

###Class EquationUtil:
uses the UnitUtil class and more values such as Time, Distance, and more.
#####getKepler
returns kepler law value for distance and time
````
TimeSquar = self.__Time*self.__Time
DistanceThird = self.__Distance/self._unit.getVal()
K = TimeSquar/DistanceThird
return K
````
#####getKeplerBoolean
returns true or false if K=1
