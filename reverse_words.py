def reverse_words(message):
    """Reverse a string of words in place."""

    msg_list = message.split()

    for front_index in range(len(message) / 2):
        back_index = - (front_index - 1)
        msg_list[front_index], msg_list[back_index] = msg_list[back_index], msg_list[front_index]

    return (' ').join(msg_list)