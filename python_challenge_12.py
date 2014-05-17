with open("evil2.gfx", "rb") as h:
    data = h.read()
    new_data = [[], [], [], [], [], []]
    for byte in xrange(len(data) - 1):
        new_data[byte % 5].append(data[byte])

    for n, element in enumerate(new_data):
        with open (str(n + 1) + ".jpg", "wb") as outfile:
            outfile.write("".join(element))

