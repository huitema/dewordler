#!/usr/bin/python
# coding=utf-8
#
# Wordle_try is a debugging app, used to try various resolving logics.
# It starts with either a user-supplied "secret word", or a secret
# word picked at random from the dictionary. At each round, it provides
# suggestions, lets the user choose a guess, and then computes the
# wordle response and applies the selected resolver strategy.

import resolv
import sys

if len(sys.argv) > 2:
    print("Usage: " + sys.argv[0] + " [suggested_world]")

w = ""
if len(sys.argv) > 1:
    w = sys.argv[1]

q = resolv.wordle_query(w)
x = ""
r = ""
s = resolv.wordle_solver()

for i in range(0,6):
    while True:
        x = input("Guess: ")
        x = x.strip()
        if x in resolv.wordle_query.word_set:
            break
        else:
            print("   " + x + " is not in list")
    r = q.compare(x)
    print(r)
    if r == "=====":
        print ("You win in " + str(i+1) + " trials.")
        break
    s.process(x, r)
    # s.show()
    if len(s.list) == 1:
        print("There is only 1 possible word.")
    else:
        print("There are " + str(len(s.list)) + " possible words")
        if len(s.list) < 10:
            sli = ""
            for w in s.list:
                sli += w + ", "
            print(sli)
    print("Solver suggests: " + s.suggest_recursive(30))
    
if r != "=====":
    print("Sorry for your loss. The answer was: " + q.w) 