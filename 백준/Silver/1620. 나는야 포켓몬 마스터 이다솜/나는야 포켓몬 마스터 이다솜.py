import sys

N, M = map(int, sys.stdin.readline().split())

Pokedex = {}

for i in range(1, N + 1):
    Pokemon_name = sys.stdin.readline().strip()
    
    Pokedex[str(i)] = Pokemon_name
    Pokedex[Pokemon_name] = i

for _ in range(M):
    question = sys.stdin.readline().strip()
    
    print(Pokedex[question])