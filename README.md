# Wordle-Python

A Python package to help you solve the Wordle by filtering the word list as guesses are made.

I used this package in conjuction with the React / Flask front end repository called wordle-helper: https://github.com/robertyounghome/wordle-helper

This program can be called via an api (again, refer to wordle-helper above), or you may directly run the program at a command prompt: python game.py 

The program starts with a complete word list. For your wordle challenge, enter your guessed word along with a mask of the result.

For the mask:
    B is Black 
    Y is Yellow 
    G is Green 

See screen shots below, run python game.py:

![Screenshot](/img/wordle-cmd1.png)

You can see that the original list contains 2315 words. More words are used to validate your guesses, 12972 actually.

I guessed the word 'table' with a mask of 'bgbyg', and we can see that there are only 8 words remaining.

![Screenshot](/img/wordle-cmd2.png)

You may continue guessing. Or if you would like, you can view the filtered word lists in the file(s) results.json or results.txt. 

For more details refer to the comments in the code. Enjoy.
