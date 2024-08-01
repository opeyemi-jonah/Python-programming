import math


class GeoPoint:
    def __init__(self):
        self.lat = 0.00
        self.lon = 0.00
        self.description = ""

    def SetPoint(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def GetPoint(self):
        return (self.lat, self.lon)

    def Distance(self, lat, lon):
        R = 6371  # Radius of the Earth in kilometers
        lat1, lon1 = self.lat, self.lon
        lat2, lon2 = lat, lon

        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        distance = R * c
        return distance

    def SetDescription(self, description):
        self.description = description

    def GetDescription(self):
        return self.description
