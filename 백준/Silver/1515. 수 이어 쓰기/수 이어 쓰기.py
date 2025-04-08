import sys
input = sys.stdin.readline

def solution():
    num = input().rstrip()
    l = len(num)
    
    curNum = 1
    idx = 0
    while idx < l:
        for i in str(curNum):
            if num[idx] == i:
                idx += 1
                if idx >= l:
                    return curNum
        curNum += 1
        
    return curNum
    
print(solution())