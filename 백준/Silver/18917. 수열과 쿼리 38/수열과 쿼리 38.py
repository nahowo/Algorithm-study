import sys
input = sys.stdin.readline

def solution():
    m = int(input())
    totalSum = 0
    totalXor = 0

    for _ in range(m):
        q = input().rstrip()
        if q[0] == '1' or q[0] == '2':
            x = int(q.split()[1])
            mark = 1 if q[0] == '1' else -1
            totalSum += x * mark
            totalXor ^= x
        elif q[0] == '3':
            print(totalSum)
        else:
            print(totalXor)

    return

solution()