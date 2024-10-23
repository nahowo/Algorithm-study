import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    dot = 2 # 한 변에 존재하는 점의 개수
    for _ in range(n):
        dot += dot - 1
    return dot * dot

print(solution())