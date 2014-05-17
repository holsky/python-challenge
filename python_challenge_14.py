import Image

wire = Image.open("wire.png")
spiral = Image.new(wire.mode, (100,100))

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

z = 0
x, y = (-1,0)
for i in xrange(50, 0, -1):
    #print "({}, {}, {}, {})".format(str(i), str(i-1), str(i-1), str(i-2))
    for j in xrange(i + 1):
        x += 1
        print "({}, {})".format(str(x), str(y))
        spiral.putpixel((x,y), wire.getpixel((z, 0)))
        z += 1
    for j in xrange(i):
        print "({}, {})".format(str(x), str(y))
        y += 1
        spiral.putpixel((x,y), wire.getpixel((z, 0)))
        z += 1
    for j in xrange(i):
        print "({}, {})".format(str(x), str(y))        
        x -= 1
        spiral.putpixel((x,y), wire.getpixel((z, 0)))
        z += 1
    for j in xrange(i - 1):
        print "({}, {})".format(str(x), str(y))
        y -= 1
        spiral.putpixel((x,y), wire.getpixel((z, 0)))
        z += 1

spiral.save("spiral.png")


#100+99+99+98 + (98+97+97+96) + (96 + 95 + 95 + 94)
