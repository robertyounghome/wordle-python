#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# guess.py
# Created By  : Robert (Bob) Young
# Created Date: 02/09/2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" Filters the words list for only words matching the guess / guess mask. """ 
# ---------------------------------------------------------------------------
# guess is the word that was guessed (a five letter valid word)
# mask is the mask of the guess (also five letters 'xxxxx' as defined below):
#   After much debate, I decided to go with the following codes.
#       B : stands for Black, incorrect guess
#       G : stands for Green, correct guess
#       Y : stands for Yellow, sort of correct guess, but the wrong position
# words is the word list that is 'filtered' to get our answer list
# ---------------------------------------------------------------------------

from collections import Counter
import re 
from exceptions import InvalidMask, InvalidWord

class Guess:
    
    def __init__(self, full_word_list):
        self.full_word_list = full_word_list

    def valid_word(self, word):
        return word in self.full_word_list

    # ---------------------------------------------------------------------------
    # verify_guess
    # The decorator verify_guess will verify whether the guess/mask are valid.
    # Exceptions are raised and the original word list is returned when either
    # the guess or mask is invalid. Otherwise, it calls the func.
    # ---------------------------------------------------------------------------
    def verify_guess(func):
        def wrapper(*args, **kwargs):
            guess_obj, words = args
            if not guess_obj.valid_word(guess_obj.guess):
                raise InvalidWord(f"An invalid word was guessed: {guess_obj.guess}")
            elif not re.search(r"^[BYG]{5}$", guess_obj.mask):
                raise InvalidMask(f"An invalid mask was entered: {guess_obj.mask}")
            else:
                return func(*args, **kwargs)
            return words        
        return wrapper

    # ---------------------------------------------------------------------------
    # filter_words
    # The decorator verify_guess will verify whether the guess is valid.
    # If the guess is invalid this function is skipped and the word list is 
    # not filtered.
    # If the guess is valid, all invalid words are filtered from the list.
    # In this case, is_valid is called for each word to determine its validity.
    # ---------------------------------------------------------------------------
    @verify_guess
    def filter_words(self, words):
        r = []
        for word in words:
            if self.is_valid(word):
                r.append(word)
        return r

    def have_a_guess(self, guess, mask, words):
        self.guess = guess
        self.mask = mask
        # self.guess_letter_count = Counter(guess)
        return self.filter_words(words)

    # ---------------------------------------------------------------------------
    # produce_mask - Given a guess and the actual word, produce the mask.
    # Note: this can be called directly if writing a program to play the 
    # actual wordle game.
    # In that case, the returned mask would be your result to display.
    # For the Wordle Helper, masks are compared to filter a list.
    # This method is the meat and potatoes that needs to be tested in detail.
    # Unitest is used for this purpose.
    # ---------------------------------------------------------------------------
    def produce_mask(self, guess, word):
        # Two collections (Counters) are used for comparisons
        # Also set up a dummy 'xxxxx' mask to start.
        word_letter_count = Counter(word)
        guess_letter_count = Counter(guess)
        guess_word_mask = ['x'] * len(guess)

        # First update the mask denoting all equal letters with a G.
        # Subtract from each Counter when a match is found.
        for i, letter in enumerate(word):
            if guess[i] == letter:
                guess_word_mask[i] = 'G'
                guess_letter_count[letter] -= 1
                word_letter_count[letter] -= 1

        # Next for each item in the mask that remains an 'x', determine
        # whether the mask should be updated to a 'Y' or 'B'. The Counter 
        # collections are used for this purpose. The guess and the word
        # must both still contain unused letters for us to have a 'Y'.
        # In other words, both the word and the guess must still contain
        # the same unmatched letter to result in a 'Y' on the mask.
        # Otherwise, just change the 'x' in the mask to a 'B'. 

        for i in range(len(guess)):
            letter = guess[i]
            if guess_word_mask[i] == 'x':
                if guess_letter_count[letter] > 0 and \
                    word_letter_count[letter] > 0:
                    guess_word_mask[i] = 'Y'
                    guess_letter_count[letter] -= 1
                    word_letter_count[letter] -= 1
                else:
                    guess_word_mask[i] = 'B'
        
        return ''.join(guess_word_mask)

    # ---------------------------------------------------------------------------
    # isValid - returns a boolean indicating whether the word should be included
    # in our result word list. Acts as if word is the answer.
    # Call produceMask to create a guess / word mask
    # This mask is then compared to the real guess mask.
    # If they are identical, the word is a possible answer and True is returned.
    # Otherwise, False.
    # ---------------------------------------------------------------------------

    def is_valid(self, word):
        return self.produce_mask(self.guess, word) == self.mask
        # ''.join(guess_word_mask) == self.mask

        # # Two collections (Counters) are used for comparisons
        # # Also set up a dummy 'xxxxx' mask to start.
        # word_letter_count = Counter(word)
        # local_guess_letter_count = self.guess_letter_count.copy()
        # guess_word_mask = ['x'] * len(self.guess)

        # # First update the mask denoting all equal letters with a G.
        # # Subtract from each Counter when a match is found.
        # for i, letter in enumerate(word):
        #     if self.guess[i] == letter:
        #         guess_word_mask[i] = 'G'
        #         local_guess_letter_count[letter] -= 1
        #         word_letter_count[letter] -= 1

        # # Next for each item in the mask that remains an 'x', determine
        # # whether the mask should be updated to a 'Y' or 'B'. The Counter 
        # # collections are used for this purpose. The guess and the word
        # # must both still contain unused letters for us to have a 'Y'.
        # # In other words, both the word and the guess must still contain
        # # the same unmatched letter to result in a 'Y' on the mask.
        # # Otherwise, just change the 'x' in the mask to a 'B'. 

        # for i in range(len(self.guess)):
        #     letter = self.guess[i]
        #     if guess_word_mask[i] == 'x':
        #         if local_guess_letter_count[letter] > 0 and \
        #             word_letter_count[letter] > 0:
        #             guess_word_mask[i] = 'Y'
        #             local_guess_letter_count[letter] -= 1
        #             word_letter_count[letter] -= 1
        #         else:
        #             guess_word_mask[i] = 'B'
        
        # return ''.join(guess_word_mask) == self.mask

    def __str__(self):
        return f"Guess: {self.guess}, mask: {self.mask}, Word: {self.word})"
