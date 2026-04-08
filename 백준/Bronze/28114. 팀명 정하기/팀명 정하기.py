import sys

years = []    
members = []  

for _ in range(3):
    s, y, p = sys.stdin.readline().split()
    
    years.append(int(y) % 100)
    
    members.append([int(s), p[0]])

years.sort()
for y in years:
    print(y, end='')

print()

members.sort(key=lambda x: x[0], reverse=True)

for m in members:
    print(m[1], end='')
print()