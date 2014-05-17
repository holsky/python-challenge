#reads whole text as one chunk
import string
with open("python_challenge_3.txt") as f:
    s = ''.join([line.strip() for line in f])
    filter(lambda x: x in string.letters, s)
