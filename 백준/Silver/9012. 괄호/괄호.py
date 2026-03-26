import sys

T = int(sys.stdin.readline())

for n in range(T):
    line = sys.stdin.readline().rstrip('\n')

    stack = []
    is_balanced = True
    
    for char in line:
        if char == '(' or char == '[':
            stack.append(char)
            
        elif char == ')':
            if not stack or stack[-1] != '(':
                is_balanced = False
                break
            stack.pop()
            
        elif char == ']':
            if not stack or stack[-1] != '[':
                is_balanced = False
                break
            stack.pop()
            

    if is_balanced and not stack:
        print("YES")
    else:
        print("NO")