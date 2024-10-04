import sys
input = sys.stdin.readline

def solution(num):
    if num[0] != '1' or num[-1] != '2':
        return False
    
    if num.count('1') != 1 or num.count('2') != 1:
        return False
    if num.count('5') != num.count('6'):
        return False
    
    for i in range(1, len(num) + 1):
        if i == len(num):
            break
        if num[i] == '3':
            if num[i - 1] != '4' and num[i - 1] != '6':
                return False
        elif num[i] == '4' or num[i] == '5':
            if num[i - 1] != '1' and num[i - 1] != '3':
                return False
        elif num[i] == '6' or num[i] == '7':
            if num[i - 1] != '8':
                return False
        elif num[i] == '8':
            if num[i - 1] != '5' and num[i - 1] != '7':
                return False
        elif num[i] == '2':
            if num[i - 1] != '4' and num[i - 1] != '6':
                return False

    return True

idx = 1
while True:
    c = input().rstrip()
    if c != '0':
        if solution(c):
            print(str(idx) + '. VALID')
        else:
            print(str(idx) + '. NOT')
        idx += 1
    else:
        break