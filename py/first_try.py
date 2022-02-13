#!/usr/bin/python
# coding=utf-8
#
# Analyze the best first try for a particular resolver.
# This program is run off line, and produces the list of potential initial
# guesses.
#
# start with a dictionary, pick potential start words, and rank them based on
# the maximum size of the resulting buckets.

import resolv
import sys
import words5
import traceback
import random


def response_list():
        x = [ ".", "*", "="]
        l = []
        r = "....."
        while True:
            l.append(r)
            if r == "=====":
                break
            nr = ""
            progressed = False
            try:
              for i in range(0,5):
                x = r[i]
                if progressed:
                    nr += x
                elif x == "=":
                    nr += "."
                else:
                    progressed = True
                    if x == "*":
                        nr += "="
                    else:
                        nr += "*"
              r = nr   
            except Exception as e:
                traceback.print_exc()
                print("Got exception: " + str(e) + "i: " + str(i) + "r: <" + r + ">")
        return l

class selected_start:
    r_list = response_list()

    def __init__(self, w):
        self.w = w
        self.max_query = 0
        self.sum_queries = 0
        self.max_bucket = 0
        self.av_bucket = 0.0
        self.max_query = 0
        self.sum_queries = 0
        self.av_queries = 0.0

    def longest_bucket(self, limit):
        self.max_bucket = 0
        nb_buckets = 0
        sum_buckets = 0
        for r in selected_start.r_list:
            s = resolv.wordle_solver()
            s.process(w, r)
            nw = len(s.list)
            if nw > 0:
                nb_buckets += 1
                sum_buckets += nw
            if nw > self.max_bucket:
                self.max_bucket = nw
                if self.max_bucket > limit:
                    break
        if nb_buckets > 0:
            self.av_bucket = sum_buckets / nb_buckets
        return self.max_bucket

    def longest_query(self, queries):
        self.max_query = 0
        self.sum_queries = 0
        for w in queries:
            q = resolv.wordle_query(w)
            s = resolv.wordle_solver()
            n = 1
            x = self.w
            while n < 10:
                r = q.compare(x)
                if r == "=====":
                    break
                n += 1
                s.process(x,r)
                if n == 2 or len(s.list) <= 10:
                    x = s.suggest_recursive(30)
                else:
                    x = s.suggest()
            self.sum_queries += n
            if n > self.max_query:
                self.max_query = n
        if len(queries) > 0:
            self.av_queries = self.sum_queries/len(queries)
        return self.max_query, self.av_queries

# Main
    

if len(sys.argv) > 1:
    print("Usage: " + sys.argv[0])
    exit()

# First, compute the list of possible responses.
print("Found " + str(len(selected_start.r_list)) + " responses.")
if False:
    s = ""
    n = 0
    for r in r_list:
        s += "\"" + r + "\"" + ", "
        n += 1
        if n >= 8:
            print(s)
            n = 0
            s = ""
    if s != "":
        print(s)

# Then, compute for each potential entries (3000?) the
# minmax size of the reminder

minimax = len(str(words5.word_list))
minimax_limit = 225
selected = []

for w in words5.word_list:
    sw = selected_start(w)
    max_bucket = sw.longest_bucket(minimax_limit)
    if max_bucket <= minimax_limit:
        if max_bucket < minimax:
            minimax = max_bucket
            print("New start: " + w + " : " + str(max_bucket))
        selected.append(sw)

print("Selected " + str(len(selected)) + " start words")

print("Selecting 100 random queries")

origin = []
queries = []
for o in words5.word_list:
    origin.append(o)
for i in range(0, 100):
    x = random.choice(origin)
    origin.remove(x)
    queries.append(x)

print("start_word,max_tries,av_tries,max_bucket,av_bucket")
for sw in selected:
    max_tries,av_tries = sw.longest_query(queries)
    print(sw.w + "," + str(max_tries) + "," + str(av_tries) + "," + str(sw.max_bucket) + "," + str(sw.av_bucket))






