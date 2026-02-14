import sys
input = sys.stdin.readline

def solution():
    s = input().rstrip()
    n = len(s)
    answer = 0

    q = 0
    i = 0
    while i < n:
        if i < n - 1 and s[i] == "(" and s[i + 1] == ")":
            answer += q # 현재 레이저 경로에 있는 막대 개수
            i += 2
        else:
            if s[i] == "(":
                q += 1
            else:
                q -= 1
                answer += 1 # 막대 끝
            i += 1
    return answer
    
print(solution())