import sys
input = sys.stdin.readline
MAX_LENGTH = 1000001

def solution():
    global s, pt
    n = int(input())
    s = [False] * MAX_LENGTH
    pt = -1

    for _ in range(n):
        tmp = input().rstrip()
        try:
            cmd, x = map(int, tmp.split())
        except:
            cmd, x = int(tmp), 0
        stack(cmd, x)
    return
    
def stack(cmd, x):
    global pt
    if cmd == 1: # push
        pt += 1
        s[pt] = x
    elif cmd == 2: # pop
        if isEmpty():
            result.append(-1)
        else:
            result.append(s[pt])
            pt -= 1
    elif cmd == 3: # len
        result.append(pt + 1)
    elif cmd == 4: # isEmpty
        result.append(isEmpty())
    elif cmd == 5: # peek
        if isEmpty():
            result.append(-1)
        else:
            result.append(s[pt])

def isEmpty():
    if pt == -1:
        return 1
    return 0

result = []
solution()
for i in result:
    print(i)