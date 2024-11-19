import sys
input = sys.stdin.readline

def getScore(a, b, building):
    return abs(a - b) * building

def solution():
    t = int(input())
    tmp = list(map(int, input().split()))
    if t <= 4:
        tmp += [0] * (5 - t)
    kor, mth, eng, sci, frn = tmp # 국, 수, 영, 탐, (외)
    studentNumber = 0

    if kor > eng:
        buildingNumber = 508
    else:
        buildingNumber = 108
    studentNumber += getScore(kor, eng, buildingNumber)
    
    if mth > sci:
        buildingNumber = 212
    else:
        buildingNumber = 305
    studentNumber += getScore(mth, sci, buildingNumber)

    studentNumber += frn * 707
    
    return studentNumber * 4763

print(solution())