#!/usr/bin/python
# coding=utf-8
#
# The dewordler application is a helper for playing wordle.
# For each round, the application asks what the guess was, and what wordle
# response was. At each round, the application filters a list of acceptable
# response, starting with the list of 5 letter words from a disctionary,
# and then crossing out all words that are not compatible with the previous
# responses. It then uses game-playing logic to find out the next best guesses,
# those that are shown to find the result in fewer rounds.

import resolv
import sys

x = ""
r = ""
s = resolv.wordle_solver()
suggested = ""

for i in range(0,6):
    while True:
        x = input("Guess: ")
        x = x.strip()
        if len(x) == 0 and len(suggested) > 0:
            x = suggested
            break
        elif x in resolv.wordle_query.word_set:
            break
        else:
            print("   <" + x + "> is not in list")
    
    r = input("Result: ")
    if r == "=====":
        print ("You win in " + str(i+1) + " trials.")
        break
    s.process(x, r)
    if len(s.list) == 0:
        print("There are no possible solutions!");
        break;
    elif len(s.list) == 1:
        print("There is only 1 possible word: " + s.list[0])
        print ("You win in " + str(i+2) + " trials.")
        r = "====="
        break
    else:
        print("There are " + str(len(s.list)) + " possible words")
        if len(s.list) < 10:
            sli = ""
            for w in s.list:
                sli += w + ", "
            print(sli)
    suggested =  s.suggest_recursive(30, debug=False)
    print("Solver suggests: " + suggested)
    
if r != "=====":
    print("Sorry for your loss.") 