import sys
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    reverseRoute = []
    for _ in range(n):
        s, e = map(int, input().split())
        if s > e:
            reverseRoute.append([s, e])
    reverseRoute.sort(key = lambda x: (-x[0], x[1]))
    answer = m
    if reverseRoute:
        s, e = reverseRoute[0]
        for i in range(1, len(reverseRoute)):
            ns, ne = reverseRoute[i]
            if ne >= e or ns >= e:
                e = min(e, ne)
            else:
                answer += (s - e) * 2
                s, e = ns, ne
        answer += (s - e) * 2
    return answer
    
print(solution())