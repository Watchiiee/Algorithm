import sys

n = int(sys.stdin.readline())

numbers = []

for _ in range(n):
    number= int(sys.stdin.readline())
    numbers.append(number)

count = 1

stack = []
is_possible = True
result = []

for i in numbers:
    while count <= i:
        stack.append(count)
        count += 1
        result.append("+")
    
    if stack[-1] == i:
        stack.pop()
        result.append("-")
    else:
        is_possible = False
        break

if is_possible:
    print("\n".join(result))
else:
    print("NO")


    