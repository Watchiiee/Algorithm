import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    
    priorities = list(map(int, sys.stdin.readline().split()))
    
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    
    count = 0 
    
    while queue:
        now = queue.popleft()
        
        if any(now[1] < q[1] for q in queue):
            queue.append(now)
        else:
            count += 1
            
            if now[0] == M:
                print(count)
                break