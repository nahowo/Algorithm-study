import sys
input = sys.stdin.readline

def dfs(s, t, cnt):
    global minCnt
    if s == t:
        minCnt = min(minCnt, cnt)
        return
    if s > t: # 태균이가 상대 점수를 넘어서기 시작하면 더 이상 점수가 같아질 수 없음(종료조건)
        return
    
    dfs(s * 2, t + 3, cnt + 1)
    dfs(s + 1, t, cnt + 1)

def solution():
    global minCnt
    minCnt = sys.maxsize
    s, t = map(int, input().split())
    dfs(s, t, 0)
    return minCnt

t = int(input())
for _ in range(t):
    print(solution())