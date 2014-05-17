import zipfile, re, collections

comments = []
next_file = "{}.txt"
regex = "Next nothing is (\d+)"
next_value = 90052

file = zipfile.ZipFile("channel.zip")

while True:
    try:
        content = file.read(next_file.format(next_value))
        print content
        next_value = re.match(regex, content).group(1)
        print next_value
    except:
        print "err: " + file.read(next_file.format(next_value))
        break
    comments.append(file.getinfo(next_file.format(next_value)).comment)

print "".join(comments)