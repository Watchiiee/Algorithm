import sys

T = int(sys.stdin.readline())

dp = [0] * 101

for i in range(1, 101):
    if i == 1 or i == 2 or i == 3:
        dp[i] = 1
    else:
        dp[i] = dp[i - 3] + dp[i - 2]


for _ in range(T):
    N = int(sys.stdin.readline())
    print(dp[N])