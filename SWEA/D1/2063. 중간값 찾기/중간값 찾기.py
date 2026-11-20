N = int(input())

nums = list(map(int, input().split()))
nums.sort()

M = N // 2
print(nums[M])
