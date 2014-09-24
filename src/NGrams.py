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
    ngram_list = []
    for i in range(0, len(text_array) - n + 1):
        ngram_list.append(text_array[i:i + n])
    return ngram_list

print generate_ngrams('this is a random piece', 2)
print generate_ngrams('this is a random piece', 3)
print generate_ngrams('this is a random piece', 4)
