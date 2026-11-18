T = int(input())
num = 1

for i in range(T):
    sum = 0
    nums = list(map(int, input().split()))
    for j in nums:
        if j % 2 != 0:
            sum += j
    print(f"#{num}", sum)
    num += 1
