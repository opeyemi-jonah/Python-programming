# JonahP9
# Programmer: Opeyemi Gabriel Jonah
# Email: ojonah@cnm.edu
# Purpose: demonstrate how to define a class

import math
from GeoPoint import GeoPoint

# Main
def main():
    # Instantiate two points using different methods
    point1 = GeoPoint(34.052235, -118.243683, "Location 1")
    
    point2 = GeoPoint()
    point2.Point = (-128.712776, -74.005974)
    point2.Description = "location 2"

    DoAnother ='y'

    while DoAnother == 'y':
        user_input = input("Enter your coordinates and description (latitude, longitude, description): ")
        lat, lon, description = user_input.split(',')
        lat = float(lat.strip())
        lon = float(lon.strip())
        description = description.strip()

        # Create a third point to represent the user's location
        pointUser = GeoPoint(lat, lon, description)
        
        distanceToOne = point1.Distance(pointUser)
        distanceToTwo = point2.Distance(pointUser)

        if distanceToOne < distanceToTwo:
            closest_point = point1
        else:
            closest_point = point2
        print(f"You are closest to {closest_point.GetDescription()} which is located at {closest_point.GetPoint()}")
        DoAnother = input("Do another (y/n)? ")


if __name__ == "__main__":
    main()