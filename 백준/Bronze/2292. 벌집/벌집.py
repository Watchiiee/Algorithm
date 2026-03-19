N = int(input())
floor = 1
count = 1

while( N > floor):
    floor += 6 * count
    count += 1

print(count)