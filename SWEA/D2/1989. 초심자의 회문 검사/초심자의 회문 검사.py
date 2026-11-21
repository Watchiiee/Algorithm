T = int(input())

for tc in range(1, T + 1):
    word = input().strip()
    reversed_word = word[::-1]

    if word == reversed_word:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")