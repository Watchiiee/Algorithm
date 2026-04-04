import sys

A, B, C = map(int, sys.stdin.readline().split())

if(A == B and B == C and C == A):
    price = 10000 + A * 1000
elif A == B:
    price = 1000 + A * 100
elif B == C:
    price = 1000 + B * 100
elif C == A:
    price = 1000 + C * 100
else:
    price = (max(A, B, C) * 100)

print(price)