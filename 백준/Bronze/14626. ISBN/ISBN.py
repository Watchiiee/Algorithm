import sys
isbn = sys.stdin.readline()

for i in range(10):
    total = 0
    
    for idx in range(13):

        if isbn[idx] == '*':
            current_num = i
        else:
            current_num = int(isbn[idx])

        if idx % 2 == 0:
            total += current_num * 1
        else:
            total += current_num * 3
            

    if total % 10 == 0:
        print(i)
        break