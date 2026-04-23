import sys

count = 0

while 1:
    N = sys.stdin.readline()

    if not N.strip():
        break

    count += int(N)

print(count)
