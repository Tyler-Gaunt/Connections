### tyler gaunt's connections ###
### v.1.3 ###

## import standard libraries
## these are libraries built into python giving my script extra functionality
import time
import random

## import stuff from other .py files in this directory
from CompleteCategories import return_categories
from TypewriterEffect import print_letter_by_letter

## function area
def GenerateEmpty4x4Grid(): 
    width = 4
    height = 4
    grid = []
    empty = "____"
    for i in range(height):
        row = []
        for i in range(width):
            row.append(empty)
        grid.append(row)
    return grid

def FlattenThenShuffleCategoryDictionariesIntoList(connections):
    all_words_flat = []       
    for row in connections:
        for word in row["words"]:
            all_words_flat.append(word)
    random.shuffle(all_words_flat) 
    return all_words_flat

def RebuildGridUsingFlattenedRandomisedList(all_words_flat):
    new_grid = [[],[],[],[]]

    word_index = 0
    while word_index <4:
        new_grid[0].append(all_words_flat[word_index])
        word_index +=1

    while word_index <8:
        new_grid[1].append(all_words_flat[word_index])
        word_index +=1

    while word_index <12:
        new_grid[2].append(all_words_flat[word_index])
        word_index +=1

    while word_index <16:
        new_grid[3].append(all_words_flat[word_index])
        word_index +=1

    return new_grid

def PrintFormatedPrettyGrid(grid):
    max_length = max(len(word) for row in grid for word in row)
    for row in grid:
        for word in row:
            print(f'{word:{max_length}}', end='  ')
        print("")

def WelcomeScreen():
    print_letter_by_letter("Welcome to Connections v1.0\n")
    print_letter_by_letter("A game by NYT painstakingly reverse engineered by Tyler Gaunt\n")
    print_letter_by_letter("Make sure to spell all words correct and use ONLY capital letters otherwise you will get it wrong\n")
    print_letter_by_letter("You will be given 4 lives so try your best\n")
    print_letter_by_letter("You can always start again at the end by typing Y when asked\n")
    print_letter_by_letter("But now good luck and have fun\n\n")

def GetPlayerGuess():
    guess = []
    for i in range(4):
        word = input("Type your word   ")
        guess.append(word)
    return guess

def ConvertListsToSetsAndCheckGuesses(connections,guess):
    for category in connections:
        if set(guess) == set(category["words"]):
            return category
            break  
    return False

def PlayGame():
    WelcomeScreen()
    connections = return_categories()
    grid = GenerateEmpty4x4Grid()
    all_words_flat = FlattenThenShuffleCategoryDictionariesIntoList(connections)
    grid = RebuildGridUsingFlattenedRandomisedList(all_words_flat)
    PrintFormatedPrettyGrid(grid)

    ## main game loop
    guessed_categories = []
    lives = 4
    won = False
    correct_guesses = 0  
    while lives > 0 and not won: 
        guess = GetPlayerGuess()
        check_guess = ConvertListsToSetsAndCheckGuesses(connections, guess)
        if check_guess is False:
            lives -= 1
            print_letter_by_letter(f"Incorrect Guess, you have {lives} lives remaining... \n")
        else:
            if check_guess not in guessed_categories:
                guessed_categories.append(check_guess)
                correct_guesses += 1  # Increment correct guesses counter
                print_letter_by_letter(f"Correct Guess! ")
                print(f"You guessed the following category: {check_guess['Category_name']}")
            else:
                print_letter_by_letter("You've already guessed this category. Try another one.\n")   
            if correct_guesses == 4:  
                won = True
    if lives == 0:
        print_letter_by_letter("Game Over\n")
    else:
        print_letter_by_letter("Congratulations! You've guessed all 4 categories correctly!\n\n")

play_again = True
while play_again == True:
    PlayGame()
    play_again = input("Play again? Y/N   ")
    if play_again == "Y":
        PlayGame()
        