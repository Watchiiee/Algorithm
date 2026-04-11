import sys

N = int(sys.stdin.readline())

count = 0

for _ in range(N):
    S = sys.stdin.readline().strip()
    
    error = 0

    for i in range(len(S) - 1):
        if S[i] != S[i + 1]:
            test = S[i + 1 :]
            if S[i] in test:
                error += 1
                break
    if error == 0:
        count += 1

print(count)