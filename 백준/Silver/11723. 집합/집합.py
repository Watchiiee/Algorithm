import sys

M = int(sys.stdin.readline())

S = set()

for _ in range(M):
    sentence = sys.stdin.readline().split()

    order = sentence[0]

    if (order == "add"):
        if int(sentence[1]) in S:
            continue
        else:
            S.add(int(sentence[1]))
    
    elif (order == "remove"):
        S.discard(int(sentence[1]))
    
    elif (order == "check"):
        if int(sentence[1]) in S:
            print(1)
        else:
            print(0)
    
    elif (order == "toggle"):
        if (int(sentence[1]) in S):
            S.remove(int(sentence[1]))
        else:
            S.add(int(sentence[1]))
    
    elif (order == "all"):
        S = set(range(1,21))

    elif(order == "empty"):
        S.clear()
    