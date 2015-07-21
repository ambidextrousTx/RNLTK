'''
The place to hold all similarity metrics. Currently implements the following:
    BLEU

'''
class SimilarityMetrics(object):
    ''' The main class that holds method to compute different similarities
    '''
    def __init__(self):
        pass

    def bleu(self, phrase1, phrase2):
        ''' Compute the BLEU score
        '''
        if phrase1 == '' or phrase2 == '':
            raise TypeError('Received one or more empty arguments')
