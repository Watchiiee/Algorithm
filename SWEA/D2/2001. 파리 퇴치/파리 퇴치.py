T = int(input())

for i in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    max = 0

    for r in range(N - M + 1):
        for t in range(N - M + 1):
            total = 0

            for j in range(M):
                for k in range(M):
                    total += grid[r + j][t + k]

            if total > max:
                max = total

    print(f"#{i} {max}")
