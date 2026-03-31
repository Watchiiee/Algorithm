import sys

N, M = map(int, sys.stdin.readline().split())

id_password = dict()

for i in range(N):
    user_id, user_pw = sys.stdin.readline().split()

    id_password[user_id] = user_pw

for _ in range(M):
    site = sys.stdin.readline().strip()
    print(id_password[site])