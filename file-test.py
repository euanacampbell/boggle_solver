with open('words.txt') as file:
    contents = file.read()
    search_word = 'zzzz'
    if search_word in contents:
        print ('word found')
    else:
        print ('word not found')