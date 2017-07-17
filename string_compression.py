def string_compression(word):
    new_word = []
    counter = 1
    pointer = 1
    while pointer < len(word):
        if word[pointer] == word[pointer - 1]:
            counter += 1
            pointer += 1
        else:
            new_word.append(word[pointer])
            new_word.append(counter)
            counter = 1
            pointer += 1 
    new_word.append(word[pointer])
    new_word.append(counter)
    return new_word