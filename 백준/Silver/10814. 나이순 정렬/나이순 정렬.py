import sys

N = int(sys.stdin.readline())
members = []

for n in range(N):
    age, name = sys.stdin.readline().split()
    members.append([int(age), name])

members.sort(key = lambda x: x[0])

for m in members:
    print(m[0], m[1])