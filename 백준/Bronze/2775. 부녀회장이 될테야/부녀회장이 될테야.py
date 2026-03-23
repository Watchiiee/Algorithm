apart = [[0] * 15 for _ in range(15)]

for i in range(1, 15):
    apart[0][i] = i

for floor in range(1, 15):
    for room in range(1, 15):
        apart[floor][room] = apart[floor][room-1] + apart[floor-1][room]

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    print(apart[k][n])
