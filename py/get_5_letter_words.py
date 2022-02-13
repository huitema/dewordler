#!/usr/bin/python
# coding=utf-8
#
# This module gets the list of lower case five letter names from the
# words file argv[1] and creates a python data block. We use it to create the
# words.py module.

import sys

# main

if len(sys.argv) < 2 or len(sys.argv) > 3:
   print("Usage: get_5_letter_words word_file [result_file]")

word_list = []

for line in open(sys.argv[1],"rt"):
    text = line.strip()
    if len(text) == 5:
        maybe = True
        for i in range(0,5):
            x = ord(text[i])
            if x < ord('a') or x > ord('z'):
                maybe=False
                break
        if maybe:
            word_list.append(text)

print("Found " + str(len(word_list)) + " words.")

if len(sys.argv) >= 3:
    with open(sys.argv[2], "wt") as F:
        # write 8 names per line
        word_in_line = 0
        for word in word_list:
            F.write(" \"" + word + "\",")
            word_in_line += 1
            if word_in_line >= 8:
                F.write("\n")
                word_in_line = 0