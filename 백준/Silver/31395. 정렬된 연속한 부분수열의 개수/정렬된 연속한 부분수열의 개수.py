import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * (n + 1)
    cnt[1] = 1
    for i in range(2, n + 1):
        cnt[i] += cnt[i - 1] + i
    answer = 0

    l = 1
    for i in range(1, n):
        if a[i] >= a[i - 1]:
            l += 1
        else:
            answer += cnt[l]
            l = 1
    answer += cnt[l]
    return answer
    
print(solution())