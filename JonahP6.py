# JonahP6
# Programmer: Opeyemi Gabriel Jonah
# Email: ojonah@cnm.edu
# Purpose: demonstrate use of functions to calculate the distance between two geographical points

import math

# Radius of the Earth in kilometers
Radius = 6371

# Haversine formula to calculate the distance between two points on the Earth's surface
def haversine_distance(lat1, lon1, lat2, lon2, R=6371):
    """
    Calculate the great-circle distance between two points given their latitude and longitude.

    Parameters:
    lat1, lon1: Latitude and Longitude of the first point (in degrees)
    lat2, lon2: Latitude and Longitude of the second point (in degrees)
    R: Radius of the Earth (default is 6371 kilometers)

    Returns:
    The distance between the two points in kilometers.
    """
    # Convert latitude and longitude from degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    
    # Haversine formula
    A = math.sin((lat2 - lat1) / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin((lon2 - lon1) / 2)**2
    C = 2 * math.atan2(math.sqrt(A), math.sqrt(1 - A))
    D = R * C
    
    return D

# Header function to print out the summary of this program
def header_func():
    """
    Display the header summarizing the purpose of the program.
    """
    print("This program calculates the distance between two Latitude/Longitude points.")
    print("You will need to enter the geographical coordinates in degrees.\n")

# Function to get a geographical location from the user
def get_location():
    """
    Prompt the user to enter a latitude and longitude.

    Returns:
    A list containing the latitude and longitude as floats.
    """
    # Ask user for location
    latitude_location = input("Enter the latitude (in degrees): ")
    longitude_location = input("Enter the longitude (in degrees): ")

    return [float(latitude_location), float(longitude_location)]

# Function to calculate the distance between two geographical points
def get_distance(geo1, geo2):
    """
    Calculate the distance between two geographical points using the Haversine formula.

    Parameters:
    geo1: List containing the latitude and longitude of the first point
    geo2: List containing the latitude and longitude of the second point

    Returns:
    The distance between the two points in kilometers.
    """
    lat1 = geo1[0]
    lon1 = geo1[1]
    lat2 = geo2[0]
    lon2 = geo2[1]
    h = haversine_distance(lat1, lon1, lat2, lon2, R=6371)
    return h

# Main program execution
# Call the header function to print the program summary
header_func()

def Calculate():
    """
    Main loop to calculate distances between pairs of geographical points.
    Continues to prompt the user for new calculations until they choose to stop.
    """
    do_another = 'y'
    while do_another == 'y':
        # Prompt user for the first and second geographical locations
        print("Enter the first geo location:")
        location1 = get_location()
        print("Enter the second geo location:")
        location2 = get_location()
        
        # Get the distance between the two locations
        Distance = get_distance(location1, location2)
        print(f'The distance between location1: {location1} and location2: {location2} is {Distance:.2f} kilometers.')

        # Ask the user if they want to perform another calculation
        do_another = input('Do you want to do another calculation? (y/n) ').strip().lower()
        if do_another not in ('y', 'n'):
            do_another = 'n'  # If the user enters anything other than 'y' or 'n', assume 'no'

# Call the Calculate function to start the program
Calculate()
