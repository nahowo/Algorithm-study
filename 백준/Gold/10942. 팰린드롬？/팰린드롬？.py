import sys
input = sys.stdin.readline

def check(s, e, p):
    key = (e + s) // 2
    if p[key] and p[key][0] <= s and e <= p[key][1]:
        if s - p[key][0] == p[key][1] - e:
            return True
    
    return False

def solution():
    n = int(input())
    board = list(map(int, input().split()))

    oddP = [None] # 패딩
    evenP = [None] # 패딩
    # 배열 길이가 홀수일 때 팰린드롬 찾기 (O(4 * 10 ^ 6))
    for i in range(n):
        s, e = i, i
        while 0 < s and e < n - 1:
            if board[s - 1] == board[e + 1]:
                s -= 1
                e += 1
            else:
                break
        oddP.append([s + 1, e + 1])
    
    # 배열 길이가 짝수일 때 팰린드롬 찾기 (O(4 * 10 ^ 6))
    for i in range(n - 1):
        s, e = i, i + 1
        if board[s] != board[e]:
            evenP.append(False)
            continue
        while 0 < s and e < n - 1:
            if board[s - 1] == board[e + 1]:
                s -= 1
                e += 1
            else:
                break
        evenP.append([s + 1, e + 1])

    answer = []
    m = int(input())
    for _ in range(m): # O(10 ^ 6)
        s, e = map(int, input().split())
        if (e - s) % 2 == 0: # 배열 길이가 홀수
            answer.append(int(check(s, e, oddP)))
        else: # 배열 길이가 짝수
            answer.append(int(check(s, e, evenP)))
    
    return answer

result = solution()
for i in result:
    print(i)