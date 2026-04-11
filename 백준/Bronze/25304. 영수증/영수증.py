import sys

X = int(sys.stdin.readline())

N = int(sys.stdin.readline())

cal = 0

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    cal += a * b

if (X == cal):
    print("Yes")
else:
    print("No")