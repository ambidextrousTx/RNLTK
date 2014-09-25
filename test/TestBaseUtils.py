import unittest
import sys
sys.path.append('../src')
import BaseUtils


class TestBaseUtils(unittest.TestCase):
    def test_word_segmenter(self):
        segments = BaseUtils.get_words('this is a random sentence')
        self.assertEqual(segments, ['this', 'is', 'a', 'random', 'sentence'])


if __name__ == '__main__':
    unittest.main()
