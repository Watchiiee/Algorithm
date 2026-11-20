T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    grid = [[0] * N for _ in range(N)]

    for n in range(N):
        for k in range(n + 1):
            if k == 0 or k == n:
                grid[n][k] = 1
            else:
                grid[n][k] = grid[n - 1][k] + grid[n - 1][k - 1]

    print(f"#{tc}")
    for n in range(N):
        for k in range(N):
            if grid[n][k] != 0:
                print(grid[n][k], end=" ")
        print() 