T = int(input())

for _ in range(T):
    tc_num = int(input())  
    scores = list(map(int, input().split())) 
    
    count = [0] * 101
    for s in scores:
        count[s] += 1
        
    max_cnt = max(count)  
    ans = 0
    
    # 100점부터 0점까지 거꾸로 확인 (최빈수가 여러 개면 큰 점수를 출력해야 하므로)
    for score in range(100, -1, -1):
        if count[score] == max_cnt:
            ans = score
            break
            
    print(f"#{tc_num} {ans}")