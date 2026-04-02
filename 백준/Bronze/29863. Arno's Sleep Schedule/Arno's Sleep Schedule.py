import sys

sleep_hour = int(sys.stdin.readline())
awake_hour = int(sys.stdin.readline())

sleeping = awake_hour - sleep_hour

if sleeping < 0:
    print(sleeping + 24)
else:
    print(sleeping)