import sys

T = sys.stdin.readline().strip()

Croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]


for i in Croatia:
    if i in T:
        T = T.replace(i, "*")

print(len(T))
