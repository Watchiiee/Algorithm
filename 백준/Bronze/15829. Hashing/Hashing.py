L = int(input())
S = input()

answer = 0
M = 1234567891
r = 31

for i in range(L):
    num = ord(S[i]) - ord("a") + 1

    answer += num * (r**i)

print(answer % M)
