import sys
from collections import deque
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())

    taller = {i: [set(), 0] for i in range(1, n + 1)} # i: [{i번 학생보다 큰 학생 명단}, 자신보다 큰 학생 수]
    tallerCnt = {i: set() for i in range(n)} # i: {자신보다 큰 학생이 i명인 학생 명단}
    student = {i: set() for i in range(1, n + 1)} # i: {i번 학생보다 작은 학생 명단}

    for _ in range(m):
        a, b = map(int, input().split())
        taller[a][0].add(b)
        taller[a][1] += 1
        student[b].add(a)

    for i in range(1, n + 1):
        tallerCnt[taller[i][1]].add(i)

    q = deque()
    q.extend(tallerCnt[0])
    tallerCnt[0] = set()
    order = []
    
    while q:
        x = q.popleft()
        for nx in student[x]:
            tmpCnt = taller[nx][1]
            tallerCnt[tmpCnt].remove(nx)
            tallerCnt[tmpCnt - 1].add(nx)

            taller[nx][0].remove(x)
            taller[nx][1] -= 1
        order.append(x)
        
        q.extend(tallerCnt[0])
        tallerCnt[0] = set()
    order = order[:: -1]

    return order
    
print(*solution())