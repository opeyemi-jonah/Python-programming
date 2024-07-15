# JonahP10
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
    # Instantiate points 
    pointList = []
    locationList = open('locations.txt')
    for line in locationList.readlines():
        if line!= '\n':
            lat, lon, description = line.split(',')
            lat = float(lat.strip())
            lon = float(lon.strip())
            description = description.strip()
            point = GeoPoint()
            # Setting points and descriptions for each point
            point.SetPoint(lat, lon)
            point.SetDescription(description)
            pointList.append(point)
    
    # Getting the closest point
    DoAnother ='y'

    while DoAnother == 'y':
        try:
            user_input = input("Enter your coordinates and description (latitude, longitude, description): ")
            lat, lon, description = user_input.split(',')
            lat = float(lat.strip())
            lon = float(lon.strip())
            description = description.strip()
            
            closest_point = None
            min_distance = float('inf')
            
            for point in pointList:
                distance = point.Distance(lat, lon)
                if distance < min_distance:
                    min_distance = distance
                    closest_point = point
            
            if closest_point:
                print(f"You are closest to {closest_point.GetDescription()} which is located at {closest_point.GetPoint()}")
            else:
                print("No points available to compare.")

        except TypeError:
            print("Please ensure your geo points are type float")
        except ValueError:
            print("Something went wrong! Check your input and try again...")
        except FileNotFoundError:
            print(f"File not found! Please ensure you have a file named 'locations.txt' in the same directory as this program")
        except Exception as e:
            print(f'Something went wrong: {e}')

        DoAnother = input("Do another (y/n)? ")
    
    locationList.close()

if __name__ == "__main__":
    main()