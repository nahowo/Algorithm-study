import sys
input = sys.stdin.readline

def checkSquare(n):
    cnt = 1
    square = 0
    triangle = 0
    squareNum = [0]

    while True:
        triangle += cnt
        square += triangle
        cnt += 1
        if square > n:
            break
        isSquare[square] = True
        squareNum.append(square)
    return squareNum

def solution():
    global isSquare
    n = int(input())
    isSquare = [False] * (n + 1)
    squareNum = checkSquare(n)
    dp = [0] * (n + 1)
    
    cnt = 0
    for i in range(1, n + 1):
        if isSquare[i]:
            dp[i] = 1
            cnt += 1
        else:
            tmp = dp[i - 1] + 1
            for j in range(cnt, 0, -1):
                tmp = min(dp[i - squareNum[j]] + 1, tmp)
            dp[i] = tmp
    return dp[n]
    
print(solution())