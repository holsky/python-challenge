import urllib
import re

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}"
response_re = "and the next nothing is (\d+)"
next_value = ""

while True:
    page = urllib.urlopen(url.format(next_value))
    response = page.read()
    print response
    next_value = int(re.match(response_re, response).group(1))
