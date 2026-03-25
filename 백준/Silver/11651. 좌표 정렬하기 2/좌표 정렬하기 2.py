import sys

N = int(sys.stdin.readline())

coordinate = []
for n in range(N):
    xy = list(map(int, sys.stdin.readline().split()))
    coordinate.append(xy)

coordinate.sort(key = lambda x: (x[1], x[0]))

for point in coordinate:
    print(*point)