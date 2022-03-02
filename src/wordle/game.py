#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# game.py
# Created By  : Robert (Bob) Young
# Created Date: 02/09/2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" Game produces a list of possible words given your Wordle guesses/masks.  """ 
# ---------------------------------------------------------------------------
# There are over 12000 words (5 letter) to guess for the Wordle each day.
# And 2315 possible words that can be the answer in the Wordle.
# I suppose some of the 12000+ words are not considered common enough.
# This program allows you to view the words (possible answers) that 
# are remaining as guesses as you are playing the game.
# Like my wife would say, it allows you to cheat (at least a little bit).
# For each round of your Wordle, simply enter your data as you go,
# input the word that you guessed and the mask. The game will output
# a count of remaing words to the terminal, and you can open the text or json
# files to view the actual remaining words.
#
#   ****YOU NEED TO KNOW THIS BELOW to use this program
#
# guess is the word that was guessed (a five letter valid word)
#
# mask is the mask of the guess (also five letters 'xxxxx' as defined below):
#   After some debate, I decided to go with the following codes.
#       B : stands for Black, incorrect guess
#       G : stands for Green, correct guess
#       Y : stands for Yellow, sort of correct guess, but in wrong position
# example:
# Let's pretend the Wordle of the day is 'table'.
# You guessed 'maven', idk why, but the mask of that would be 'BGBYB'
# Run the program and enter 'maven' for the guess and 'BGBYB' as the mask.
# Your list of remaining words is filtered. There are now 33 words that could
# be the answer, and 'table' is one of those words. Check results.txt or 
# results.json to see this is true. Simple.
#
# Note that this program is a starting point for me for other Wordle projects.
# It is not meant to be a thing of beauty. I will likely make updates to it,
# converting it into a better and more usable api for future projects.
#
# Enjoy, and feel free to use this in your projects.
#
# data.words is the word list that is 'filtered' (the answer list)
# full_word_list is kept around to validate word guesses against a 
# full list of valid Wordle words.
# ---------------------------------------------------------------------------

from data import Data
from guess import Guess
from exceptions import Error 

DATA_TXT_ALLOWED_WORDS = "wordle-allowed-guesses.txt"
DATA_TXT_ANSWERS = "wordle-answers-alphabetical.txt"
DATA_TXT_FILE = "words.txt"

class Game:
    def __init__(self):
        pass

    def local_init(self):
        self.data = Data(DATA_TXT_ANSWERS)
        self.full_word_list = Data(DATA_TXT_ALLOWED_WORDS).words
        self.full_word_list = set(self.full_word_list + self.data.words)

    def api_init(self, answers, full_list):
        self.data = Data(answers)
        self.full_word_list = Data(full_list).words 
        self.full_word_list = set(self.full_word_list + self.data.words)

    def api_update(self, answers):
        self.data = Data(None)
        self.data = self.data.init_list(answers)

    def __str__(self):
        return self.data.__str__()

if __name__ == '__main__':
    keep_playing = 'R'
    while keep_playing == 'R':
        g = Game()
        g.local_init()
        gg = Guess(g.full_word_list)
        keep_playing = 'Y'
        print('\n'*40)
        print('---------New game-----------')
        print(f"Number of words for validations is {len(g.full_word_list)}.")
        print()
        print(g)
        while keep_playing == 'Y':
            guess = input("Enter your guess (xxxxx): ").lower()
            mask = input("What is the mask (xxxxx) with BYG only valid choices): ").upper()
            try:
                g.data.words = gg.have_a_guess(guess, mask, g.data.words)
            except Error as e:
                print(f"*** {e}. Please try again.***")
            except Exception:
                keep_playing = 'N'
                break
            g.data.output_to_file("results.txt")
            g.data.output_to_json("results.json")
            print(g)
            keep_playing = input('Keep playing (Y / N) or restart (R) new game? ').upper()
    print()
    print('Ok then, have a nice day!')