N = int(input())

numbers = list(map(int, input().split()))

prime_count = 0 

for n in numbers:
    if n == 1:
        continue
    
    is_prime = True
    
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    
    if is_prime:
        prime_count += 1

print(prime_count)