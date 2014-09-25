'''
Base NLP utilities
'''


def get_words(sentence):
    ''' Return all the words found in a sentence.
    Ignore whitespace and all punctuation
    >>> get_words('a most interesting piece')
    >>> ['a', 'most', 'interesting', 'piece']
    >>> get_words('a, most$ **interesting   piece')
    >>> ['a', 'most', 'interesting', 'piece']
    '''
    clean_sentence = ''.join([char for char in sentence if char.isalpha()
                             or char.isspace()])
    segments = clean_sentence.split(' ')
    words = [word for word in segments if not word == '']
    return words
