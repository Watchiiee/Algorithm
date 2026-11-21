T = int(input())

for tc in range(1, T + 1):
    len_n, len_m = map(int, input().split())
    N = list(map(int, input().split()))
    M = list(map(int, input().split()))

    real_sum = 0

    if len(N) > len(M):
        for i in range(len(N) - len(M) + 1):
            test_sum = 0 
            for j in range(len(M)):
                test_sum += N[i + j] * M[j] 
            if test_sum > real_sum:
                real_sum = test_sum

    elif len(N) < len(M):
        for i in range(len(M) - len(N) + 1):
            test_sum = 0
            for j in range(len(N)):
                test_sum += N[j] * M[i + j]  
            if test_sum > real_sum:
                real_sum = test_sum

    else:
        test_sum = 0
        for i in range(len(N)):
            test_sum += N[i] * M[i]
        real_sum = test_sum

    print(f"#{tc} {real_sum}")