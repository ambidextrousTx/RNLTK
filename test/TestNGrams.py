''' Main class for testing the NGrams module
'''
import unittest
import sys
sys.path.append('../src')
import NGrams


class TestNGrams(unittest.TestCase):
    ''' Class to test n-gram creation methods '''
    def test_unigrams(self):
        ''' Unigrams are just tokenized words from the
        original string '''
        sentence = 'this is a random piece of text'
        ngram_list = NGrams.generate_ngrams(sentence, 1)
        self.assertEqual(ngram_list, [['this'], ['is'], ['a'], ['random'],
                                      ['piece'], ['of'], ['text']])

    def test_bigrams(self):
        ''' Bigrams are tokens from the original text
        taken two tokens at a time '''
        sentence = 'this is a random piece of text'
        ngram_list = NGrams.generate_ngrams(sentence, 2)
        self.assertEqual(ngram_list, [['this', 'is'], ['is', 'a'],
                                      ['a', 'random'], ['random', 'piece'],
                                      ['piece', 'of'], ['of', 'text']])

    def test_fourgrams(self):
        ''' 4-grams are tokens from the original text
        taken four tokens at a time '''
        sentence = 'this is a random piece of text'
        ngram_list = NGrams.generate_ngrams(sentence, 4)
        self.assertEqual(ngram_list, [['this', 'is', 'a', 'random'],
                                      ['is', 'a', 'random', 'piece'],
                                      ['a', 'random', 'piece', 'of'],
                                      ['random', 'piece', 'of', 'text']])


if __name__ == '__main__':
    unittest.main()
