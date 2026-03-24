import sys
import math

N, K = map(int, sys.stdin.readline().split())

N_fact = math.factorial(N)
K_fact = math.factorial(K)
N_K_fact = math.factorial(N-K)

NK = N_fact / (K_fact * N_K_fact)

print(math.ceil(NK))