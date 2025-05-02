import sys
input = sys.stdin.readline

def graph():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                time[i][j] = min(time[i][j], time[i][k] + time[k][j])

def solution():
    global time, n
    n, m = map(int, input().split())
    time = [list(map(int, input().split())) for _ in range(n)]
    graph()

    answer = ["Enjoy other party"] * m
    for i in range(m):
        a, b, c = map(int, input().split())
        if time[a - 1][b - 1] > c:
            answer[i] = "Stay here"
    
    return "\n".join(answer)
    
print(solution())