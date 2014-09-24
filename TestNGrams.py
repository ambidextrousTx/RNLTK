import unittest
import NGrams


class TestNGrams(unittest.TestCase):
    def test_unigrams(self):
        sentence = 'this is a random piece of text'
        ngram_list = NGrams.generate_ngrams(sentence, 1)
        self.assertEqual(ngram_list, [['this'], ['is'], ['a'], ['random'],
                                      ['piece'], ['of'], ['text']])

if __name__ == '__main__':
    unittest.main()
