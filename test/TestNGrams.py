import unittest
import sys
sys.path.append('../src')
import NGrams


class TestNGrams(unittest.TestCase):
    def test_unigrams(self):
        sentence = 'this is a random piece of text'
        ngram_list = NGrams.generate_ngrams(sentence, 1)
        self.assertEqual(ngram_list, [['this'], ['is'], ['a'], ['random'],
                                      ['piece'], ['of'], ['text']])

    def test_bigrams(self):
        sentence = 'this is a random piece of text'
        ngram_list = NGrams.generate_ngrams(sentence, 2)
        self.assertEqual(ngram_list, [['this', 'is'], ['is', 'a'],
                                      ['a', 'random'], ['random', 'piece'],
                                      ['piece', 'of'], ['of', 'text']])

    def test_fourgrams(self):
        sentence = 'this is a random piece of text'
        ngram_list = NGrams.generate_ngrams(sentence, 4)
        self.assertEqual(ngram_list, [['this', 'is', 'a', 'random'],
                                      ['is', 'a', 'random', 'piece'],
                                      ['a', 'random', 'piece', 'of'],
                                      ['random', 'piece', 'of', 'text']])


if __name__ == '__main__':
    unittest.main()
