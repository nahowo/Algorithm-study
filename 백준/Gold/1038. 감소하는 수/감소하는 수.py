import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    table = [[] for _ in range(11)] # 길이가 i인 감소하는 수들을 인덱스 i번째 배열에 저장
    table[1] = {i: [i] for i in range(10)} # k: [v]에서 k는 v의 가장 왼쪽에 위치한 수
    cnt = 0

    if n < 10:
        return table[1][n][0]
    cnt += 9

    for l in range(2, 11): # 숫자의 길이
        table[l] = {t: [] for t in range(10)}
        for j in range(l - 1, 10): # 가장 왼쪽에 위치한 수
            for rest in range(0, j): # j의 오른쪽 수(왼쪽에서 2번째 수)
                for ending in table[l - 1][rest]:
                    tmp = j * 10 ** (l - 1) + ending
                    cnt += 1
                    if cnt == n:
                        return tmp
                    table[l][j].append(tmp)
    return -1

print(solution())