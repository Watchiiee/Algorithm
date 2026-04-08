import sys

count = 0

while(True):
    line = sys.stdin.readline().strip()
    
    if not line:
        break

    if (line == "gum gum for jay jay"):
        count += 1

print(count)
