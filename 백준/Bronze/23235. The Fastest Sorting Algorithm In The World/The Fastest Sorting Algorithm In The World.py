import sys

case_num = 1

while True:
    line = sys.stdin.readline().split()
    
    if not line or line[0] == '0':
        break

    print(f"Case {case_num}: Sorting... done!")
    
    case_num += 1