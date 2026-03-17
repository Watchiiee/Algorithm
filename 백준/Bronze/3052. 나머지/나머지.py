num = []
for _ in range(10):
    n = int(input())
    num.append(n % 42)

unique_num = set(num)

print(len(unique_num))