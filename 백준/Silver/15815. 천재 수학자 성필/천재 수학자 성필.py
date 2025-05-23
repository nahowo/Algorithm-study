import sys
input = sys.stdin.readline

def solution():
    formular = input().rstrip()
    n = len(formular)
    stack = []
    
    for i in formular:
        if i.isnumeric():
            stack.append(int(i))
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(calc(a, b, i))
    return stack.pop()

def calc(a, b, i):
    if i == '+':
        return a + b
    elif i == '-':
        return a - b
    elif i == '*':
        return a * b
    else:
        return a // b

print(solution())