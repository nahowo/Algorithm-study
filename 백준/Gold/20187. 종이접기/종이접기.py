import sys
import copy
input = sys.stdin.readline

reverseV = {0: 1, 1: 0, 2: 3, 3: 2}
reverseH = {0: 2, 1: 3, 2: 0, 3: 1}

def reverseHorizontal(paper):
    l = len(paper)
    result = copy.deepcopy(paper)
    for i in range(l // 2 + 1):
        for j in range(len(result[i])):
            result[i][j], result[l - i - 1][j] = reverseH[result[l - i - 1][j]], reverseH[result[i][j]]
    return result

def reverseVertical(paper):
    l = len(paper[0])
    result = copy.deepcopy(paper)
    for i in range(len(paper)):
        for j in range(l // 2 + 1):
            result[i][j], result[i][l - j - 1] = reverseV[result[i][l - j - 1]], reverseV[result[i][j]]
    return result

def sumHorizontal(a, b):
    result = []
    for i in a:
        result.append(i)
    for i in b:
        result.append(i)
    return result

def sumVertical(a, b):
    result = []
    for i in range(len(a)):
        tmp = a[i] + b[i]
        result.append(tmp)
    return result
    
def solution():
    k = int(input())
    method = list(input().rstrip().split())
    h = int(input())

    base = [[h]]
    for m in method[:: -1]: # 역으로 펼치기
        if m == 'D' or m == 'U': # 세로
            rBase = reverseHorizontal(base)
            if m == 'D':
                newBase = sumHorizontal(rBase, base)
            else:
                newBase = sumHorizontal(base, rBase)
        else: # 가로
            rBase = reverseVertical(base)
            if m == 'R':
                newBase = sumVertical(rBase, base)
            else:
                newBase = sumVertical(base, rBase)
        base = copy.deepcopy(newBase)
    
    for i, v in enumerate(base):
        base[i] = ' '.join(map(str, v))
    return '\n'.join(base)

print(solution())