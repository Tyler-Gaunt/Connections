# # from Dictionaries import cars, common_colours, wings, island_countries # Importing connection categories from different file
# # import random

# # from GenerateGrid import GenerateGrid
# # def GenerateGrid(): # Creating an empty 4x4 grid to be filled later in
# #     width = 4
# #     height = 4
# #     grid = []
# #     empty = "____"
# #     for i in range(height):
# #         row = []
# #         for i in range(width):
# #             row.append(empty)
# #         grid.append(row)
# #     return grid

# grid = GenerateGrid()

# connections = [                                 
#     cars, common_colours, wings, island_countries,  # Telling the code that these random words are the connections categories
# ]

# all_words_flat = []         # Flatten the grid into one singular array
# for row in connections:
#     for word in row:
#         all_words_flat.append(word)
        
# random.shuffle(all_words_flat)  # Shuffle the flattened grid into a random order

# randomized_words_2d = []        # Places the shuffled flattened array back into 4 with random words
# row_length = len(connections[0])  
# for i in range(0, len(all_words_flat), row_length):
#     row = []
#     for j in range(row_length):
#         row.append(all_words_flat[i+j])
#     randomized_words_2d.append(row)

# row = 0
# for connection in connections:
#     col = 0
#     for word in connection["words"]:
#         grid[row][col] = word
#         col += 1
#     row += 1




# flattened_list = []
# # flatten the grid so all words appear inside of a 1d array e.g. ["red", "green", "blue", "orange", "yellow"]
# for row in grid:
#     for word in row:
#         flattened_list.append(word)

# # print(flattened_list)
# random.shuffle(flattened_list)
# # shuffle them using import random, then use listname.shuffle()
# # then put them into a grid again like before



# index_of_word_in_flattened_list = 0
# new_grid = [[],[],[],[]]

# word_index = 0
# while word_index <4:
#     new_grid[0].append(flattened_list[word_index])
#     word_index +=1

# while word_index <8:
#     new_grid[1].append(flattened_list[word_index])
#     word_index +=1


# while word_index <12:
#     new_grid[2].append(flattened_list[word_index])
#     word_index +=1

# while word_index <16:
#     new_grid[3].append(flattened_list[word_index])
#     word_index +=1

# grid = new_grid


# print("___________________________________________")
# max_length = max(len(word) for row in grid for word in row)
# for row in grid:
#     for word in row:
#         print(f'{word:{max_length}}', end=' | ')
#     print()
# print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")