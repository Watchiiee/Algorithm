T = int(input())
grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    scores = []

    for i in range(N):
        mid, final, hw = map(int, input().split())
        total = mid * 0.35 + final * 0.45 + hw * 0.20
        scores.append(total)

    target_score = scores[K - 1]

    scores.sort(reverse=True)

    rank = scores.index(target_score)

    grade_idx = rank // (N // 10)

    print(f"#{tc} {grades[grade_idx]}")