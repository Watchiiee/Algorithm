import sys

D, H, W = map(int, sys.stdin.readline().split())

ratio = (D**2 / (H**2 + W**2)) ** 0.5

print(int(H * ratio), int(W * ratio))
