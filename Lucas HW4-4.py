# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 14:14:53 2020

@author: Dana
"""
space = [' ']*9

# Function to draw board
def displayboard():
    print('-------------\n| {} | {} | {} |\n-------------\n| {} | {} | {} |\n-------------\n| {} | {} | {} |\n-------------'.format(space[0],space[1],space[2],space[3],space[4],space[5],space[6],space[7],space[8]))

play = True
player1 = 1
invalidspace = '----------------------\nThat space is already filled! Please choose a different space.'

# This is intro text explaining rules
print('\n\nWelcome to Tic-Tac-Toe with Dana! (or most likely by yourself lol...)\n')
print('You probably know how to play. Simply type in a number 1 through 9 during your turn and press enter. 1-3 corresponds to the first row moving left to right, 4-6 for the middle row, and 7-9 for the last row. If you wish to quit the game during your turn, just type "quit". The rest is up to you to figure out :)')

# Display empty board
displayboard()

while play == True:
    
    # Determine if it is now player 1 or player 2's turn; kinda works like toggling a boolean
    if player1 % 2 == 1:
        player = 'one'
        mark = 'X'
    else:
        player = 'two'
        mark = 'O'
    turn = input('Player '+player+': Where would you like to place your mark?\n')
    
    # Mark is placed
    if turn == '1':
        if space[0] == ' ':
            space[0] = mark
            player1 += 1
            displayboard()
        else:
            print(invalidspace)
            continue
    elif turn == '2':
        if space[1] == ' ':
            space[1] = mark
            player1 += 1
            displayboard()
        else:
            print(invalidspace)
            continue
    elif turn == '3':
        if space[2] == ' ':
            space[2] = mark
            player1 += 1
            displayboard()
        else:
            print(invalidspace)
            continue
    elif turn == '4':
        if space[3] == ' ':
            space[3] = mark
            player1 += 1
            displayboard()
        else:
            print(invalidspace)
            continue
    elif turn == '5':
        if space[4] == ' ':
            space[4] = mark
            player1 += 1
            displayboard()
        else:
            print(invalidspace)
            continue
    elif turn == '6':
        if space[5] == ' ':
            space[5] = mark
            player1 += 1
            displayboard()
        else:
            print(invalidspace)
            continue
    elif turn == '7':
        if space[6] == ' ':
            space[6] = mark
            player1 += 1
            displayboard()
        else:
            print(invalidspace)
            continue
    elif turn == '8':
        if space[7] == ' ':
            space[7] = mark
            player1+= 1
            displayboard()
        else:            
            print(invalidspace)
            continue
    elif turn == '9':
        if space[8] == ' ':
            space[8] = mark
            player1 += 1
            displayboard()
        else:
            print(invalidspace)
            continue
        
    # Quit game    
    elif turn == 'quit':
        print('---------------\nYou have quit the game.')
        print('Thank you for playing Tic-Tac-Toe. I hope you had fun and have a great day!')
        play = False
    else:
        print('-----------------\nThat is an invalid command! Please choose a number 1-9')
        continue
    
    # Check for winner
    endsequence = 'Thank you for playing Tic-Tac-Toe. Player ' +player+ ' won! I hope you had fun and have a great day!'
    if (space[0] == space[1]) and (space[0] == space[2]) and (space[0] != ' '):
        print(endsequence)
        play = False
    if (space[0] == space[3]) and (space[0] == space[6]) and (space[0] != ' '):
        print(endsequence)
        play = False
    if (space[0] == space[4]) and (space[0] == space[8]) and (space[0] != ' '):
        print(endsequence)
        play = False
    if (space[2] == space[4]) and (space[2] == space[6]) and (space[2] != ' '):
        print(endsequence)
        play = False
    if (space[1] == space[4]) and (space[1] == space[7]) and (space[1] != ' '):
        print(endsequence)
        play = False
    if (space[2] == space[5]) and (space[2] == space[8]) and (space[2] != ' '):
        print(endsequence)
        play = False
    if (space[3] == space[4]) and (space[3] == space[5]) and (space[3] != ' '):
        print(endsequence)
        play = False
    if (space[6] == space[7]) and (space[6] == space[8]) and (space[6] != ' '):
        print(endsequence)
        play = False
    
    # Check to see if all spaces are filled
    count = 0
    for i in space:
        if i != ' ':
            count += 1
        if count == 9:
            print('All spaces have been filled! The game is tied. I hope you had fun and have a great day!\n')
            play = False