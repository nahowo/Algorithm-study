import sys
input = sys.stdin.readline

def wash(d):
    for _ in range(d):
        washed.append(unwashed.pop())

def dry(d):
    for _ in range(d):
        dried.append(washed.pop())

def solution():
    global unwashed, washed, dried, n
    n = int(input())
    unwashed = [i for i in range(n, 0, -1)]
    washed = []
    dried = []
    driedDishes = 0
    
    while True:
        if driedDishes == n:
            break
        
        c, d = map(int, input().split())
        if c == 1: # wash
            wash(d)
        else: # dry
            dry(d)
            driedDishes += d
    return dried

result = solution()
for i in range(n - 1, -1, -1):
    print(result[i])