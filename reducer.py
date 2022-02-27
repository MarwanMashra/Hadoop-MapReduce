#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""reducer.py"""

from operator import itemgetter
import sys

current_word = None
word = None
french_found = False
english_found = False

for line in sys.stdin:
    line = line.strip()
    word, lang = line.split('\t', 1)
    if current_word == word:
        if lang=="fr":
            french_found = True
        elif lang=="en":
            english_found = True

    else:
        if current_word:
            if french_found and english_found:
                print ('%s\t%s' % (current_word, 0))
            french_found = False
            english_found = False

        current_word = word
        if lang=="fr":
            french_found = True
        elif lang=="en":
            english_found = True

if current_word == word and french_found and english_found:
    print ('%s\t%s' % (current_word, 0))
