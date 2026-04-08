import sys

n = int(sys.stdin.readline())

for _ in range(n):
    a, h = map(float, sys.stdin.readline().split())

    b = (2 * a) / h 
    
    print("The height of the triangle is", f"{b:.2f}", "units")
