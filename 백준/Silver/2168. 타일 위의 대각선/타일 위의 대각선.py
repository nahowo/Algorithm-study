import sys, math
input = sys.stdin.readline

def solution():
    x, y = map(int, input().split())
    gcd = math.gcd(x, y)
    sx, sy = x // gcd, y // gcd
    tilePerPiece = sx + sy - 1

    return tilePerPiece * (x // sx)

print(solution())