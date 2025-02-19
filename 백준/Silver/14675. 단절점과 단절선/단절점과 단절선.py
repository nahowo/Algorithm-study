import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    # 리프인 경우 단절점이 아님
    # 리프는 cnt(연결점) 개수가 1인 정점
    cnt = [0] * (n + 1)
    for _ in range(n - 1):
        a, b = map(int, input().split())
        cnt[a] += 1
        cnt[b] += 1
    q = int(input())
    answer = ['yes'] * q
    for i in range(q):
        t, k = map(int, input().split())
        if t == 1:
            if cnt[k] == 1:
                answer[i] = 'no'
    for i in answer:
        print(i)

solution()