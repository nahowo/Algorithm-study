import sys
input = sys.stdin.readline

def solution():
    global cls
    n = int(input())
    cls = [] # 반별 학생 수 [남자 수, 여자 수]
    for _ in range(3):
        cls.append(list(map(int, input().split())))

    for i in range(cls[0][0]):
        ab = i
        ac = cls[0][0] - i
        bc = cls[2][1] - ac
        ba = cls[1][0] - bc
        ca = cls[0][1] - ba
        cb = cls[1][1] - ab
        if bc >= 0 and ba >= 0 and ca >= 0 and cb >= 0:
            print(1)
            print(ab, ac)
            print(ba, bc)
            print(ca, cb)
            return
    print(0)
    return

solution()