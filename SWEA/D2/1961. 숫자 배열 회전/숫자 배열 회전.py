T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    rot90 = [[0] * N for _ in range(N)]
    rot180 = [[0] * N for _ in range(N)]
    rot270 = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            rot90[c][N - 1 - r] = grid[r][c]
            rot180[N - 1 - r][N - 1 - c] = grid[r][c]
            rot270[N - 1 - c][r] = grid[r][c]

    print(f"#{tc}")
    for i in range(N):
        for j in range(N):
            print(rot90[i][j], end="")
        print(" ", end="")

        for j in range(N):
            print(rot180[i][j], end="")
        print(" ", end="")

        for j in range(N):
            print(rot270[i][j], end="")
        print()