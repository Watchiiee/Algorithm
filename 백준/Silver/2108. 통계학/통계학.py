import sys
from collections import Counter

N = int(sys.stdin.readline())

numbers = []

for _ in range(N):
    number = int(sys.stdin.readline())
    numbers.append(number)

mean = round(sum(numbers) / N )

sorted_numbers = sorted(numbers)
median = sorted_numbers[N // 2]

count = Counter(sorted_numbers).most_common()

if len(count) > 1 and count[0][1] == count[1][1]:
    mode = count[1][0]
else:
    mode = count[0][0]

num_range = sorted_numbers[-1] - sorted_numbers[0]

print(mean)
print(median)
print(mode)
print(num_range)