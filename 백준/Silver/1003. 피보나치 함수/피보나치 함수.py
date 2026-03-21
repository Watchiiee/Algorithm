T = int(input())

zero = [1, 0, 1] + [0] * 38
one = [0, 1, 1] + [0] * 38
3
for i in range(3, 41):
    zero[i] = zero[i-1] + zero[i-2]
    one[i] = one[i-1] + one[i-2]

for _ in range(T):
    N = int(input())
    print(zero[N], one[N])

