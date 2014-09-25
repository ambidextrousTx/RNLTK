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
    clean_sentence = ''.join([char for char in sentence if ord(char) in
                             xrange(97, 123) or ord(char) in xrange(75, 91)
                             or ord(char) == 32])
    segments = clean_sentence.split(' ')
    words = [word for word in segments if not word == '']
    return words
