import sys
input = sys.stdin.readline
INF = 10 ** 7 + 1

def isPrime(n):
    if n < 2:
        return False
    
    for i in range(2, (int((n + 1) ** (1 / 2)) + 1)):
        if n % i == 0 and n != i:
            return False
    return True

def dfs(l, visited, n, number):
    if len(number) >= 1:
        tmp = int(number)
        if tmp not in count and isPrime(tmp):
            count.add(tmp)
        if l == n:
            return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(l + 1, visited, n, number + paper[i])
            visited[i] = False

def solution():
    global count, paper
    paper = list(input().rstrip())
    count = set()
    n = len(paper)
    visited = [False] * n
    dfs(0, visited, n, "")
    return len(count)

c = int(input())
for _ in range(c):
    print(solution())