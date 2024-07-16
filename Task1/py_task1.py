import sys

len = int(sys.argv[1])
step = int(sys.argv[2]) - 1

pos = 0


res = "1"
pos = (pos + step) % len


while pos != 0:
    res += str(pos + 1)
    pos = (pos + step) % len

print(res)
