def generate_ngrams(text, n):
    ''' Generates all possible n-grams of a
    piece of text

    >>> text = 'this is a random piece'
    >>> n = 2
    >>> generate_ngrams(text, n)
    this is
    is a
    a random
    random piece
    '''
    text_array = text.split(' ')
    for i in range(0, len(text_array) - n + 1):
        print text_array[i:i + n]

generate_ngrams('this is a random piece', 2)
generate_ngrams('this is a random piece', 3)
