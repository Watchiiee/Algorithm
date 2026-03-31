import sys

N = int(sys.stdin.readline())

people = list(map(int, sys.stdin.readline().split()))

people.sort()

time = 0
current_sum = 0

for i in people:
    current_sum += i
    time += current_sum

print(time)