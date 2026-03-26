import sys


K = int(sys.stdin.readline())
stack = []

for n in range (K):
    num = int(sys.stdin.readline())
    
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
    
sum = 0
for n in stack:
    sum += n

print(sum)