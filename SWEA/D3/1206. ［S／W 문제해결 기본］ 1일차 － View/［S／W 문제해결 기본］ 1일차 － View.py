for tc in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    
    ans = 0
    for i in range(2, N - 2):
        max_neighbor = max(buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2])
        
        if buildings[i] > max_neighbor:
            ans += buildings[i] - max_neighbor
            
    print(f"#{tc} {ans}")