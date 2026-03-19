N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())

t_bundle = 0
for s in size:
    if s == 0:
        continue 
    
    if s % T == 0:
        t_bundle += s // T
    else:
        t_bundle += (s // T) + 1

print(t_bundle)

print(N // P, N % P)