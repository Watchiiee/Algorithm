import sys

n = int(sys.stdin.readline())

count = 0

for _ in range(n):
    d = int(sys.stdin.readline())
    if (d % 2 == 0):
        continue
    count += 1

print(count)