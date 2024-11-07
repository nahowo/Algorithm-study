import sys
input = sys.stdin.readline

def solution():
    n, h, w = map(int, input().split())
    note = []
    for _ in range(h):
        note.append(input().rstrip())
    original = ''

    for i in range(n):
        key = '?'
        for x in range(i * w, (i + 1) * w):
            for y in range(0, h):
                if note[y][x] != '?':
                    key = note[y][x]
        original += key
    return original

print(solution())