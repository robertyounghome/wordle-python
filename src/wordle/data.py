#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# data.py
# Created By  : Robert (Bob) Young
# Created Date: 02/09/2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" Loads the word data, has export methods, and some procs to evaluate the data. """ 
# ---------------------------------------------------------------------------
# Loads the 5757 five letter words that are possible answers to Wordle.
# There are a few methods here to look at this data. For instance, did 
# you know that there are 53 words with 3 or more of the same letters.
# I see ahhhh is listed as a word too. Exclamations, good grief.
# Data is also the place where the data gets imported and exported.
# Likely more methods may get added to data in the future, should I decide
# to further analyze the word data.
# ---------------------------------------------------------------------------

import json
from collections import Counter 

class Data:
    def __init__(self, file_name):
        self.words = None
        if file_name:
            self.words = open(file_name).read().splitlines()

    def __str__(self):
        return f"Data contains {len(self.words)} total words."

    def init_list(self, words):
        self.words = words

    def words_with_multiple_of_same_letter(self):
        r = []
        for word in self.words:
            if len(word) != len(set([c for c in word])):
                r.append(word)
        return r

    def words_with_three_of_same_letter(self):
        r = []
        for word in self.words:
            c = Counter(word)
            for key, value in c.items():
                if value > 2:
                    r.append(word)
        return r

    def output_to_file(self, file1):
        f = open(file1, "w")
        for word in self.words:
            f.write(word)
            f.write("\r\n")
        f.close()

    def output_to_json(self, file1):
        f = open(file1, "w")
        s = str(json.dumps(self.words))
        f.write(s)
        f.write("\r\n")
        f.close()
        
if __name__ == '__main__':
    d = Data("words.txt")
    print(d)
    r = d.words_with_multiple_of_same_letter()
    print(f"Words with multiple of same letter: {len(r)}")
    r = d.words_with_three_of_same_letter()
    print(f"Words with three or more of the same letter: {len(r)}")
    print("The following words have three or more of the same letter: ")
    print(r)
