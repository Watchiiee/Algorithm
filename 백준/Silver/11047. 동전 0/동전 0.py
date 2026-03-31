import sys

N, K = map(int, sys.stdin.readline().split())

count = 0 
coin_list = set()

for n in range(N):
    coin = int(sys.stdin.readline().strip())
    coin_list.add(coin)

for i in sorted(coin_list, reverse=True):
    if i > K :
        continue
    elif i == 0 :
        break
    else:
        count += K //i
        K = K % i

print(count)