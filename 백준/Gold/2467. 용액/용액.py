import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    liq = list(map(int, input().split()))
    minSum = 2 * 10 ** 9 + 1
    liqAnswer = [0, 0]

    left, right = 0, n - 1
    while left < right:
        tmp = liq[left] + liq[right]
        
        if abs(tmp) < minSum:
            liqAnswer = [liq[left], liq[right]]
            minSum = abs(tmp)
        
            if tmp == 0:
                break
        
        if tmp > 0:
            right -= 1
        else:
            left += 1
    
    return liqAnswer

print(*solution())