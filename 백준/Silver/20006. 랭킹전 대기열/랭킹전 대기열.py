import sys
input = sys.stdin.readline

def enterRoom(l, n):
    for i in range(len(room)):
        if room[i][1] < m and room[i][0] - 10 <= l <= room[i][0] + 10:
            room[i][1] += 1
            room[i][2].append(n)
            return
    room.append([l, 1, [n]])
    return

def solution():
    global m, room
    p, m = map(int, input().split())
    room = [] # [처음 입장한 플레이어의 레벨, 입장한 정원 수, [입장 멤버]]
    level = dict()
    
    for _ in range(p):
        l, n = input().rstrip().split()
        l = int(l)
        enterRoom(l, n)
        level[n] = l

    for r in room:
        if r[1] == m:
            print("Started!")
        else:
            print("Waiting!")
        for player in sorted(r[2]):
            print(level[player], player)
    return

solution()