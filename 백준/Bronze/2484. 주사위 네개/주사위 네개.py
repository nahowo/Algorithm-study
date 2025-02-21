import sys
input = sys.stdin.readline

def score(num):
    cnt = dict()
    for n in num:
        cnt[n] = cnt.get(n, 0) + 1

    arr = list(cnt.items())
    ret = sorted(cnt.values(), reverse = True)
    if ret[0] == 4:
        return arr[0][0] * 5000 + 50000
    elif ret[0] == 3:
        for k, v in arr:
            if v == 3:
                return k * 1000 + 10000
    elif ret[0] == 2 and ret[1] == 2:
        tmp = 0
        for k, v in arr:
            tmp += (k * 500)
        return tmp + 2000
    elif ret[0] == 2:
        for k, v in arr:
            if v == 2:
                return k * 100 + 1000
    else:
        return max(arr, key = lambda x: x[0])[0] * 100

def solution():
    n = int(input())
    answer = [0] * n
    for i in range(n):
        answer[i] = score(list(map(int, input().split())))

    return max(answer)

print(solution())