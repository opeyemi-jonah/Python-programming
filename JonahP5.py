# JonahP5
# Programmer: Opeyemi Jonah
# EMail: ojonah@cnm.edu
# Purpose: rock paper scissors game
import random

# Initialize hand gestures for game
game_hand_gestures = ["Rock", "Paper", "Scissors"]
game_hand_gestures_list = '||'.join(game_hand_gestures)

def get_computer_hand():
    # Initialize computer's hand gesture
    computers_hand = random.choice(game_hand_gestures).lower()
    print(f'Computer played {computers_hand}')
    return computers_hand

def get_user_hand():
    print(f'Select your choice of: {game_hand_gestures_list}')
    user_hand = input('Select your choice: ').lower()
    return user_hand

def play_round():
    usr_score = 0
    com_score = 0
    while usr_score < 3 and com_score < 3:
        user = get_user_hand()
        computer = get_computer_hand()
        
        # Rock beats Scissors
        if user == computer:
            print("It's a tie")
        
        elif user == 'rock' and computer == 'scissors':
            # Add +1 to user score
            usr_score += 1
            print('User won! - Rock beats Scissors')
        
        elif user == 'paper' and computer == 'rock':
            # Add +1 to user score
            usr_score += 1
            print('User won! - Paper beats Rock')
        
        elif user == 'scissors' and computer == 'paper':
            # Add +1 to user score
            usr_score += 1
            print('User won! - Scissors beats Paper')
        
        else:
            com_score += 1
            print(f'Computer won! - {computer.capitalize()} beats {user.capitalize()}')
        
        print(f'Score is User: {usr_score} - Computer: {com_score}')
    
    if usr_score == 3:
        print("You won the game!")
    else:
        print("Computer won the game!")

def play():
    do_another = 'y'
    while do_another == 'y':
        play_round()
        do_another = input('Do you want to play again? (y/n) ').strip().lower()
        if do_another not in ('y', 'n'):
            do_another = 'n'  # If the user enters anything other than 'y' or 'n', assume 'no'

play()
