# JonahP8
# Programmer: Opeyemi Gabriel Jonah
# Email: ojonah@cnm.edu
# Purpose: demonstrate how to define a class and catch exceptions

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
        return (self.lat,self.lon)

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
    
    def SetDescription(self,description):
        self.description = description
    def GetDescription(self):
        return self.description

# Main
def main():
    # Instantiate two points 
    point_one = GeoPoint()
    point_two = GeoPoint()

    # Setting points and descriptions for poin_one and point_two
    point_one.SetPoint(34.052235, -118.243683)  # Example coordinates (Los Angeles, CA)
    point_one.SetDescription("Los Angeles")

    point_two.SetPoint(40.712776, -74.005974)  # Example coordinates (New York, NY)
    point_two.SetDescription("New York")

    DoAnother ='y'

    while DoAnother == 'y':
        try:
            user_input = input("Enter your coordinates and description (latitude, longitude, description): ")
            lat, lon, description = user_input.split(',')
            lat = float(lat.strip())
            lon = float(lon.strip())
            description = description.strip()
            distanceToOne = point_one.Distance(lat, lon)
            distanceToTwo = point_two.Distance(lat, lon)

            if distanceToOne < distanceToTwo:
                closest_point = point_one
            else:
                closest_point = point_two
            print(f"You are closest to {closest_point.GetDescription()} which is located at {closest_point.GetPoint()}")

        except TypeError:
            print("Please ensure your geo points are type float")
        except ValueError:
            print("Something went wrong! Check your input and try again...")
        except Exception as e:
            print(f'Something went wrong: {e}')

        DoAnother = input("Do another (y/n)? ")


if __name__ == "__main__":
    main()