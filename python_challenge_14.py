import Image

def fold_spiral(move_direction, line_length):
    global z
    for i in xrange(line_length):
        move_direction()
        spiral.putpixel((x,y), wire.getpixel((z, 0)))
        z += 1


def move_right():
    global x
    x += 1

def move_down():
    global y
    y += 1

def move_left():
    global x
    x -= 1

def move_up():
    global y
    y -= 1
    
wire = Image.open("wire.png")
spiral = Image.new(wire.mode, (100,100))

z = 0
x, y = (-1, 0)
rounds = 50

for round_number in xrange(rounds, 0, -1):
    round_length = round_number * 2
    fold_spiral(move_right, round_length)
    fold_spiral(move_down, round_length - 1)
    fold_spiral(move_left, round_length - 1)
    fold_spiral(move_up, round_length - 2)

spiral.save("spiral.png")




#100+99+99+98 + (98+97+97+96) + (96 + 95 + 95 + 94)
