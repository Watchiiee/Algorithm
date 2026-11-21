T = int(input())

for tc in range(1, T + 1):
    nums = list(map(int, input().split()))

    total = sum(nums) - max(nums) - min(nums)
    avg_val = round(total / (len(nums) - 2))

    print(f"#{tc} {avg_val}")