''' Tests for BaseUtils
'''
import unittest
import sys
sys.path.append('../src')
import BaseUtils


class TestBaseUtils(unittest.TestCase):
    ''' Main test class for the BaseUtils '''
    def test_word_segmenter_with_empty(self):
        ''' For an empty string, the segmenter returns
        just an empty list '''
        segments = BaseUtils.get_words('')
        self.assertEqual(segments, [])

    def test_word_segmenter(self):
        ''' The word segmenter returns the expected
        array of strings '''
        segments = BaseUtils.get_words('this is a random sentence')
        self.assertEqual(segments, ['this', 'is', 'a', 'random', 'sentence'])

    def test_ignoring_whitespace(self):
        ''' Whitespace in the input string is ignored
        in the input string '''
        segments = BaseUtils.get_words('this   is   a random sentence')
        self.assertEqual(segments, ['this', 'is', 'a', 'random', 'sentence'])

    def test_ignoring_special_chars(self):
        ''' If there are special characters in the input,
        they are ignored as well '''
        segments = BaseUtils.get_words('this   is   $$%%a random --00sentence')
        self.assertEqual(segments, ['this', 'is', 'a', 'random', 'sentence'])

    def test_segmenter_common_delims(self):
        ''' The sentence segmenter is able to split sentences
        on ., !, ?, etc. '''
        segments = BaseUtils.get_sentences('Wow! Did you see this? Amazing.')
        self.assertEqual(segments, ['Wow', 'Did you see this', 'Amazing'])

    def test_ignore_whitespace_sent(self):
        ''' Whitespace in the sentences is also ignored '''
        segments = BaseUtils.get_sentences('Wow!   Did you see this? Amazing.')
        self.assertEqual(segments, ['Wow', 'Did you see this', 'Amazing'])



if __name__ == '__main__':
    unittest.main()
