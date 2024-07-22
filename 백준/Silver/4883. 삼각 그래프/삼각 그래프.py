import sys
input = sys.stdin.readline
INF = sys.maxsize
d = [(-1, 0), (-1, -1), (-1, 1), (0, -1)]

def solution():
    cnt = 1
    while True:
        n = int(input())
        if n == 0:
            break

        graph = []
        for _ in range(n):
            graph.append(list(map(int, input().split())))
        dp = [[INF] * 5 for _ in range(n + 1)]

        for i in range(1, 4):
            dp[1][i] = graph[0][i - 1]

        # 시작 정점은 가장 위쪽 가운데 정점: 가장 위쪽 오른쪽/왼쪽 정점에서 시작할 수 없음
        dp[1][3] = min(graph[0][1], dp[1][2] + graph[0][2])
        dp[1][1] = graph[0][1]
        
        for i in range(2, n + 1):
            for j in range(1, 4):
                tmpMin = INF
                for di, dj in d:
                    ni, nj = i + di, j + dj
                    tmpMin = min(tmpMin, dp[ni][nj])
                dp[i][j] = graph[i - 1][j - 1] + tmpMin
        
        print(str(cnt) + '. ' + str(dp[n][2]))
        cnt += 1
    return

solution()