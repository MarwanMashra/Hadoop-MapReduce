#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""mapper.py"""

import sys

for line in sys.stdin:
    line = line.strip()
    if line:
        lang, word = line.split(' ',1)
        if lang=="français":
            print ('%s\t%s' % (word, 'fr'))
        elif lang=="english":
            print ('%s\t%s' % (word, 'en'))

