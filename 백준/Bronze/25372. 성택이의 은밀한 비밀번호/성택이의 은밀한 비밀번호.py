import sys

N = int(sys.stdin.readline())

for _ in range(N):
    T = sys.stdin.readline().strip()
    if (len(T) >= 6) and (len(T) <= 9):
        print("yes")
    else:
        print("no")
