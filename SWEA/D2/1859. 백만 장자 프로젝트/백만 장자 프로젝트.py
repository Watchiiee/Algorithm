T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    prices = list(map(int, input().split()))
    
    ans = 0
    max_price = 0
    
    for i in reversed(range(N)):
        if prices[i] > max_price:
            max_price = prices[i]  
        else:
            ans += max_price - prices[i]  
            
    print(f"#{tc} {ans}")