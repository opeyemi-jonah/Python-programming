# Jonah
# Programmer: Opeyemi Gabriel Jonah
# Email: ojonah@cnm.edu
# Purpose: Translates a phrase from one language to english

# Creates a dictionary with common phrases in language a as the key and the translation in another language 2 as the values.
phrases = {'E kaaro':'Good morning', 'Bawo ni':'How are you?', 'Nibo lowa?':'Where are you from?'}

# Display a list of the phrases of language 1 to the user.
print(', '.join(list(phrases.keys())))

# Ask the user to type in a phrase to translate.
language_one = input('Please enter a phrase from the above to translate: ')

# Get the value of the key
language_two = phrases[language_one]

# Display the translation of that phrase to the user.
print(f'Your sentence in English: {language_two}')


