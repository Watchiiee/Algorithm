import sys

while(True):
    line = sys.stdin.readline()

    if not line:
        break

    N, S = map(int, line.split())
    print(S // (N + 1))