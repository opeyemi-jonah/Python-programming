# JonahP6
# Programmer: Opeyemi Gabriel Jonah
# Email: ojonah@cnm.edu
# Purpose: demonstrate use of functions
import math

# Radius of earth
Radius = 6371

# Haversine formula
def haversine_distance(lat1, lon1, lat2, lon2, R=6371):
    # Convert latitude and longitude from degrees to radians
    lat1 = math.degrees(lat1)
    lon1 = math.degrees(lon1)
    lat2 = math.degrees(lat2)
    lon2 = math.degrees(lon2)
    
    # Haversine formula
    A = math.sin((lat2 - lat1) / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin((lon2 - lon1) / 2)**2
    C = 2 * math.atan2(math.sqrt(A), math.sqrt(1 - A))
    D = R * C
    
    return D

# Header function to print out the summary of this program
def header_func():
    print("This program calculates the distance, bearing and more between Latitude/Longitude points")
    print("Please you will need two geo locations to get the distance which are measured in degrees")

# Get Geo location function
# [latitude, longitude] in degrees
def get_location():
    # Ask user for location
    latitude_location = input("Enter the latitude: ")
    longitude_location = input("Enter the longitude: ")

    return [float(latitude_location),float(longitude_location)]

# Get distance function
# Params [geo1] & [geo2]
# Return distance
def get_distance(geo1,geo2):
    lat1 = geo1[0]
    lat2 = geo2[0]
    lon1 = geo1[1]
    lon2 = geo1[1]
    h = haversine_distance(lat1, lon1, lat2, lon2, R=6371)
    return h

# Call header function
header_func()

def Calculate():
    do_another = 'y'
    while do_another == 'y':
        print("Enter the first geo location:")
        location1 = get_location()
        print("Enter the second geo location")
        location2 =get_location()
        # Get the distance
        Distance = get_distance(location1,location2)
        print(f'The distance between location1: {location1} and location2: {location2} is {Distance} degrees')


        do_another = input('Do you want to do another calculation? (y/n) ').strip().lower()
        if do_another not in ('y', 'n'):
            do_another = 'n'  # If the user enters anything other than 'y' or 'n', assume 'no'
Calculate()