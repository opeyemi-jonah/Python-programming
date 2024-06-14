# JonahP3
# Programmer: Opeyemi Gabriel Jonah
# Email: ojonah@cnm.edu
# Purpose: provides user capability to find fruit in a string
import random

# Broad list of fruits
fruits = [
'Apricot',
'Asian Pear',
'Avocado',
'Banana',
'Blackberries',
'Blueberries',
'Boysenberries',
'Cactus Pear',
'Cantaloupe',
'Cherries',
'Coconut',
'Cranberries',
'Figs',
'Gooseberries',
'Grapefruit',
'Grapes',
'Honeydew Melon',
'Kiwifruit',
'Limes',
'Longan',
'Loquat',
'Lychee',
'Madarins',
'Malanga',
'Mandarin Oranges',
'Mangos',
'Mulberries',
'Nectarines',
'Oranges',
'Papayas',
'Passion Fruit',
'Peaches',
'Pears',
'Persimmons',
'Pineapple',
'Plums',
'Pomegranate',
'Prunes',
'Quince',
'Raisins',
'Raspberries',
'Rhubarb',
'Strawberries',
'Tangelo',
'Tangerines',
'Tomato',
'Ugli Fruit',
'Watermelon'
]

# Create a sequence that has the names of seven random fruits
seven_fruits = random.sample(fruits, 7)
print("Seven random fruits selected:", seven_fruits)

# Ask the user for a sentence
user_input_sentence = input("Enter a sentence: ")

# Split the sentence into words
words = user_input_sentence.split()

# Find fruits from seven_fruits in the user's input sentence
fruits_in_sentence = list(set(seven_fruits) & set(words))
print("Fruits from the seven selected fruits found in the sentence:", fruits_in_sentence)

# Finds and replaces one instance of a fruit in the sentence with “Brussel Sprouts”.
sentenceWithBrusselSprouts = user_input_sentence.replace(fruits_in_sentence[0],"brussel sprouts")

# Displays the new sentence to the user.
print("Your sentence with brussel sprouts:",sentenceWithBrusselSprouts)
