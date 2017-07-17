def condense_sentences(sentence):
    """Combine words in a sentence if the last letter 
    matches the next word's first letter.
    """

    word_list = sentence.split()

    for i in range(len(word_list) - 1):
        if word_list[i][-1] == word_list[i + 1][0]:
            word_list[i] = str(word_list[i] + word_list[i + 1])
            del word_list[i + 1]

    return ' '.join(word_list) 

