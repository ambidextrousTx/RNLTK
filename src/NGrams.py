''' Methods (static for now) to do with NGram
creation and calculations '''

def generate_ngrams(text, num):
    ''' Generates all possible n-grams of a
    piece of text

    >>> text = 'this is a random piece'
    >>> n = 2
    >>> generate_ngrams(text, num)
    this is
    is a
    a random
    random piece
    '''
    text_array = text.split(' ')
    ngram_list = []
    for i in range(0, len(text_array) - num + 1):
        ngram_list.append(text_array[i:i + num])
    return ngram_list
