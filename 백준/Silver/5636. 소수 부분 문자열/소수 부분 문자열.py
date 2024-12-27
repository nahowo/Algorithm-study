import sys
input = sys.stdin.readline
MAX_SIZE = 100001

def getPrimes():
    global prime
    prime = [True] * MAX_SIZE
    prime[0], prime[1] = False, False

    for i in range(2, int(MAX_SIZE ** (1 / 2))):
        if prime[i]:
            for j in range(2, MAX_SIZE // i + 1):
                if i * j < MAX_SIZE:
                    prime[i * j] = False
    return prime

def makePartial(s):
    word = []
    for l in range(1, len(s)):
        for start in range(len(s) - l):
            word.append(int(s[start: start + l]))
    return word

def solution(s):
    maxPrime = 2
    word = makePartial(s)
    for i in range(len(word)):
        if word[i] < MAX_SIZE and prime[word[i]]:
            maxPrime = max(word[i], maxPrime)
    return maxPrime

getPrimes()
while True:
    s = input().rstrip()
    if s == '0':
        break
    print(solution(s))