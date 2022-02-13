#!/usr/bin/python
# coding=utf-8
#
# This module implements the rules

import words5
import random

class wordle_query:
    word_set = set(words5.word_list)

    def __init__(self, w):
        if w == "":
            w = random.choice(words5.word_list)
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

class wordle_solver:
    def __init__(self):
        self.list = []
        for w in words5.word_list:
            self.list.append(w)
        self.found = [".", ".", ".", ".", "."]
        self.excluded = set()
        self.included = set()

    def cx(self):
        c = wordle_solver()
        c.list = []
        for x in self.list:
            c.list.append(x)
        c.found = []
        for x in self.found:
            c.found.append(x)
        c.excluded = set()
        for x in self.excluded:
            c.excluded.add(x)
        c.included = set()
        for x in self.included:
            c.included.add(x)
        return c

    def pattern_match(self, w, guess, result):
        ret = True
        not_matched = set()
        for i in range(0,5):
            x = w[i]
            if self.found[i] != ".":
                if x != self.found[i]:
                    ret = False
                    break
            elif result[i] != "=":
                if x == guess[i]:
                    ret = False
                    break
                elif x in self.excluded:
                    ret = False
                    break
                else:
                    not_matched.add(x)
        if ret:
            for l in self.included:
                if not l in not_matched:
                    ret = False
        return ret
        
    def filter(self, guess, result): 
        l = []
        for w in self.list:
            if self.pattern_match(w, guess, result):
                l.append(w)
        self.list = l

    def process(self, guess, result):
        removed = set()
        for i in range(0,5):
            if result[i] == "=" and self.found[i] == ".":
                x = guess[i]
                self.found[i] = x
                if x in self.included:
                    self.included.remove(x)
        for i in range(0,5):
            x = guess[i]
            if self.found[i] == ".":
                if result[i] == "*":
                    if not x in self.included:
                        self.included.add(x)
                elif result[i] == "." and not x in self.excluded:
                    self.excluded.add(x)
        self.filter(guess, result)

    def show(self):
        found = ""
        for a in self.found:
            found += a
        include = ""
        for b in self.included:
            include += b
        exclude = ""
        for c in self.excluded:
            exclude += c
        print("Found: " + found + ", include: [" + include + "], exclude: [" + exclude + "]")

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
        return random.choice(lc_w)

    def suggest(self):
        return wordle_solver.long_pick(self.list)

    # recursive resolver, rank N.
    # pick up to N possible responses or solutions at random
    # for each response, 
    #     for each solution (minimax)
    #         run a random resolver until success.
    #         count the number of steps
    #     count the highest number of steps for the solutions.
    # retain the responses with the lowest numbers of steps (minimax)
    # return one of the best responses at random.
    def suggest_recursive(self, n_max,debug=False):
        minimax = len(self.list)
        minisum = 1000000
        minimax_list = []
        selected = []
        if n_max > len(self.list):
            n_max = len(self.list)
            selected = self.list
        else:
            origin = []
            for o in self.list:
                origin.append(o)
            for i in range(0, n_max):
                x = random.choice(origin)
                origin.remove(x)
                selected.append(x)
        for response in selected:
            response_max = 0
            sum_max = 0
            for solution in selected:
                q = wordle_query(solution)
                s = self.cx()
                n = 1
                x = response
                # print(response + ":" + solution + ":" + str(len(s.list)))
                while n < 10:
                    r = q.compare(x)
                    if r == "=====":
                        break
                    n += 1
                    s.process(x,r)
                    # for w in s.list:
                    #    print("--- " + w)
                    # print(response + ":" + solution + ":" + str(n) + ":" + x + ":" + r + ":" + str(len(s.list)))
                    x = s.suggest()
                sum_max += n
                if n > response_max:
                    response_max = n
                    if response_max > minimax:
                        break
            if response_max < minimax:
                minimax = response_max
                minisum = sum_max
                minimax_list = [ response ]
                # print("New best response: " + response + " (" + str(minimax) + ")")
            elif response_max == minimax:
                if sum_max < minisum:
                    minisum = sum_max
                    minimax_list = [ response ]
                    # print("New best response: " + response + " (" + str(minimax) + ")")
                else:
                    minimax_list.append(response)
                    # print("New good response: " + response + " (" + str(minimax) + ")")
        return wordle_solver.long_pick(minimax_list, debug)


        

                    
                
    
     