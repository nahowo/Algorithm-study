import sys
input = sys.stdin.readline

def solution(n):
    name = []
    for _ in range(n):
        name.append(input().rstrip())
    
    newName = [0] * n

    for i in range(n):
        if i % 2 == 0:
            newName[i // 2] = name[i]
        else:
            newName[n - (i + 1) // 2] = name[i]
    
    return newName

cnt = 1
while True:
    n = int(input())
    if n == 0:
        break

    result = solution(n)
    print("SET", cnt)
    for i in result:
        print(i)

    cnt += 1