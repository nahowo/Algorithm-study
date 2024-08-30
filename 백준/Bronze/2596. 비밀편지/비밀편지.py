import sys
input = sys.stdin.readline
code = {'000000': 'A', '001111': 'B', '010011': 'C', '011100': 'D', '100110': 'E', '101001': 'F', '110101': 'G', '111010': 'H'}

def compare(a, b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
            if cnt > 1:
                return False
    return True

def solution():
    n = int(input())
    incode = input().rstrip()
    decode = ''

    for i in range(0, n * 6, 6):
        flag = False
        word = incode[i : i + 6]
        if word in code:
            decode += code[word]
        else:
            for k, v in code.items():
                if compare(word, k) == True:
                    decode += v
                    flag = True
                    break
            if not flag:
                return (i // 6) + 1
    
    return decode

print(solution())