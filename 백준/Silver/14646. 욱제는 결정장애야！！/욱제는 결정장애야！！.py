import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    pick = list(map(int,input().split()))
    check = [False] * (n + 1)
    maxSticker = 0

    sticker = 0
    for i in pick:
        if check[i] == False:
            check[i] = True
            sticker += 1
            maxSticker = max(maxSticker, sticker)
        else:
            check[i] = False
            sticker -= 1
    return maxSticker

print(solution())