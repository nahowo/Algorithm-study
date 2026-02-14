import sys
input = sys.stdin.readline

def binarySearch(target, b):
    start, end = 0, len(b) - 1

    while start <= end:
        mid = (start + end) // 2
        if b[mid] == target:
            return True
        elif b[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

def solution():
    answer = []
    na, nb = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()

    for i in a:
        if not binarySearch(i, b):
            answer.append(i)
    return str(len(answer)) + "\n" + " ".join(map(str, answer))
    
print(solution())