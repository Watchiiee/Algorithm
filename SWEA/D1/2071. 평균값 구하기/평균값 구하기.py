T = int(input())
ans = 1

for _ in range(T):
    nums = list(map(int, input().split()))
    avg = round(sum(nums) / len(nums))
    print(f"#{ans} {avg}")
    ans += 1
