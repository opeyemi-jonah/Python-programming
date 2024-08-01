# JonahP11
# Programmer: Opeyemi Gabriel Jonah
# Email: ojonah@cnm.edu
# Purpose: demonstrate how to use a GUI

import tkinter as tk
from tkinter import messagebox
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

def find_closest_point():
    file_name = entry_file.get()
    user_lat = float(entry_lat.get())
    user_lon = float(entry_lon.get())

    try:
        with open(file_name, 'r') as file:
            points = []
            for line in file:
                if line.strip():  # Skip empty lines
                    lat, lon, description = line.split(',')
                    lat = float(lat.strip())
                    lon = float(lon.strip())
                    description = description.strip()
                    point = GeoPoint()
                    point.SetPoint(lat, lon)
                    point.SetDescription(description)
                    points.append(point)

        user_point = GeoPoint()
        user_point.SetPoint(user_lat, user_lon)
        user_point.SetDescription("User Location")

        closest_point = None
        min_distance = float('inf')
        for point in points:
            distance = point.Distance(user_lat, user_lon)
            if distance < min_distance:
                min_distance = distance
                closest_point = point

        if closest_point:
            result_text.set(f"You are closest to {closest_point.GetDescription()} which is located at {closest_point.GetPoint()}")
        else:
            result_text.set("No points found in the file.")
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found! Please ensure the file exists.")
    except ValueError:
        messagebox.showerror("Error", "Invalid data! Please check your input and file content.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

# Creating the main window
root = tk.Tk()
root.title("GeoPoint Finder")

# Creating and placing widgets
tk.Label(root, text="File Name:").grid(row=0, column=0, padx=5, pady=5)
entry_file = tk.Entry(root)
entry_file.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Your Latitude:").grid(row=1, column=0, padx=5, pady=5)
entry_lat = tk.Entry(root)
entry_lat.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Your Longitude:").grid(row=2, column=0, padx=5, pady=5)
entry_lon = tk.Entry(root)
entry_lon.grid(row=2, column=1, padx=5, pady=5)

btn_find = tk.Button(root, text="Find Closest Point", command=find_closest_point)
btn_find.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, wraplength=300)
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Starting the main loop
root.mainloop()
