T= int(input())

for n in range(T):
    a, b = map(int,input().split())

    res = pow(a, b, 10)
    
    if res == 0:
        print(10)
    else:
        print(res)