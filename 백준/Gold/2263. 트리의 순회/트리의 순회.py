import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def find(inLeft, inRight, postLeft, postRight):
    if inLeft > inRight:
        return
    
    root = postOrder[postRight]
    preOrder.append(root)

    rootIdx = inIdx[root]
    move = rootIdx - inLeft

    find(inLeft, rootIdx - 1, postLeft, postLeft + move - 1) # left
    find(rootIdx + 1, inRight, postLeft + move, postRight - 1) # right

def solution():
    global inOrder, postOrder, preOrder, inIdx
    n = int(input())
    inOrder = list(map(int, input().split()))
    postOrder = list(map(int, input().split()))
    preOrder = []

    inIdx = dict()
    for i in range(n):
        inIdx[inOrder[i]] = i
    find(0, n - 1, 0, n - 1)

    return preOrder

print(*solution())