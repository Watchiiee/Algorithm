import sys
import math

N = int(sys.stdin.readline())

N_fact = math.factorial(N)

count = 0
num= 10

while(1):
    if(N_fact < num):
        break
    else:
        if (N_fact % num == 0):
            count += 1
        num *= 10

print(count)