import sys
input = sys.stdin.readline

def segment(left, right, i):
    if left == right:
        tree[i] = num[left]
        return tree[i]
    mid = (left + right) // 2
    tree[i] = segment(left, mid, i * 2) + segment(mid + 1, right, i * 2 + 1)
    return tree[i]

def search(b, c, left, right, i):
    if c < left or right < b:
        return 0
    
    if b <= left and right <= c:
        return tree[i]
    
    mid = (left + right) // 2
    return search(b, c, left, mid, i * 2) + search(b, c, mid + 1, right, i * 2 + 1)

def update(left, right, idx, newV, i):
    if left == right == idx:
        tree[i] = newV
        return
    
    if idx < left or right < idx:
        return

    mid = (left + right) // 2
    update(left, mid, idx, newV, i * 2)
    update(mid + 1, right, idx, newV, i * 2 + 1)
    tree[i] = tree[i * 2] + tree[i * 2 + 1]

def solution():
    global tree, num
    n, m, k = map(int, input().split())
    num = [int(input()) for _ in range(n)]
    tree = [0] * (n * 4)
    answer = []
    segment(0, n - 1, 1)

    for i in range(m + k):
        a, b, c = map(int, input().split())
        if a == 1:
            update(0, n - 1, b - 1, c, 1)
        else:
            answer.append(str(search(b - 1, c - 1, 0, n - 1, 1)))

    return '\n'.join(answer)
    
print(solution())