import sys

N = int(sys.stdin.readline())

A = sys.stdin.readline().split()
B = sys.stdin.readline().split()

str_A = "".join(A)
str_B = "".join(B)

if int(str_A) < int(str_B):
    print(int(str_A))
else:
    print(int(str_B))
