import math

T = int(input())

for n in range(T):
    N, M = map(int,input().split())

    N_fact = math.factorial(N)
    M_fact = math.factorial(M)
    M_N_fact = math.factorial(M-N)

    result = M_fact // (N_fact * M_N_fact)

    print(result)
