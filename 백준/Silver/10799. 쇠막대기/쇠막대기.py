import sys
input = sys.stdin.readline

def solution():
    s = input().rstrip()
    s = s.replace("()", "|")
    n = len(s)
    answer = 0

    q = 0
    for i in range(n):
        if s[i] == "|":
            answer += q
        else:
            if s[i] == "(":
                q += 1
            else:
                q -= 1
                answer += 1
    return answer
    
print(solution())