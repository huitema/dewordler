#!/usr/bin/python
# coding=utf-8
#
# This module implements the rules

import wordle_words
import random
import traceback

class word_frequency:
    def __init__(self, word, weight):
        self.word = word
        self.weight = weight

    def myComp(self, other):
        r = 0
        if self.weight < other.weight:
            r = -1
        elif self.weight > other.weight:
            r = 1
        elif self.word < other.word:
            r = -1
        elif self.word > other.word:
            r = 1
        return r

    def __lt__(self, other):
        return self.myComp(other) < 0
    def __gt__(self, other):
        return self.myComp(other) > 0
    def __eq__(self, other):
        return self.myComp(other) == 0
    def __le__(self, other):
        return self.myComp(other) <= 0
    def __ge__(self, other):
        return self.myComp(other) >= 0
    def __ne__(self, other):
        return self.myComp(other) != 0

class char_frequencies:
    def __init__(self, mask="....."):
        self.mask=mask
        self.c = []
        self.count = []
        self.frequency = []
        self.nb_words = 0
        self.is_computed = False
        for i in range(0,26):
            self.c.append(chr(ord('a') + i))
            self.count.append(0)
            self.frequency.append(0.0)

    # weight a word 
    def weight_word(self, w):
        y = 0.0
        seen = set()
        for i in range(0,5):
            if self.mask[i] != '=':
                x = w[i]
                if not x in seen:
                    y += self.frequency[ord(x) - ord('a')]
                    seen.add(x)
        return y

    # parse a word and update the counts
    # the character positions marked as already know are ignored
    def add_word(self, w):
        seen = set()
        for i in range(0,5):
            if self.mask[i] != '=':
                x = w[i]
                if not x in seen:
                    self.count[ord(x) - ord('a')] += 1
                    seen.add(x)
        self.nb_words += 1
        self.is_computed = False

    # parse a list of words and update the frequencies
    # the character positions marked as already know are ignored
    def add_list(self, l):
        for w in l:
            self.add_word(w)

    # update the table of frequencies after adding words
    def set_frequencies(self):
        for i in range(0,26):
            self.frequency[i] = self.count[i]/self.nb_words
        self.is_computed = True

    def weight_and_sort_list(self, l, n, debug=False):
        r_list = []
        self.add_list(l)
        self.set_frequencies()
        for w in l:
            r_list.append(word_frequency(w, self.weight_word(w)))
        s_list = sorted(r_list, reverse=True)
        if debug:
            for wf in s_list[0:5]:
                print("Selected: " + wf.word + " (" + str(wf.weight) + ")")
        selected = []
        for wf in s_list[0:n]:
            selected.append(wf.word)
        return selected

class wordle_query:
    word_set = set(wordle_words.word_list)

    def __init__(self, w):
        if w == "":
            w = random.choice(wordle_words.word_list)
        elif not w in wordle_query.word_set:
            print("Weird: " + w)
        self.w = w
    
    def compare_word(w, trial5):
        ret = ""
        match = [ False, False, False, False, False ]
        present_set = set()
        for i in range(0,5):
            x = trial5[i]
            if x == w[i]:
                match[i] = True
            else:
                present_set.add(w[i])
        for i in range(0,5):
            x = trial5[i]
            if match[i]:
                ret += "="
            elif x in present_set:
                ret += "*"
            else:
                ret += "."
        return ret

    def compare(self, trial5):
        return wordle_query.compare_word(self.w, trial5)

# Does a guess match a pattern?
# For each position, we can see ".", "*" or "=".
# testing for =?
# - false if does not exactly match.
# testing for ".":
# - skip the character if marked as "="
# - for all other characters, mark false if match
# testing for "*"
# - mark false if match at position
# - skip if position is known
# - mark false if not found at least once at other position
# - Need to treat special cases with multiple occurence of
#   same letter. In NYT UI, the first ocurence is marked "*",
#   the next ones ".", but this works badly with our solver.
#

