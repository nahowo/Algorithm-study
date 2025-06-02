import sys
input = sys.stdin.readline

def solution():
    global cnt, studentCnt, grade
    n = int(input())
    dp = [[] for _ in range(n)]
    dp[0] = list(map(int, input().split()))
    cnt = [[1, 1] for _ in range(n)]
    studentCnt = 1
    grade = min(dp[0])

    for i in range(1, n):
        a, b = map(int, input().split())
        dp[i] = [a, b]
        if a == dp[i - 1][0]:
            add(i, 0, 0, a)
        if a == dp[i - 1][1]:
            add(i, 0, 1, a)
        if b == dp[i - 1][0]:
            add(i, 1, 0, b)
        if b == dp[i - 1][1]:
            add(i, 1, 1, b)
    print(studentCnt, grade)

def add(i, idx1, idx2, target):
    global studentCnt, grade
    cnt[i][idx1] = cnt[i - 1][idx2] + 1
    if cnt[i][idx1] > studentCnt:
        studentCnt = cnt[i][idx1]
        grade = target
    elif cnt[i][idx1] == studentCnt:
        if target < grade:
            grade = target
    
solution()