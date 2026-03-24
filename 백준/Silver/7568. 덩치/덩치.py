import sys

N = int(sys.stdin.readline())

data = [[0] * 2 for _ in range(N)]

for n in range(N):
    x, y= map(int,sys.stdin.readline().split())
    data[n] = x, y

ans = []
for i in range(N):
    rank = 1 
    for j in range(N):
        if i == j: continue 
        
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            rank += 1
    ans.append(rank)

print(*(ans))