import sys

N = int(sys.stdin.readline())

coordinate = []
for n in range(N):
    xy = list(map(int, sys.stdin.readline().split()))
    coordinate.append(xy)

for point in sorted(coordinate):
    print(*point)