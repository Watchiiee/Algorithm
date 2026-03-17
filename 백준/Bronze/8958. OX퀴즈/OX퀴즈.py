num = int(input())

for _ in range(num):
    ox_list = input()
    total_score = 0
    current_score = 0

    for n in ox_list:
        if n == 'O':
            current_score += 1
            total_score += current_score
        else:
            current_score = 0
    print(total_score)