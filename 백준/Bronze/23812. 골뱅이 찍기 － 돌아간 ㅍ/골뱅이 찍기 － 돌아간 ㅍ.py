import sys

n = int(sys.stdin.readline())

for _ in range(n):
    print('@' * n + ' ' * (n * 3) + '@' * n)

for _ in range(n):
    print('@' * (n * 5))

for _ in range(n):
    print('@' * n + ' ' * (n * 3) + '@' * n)

for _ in range(n):
    print('@' * (n * 5))

for _ in range(n):
    print('@' * n + ' ' * (n * 3) + '@' * n)