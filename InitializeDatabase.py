# JonahP12
# Programmer: Opeyemi Gabriel Jonah
# Email: ojonah@cnm.edu
# Purpose: demonstrate how to use a database

import sqlite3

# Create a new SQLite database (or connect to an existing one)
conn = sqlite3.connect('locationsDB.db')
cursor = conn.cursor()

# Create a new table called loactions to store geo points
cursor.execute('''
CREATE TABLE IF NOT EXISTS locations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    latitude REAL,
    longitude REAL,
    description TEXT
)
''')

# Insert at least five points into the table
points = [
    (35.0718872, -106.6287606, 'Main Campus'),
    (35.1348554, -106.5211239, 'Montoya'),
    (35.3182524, -106.6839137, 'Rio Rancho'),
    (35.0856871, -106.6493166, 'STEMULUS Center'),
    (35.1836381, -106.5941213, 'ATC')
]

cursor.executemany('INSERT INTO locations (latitude, longitude, description) VALUES (?, ?, ?)', points)

# Commit the transaction and close the connection
conn.commit()
conn.close()

print("Database initialized and points inserted.")
