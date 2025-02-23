import sys
input = sys.stdin.readline

def solution():
    n, m, v = map(int, input().split())
    c = list(map(int, input().split()))
    answer = [-1] * m
    l = n - v + 1 # 사이클 길이
    for i in range(m):
        k = int(input())
        if k <= v: # 사이클 진입 전 노드
            answer[i] = c[k]
        else: # 사이클 진입 후 노드
            answer[i] = c[(k - (v - 1)) % l + (v - 1)]
    for i in answer:
        print(i)

solution()