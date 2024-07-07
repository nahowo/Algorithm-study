import sys
input = sys.stdin.readline

n, k = map(int, input().split())
students = [0] * 5 # [1~2, 3~4 F, 3~4 M, 5~6 F, 5~6 M]
for _ in range(n):
    s, y = map(int, input().split())
    if 1 <= y <= 2:
        students[0] += 1
    else:
        students[(y // 5) * 2 + s + 1] += 1

roomCount = 0
for i in students:
    if i % k == 0:
        roomCount += i // k
    else:
        roomCount += i // k + 1
print(roomCount)