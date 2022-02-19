#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# load_words.py
# Created By  : Robert (Bob) Young
# Created Date: 02/14/2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" Unused, just for testing data loads, for instance the Linux Ubuntu words.  """ 
# ---------------------------------------------------------------------------

from data import Data
from guess import Guess
from exceptions import Error 
import re

DATA_TXT_ALLOWED_WORDS = "wordle-allowed-guesses.txt"
DATA_TXT_ANSWERS = "wordle-answers-alphabetical.txt"
OUTPUT_TXT_FILE = "words.txt"
DATA_TXT_FILE = "/usr/share/dict/words"
FULL_WORD_LIST = Data(DATA_TXT_ALLOWED_WORDS).words

class LoadData:
    def __init__(self):
        self.data = Data(DATA_TXT_ANSWERS)

    def __str__(self):
        return self.data.__str__()

    def filter_data_by_length(self, word_length):
        self.data.init_list([word for word in self.data.words if len(word) == word_length])

    def filter_non_letters(self):
        self.data.init_list([word for word in self.data.words if re.match(r"^[a-z]{5}$", word)])

if __name__ == '__main__':
    d = LoadData()
    print("---Complete Word List---")
    print(d)

    # d.filter_data_by_length(5)
    # print("---Five Letter Word List---")
    # print(d)

    # d.filter_non_letters()
    # print("---Valid Five Letter Word List---")
    # print(d)

    # print(FULL_WORD_LIST[:100])

    print(d.data.words[0] == 'aback')



