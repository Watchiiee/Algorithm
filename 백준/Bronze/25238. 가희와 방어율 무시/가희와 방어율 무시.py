import sys

a, b = map(int, sys.stdin.readline().split())

defense_cal = a  - (a * b / 100)

if (defense_cal >= 100):
    print("0")
else:
    print("1")