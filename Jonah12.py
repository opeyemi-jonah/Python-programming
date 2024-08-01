# JonahP12
# Programmer: Opeyemi Gabriel Jonah
# Email: ojonah@cnm.edu
# Purpose: demonstrate how to use a database

import tkinter as tk
from tkinter import messagebox
import sqlite3
from GeoPoint import GeoPoint

def find_closest_point():
    user_lat = float(entry_lat.get())
    user_lon = float(entry_lon.get())

    try:
        conn = sqlite3.connect('locationsDB.db')
        cursor = conn.cursor()
        cursor.execute('SELECT latitude, longitude, description FROM locations')
        rows = cursor.fetchall()
        conn.close()

        points = []
        for row in rows:
            point = GeoPoint()
            point.SetPoint(row[0], row[1])
            point.SetDescription(row[2])
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
            result_text.set(f"You are closest to {closest_point.GetDescription()} which is located at {closest_point.GetPoint()} with a distance of {min_distance:.2f} kilometers.")
        else:
            result_text.set("No points found in the database.")
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"An error occurred while accessing the database: {e}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid latitude and longitude separated by a comma.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

# Creating the main window
root = tk.Tk()
root.title("GeoPoint Finder")

# Creating and placing widgets
tk.Label(root, text="Your Latitude:").grid(row=0, column=0, padx=5, pady=5)
entry_lat = tk.Entry(root)
entry_lat.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Your Longitude:").grid(row=1, column=0, padx=5, pady=5)
entry_lon = tk.Entry(root)
entry_lon.grid(row=1, column=1, padx=5, pady=5)

btn_find = tk.Button(root, text="Find Closest Point", command=find_closest_point)
btn_find.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, wraplength=300)
result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Starting the main loop
root.mainloop()
