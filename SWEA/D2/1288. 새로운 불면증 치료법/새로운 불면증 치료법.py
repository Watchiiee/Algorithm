T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    seen = set()  
    k = 0

    while len(seen) < 10:
        k += 1
        num = N * k

        for ch in str(num):
            seen.add(ch)

    print(f"#{tc} {N * k}")