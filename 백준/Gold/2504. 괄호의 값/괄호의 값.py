import sys
input = sys.stdin.readline

def checkPossible(string):
    q = []
    for s in string:
        if s == "(" or s == "[":
            q.append(s)
        elif s == ")":
            if q and q[-1] == "(":
                q.pop()
            else:
                return False
        else:
            if q and q[-1] == "[":
                q.pop()
            else:
                return False
    return len(q) == 0

def solution():
    string = input().rstrip()
    if not checkPossible(string):
        return 0

    q = []
    for s in string:
        if s == "(" or s == "[":
            q.append(s)
        elif s == ")":
            if q[-1] == "(":
                q.pop()
                q.append(2)
            elif isinstance(q[-1], int):
                tmp = int(q[-1]) * 2
                q.pop()
                q.pop()
                q.append(tmp)
        elif s == "]":
            if q[-1] == "[":
                q.pop()
                q.append(3)
            elif isinstance(q[-1], int):
                tmp = int(q[-1]) * 3
                q.pop()
                q.pop()
                q.append(tmp)
        while len(q) >= 2 and isinstance(q[-1], int) and isinstance(q[-2], int):
            q.append(q.pop() + q.pop())

    return q.pop()
    
print(solution())