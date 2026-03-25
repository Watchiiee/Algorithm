import sys
from collections import deque

N = int(sys.stdin.readline())

cards = deque(range(1, N + 1))


while len(cards) > 1:
    cards.popleft()
    
    top = cards.popleft()

    cards.append(top)

print(cards[0])