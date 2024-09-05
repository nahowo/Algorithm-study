import sys
input = sys.stdin.readline

def dfs(pos, flag, e):
    global minE
    if pos == n:
        minE = min(minE, e)
        return
    elif pos > n:
        return
    
    dfs(pos + 1, flag, e + energy[pos][0])
    dfs(pos + 2, flag, e + energy[pos][1])
    if flag == False:
        dfs(pos + 3, True, e + k)
    return

def solution():
    global n, minE, energy, k
    n = int(input())
    energy = [0] # n번 돌에서 출발할 때의 에너지
    for _ in range(n - 1):
        energy.append(list(map(int, input().split())))
    k = int(input())

    minE = 10 ** 5

    dfs(1, False, 0)
    return minE
    
print(solution())