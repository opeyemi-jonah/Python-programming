# JonahP5
# Programmer: Opeyemi Jonah
# EMail:ojonah@cnm.edu
# Purpose: rock paper scissors game
import random

game_score = 0

doAnother = 'y'

while doAnother == 'y':
    someValue = random.randrange(3)
    print(someValue)
    doAnother = input('Again y/n: ').strip().lower()[0]