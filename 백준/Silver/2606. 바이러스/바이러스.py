import sys

n = int(sys.stdin.readline())

v = int(sys.stdin.readline())

graphs = [[] for _ in range(n + 1)]

for i in range(v):
    a, b = map(int, sys.stdin.readline().split())
    graphs[a].append(b)
    graphs[b].append(a)

count = 0

visited = [False] * (n + 1)

def algorithm(num):
    global count
    visited[num] = True

    for i in graphs[num]:
        if not visited[i]:
            count += 1
            algorithm(i)
    

algorithm(1)
print(count)