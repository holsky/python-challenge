from __future__ import print_function
import urllib
import pickle

page = urllib.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
data = pickle.load(page)
page.close()

for line in data:
    print("".join(sign[0] * sign[1] for sign in line))