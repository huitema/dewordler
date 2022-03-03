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
import wordle_words
import traceback
import random

start_candidates = [
"aider",
"aisle",
"alert",
"alien",
"alone",
"alter",
"arise",
"arose",
"aside",
"atone",
"canoe",
"certs",
"crane",
"crest",
"early",
"fried",
"irate",
"larnt",
"later",
"layer",
"leant",
"learn",
"least",
"loser",
"nerts",
"notes",
"opera",
"raise",
"ratio",
"relay",
"renal",
"rents",
"resin",
"saner",
"saute",
"senor",
"slart",
"slate",
"snare",
"soare",
"stale",
"stern",
"stole",
"styre",
"tares",
"teary",
"trail",
"trial",
"tyler",
"yearn"]

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
        self.failed_rate = 0.0
        self.nb_failed = 0.0

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
        self.nb_failed = 0
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
            if n > 6:
                self.nb_failed += 1
            self.sum_queries += n
            if n > self.max_query:
                self.max_query = n
        if len(queries) > 0:
            self.av_queries = self.sum_queries/len(queries)
            self.failed_rate = self.nb_failed/len(queries)
        return self.max_query, self.av_queries


# exploration of a candidate
#
# start with plausible start word.
# load buckets from complete list of words
# compute statistics, such as frequency and average bucket size.
# if the candidate is deemed interesting, explore each bucket
#    if bucket is type "all match", this was a success
#    if not and more than 6 trials, this is a failure
#    each name in the buckets is a potential candidate
#        create a list of candidates.
#        if more than N:
#            compute a metric, order with that metric.
#            retain N candidates with best metric
#            evaluate candidates:
#                for recursive evaluation, create a resolver for each candidate,
#                call recursive evaluation for that resolver
#                
#            select best candidate
#            create sub buckets by evaluating the best candidate
#            (sub buckets depend only on list of candidates from the top)

class candidate_bucket:
    def __init__(self, w):
        self.l = [ w ]

class candidate:
    def __init__(self, w):
        self.candidate = w
        self.frq = 0
        self.max_bucket = 0
        self.av_bucket = 0
        self.buckets = dict()

    # load buckets from a list.
    def set_buckets(self, l):
        for w in l:
            r = resolv.wordle_query.compare_word(w, self.candidate)
            if r in self.buckets:
                self.buckets[r].l.append(w)
            else:
                self.buckets[r] = candidate_bucket(w)
        sum_n = 0
        for r in self.buckets:
            n = len(self.buckets[r].l)
            sum_n += n
            if n > self.max_bucket:
                self.max_bucket = n
        if len(self.buckets) > 0:
            self.av_bucket = sum_n / len(self.buckets)

    # iterate on resolution of the buckets
    def iterate(self, l, previous_solver):
        for r in self.buckets:
            if r == "=====":
                pass
            else:
                # Create a resolver by cloning the upper level one.
                # todo: variation of clone and resolve
                b = bucket[r]
                solver = previous_solver.cx()
                solver.process(self.w, r)
                # call solver with preset parameters
                guess = solver.suggest()
                # create sub-buckets for this guess.
                
                
        

               

# Main
    

if len(sys.argv) > 2:
    print("Usage: " + sys.argv[0] + " [nb_trials_queries]")
    exit()

nb_trials_queries = 100
if len(sys.argv) > 1:
    nb_trials_queries = int(sys.argv[1])
    if nb_trials_queries > len(wordle_words.word_list):
        nb_trials_queries  = len(wordle_words.word_list)

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

# Compute the frequency metric of the candidate list

frq=resolv.char_frequencies()
frq.add_list(wordle_words.word_list)
frq.set_frequencies()
print("char,Frequency")
for i in range(0,26):
    print(chr(ord('a')+i) + "," + str(frq.frequency[i]))
print("Start_word,Frequency")
for w in start_candidates:
    print(w + "," + str(frq.weight_word(w)))

# Then, compute for each potential entries (3000?) the
# minmax size of the reminder

if nb_trials_queries > 0:
  minimax = len(str(wordle_words.word_list))
  minimax_limit = 225
  selected = []

  if False:
   for w in wordle_words.word_list:
    sw = selected_start(w)
    max_bucket = sw.longest_bucket(minimax_limit)
    if max_bucket <= minimax_limit:
        if max_bucket < minimax:
            minimax = max_bucket
            print("New start: " + w + " : " + str(max_bucket))
        selected.append(sw)
  else:
   minimax_limit = len(str(wordle_words.word_list))
   for w in start_candidates:
    sw = selected_start(w)
    max_bucket = sw.longest_bucket(minimax_limit)
    selected.append(sw)  

  print("Selected " + str(len(selected)) + " start words")

  print("Selecting " + str(nb_trials_queries) + " random queries")

  origin = []
  queries = []
  for o in wordle_words.word_list:
    origin.append(o)
  if nb_trials_queries >= len(origin):
    queries = origin
  else:
    for i in range(0, nb_trials_queries):
        x = random.choice(nb_trials_queries)
        origin.remove(x)
        queries.append(x)
  print("start_word,max_bucket,av_bucket,fail_rate,av_tries,max_tries,")
  for sw in selected:
    max_tries,av_tries = sw.longest_query(queries)
    print(sw.w + "," + str(sw.max_bucket) + "," + str(sw.av_bucket) + "," + str(sw.failed_rate) + "," + str(av_tries)  + "," + str(max_tries) )






