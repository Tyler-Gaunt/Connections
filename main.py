### tyler gaunt's connections ###
### v.1.1 ###

# import standard libraries
# these are libraries built into python giving my script extra functionality
import time
import random

# import stuff from other .py files in this directory
from Dictionaries import selected_categories
from PrintGrid import print_letter_by_letter

# function area
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
    index_of_word_in_flattened_list = 0
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

def RebuildAfterGuessCorrect(guessed_categories, original_categories):
    row1 = []
    row2 = []
    row3 = []
    row4 = []
    # if one category has been guessed:
        # first row populate with words in the new grid is the guessed category
        # take out the guessed category from the original categories so there is only 3 left
        # flatten remaining 12 words and then rebuild as the function above does but only go to 12
    
    # elif two categories have been guessed
        # populate row 1 and 2 with the two two guessed category words
        # make sure that both categories are removed from the original categories
        # flatten remaining 8 words and rebuild up to 8 as above

    # elif three 

    # else:
    # just display the original categories in a grid
    pass

def PrintFormatedPrettyGrid(grid):
    # print("___________________________________________")
    max_length = max(len(word) for row in grid for word in row)
    for row in grid:
        for word in row:
            print(f'{word:{max_length}}', end='  ')
        print()
    # print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

def WelcomeScreen():
    print_letter_by_letter("Welcome to Connections v1.0\n")
    print_letter_by_letter("A game by NYT painstakingly reverse engineered by Tyler Gaunt\n\n")

def GetPlayerGuess():
    guess = []
    for i in range(4):
        word = input("Type your word")
        guess.append(word)
    return guess

def ConvertListsToSetsAndCheckGuesses(connections,guess):
    # if set(guess) == set(connections[0]["words"]) or set(guess) == set(connections[1]["words"]) or set(guess) == set(connections[2]["words"]) or set(guess) == set(connections[3]["words"]):
    #     return True
    # else:
    #     return False
    for category in connections:
        if set(guess) == set(category["words"]):
            return category
            break
    
    return False
    
# def ReDrawTheGridAfterCorrectGuess(connections, guess):    

# mainline
WelcomeScreen()
connections = selected_categories
grid = GenerateEmpty4x4Grid()
all_words_flat = FlattenThenShuffleCategoryDictionariesIntoList(connections)
grid = RebuildGridUsingFlattenedRandomisedList(all_words_flat)
PrintFormatedPrettyGrid(grid)

# main game loop
guessed_categories = []
lives = 4
won = False
while lives > 0 and won is False:
    guess = GetPlayerGuess()
    check_guess = ConvertListsToSetsAndCheckGuesses(connections, guess)
    if check_guess is False:
        lives = lives - 1
        print_letter_by_letter(f"Incorrect Guess, you have {lives} remaining.. ")
    else:
        guessed_categories.append(check_guess)
        print_letter_by_letter(f"Correct Guess! ")

        print(f"You guessed the following category: {check_guess["Category_name"]}")
        


if lives == 0:
    print_letter_by_letter("Game Over")