import sys

X = int(sys.stdin.readline())

sticks = [64] 

while sum(sticks) > X:
    sticks.sort()
    shortest = sticks.pop(0)
    half = shortest // 2
    
    if sum(sticks) + half >= X:
        sticks.append(half)
    else:
        sticks.append(half)
        sticks.append(half)

print(len(sticks))