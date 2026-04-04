import sys

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

dp = [0] * (N + 1)
for k in range(1, N + 1):
    dp[k] = dp[k-1] + numbers[k-1]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(dp[j] - dp[i-1])