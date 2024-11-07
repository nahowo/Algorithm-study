import sys
input = sys.stdin.readline

def solution():
    alpha = input().rstrip()
    if alpha == 'N' or alpha == 'n':
        return "Naver D2"
    return "Naver Whale"

print(solution())