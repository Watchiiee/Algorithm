N = int(input())
num = []

L = list(map(int,input().split()))

top_num = max(L)

for n in L:
    num.append( n / top_num * 100)

average = sum(num) / len(num)
print(average)