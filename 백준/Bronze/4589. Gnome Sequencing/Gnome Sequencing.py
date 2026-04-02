import sys

n = int(sys.stdin.readline())
print("Gnomes:")

for _ in range(n):
    original = list(map(int, sys.stdin.readline().split()))
    
    asc_sort = sorted(original)
    
    desc_sort = sorted(original, reverse=True)
    
    if original == asc_sort or original == desc_sort:
        print("Ordered")
    else:
        print("Unordered")