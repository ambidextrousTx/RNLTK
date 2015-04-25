'''
Base NLP utilities
'''

import re


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

def get_sentences(phrase):
    ''' Return all sentences found in a phrase. Also
    trim the individual sentences of the special characters
    as well as spaces

    >>> get_sentences('What an amazing opportunity! I am so glad.')
    >>> ['What an amazing opportunity', 'I am so glad']
    >>> get_sentences('It is raining outside. Are you awake?')
    >>> ['It is raining outside', 'Are you awake']
    '''
    sentences = re.split(r'\?|!|\.', phrase)
    trimmed_sentences = []
    for sentence in sentences:
        if not sentence == '':
            trimmed_sentence = sentence.lstrip().rstrip()
            trimmed_sentences.append(trimmed_sentence)
    return trimmed_sentences

