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

# Create a sequence that has the names of seven fruits.
seven_fruits = random.sample(fruits, 7)

def formatFruitList(fruitList):
    fruits = ""
    for x in fruitList:
        if(x != seven_fruits[-1]):
            fruits += x+', '
        else:
            fruits += x
    return "Some fruit: "+fruits

def count_fruits_in_sentence(sentence, fruits):
    # Convert the sentence to lowercase
    sentence_lower = sentence.lower()
    
    # Initialize variables to keep track of the fruits found
    fruit_count = 0
    fruits_in_sentence = set()
    
    # Check for each fruit in the sentence
    for fruit in fruits:
        fruit_lower = fruit.lower()
        if fruit_lower in sentence_lower:
            count = sentence_lower.count(fruit_lower)
            fruit_count += count
            fruits_in_sentence.add(fruit)
    
    return fruit_count, fruits_in_sentence

def replace_fruit_with_brussel_sprouts(sentence, fruits):
    sentence_lower = sentence.lower()
    
    for fruit in fruits:
        fruit_lower = fruit.lower()
        if fruit_lower in sentence_lower:
            # Find the first occurrence and replace it
            sentence = sentence.replace(fruit, "Brussel Sprouts", 1)
            break
    
    return sentence

# Instructional prompt to guide user's input
some_fruit = formatFruitList(seven_fruits)
print("Please enter a sentence with a fruit in it: ",some_fruit)

# Ask the user for a sentence
user_input_sentence = input("Enter sentence: ").lower()   

count_fruits_in_sentence(user_input_sentence, seven_fruits)

# Tell the user how many fruits are in that sentence
fruit_count, fruit_list = count_fruits_in_sentence(user_input_sentence, fruits)
print(f"There are {fruit_count} fruits in the sentence.")

# Display a list of fruits in the sentence
print("Fruits in the sentence:", list(fruit_list))

# Replace one instance of a fruit with "Brussel Sprouts"
new_sentence = replace_fruit_with_brussel_sprouts(user_input_sentence, fruit_list)
print("New sentence:", new_sentence)