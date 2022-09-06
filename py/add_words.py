#!/usr/bin/python
# coding=utf-8
#
# Update the list of words used in the game. 
# We do this by running wordlebot, then copying the text of the
# page listing all groups of step 1 solutions to a text file,
# finding the 5 letter words in that file, and if they are not
# already know, adding them to the list of words.
# 
# The new version of the wordlist is stored in ../tmp/wordle_words.py

import wordle_words
import sys

words = set(wordle_words.word_list)
nb_added = 0

for file_in in sys.argv[1:]:
    for line in open(file_in, "rt"):
        text = line.strip()
        parts = text.split(" ")
        for p in parts:
            if len(p) == 5:
                alpha = True
                for i in range(0,5):
                    if ord(p[i]) < ord("a") or ord(p[i]) > ord("z"):
                        alpha = False
                        break
                if alpha and not p in words:
                    print("Adding: " + p)
                    words.add(p) 
                    nb_added += 1
if nb_added > 0:
    with open("../tmp/wordle_words.py", "wt") as F:
        F.write("#!/usr/bin/python\n")
        F.write("# coding=utf-8\n")
        F.write("#\n")
        F.write("# This module stores the list of words used in the game.\n")
        F.write("\nword_list = [")
        rank = 0
        new_words = sorted(list(words))
        for word in new_words:
            s = ""
            if rank != 0:
                s += ","
            if (rank%8) == 0:
                s += "\n"
            s += " \"" + word + "\""
            rank += 1
            F.write(s)
        F.write("]\n")
        print("Saved " + str(rank) + " words.")