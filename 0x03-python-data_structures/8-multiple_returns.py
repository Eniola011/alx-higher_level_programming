#!/usr/bin/python3
def multiple_returns(sentence):
    my_sentence = len(sentence)

    if my_sentence == 0:
        my_tuple = (my_sentence, None)
    else:
        my_tuple = (my_sentence, sentence[0])
    return my_tuple
