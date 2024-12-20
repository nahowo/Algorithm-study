import sys
input = sys.stdin.readline

def solution(pages):
    printing = [False] * (pages + 1)
    ranges = input().rstrip().split(",")
    for i in range(len(ranges)):
        try:
            start, end = map(int, ranges[i].split("-"))
            for p in range(start, min(end, pages) + 1):
                printing[p] = True
        except:
            idx = int(ranges[i])
            if idx <= pages:
                printing[idx] = True

    return printing.count(True)

while True:
    pages = int(input())
    if pages == 0:
        break
    print(solution(pages))