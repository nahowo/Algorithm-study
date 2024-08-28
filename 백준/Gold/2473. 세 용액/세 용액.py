import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    liq = sorted(list(map(int, input().split())))
    minSum = 10 ** 10
    liqAnswer = [0, 0, 0]

    for i in range(n):
        left = i + 1
        right = n - 1

        while left < right:
            tmp = liq[i] + liq[left] + liq[right]

            if abs(tmp) < minSum:
                liqAnswer = [liq[i], liq[left], liq[right]]
                minSum = abs(tmp)

                if minSum == 0:
                    break
                
            if tmp > 0:
                right -= 1
            else:
                left += 1

    return liqAnswer

print(*solution())