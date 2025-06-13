import sys
input = sys.stdin.readline

def solution(n: int) -> str:
    if n % 6 == 0:
        return 'Y'
    return 'N'

while True:
    n = input().rstrip()
    if n == '':
        break
    print(solution(int(n)))