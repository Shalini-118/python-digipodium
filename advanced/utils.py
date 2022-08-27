def char_character(sentence):
    data={}#blank dict
    for char in set(sentence):
        data[char]=sentence.count(char)
        print(char,sentence.count(char))
    return data    

def word_counter(sentence):
    data={}
    words=sentence.split()
    for words in set(words):
        data[words]=words.count(words)
    return data

def remove_punc(sentence):
    '''removes punctuation(TBC)'''
    pass 