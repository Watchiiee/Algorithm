import sys

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()
S = sys.stdin.readline().strip()

if (S in A) and (S in B):
    print("YES")
else:
    print("NO")