class wordle_solver:
    # Init  a solver. 
    def __init__(self, strategy=2, n_max=8, n_trials=0):
        # initialize the list of valid responses with the complete list.
        self.list = []
        for w in wordle_words.word_list:
            self.list.append(w)
        # Found will list either a dot or a match character, for each position
        self.found = [".", ".", ".", ".", "."]
        self.strategy=strategy
        self.n_max = n_max
        self.rec_string = ""

    def cx(self):
        c = wordle_solver()
        c.list = []
        for x in self.list:
            c.list.append(x)
        c.found = []
        for x in self.found:
            c.found.append(x)
        return c
  
    def pattern_match(self, w, guess, result):
        ret = True
        for i in range(0,5):
            r = result[i]
            if r == '=':
                if w[i] != guess[i]:
                    ret = False
            elif r == ".":
                # this character is excluded.
                g = guess[i]
                for j in range(0,5):
                    if result[j] != '=' and w[j] == g:
                        ret = False
                        break
            elif r == "*":
                g = guess[i]
                ret = False
                if w[i] != g:
                    for j in range(0,5):
                        if result[j] != '=' and w[j] == g:
                            ret = True
                            break
            if not ret:
                break
        return ret
    
    def filter(self, guess, result): 
        l = []
        for w in self.list:
            if self.pattern_match(w, guess, result):
                l.append(w)
        self.list = l

    # Process a guess. 
    # First, update all characters marked as "="
    def process(self, guess, result):
        try:
            removed = set()
            for i in range(0,5):
                if result[i] == "=" and self.found[i] == ".":
                    x = guess[i]
                    self.found[i] = x
            for i in range(0,5):
                if self.found[i] == ".":
                    x = guess[i]
                    if result[i] == '*':
                        removed.add(x)
                    elif result[i] == '.' and x in removed:
                        result = result[0:i] + "*" + result[i+1:]
            self.filter(guess, result)
        except:
            print("Result(" + guess + "," + result + " )")
            traceback.print_exc()

    def show(self):
        found = ""
        for a in self.found:
            found += a
        print("Found: " + found)

    def long_pick(l, debug=False):
        lc_max = 0
        lc_w = []
        nb_print = 0
        for w in l:
            ltrs = set()
            for i in range(0,5):
                x = w[i]
                if not x in ltrs:
                    ltrs.add(x)
            if debug:
                print("??? " + w + ": " + str(len(ltrs)))
                nb_print += 1
                if nb_print > 5:
                    debug = False
            if len(ltrs) > lc_max:
                lc_max = len(ltrs)
                lc_w = [ w ]
            elif len(ltrs) == lc_max:
                lc_w.append(w)
        return lc_w[0]

    def frequency_list(self, l_max, debug=False):
        f_mask = ""
        for i in range(0,5):
            if self.found[i] == ".":
                f_mask += "."
            else:
                f_mask += "="
        if debug:
            print("Frequency mask:" + f_mask)
        cf = char_frequencies(f_mask)
        return cf.weight_and_sort_list(self.list, l_max, debug=debug)

    def frequency_pick(self, debug=False):
        l = self.frequency_list(1, debug)
        return l[0]

    # recursive resolver, rank N.
    # pick up to N possible responses or solutions at random
    # for each response, 
    #     for each solution (minimax)
    #         run a random resolver until success.
    #         count the number of steps
    #     count the highest number of steps for the solutions.
    # retain the responses with the lowest numbers of steps (minimax)
    # return one of the best responses at random.
    def suggest_recursive(self, n_max, debug=False, rank=0):
        minimax = len(self.list) + rank + 10
        minisum = 1000000
        minimax_list = []
        selected = []
        if n_max > len(self.list):
            n_max = len(self.list)
            selected = self.list
        else:
            if debug:
                print(self.rec_string + "Select " + str(n_max) + " responses by frequency.")
            selected = self.frequency_list(n_max, False)

        max_recurs = 6
        if rank == 0:
            max_recurs = 15
        elif rank > 2:
            max_recurs = 6 - rank

        for response in selected:
            # for each solution that is still valid, compute
            # the maximum number of steps (response max) and
            # the total number of steps for the response.
            response_max = 0
            sum_max = 0
            if debug and rank <  6:
                print(str(rank) + ": Trying " + response)
            for solution in self.list:
                q = wordle_query(solution)
                s = self.cx()
                s_debug = debug
                if len(s.list) <= max_recurs:
                    s.strategy = 3
                else:
                    s_debug = False
                    s.strategy = 2
                s.n_max = 6
                s.rec_string = self.rec_string + ">"
                n = 1 + rank
                x = response
                while n + rank < 10:
                    r = q.compare(x)
                    if r == "=====":
                        break
                    n += 1
                    s.process(x,r)
                    x = s.suggest(s_debug, s_rank=n)
                sum_max += n
                    
                if n > response_max:
                    response_max = n
                    if response_max > 6 and minimax <= 6:
                        sum_max = minisum + len(s.list)
                        if debug:
                            print("Abandon " + response + " after " + solution + ":" + str(n))
                        break

            if (response_max <= 6 and minimax > 6) or \
               (response_max <= 6 and minimax <= 6 and sum_max < minisum) or \
               (response_max > 6 and minimax > 6 and (sum_max < minisum \
                or (sum_max == minisum and response_max < minimax))):
                minimax = response_max
                minisum = sum_max
                minimax_list = [ response ]
                if debug:
                    print(self.rec_string + "New best response: " + response + " (" + str(response_max) + ", " + str(sum_max) + ")")
            elif response_max == minimax and sum_max == minisum:
                minimax_list.append(response)
                if debug:
                    print(self.rec_string + "New good response: " + response + " (" + str(response_max) + ", " + str(sum_max) + ")")
            elif debug:
                print(self.rec_string + "Not a good response: " + response + " (" + str(response_max) + ", " + str(sum_max) + ")")
        # return wordle_solver.long_pick(minimax_list, debug)
        if len(minimax_list) == 0:
            print("Empty response at rank= " + str(rank) + " from:")
            for w in self.list:
                print("    " + w)
            exit()

        if debug:
            print("Selected: " + minimax_list[0])
        return minimax_list[0]

    def suggest(self, debug=False, s_rank=0):
        if self.strategy == 3:
            return self.suggest_recursive(self.n_max, debug, rank=s_rank)
        elif self.strategy == 2:
            return self.frequency_pick(debug)
        elif self.strategy == 1:
            return wordle_solver.long_pick(self.list)
        else:
            return self.list[0]
        

                    
                
    
     