import re, Image

i = Image.open("oxygen.png")
row = [i.getpixel((x, 45)) for x in xrange(0, i.size[0], 7)]
decoded_message = "".join([chr(pixel[0]) for pixel in row])
extracted_solution = re.findall("\d+", decoded_message)
print "".join([chr(int(c)) for c in extracted_solution])