T = int(input())

for i in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    A_total = P * W

    if R >= W:
        B_total = Q
    else:
        B_total = Q + S * (W - R)

    if A_total <= B_total:
        print(f"#{i} {A_total}")
    else:
        print(f"#{i} {B_total}")
