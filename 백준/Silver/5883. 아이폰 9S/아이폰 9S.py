import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    b = []
    s = set()
    for _ in range(n):
        tmp = int(input())
        b.append(tmp)
        s.add(tmp)
    
    maxLength = 0
    for i in s:
        tmpLength = 0
        cntLength = 0
        tmpB = b[0]
        for j in range(n):
            if b[j] != i:
                if b[j] == tmpB:
                    cntLength += 1
                else:
                    tmpLength = max(tmpLength, cntLength)
                    cntLength = 1
                    tmpB = b[j]
        tmpLength = max(tmpLength, cntLength)
        maxLength = max(maxLength, tmpLength)
    
    return maxLength

print(solution())