import sys
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    for _ in range(m):
        k = int(input())
        books = list(map(int, input().split()))
        for i in range(k - 1):
            if books[i] < books[i + 1]:
                return "No"
    return "Yes"

print(solution())