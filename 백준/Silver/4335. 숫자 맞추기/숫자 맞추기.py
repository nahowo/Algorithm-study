import sys
input = sys.stdin.readline
TALK = {True: "Stan may be honest", False: "Stan is dishonest"}

def solution():
    while True:
        result = TALK[True]
        start = 1
        end = 10
        while True:
            n = int(input())
            if n == 0:
                return

            answer = input().rstrip()
            if answer == "right on":
                if start > n or end < n:
                    result = TALK[False]
                print(result)
                break

            if answer == "too low":
                start = max(start, n + 1)
            elif answer == "too high":
                end = min(end, n - 1)

solution()