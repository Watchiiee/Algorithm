T = int(input())

for i in range(1, T + 1):
    N = int(input())
    box = [[0] * N for _ in range(N)]

    num = 1
    start = 0
    end = N - 1

    while start <= end:
        for j in range(start, end + 1):
            box[start][j] = num
            num += 1

        for k in range(start + 1, end + 1):
            box[k][end] = num
            num += 1

        for l in range(end -1, start -1, -1):
            box[end][l] = num
            num += 1

        for m in range(end -1, start, -1):
            box[m][start] =  num
            num += 1

        start += 1
        end -= 1

    print(f"#{i}")
    for row in box:
        print(*row)