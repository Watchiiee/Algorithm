import sys

N = int(sys.stdin.readline())

pattern = list(sys.stdin.readline().strip())

for _ in range(N - 1):
    current_file = sys.stdin.readline().strip()
    
    for i in range(len(pattern)):
        if pattern[i] != current_file[i]:
            pattern[i] = '?'

print("".join(pattern))
