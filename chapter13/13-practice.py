f = open("1-bluemarble_west.jpg", "rb")
g = open("earth-copy.jpg", "wb")
count = 0
while True:
    buf = f.read(1024)
    if len(buf) == 0:
         break
    g.write(buf)
    count += 1

print(count)
f.close()
g.close()