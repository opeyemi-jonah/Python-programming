import math


class GeoPoint:
    def __init__(self, lat=0, lon=0, description='TBD'):
        self.__lat = lat
        self.__lon = lon
        self.__description = description

    def SetPoint(self, point):
        self.__lat, self.__lon = point

    def GetPoint(self):
        return (self.__lat, self.__lon)

    def Distance(self, toPoint):
        # Using the Haversine formula to calculate the distance between two points on the Earth
        R = 6371  # Radius of the Earth in kilometers
        lat1, lon1 = self.__lat, self.__lon
        lat2, lon2 = toPoint.GetPoint()

        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        distance = R * c
        return distance
    
    def SetDescription(self,description):
        self.__description = description
    def GetDescription(self):
        return self.__description
    
    Point = property(GetPoint,SetPoint)
    Description = property(GetDescription, SetDescription)
