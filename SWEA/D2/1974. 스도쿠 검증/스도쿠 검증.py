T = int(input())

for tc in range(1, T + 1):
    grid = [list(map(int, input().split())) for _ in range(9)]
    ans = 1  

    for i in range(9):
        row = grid[i]
        col = [grid[r][i] for r in range(9)]
        
        if len(set(row)) != 9 or len(set(col)) != 9:
            ans = 0
            break

    if ans == 1:
        for sr in (0, 3, 6):
            for sc in (0, 3, 6):
                box = []
                for dr in range(3):
                    for dc in range(3):
                        box.append(grid[sr + dr][sc + dc])
                
                if len(set(box)) != 9:
                    ans = 0
                    break
            if ans == 0:
                break

    print(f"#{tc} {ans}")