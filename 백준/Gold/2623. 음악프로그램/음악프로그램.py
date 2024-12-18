import sys
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    indegree = {i: 0 for i in range(1, n + 1)}
    cnt = {i: set() for i in range(n)}
    link = {i: set() for i in range(1, n + 1)}

    for _ in range(m):
        order = list(map(int, input().split()))
        for i in range(1, order[0]):
            if order[i + 1] not in link[order[i]]:
                indegree[order[i + 1]] += 1
                link[order[i]].add(order[i + 1])
    
    for i, c in indegree.items():
        cnt[c].add(i)
    
    l = 0
    order = []
    while l < n:
        # 모든 순서가 정해지지 않았는데 cnt[0] 배열이 비어있다면 정렬 불가능
        if len(cnt[0]) == 0:
            print(0)
            return
        
        tmp = cnt[0].copy()
        for x in tmp:
            cnt[0].remove(x)
            for lx in link[x]:
                cnt[indegree[lx]].remove(lx)
                indegree[lx] -= 1
                cnt[indegree[lx]].add(lx)
            order.append(x)
            l += 1

    for i in order:
        print(i)
    return

solution()