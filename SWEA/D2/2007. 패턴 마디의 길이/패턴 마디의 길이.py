T = int(input())

for tc in range(1, T + 1):
    s = input().strip()

    for length in range(1, 11): 
        if s[:length] == s[length : length * 2]:
            ans = length
            break

    print(f"#{tc} {ans}")