from collections import deque

def canChange(a, b):
    diff = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1
        if diff > 1:
            return 0
    return 1

def solution(begin, target, words):
    answer = 0
    n = len(words)
    graph = {i: [] for i in words}
    if target not in graph:
        return 0
    if canChange(begin, target):
        return 1
    graph[begin] = []
    for i in range(n):
        if canChange(words[i], begin):
            graph[begin].append(words[i])
        for j in range(i + 1, n):
            if canChange(words[i], words[j]):
                graph[words[i]].append(words[j])
                graph[words[j]].append(words[i])
    
    cnt = {i: 0 for i in words}
    cnt[begin] = 0
    q = deque([begin])
    
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if cnt[nx] == 0:
                cnt[nx] = cnt[x] + 1
                q.append(nx)
    answer = cnt[target]
    return answer