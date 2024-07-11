import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    pick = list(map(int,input().split()))
    check = set()
    maxSticker = 0

    sticker = 0
    for i in pick:
        if i not in check:
            check.add(i)
            sticker += 1
            maxSticker = max(maxSticker, sticker)
        else:
            check.remove(i)
            sticker -= 1
    return maxSticker

print(solution())