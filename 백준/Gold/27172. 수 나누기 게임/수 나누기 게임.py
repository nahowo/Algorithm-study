import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    cards = list(map(int, input().split()))
    maxNum = max(cards)
    sieve = [False] * (maxNum + 1)
    score = {i: 0 for i in cards}

    for i in range(n):
        sieve[cards[i]] = True
    
    for i in range(n):
        card = cards[i]
        for j in range(card * 2, maxNum + 1, card):
            if sieve[j] != False:
                score[card] += 1
                score[j] -= 1
        
    answer = []
    for i in range(n):
        answer.append(score[cards[i]])

    return answer

print(*solution())