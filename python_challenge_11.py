import Image

image = Image.open("cave.jpg")
print image.size
half_size = tuple([n / 2 for n in image.size])
print half_size
odd = Image.new(image.mode, half_size)
even = Image.new(image.mode, half_size)

for x in xrange(1, image.size[0] - 1):
    for y in xrange(1, image.size[1] - 1):
        if x % 2 == 0 and y % 2 == 0:
            even.putpixel((x / 2, y / 2 ), image.getpixel((x,y)))
        if x % 2 == 0 and y % 2 == 1:
            odd.putpixel((x / 2, (y-1) / 2), image.getpixel((x,y)))
        if x % 2 == 1 and y % 2 == 0:
            even.putpixel(((x - 1) / 2, y / 2), image.getpixel((x, y)))
        else:
            print str(x) + ", " + str(y)
            odd.putpixel(((x - 1) / 2, (y - 1) / 2), 
                image.getpixel((x, y)))
odd.save("odd.jpg")
even.save("even.jpg")