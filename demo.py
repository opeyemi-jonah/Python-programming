import math

class GeoPoint:
    def __init__(self):
        self.lat = 0.0
        self.lon = 0.0
        self.description = ""

    def SetPoint(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def GetPoint(self):
        return (self.lat, self.lon)

    def Distance(self, lat, lon):
        # Using the Haversine formula to calculate the distance between two points on the Earth
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

def main():
    point1 = GeoPoint()
    point2 = GeoPoint()

    # Setting points and descriptions for point1 and point2
    point1.SetPoint(34.052235, -118.243683)  # Example coordinates (Los Angeles, CA)
    point1.SetDescription("Los Angeles")

    point2.SetPoint(40.712776, -74.005974)  # Example coordinates (New York, NY)
    point2.SetDescription("New York")

    while True:
        user_input = input("Enter your coordinates (latitude, longitude): ")
        lat, lon = map(float, user_input.split(','))

        distanceToOne = point1.Distance(lat, lon)
        distanceToTwo = point2.Distance(lat, lon)

        if distanceToOne < distanceToTwo:
            closest_point = point1
        else:
            closest_point = point2

        print(f"You are closest to {closest_point.GetDescription()} which is located at {closest_point.GetPoint()}")

        another = input("Do another (y/n)? ")
        if another.lower() != 'y':
            break

if __name__ == "__main__":
    main()
