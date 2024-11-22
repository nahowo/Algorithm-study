import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()

    rSum = [0] # -> 방향으로의 누적합
    lSum = [0] # <- 방향으로의 누적합
    for i in range(0, n - 2, 2):
        rSum.append(rSum[-1] + numbers[i + 1] - numbers[i])
    
    for i in range(n - 1, 1, -2):
        lSum.append(lSum[-1] + numbers[i] - numbers[i - 1])

    teamMood = 10 ** 9 * n
    for i in range(0, n - 2, 2):
        tmpSum = numbers[i + 2] - numbers[i] # 3명 조
        tmpSum += rSum[i // 2] + lSum[(n - (i + 3)) // 2]
        teamMood = min(teamMood, tmpSum)
    
    return teamMood

print(solution())