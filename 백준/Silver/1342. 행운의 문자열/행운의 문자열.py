import sys
input = sys.stdin.readline

def recursion(pre, l, d):
    answer = 0
    if l == n:
        return 1
    
    for i in d.keys():
        if d[i] == 0 or i == pre:
            continue
        d[i] -= 1
        answer += recursion(i, l + 1, d)
        d[i] += 1
    
    return answer

def solution():
    global n
    s = list(input().rstrip())
    n = len(s)
    d = dict()
    for i in s:
        d[i] = d.get(i, 0) + 1

    return recursion("", 0, d)

print(solution())