len = int(5)
step = int(4) - 1

pos = 0


res = "1"
pos = (pos + step) % len


while pos != 0:
    res += str(pos + 1)
    pos = (pos + step) % len

print(res)
