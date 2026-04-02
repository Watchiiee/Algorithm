import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    clothes = {}

    for _ in range(n):
        name, kind = sys.stdin.readline().split()

        if kind in clothes:
            clothes[kind] += 1
        else:
            clothes[kind] = 1
    
    answer = 1

    for kind in clothes:
        answer *= clothes[kind] + 1
    
    print(answer - 1)