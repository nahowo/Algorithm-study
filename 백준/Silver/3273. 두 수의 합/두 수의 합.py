import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    cnt = dict()
    answer = 0

    for i in a:
        answer += cnt.get(x - i, 0)
        cnt[i] = cnt.get(i, 0) + 1
    
    return answer

print(solution())