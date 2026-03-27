import sys
import math

def decimal(val):
    if val < 2:
        return False
    
    for n in range(2, int(math.sqrt(val)) + 1):
        if val % n == 0:
            return False
            
    return True

M, N = map(int, sys.stdin.readline().split())

for i in range (M, N + 1):
    if decimal(i):
        print(i)

