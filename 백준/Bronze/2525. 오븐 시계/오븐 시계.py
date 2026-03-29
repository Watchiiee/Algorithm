import sys

A, B = map(int, sys.stdin.readline().split())

C = int(sys.stdin.readline())

minutes = B + C

if minutes >= 60:
    if A + (minutes // 60) >= 24:
        print((A + (minutes // 60) - 24), minutes % 60)
    else:
        A += minutes // 60
        print(A, minutes % 60)

else:
    print(A, minutes)
