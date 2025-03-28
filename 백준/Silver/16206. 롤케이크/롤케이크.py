import sys
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    cake = list(map(int, input().split()))
    cake.sort(key = lambda x: ((x % 10), x))
    answer = 0

    for i in range(n):
        if cake[i] % 10 == 0:
            cnt = (cake[i] // 10) - 1
            if m <= cnt:
                answer += m
                if cake[i] - m * 10 == 10:
                    answer += 1
                break
            answer += cnt + 1
            m -= cnt
        else:
            cnt = cake[i] // 10
            if m <= cnt:
                answer += m
                break
            answer += cnt
            m -= cnt

    return answer
    
print(solution())