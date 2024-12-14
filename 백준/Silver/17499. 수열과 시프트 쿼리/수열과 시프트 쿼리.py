import sys
input = sys.stdin.readline

def solution():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    start = 0 # 1번째 인덱스의 위치

    for i in range(q):
        tmp = list(map(int, input().split()))

        if tmp[0] == 1:
            a[(start + (tmp[1] - 1)) % n] += tmp[2]
        
        elif tmp[0] == 2:
            start = (start - tmp[1]) % n
        
        else:
            start = (start + tmp[1]) % n
    
    result = []
    for i in range(start, start + n):
        result.append(a[i % n])
    return result

print(*solution())