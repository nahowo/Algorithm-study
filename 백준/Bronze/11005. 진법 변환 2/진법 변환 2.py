import sys
input = sys.stdin.readline

def solution():
    n, b = map(int, input().split())

    arr = []
    while n > 0:
        arr.append(n % b)
        n //= b

    arr = arr[:: -1]
    for i in range(len(arr)):
        if arr[i] > 9:
            arr[i] = chr(55 + arr[i])
        else:
            arr[i] = str(arr[i])

    return ''.join(arr)

print(solution())