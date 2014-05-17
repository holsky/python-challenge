from __fututre__ import print_function
from collections import defaultdict


chars = defaultdict(int)

with open("python_challenge_3.txt") as f:
    for line in f:
        for c in line:
            chars[c] = chars[c] + 1

rare_chars = {k: v for k, v in chars.iteritems() if v < 5 }

with open("python_challenge_3.txt") as f:
    for line in f:
        for c in line:
             if c in rare_chars.keys():
                  print(c, end="")

# next solution
