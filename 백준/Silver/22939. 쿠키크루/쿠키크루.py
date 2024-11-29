import sys
from itertools import permutations
input = sys.stdin.readline
MAX_SIZE = 10001

def calcDist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def getMinDist(pos):
    start = home.copy()
    minDist = MAX_SIZE

    permutation = list(permutations(pos, 3))
    for route in permutation:
        tmpDist = calcDist(home, route[0]) + calcDist(route[0], route[1]) + calcDist(route[1], route[2]) + calcDist(route[2], cookie)
        minDist = min(minDist, tmpDist)
    return minDist

def solution():
    global home, cookie
    n = int(input())
    board = []
    group = ['Assassin', 'Healer', 'Mage', 'Tanker']
    pos = [[] for _ in range(4)]
    for i in range(n):
        board.append(list(input().rstrip()))
        for j in range(n):
            if board[i][j] == 'H':
                home = [i, j]
            elif board[i][j] == '#':
                cookie = [i, j]
            elif board[i][j] == 'J':
                pos[0].append([i, j])
            elif board[i][j] == 'C':
                pos[1].append([i, j])
            elif board[i][j] == 'B':
                pos[2].append([i, j])
            elif board[i][j] == 'W':
                pos[3].append([i, j])
    
    result = []
    result.append([getMinDist(pos[0]), 0])
    result.append([getMinDist(pos[1]), 1])
    result.append([getMinDist(pos[2]), 2])
    result.append([getMinDist(pos[3]), 3])
    result.sort()
    return group[result[0][1]]

print(solution())