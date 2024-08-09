import sys
input = sys.stdin.readline

def multi(a, b):
    return [a[0], b[1]]

def calcCnt(a, b):
    return a[0] * a[1] * b[1]

def calcExp(exp, d):
    stack = []
    cnt = 0
    for i in range(len(exp)):
        if exp[i] == "(":
            pass
        elif exp[i] == ")":
            b = stack.pop()
            a = stack.pop()
            if a[1] != b[0]:
                return "error"
            stack.append(multi(a, b))
            cnt += calcCnt(a, b)
        else:
            stack.append(d[exp[i]])
    
    return cnt

def solution():
    n = int(input())
    matrices = dict()
    for _ in range(n):
        a, b, c = input().rstrip().split()
        matrices[a] = [int(b), int(c)]
    
    while True:
        exp = input().rstrip()
        if exp == "":
            break
        result = calcExp(exp, matrices)
        print(result)
    
solution()