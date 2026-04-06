import sys

S = list(sys.stdin.readline().strip())

times = 0

for i in S:
    if i == 'A' or i == 'B' or i == 'C':
        times += 3
    elif i == 'D' or i == 'E' or i == 'F':
        times += 4
    elif i == 'G' or i == 'H' or i == 'I':
        times += 5
    elif i == 'J' or i == 'K' or i == 'L':
        times += 6
    elif i == 'M' or i == 'N' or i == 'O':
        times += 7
    elif i == 'P' or i == 'Q' or i == 'R' or i == 'S':
        times += 8
    elif i == 'T' or i == 'U' or i == 'V':
        times += 9
    elif i == 'W' or i == 'X' or i == 'Y' or i == 'Z':
        times += 10

print(times)