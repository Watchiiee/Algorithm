N = int(input())

for i in range(1, N + 1):
    num = list(map(int, str(i)))
    
    cnt = 0  
    
    for j in num:
        if j != 0 and j % 3 == 0:
            cnt += 1
            
    if cnt > 0:
        print("-" * cnt, end=" ")
    else:
        print(i, end=" ")