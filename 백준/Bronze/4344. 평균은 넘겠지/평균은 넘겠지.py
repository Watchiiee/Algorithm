import sys

C = int(sys.stdin.readline())

for _ in range(C):
    N = list(map(int, sys.stdin.readline().split()))
    score = 0
    for i in range(1, len(N)):
        score += N[i]

    avg_score = score / N[0]
    upper_people = 0

    for j in range(1, len(N)):
        if N[j] > avg_score:
            upper_people += 1

    print(f"{(upper_people / (len(N) -1) * 100):.3f}%")
