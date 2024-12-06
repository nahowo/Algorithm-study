import sys
input = sys.stdin.readline

def checkPuzzle(verticalIdx, horizontalIdx):
    vertical = []
    horizontal = []
    for idx in verticalIdx:
        vertical.append(word[idx])
    for idx in horizontalIdx:
        horizontal.append(word[idx])
    
    for i in range(3):
        tmp = ''
        for j in range(3):
            tmp += horizontal[j][i]
        if tmp in vertical:
            vertical.remove(tmp)
        else:
            return False
    return True

def makePuzzle(horizontal, vertical, cnt): # vertical -> horizontal
    if cnt == 3:
        if checkPuzzle(vertical, horizontal):
            puzzle = ""
            for idx in horizontal:
                puzzle += word[idx]
            puzzles.add(puzzle)
        return
    
    for i in range(6):
        if i not in horizontal:
            tmpH = horizontal.copy()
            tmpH.append(i)
            tmpV = vertical.copy()
            tmpV.remove(i)
            makePuzzle(tmpH, tmpV, cnt + 1)

def solution():
    global puzzles, word
    word = [input().rstrip() for _ in range(6)]
    puzzles = set()
    makePuzzle([], [i for i in range(6)], 0)

    if len(puzzles) == 0:
        print(0)
    else:
        puzzles = list(puzzles)
        result = min(puzzles)
        for i in range(3):
            print(result[i * 3 : i * 3 + 3])

solution()