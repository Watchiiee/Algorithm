import sys
from collections import Counter

N = int(sys.stdin.readline())
N_cards = list(map(int, sys.stdin.readline().split()))

count = Counter(N_cards)

M = int(sys.stdin.readline())
M_cards = list(map(int, sys.stdin.readline().split()))


ans = []
for card in M_cards:
    ans.append(count[card])

print(*(ans))