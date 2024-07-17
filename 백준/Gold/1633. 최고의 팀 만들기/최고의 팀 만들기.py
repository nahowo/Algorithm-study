import sys
input = sys.stdin.readline

def solution():
    player = []
    while True:
        try:
            a, b = map(int, input().split())
            player.append([a, b])
        except ValueError:
            break
    n = len(player)
    dp = [[[0] * 17 for _ in range(17)] for _ in range(n + 1)] # dp[i][w][b]: i번째에서 백팀이 w명, 흑팀이 b명 존재할 때의 최대 능력치

    for i in range(1, n + 1):
        for w in range(16):
            for b in range(16):
                if w <= 15: # i번째 선수를 백팀으로 선택하는 경우
                    dp[i][w + 1][b] = max(dp[i][w + 1][b], dp[i - 1][w][b] + player[i - 1][0])
                if b <= 15: # i번째 선수를 흑팀으로 선택하는 경우
                    dp[i][w][b + 1] = max(dp[i][w][b + 1], dp[i - 1][w][b] + player[i - 1][1])
                dp[i][w][b] = max(dp[i][w][b], dp[i - 1][w][b])
    
    return dp[n][15][15]

print(solution())