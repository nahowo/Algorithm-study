import sys
from collections import deque
input = sys.stdin.readline

def solution():
    n = int(input())
    cards = deque(i for i in range(1, n + 1))
    answer = []

    while n > 1:
        throw = cards.popleft()
        n -= 1
        answer.append(throw)
        keep = cards.popleft()
        cards.append(keep)
    answer.append(cards.pop())
    
    return ' '.join(map(str, answer))

print(solution())