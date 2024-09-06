import sys
input = sys.stdin.readline

def change(n, i):
    answer = []
    while n >= 1:
        answer.append(str(n % i))
        n //= i
    answer = answer[:: -1]
    return ''.join(answer)

def check(x):
    for i in range(len(x) // 2):
        if x[i] != x[len(x) - i - 1]:
            return False
    return True

def solution():
    flag = False
    n = int(input())
    for i in range(2, 11):
        result = change(n, i)
        if check(result):
            flag = True
            print(i, result)
    if not flag:
        print("NIE")

solution()