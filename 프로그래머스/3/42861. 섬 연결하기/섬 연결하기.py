def find(a):
    if parent[a] != a:
        return find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    global parent
    answer = 0
    parent = [i for i in range(n)]
    bridge = []
    m = len(costs)
    costs.sort(key = lambda x: x[2])

    cnt = 0
    for i in range(m):
        a, b, cost = costs[i]
        if find(a) == find(b): # 이미 연결
            continue
        union(a, b) # 연결
        cnt += 1
        answer += cost
        if cnt == n:
            break
    
    return answer