#!/usr/bin/env python

from operator import itemgetter
import sys

current_word = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    if '\t' not in line:
        continue  # Skip malformed lines
    word, count = line.split('\t', 1)
    
    try:
        count = int(count)
    except ValueError:
        continue  # Ignore lines with non-integer counts

    if current_word == word:
        current_count += count
    else:
        if current_word is not None:
            print('%s\t%s' % (current_word, current_count))
        current_word = word
        current_count = count

# Output the final word
if current_word is not None:
    print('%s\t%s' % (current_word, current_count))