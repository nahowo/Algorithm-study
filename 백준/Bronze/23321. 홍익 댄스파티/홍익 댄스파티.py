import sys
input = sys.stdin.readline
POS = {'.omln': 'owln.', 'owln.': '.omln', '..oLn': '..oLn'}

def solution():
    tmp = []
    for _ in range(5):
        tmp.append(input().rstrip())
    
    pic = ['' for _ in range(len(tmp[0]))]
    for i in range(len(tmp[0])):
        for j in range(5):
            pic[i] += tmp[j][i]

    newPic = []
    for i in range(len(pic)):
        newPic.append(POS[pic[i]])

    for j in range(5):
        for i in range(len(newPic)):
            print(newPic[i][j], end = "")
        print()

solution()