import sys
input = sys.stdin.readline

def rec(n):
    if n <= 0:
        return 0
    if cache[n] != -1:
        return cache[n]
    
    ret = rec(n - 1) + rec(n - 2) * 2
    cache[n] = ret
    return ret

query = []
while True:
    ipt = input().rstrip()
    if ipt == '':
        break
    query.append(int(ipt))

cache = [-1] * (max(query) + 3)
cache[0] = 1
cache[1] = 1
cache[2] = 3
rec(max(query))
for q in query:
    print(cache[q])