from grid import Grid
import cProfile

grid_format = [
        ['M','A','P','O'],
        ['E','T','E','R'],
        ['D','E','N','I'],
        ['L','D','H','C']
    ]

grid = Grid(existing_array=grid_format)

print('< grid >')
grid.print_grid()

words = grid.find_all_words()

sortedwords = sorted(words, key=len)
print(f"Words found: {len(words)}")
print(f"Shortest word: {sortedwords[0]}")
print(f"Longest word: {sortedwords[-1]}")


# print('\n< position >')
# find_pos = (0, 0)
# letter = grid.get_letter(find_pos)
# print( f"Found {letter.letter} at position {find_pos}" )

# print('\n< surrounding >')
# pos=(0, 0)
# letters = grid.get_surrounding_letters(pos)
# for letter in letters:
#     print(letter)


# print('\n< word checker >')
# words = ['aardvark','zen','pickr','hell']
# for word in words:
#     result = grid.valid_word(word)
#     print(f'{word}: {result}')
# print('')
# for word in words:
#     result = grid.valid_start(word)
#     print(f'{word}: {result}')