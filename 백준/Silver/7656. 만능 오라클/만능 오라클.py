import sys
input = sys.stdin.readline

def printS(s):
    s = s.replace("What", "Forty-two")
    newS = s[:-1] + "."
    return newS

def splitS(s):
    arr = []
    flag = False
    start = 0
    for i in range(len(s)):
        if not flag:
            if 65 <= ord(s[i]) <= 90: # 대문자인 경우
                flag = True
                start = i
        else:
            if s[i] == '.' or s[i] == '?':
                arr.append(s[start : i + 1])
                flag = False
    return arr

def solution():
    s = input().rstrip()
    arr = splitS(s)
    answer = []

    for q in arr:
        if q[:7] == "What is" and q[-1] == "?":
            answer.append(printS(q))
    
    for i in answer:
        print(i)
    return

solution()