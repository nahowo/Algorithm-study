import sys
input = sys.stdin.readline

def washOrDry(dishA, dishB, dishCnt): # washA -> washB
    for _ in range(dishCnt):
        dishB.append(dishA.pop())

def solution():
    global n
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
            washOrDry(unwashed, washed, d)
        else: # dry
            washOrDry(washed, dried, d)
            driedDishes += d
    return dried

result = solution()
for i in range(n - 1, -1, -1):
    print(result[i])