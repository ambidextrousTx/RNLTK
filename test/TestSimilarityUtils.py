'''
Test cases for the similarity utilities
'''

import sys
import unittest
sys.path.append('../src')
import SimilarityUtils


class TestSimilarityUtils(unittest.TestCase):
    ''' Main class that tests all similarity methods '''
    def test_bleu_needs_nonempty_input(self):
        ''' The BLEU method should not work on empty arguments '''
        bleu_scorer = SimilarityUtils.SimilarityMetrics()
        self.assertRaises(TypeError, bleu_scorer.bleu, '', '')
        self.assertRaises(TypeError, bleu_scorer.bleu, 'one', '')


if __name__ == '__main__':
    unittest.main()
