import sys
import math

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    print((math.factorial(N)) % 10)
