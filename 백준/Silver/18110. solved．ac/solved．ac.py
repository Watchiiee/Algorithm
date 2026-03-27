import sys

def my_round(val):
    if val - int(val) >= 0.5:
        return int(val) + 1
    else:
        return int(val)

n = int(sys.stdin.readline())

if n == 0:
    print(0)
else:
    opinions = []
    for _ in range(n):
        opinions.append(int(sys.stdin.readline()))
    
    opinions.sort()
    
    exception_people = my_round(n * 0.15)

    target = opinions[exception_people : n - exception_people]

    if not target:
        print(0)
    else:
        calculate = sum(target) / len(target)
        print(my_round(calculate))