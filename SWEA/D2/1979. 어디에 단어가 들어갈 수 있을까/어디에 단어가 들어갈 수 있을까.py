T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0

    for r in range(N):
        length = 0
        for c in range(N):
            if grid[r][c] == 1:
                length += 1
            else:
                if length == K:
                    cnt += 1
                length = 0
        if length == K:
            cnt += 1


    for c in range(N):
        length = 0
        for r in range(N):
            if grid[r][c] == 1:
                length += 1
            else:
                if length == K:
                    cnt += 1
                length = 0
        if length == K:
            cnt += 1

    print(f"#{tc} {cnt}")