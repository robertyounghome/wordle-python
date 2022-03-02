import unittest
from guess import Guess

class TestProduceMask(unittest.TestCase):
    def setUp(self):
        self.word_list = ['unfit', 'cynic', 'dumbs', 'undid', 'water']
        self.gg = Guess(self.word_list)
        self.answer1 = 'cynic'

    def test_word_list_lost(self):
        return len(self.word_list) == len(self.gg.full_word_list)

    def test_valid_mask_creation(self):
        test_mask = self.gg.produce_mask('dumbs', self.answer1)

        valid = self.gg.produce_mask('unfit', self.answer1) != test_mask
        valid = self.gg.produce_mask('undid', self.answer1) != test_mask
        valid = self.gg.produce_mask('water', self.answer1) == test_mask

        return valid      

    def test_is_valid(self):
        self.gg.mask = 'BBBBB'
        self.gg.guess = 'dumbs'
        valid =  self.gg.is_valid(self.answer1)

        self.gg.mask = 'BYBGB'
        self.gg.guess = 'unfit'
        valid = self.gg.is_valid(self.answer1)

        return valid

if __name__ == '__main__':
    unittest.main()