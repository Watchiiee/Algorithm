N = int(input())
result = 0

for i in range(1, N + 1):
    digit_sum = sum(map(int, str(i)))
    
    target = i + digit_sum
    
    if target == N:
        result = i
        break 

print(result)