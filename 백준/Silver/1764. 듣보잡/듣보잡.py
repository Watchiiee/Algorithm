import sys

n, m = map(int, sys.stdin.readline().split())

no_listen = set()
for _ in range(n):
    no_listen.add(sys.stdin.readline().strip())

no_see = set()
for _ in range(m):
    no_see.add(sys.stdin.readline().strip())

result = sorted(list(no_listen & no_see))

print(len(result))
for name in result:
    print(name)